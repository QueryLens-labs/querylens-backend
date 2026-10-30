# QueryLens — funcionalidades pendientes

Este archivo reserva las siguientes fases. La Fase 1 se limita al análisis básico de consultas de lectura y su plan de ejecución.

## Fase 1.5 — verificación y estabilización (2026-10-30)

- [x] Construcción y arranque de frontend, backend y PostgreSQL con Docker Compose; contenedores activos y healthchecks correctos.
- [x] Verificados 100 productos, 100.000 ventas, FK `sales.product_id → products.id` y permisos de lectura sin permisos de escritura.
- [x] Persistencia comprobada: el recuento de ventas siguió en 100.000 después de reiniciar PostgreSQL.
- [x] Flujo real navegador → Nginx → FastAPI → PostgreSQL → `EXPLAIN ANALYZE` → árbol del plan, con JOIN, GROUP BY y ORDER BY.
- [x] Rechazo de INSERT, UPDATE, DELETE, DROP y múltiples sentencias; error SQL controlado y timeout comprobado.
- [x] Estados de carga y error comprobados en Chrome; sin excepciones JavaScript.
- [x] Pytest: 14 pruebas aprobadas. Build de frontend aprobado. `npm audit`: 0 vulnerabilidades tras actualizar Vite a 7.3.7.
- [x] `docker compose config --quiet` validado.

El puerto local 5432 ya estaba ocupado por otro PostgreSQL; la verificación usó 55432 y `.env.example` queda configurado con ese puerto para el entorno local.

## Fase 2 — Análisis visual avanzado

- [ ] Visualizador interactivo de planes con selección y navegación por nodos.
- [ ] Identificación de operaciones potencialmente costosas mediante reglas explicables.
- [ ] Métricas detalladas por nodo y contexto de buffers.
- [ ] Explicaciones de las operaciones y estrategias de PostgreSQL.

## Fase 3 — Experimentos de optimización

- [ ] Creación y limpieza de índices temporales en entornos de prueba aislados.
- [ ] Comparación antes y después de aplicar una optimización.
- [ ] Historial de experimentos.
- [ ] Comparación visual de planes de ejecución.

## Fase 4 — Benchmarks reproducibles

- [ ] Ejecución repetida de consultas con parámetros controlados.
- [ ] Estadísticas de rendimiento, variabilidad y distribución.
- [ ] Comparación con diferentes volúmenes de datos ficticios.
- [ ] Exportación de resultados y configuración del benchmark.

## Fase 5 — Mejoras del producto

- [ ] Guardar consultas y experimentos.
- [ ] Importar y exportar escenarios reproducibles.
- [ ] Recomendaciones basadas en reglas y evidencia del plan.
- [ ] Mejoras de interfaz, accesibilidad y experiencia de usuario.

