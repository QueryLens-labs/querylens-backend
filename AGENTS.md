# Instrucciones de desarrollo de QueryLens

Estas instrucciones cubren el backend y la infraestructura compartida. Cuando una tarea afecta al contrato HTTP o al workspace completo, coordina con las instrucciones de ../querylens-frontend/AGENTS.md.

## Proyecto y alcance

QueryLens ayuda a analizar consultas PostgreSQL y comprender sus planes de ejecución. La Fase 1 implementa una API FastAPI de solo lectura, acceso a PostgreSQL y una interfaz React en el repositorio hermano. El roadmap futuro está en TODO.md; no implementes sus tareas sin una solicitud concreta.

## Documentation language

Keep project documentation, including TODO.md and both repositories' README.md files, entirely in English. When editing a README, write the complete document in English. Do not change the application UI language unless requested.

## Tecnologías

- Backend: Python 3, FastAPI y Psycopg 3.
- Base de datos: PostgreSQL.
- Infraestructura: Docker y Docker Compose.
- Pruebas: Pytest.
- Cliente relacionado: React, TypeScript, Vite y Tailwind CSS en ../querylens-frontend.

No cambies las tecnologías, versiones ni dependencias salvo necesidad justificada.

## Forma de trabajar

1. Inspecciona los archivos y las instrucciones pertinentes antes de cambiar código.
2. Limita cada petición a su alcance. Mantén separados API, lógica de análisis y acceso a datos.
3. Evita funcionalidades, abstracciones, archivos y dependencias innecesarias; no elimines capacidades existentes.
4. Respeta el comportamiento visual y los contratos actuales del frontend.
5. Diagnostica los errores antes de cambiar archivos para corregirlos.
6. No incluyas secretos, .env reales, entornos virtuales, cachés ni archivos generados en Git.
7. No hagas commits, push, despliegues ni operaciones destructivas sin autorización expresa.
8. Verifica los cambios con las pruebas, compilación o validación pertinente y describe solo lo que comprobaste.
9. Al finalizar, informa qué cambió, los archivos principales, las verificaciones y los pendientes.

## Contrato entre repositorios

La API publica GET /api/health y POST /api/analyze; sus esquemas están en app/schemas.py. El frontend en ../querylens-frontend consume rutas relativas /api. En desarrollo, Vite hace proxy a localhost:8000; en Docker Compose, Nginx hace proxy al servicio backend:8000. Coordina cambios de rutas o esquemas con el frontend y conserva compatibilidad salvo petición explícita.

## Seguridad de consultas

- Usa datos locales completamente ficticios; no conectes datos personales, corporativos ni confidenciales.
- Ejecuta análisis con permisos limitados, solo lectura y tiempos máximos.
- Recuerda que EXPLAIN ANALYZE ejecuta la consulta.
- Distingue los valores reales devueltos por PostgreSQL de estimaciones e interpretaciones; el coste estimado no representa tiempo real.
- Conserva la posibilidad de pruebas reproducibles en fases futuras sin implementarlas por adelantado.

## Docker Compose

docker-compose.yml vive en este repositorio. Desde la raíz backend, docker compose up --build -d construye el backend con contexto . y el frontend desde ../querylens-frontend; PostgreSQL monta ./database/init. Usa únicamente rutas relativas para las carpetas del proyecto. El workspace esperado contiene exactamente las dos carpetas hermanas querylens-frontend y querylens-backend.

## Agente y Claude Code

El workspace VS Code está en QueryLens.code-workspace. El agente de QueryLens está en .github/agents/querylens.agent.md; debe consultar ambas instrucciones AGENTS cuando el cambio atraviese los dos repositorios. Claude Code debe leer CLAUDE.md.
