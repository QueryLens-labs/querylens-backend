from fastapi.testclient import TestClient

from app.main import app


def test_analyze_returns_structured_plan(monkeypatch) -> None:
    plan = [
        {
            "Plan": {
                "Node Type": "Seq Scan",
                "Relation Name": "products",
                "Startup Cost": 0.0,
                "Total Cost": 15.0,
                "Plan Rows": 100,
                "Actual Rows": 100,
                "Actual Loops": 1,
                "Plans": [],
            },
            "Planning Time": 0.12,
            "Execution Time": 0.34,
        }
    ]
    monkeypatch.setattr("app.main.explain_query", lambda query: plan)
    client = TestClient(app)

    response = client.post("/api/analyze", json={"query": "SELECT * FROM products"})

    assert response.status_code == 200
    assert response.json()["root"]["node_type"] == "Seq Scan"
    assert response.json()["root"]["estimated_rows"] == 100
    assert response.json()["execution_time_ms"] == 0.34


def test_analyze_rejects_non_select_before_connecting() -> None:
    client = TestClient(app)

    response = client.post("/api/analyze", json={"query": "DELETE FROM sales"})

    assert response.status_code == 422
    assert "SELECT" in response.json()["detail"]["message"]


def test_health_reports_unavailable_database(monkeypatch) -> None:
    def unavailable_connection():
        raise RuntimeError("database credentials must not be returned")

    monkeypatch.setattr("app.main.connect", unavailable_connection)
    client = TestClient(app)

    response = client.get("/api/health")

    assert response.status_code == 503
    assert "credentials" not in response.text

