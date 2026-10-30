---
name: QueryLens
description: Agente de desarrollo para los repositorios frontend y backend de QueryLens dentro del workspace Multi-root.
---

# QueryLens

Antes de trabajar, lee AGENTS.md del repositorio afectado. Si la tarea cruza los dos proyectos, lee también ../querylens-frontend/AGENTS.md o ../querylens-backend/AGENTS.md, según corresponda. El backend conserva el roadmap general en TODO.md.

El workspace contiene dos repositorios Git independientes. La API FastAPI en el backend ofrece GET /api/health y POST /api/analyze; el frontend consume /api. Vite reenvía esa ruta a localhost:8000 en desarrollo y Nginx la reenvía al servicio backend en Docker Compose. Mantén coordinados los esquemas y rutas, conserva las capacidades de la Fase 1 y sigue las reglas de seguridad e instrucciones de cada repositorio. No implementes tareas del roadmap ni cambies el diseño sin una petición concreta.