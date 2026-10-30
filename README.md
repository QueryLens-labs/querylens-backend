# QueryLens Backend e infraestructura

Este repositorio contiene la API FastAPI, el análisis y validación SQL, el acceso de solo lectura a PostgreSQL, las pruebas, los scripts de inicialización y Docker Compose. La Fase 1 conserva la base local ficticia con 100.000 ventas y el análisis de planes de consulta.

## Requisitos

- Docker Desktop con Docker Compose.
- El repositorio querylens-frontend como carpeta hermana para construir la aplicación completa.
- Para ejecutar piezas fuera de Docker: Python 3.13; Node.js 20.19 o posterior para el frontend.

## Preparar los repositorios

Clona ambos repositorios dentro de QueryLensWorkspace, de modo que queden como carpetas hermanas:

    git clone https://github.com/querylens-labs/querylens-frontend.git
    git clone https://github.com/querylens-labs/querylens-backend.git
    cd querylens-backend

Si ya abriste QueryLens.code-workspace, puedes ejecutar estos comandos desde su terminal integrada.

## Ejecutar la aplicación completa

En PowerShell, desde la raíz de querylens-backend:

    Copy-Item .env.example .env
    docker compose up --build -d

Abre http://localhost:3000. Compose construye el backend desde este repositorio y el frontend desde ../querylens-frontend; Nginx reenvía /api a FastAPI. PostgreSQL inicializa el esquema y los datos ficticios al crear el volumen por primera vez.

Para revisar el estado y la base de demostración:

    docker compose ps
    docker compose exec db psql -U querylens_admin -d querylens -c "SELECT count(*) AS ventas FROM sales;"

Los scripts de inicialización solo se ejecutan cuando el volumen está vacío. Eliminar el volumen destruye los datos locales de demostración.

## Ejecutar componentes fuera de Docker

Para la API, arranca PostgreSQL con Compose y configura QUERYLENS_DB_HOST=localhost, QUERYLENS_DB_PORT según `.env` (55432 en `.env.example`), QUERYLENS_DB_NAME=querylens, QUERYLENS_DB_USER=querylens_readonly y QUERYLENS_DB_PASSWORD según `.env`.

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements-dev.txt
    uvicorn app.main:app --reload --port 8000

En otra terminal, desde ../querylens-frontend:

    npm ci
    npm run dev

Vite publica http://localhost:5173 y hace proxy de /api a http://localhost:8000.

## API y seguridad

- GET /api/health: estado de FastAPI y conexión PostgreSQL.
- POST /api/analyze: recibe {"query": "SELECT ..."} y devuelve tiempos y nodos del plan.
- /docs: documentación interactiva de FastAPI.

La API acepta una sentencia SELECT (también WITH ... SELECT) dentro de una transacción de solo lectura con límite de 10 segundos. EXPLAIN ANALYZE ejecuta realmente la consulta; usa únicamente la base local de demostración. El usuario de la API solo tiene permisos SELECT en las tablas configuradas. Los valores de .env.example son exclusivamente para desarrollo local y no deben usarse al exponer servicios.

## Pruebas

    py -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements-dev.txt
    pytest

## Workspace e instrucciones

Abre QueryLens.code-workspace en VS Code para cargar ambos repositorios como carpetas y repositorios Git independientes. Las reglas del proyecto están en AGENTS.md; Claude Code debe leer CLAUDE.md. El agente personalizado está en .github/agents/querylens.agent.md.

El roadmap general de QueryLens se mantiene en [TODO.md](TODO.md).
