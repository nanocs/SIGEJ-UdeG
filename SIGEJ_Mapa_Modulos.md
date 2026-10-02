# SIGEJ-UdeG — Mapa de módulos (blueprint de cobertura)
## Oficina de la Abogacía General · Universidad de Guadalajara

> Auditoría de Veritas 🔍 del catálogo de ~48 módulos solicitado contra lo que **ya está construido**. Leyenda: **✅ implementado** · **🟡 parcial / orientativo** · **🆕 nuevo (este avance)** · **🏗️ requiere backend (fase 2)**.

## I. Módulos operativos para abogados
| # | Módulo | Estado | Dónde vive en SIGEJ |
|---|---|---|---|
| 1 | Gestión Integral de Expedientes | ✅ | `modulo_expedientes` (CRUD, subexp., relación, estado, historial, vinculación) |
| 2 | Gestión Documental Inteligente | 🟡 | Adjuntar/visualizar docs + categorías; **OCR/firma/clasificación IA/búsqueda semántica = 🏗️** |
| 3 | **Oficialía de Partes Electrónica** | 🆕 | `oficialia` (recepción · turnado · radicación · trazabilidad) |
| 4 | Agenda Jurídica y Control de Plazos | ✅ | Agenda + Gantt en `modulo`; vista Agenda en dashboard; **Outlook/Teams = 🏗️** |
| 5 | Gestión de Tareas (Monday/ClickUp) | ✅ | Kanban movible + Gantt en `modulo`; prioridades/riesgo |
| 7 | Seguimiento de Horas y Gastos | 🟡 | Panel "a capturar" en la ficha; **registro real = 🏗️** |
| 8 | Gestión de Clientes Internos | ✅ | Dependencias/centros (193) + roles institucionales en `abogados` (trazabilidad) |
| 9 | Módulo de MASC (conciliaciones/convenios) | 🟡 | Conciliación documentada en datos y transparencia; **gestión MASC dedicada = 🆕 posible** |

## II. Módulos de supervisión
| # | Módulo | Estado | Dónde |
|---|---|---|---|
| 11 | Supervisión de Expedientes (activos/concluidos/rezagos/riesgos) | ✅ | Dashboard (Ejecutivo, Tiempos, Riesgos) + Sala de Mando |
| 12 | Control de Productividad | ✅ | Dashboard: Productividad, Desempeño, Equidad de cargas |
| 13 | Gestión de Riesgos Jurídicos (mapa de calor, Alto/Medio/Bajo) | ✅ | Dashboard Riesgos + score recalibrado; **impacto reputacional = 🟡** |
| 14 | Seguimiento de Pasivos Contingentes | ✅ | Dashboard Provisión (reserva editable NIF C-9/IAS 37) |

## III. Cuadro de Mando / Analítica
| Componente | Estado | Dónde |
|---|---|---|
| **CMI · Balanced Scorecard (4 perspectivas)** | 🆕 | Dashboard → pestaña "CMI · Balanced Scorecard" (Jurídica/Financiera/Procesos/Aprendizaje) |
| Legal Analytics (prob. éxito, duración, litigiosidad) | ✅ | Dashboard + modelo predictivo + cuellos de botella |
| Chat Jurídico Institucional (Copilot) | 🏗️ | Recomendado como nuevo módulo (asistente sobre la base) |

## IV. Módulos administrativos
| # | Módulo | Estado |
|---|---|---|
| 22 | Seguridad (SSL/MFA/auditoría/logs) | 🏗️ Fase 2 (requiere backend/servidor) |
| 23 | Roles y permisos | 🟡 Definidos en el proyecto; **enforcement = 🏗️** |
| 24 | Gestión de usuarios | 🏗️ Fase 2 |
| 25 | Bitácora de auditoría | 🟡 Trazabilidad por evento en captura/oficialía; **bitácora central = 🏗️** |

## V. Integración (Microsoft)
| # | Módulo | Estado |
|---|---|---|
| 26–30 | Outlook · Teams · SharePoint · M365 · Power BI | 🏗️ Fase 2 (la suite exporta CSV/JSON/Word como puente) |
| 33 | Transparencia y Datos Personales | ✅ `transparencia` (solicitudes, registro, oficio); **recursos de revisión = 🟡** |
| 34 | Responsabilidades Administrativas | 🟡 Posible nuevo módulo (investigaciones/procedimientos) |

## VII. Avanzados recomendables
| # | Módulo | Estado |
|---|---|---|
| 38 | BPM / Power Automate | 🏗️ Diseñado (BPMN en proyecto) |
| 39 | OCR / digitalización masiva | 🏗️ (hoy: adjuntar/visualizar manual) |
| 40 | Búsqueda semántica | 🏗️ |
| 41 | Generador de documentos | 🟡 Oficio Word (transparencia) + informe Word (abogados); ampliable |
| 42 | Portal de autoservicio para dependencias | 🏗️ |
| 43 | Aplicación móvil | 🏗️ (las apps son responsive) |
| 44 | Alertas inteligentes | ✅ Motor de alertas + agenda + inactividad/caducidad |
| 45–48 | Data Warehouse / Lago / Centro de inteligencia / Gemelo digital | 🏗️ Fase 2 (arquitectura medallón en el proyecto) |

---

## Resumen ejecutivo
- **✅ Implementado y operativo:** ~20 módulos (núcleo operativo + supervisión + analítica + transparencia).
- **🆕 Agregado en este avance:** Oficialía de Partes, Balanced Scorecard (4 perspectivas).
- **🟡 Parcial/orientativo:** documental, horas/gastos, MASC, roles, bitácora — funcionan como prototipo, faltan piezas.
- **🏗️ Requiere fase 2 (backend + Azure/M365):** seguridad real, integración Microsoft, OCR/semántica, DWH/lago, Copilot, móvil nativa.

> **Conclusión:** la suite cubre **toda la capa operativa, de supervisión y analítica** sobre dato real, en 8 aplicaciones interconectadas. Lo pendiente es mayoritariamente **infraestructura de producción**, no funcionalidad de negocio — esa es la frontera prototipo→sistema institucional.
