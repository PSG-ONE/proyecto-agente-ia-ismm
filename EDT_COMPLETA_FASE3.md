# 📊 EDT COMPLETA - PROYECTO AGENTE IA (DESDE FASE 3)

## Estructura de Desglose del Trabajo Detallada

**Proyecto:** Agente de IA para ISMM  
**Fecha de inicio:** 20/02/2026  
**Fecha de finalización:** 09/04/2026  
**Duración total:** 35 días laborables

---

## LEYENDA

- **WBS:** Work Breakdown Structure (Código jerárquico)
- **Duración:** Días laborables (d) u horas (h)
- **Predecesoras:** Tareas que deben completarse antes (FC = Fin a Comienzo)
- **Recursos:** P1 = Persona 1, P2 = Persona 2, Ambos = Trabajo colaborativo
- **% Asig:** Porcentaje de dedicación del recurso
- **Horas:** Horas estimadas de trabajo
- **Hito:** Punto de control importante (duración 0)
- **R.C.:** Ruta Crítica (Sí/No)

---

| WBS | Tarea | Dur. | Inicio | Fin | Predecesoras | Recursos | %Asig | Horas | Hito | R.C. | Estado | Notas |
|-----|-------|------|--------|-----|--------------|----------|-------|-------|------|------|--------|-------|
| **3.0** | **FASE 3: INTEGRACIÓN META API - WHATSAPP** | **7d** | **20/02/26** | **28/02/26** | **2.0** | **Equipo** | **100%** | **112h** | **No** | **Sí** | ⬜ Pendiente | **Fase crítica para comunicación** |
| 3.1 | Verificación del número telefónico | 1d | 20/02/26 | 20/02/26 | 2.0 | P1 | 100% | 8h | No | Sí | ⬜ Pendiente | Verificar en Meta Business Suite |
| 3.2 | Validación del portafolio empresarial | 1d | 20/02/26 | 20/02/26 | 2.0 | P2 | 100% | 8h | No | Sí | ⬜ Pendiente | Verificar estado en Meta |
| 3.3 | Preparación de documentación empresarial | 1d | 21/02/26 | 21/02/26 | 3.1;3.2 | P1 | 100% | 8h | No | Sí | ⬜ Pendiente | RUC, documentos legales, etc. |
| 3.4 | Envío y seguimiento de verificación | 2d | 24/02/26 | 25/02/26 | 3.3 | P2 | 50% | 8h | No | Sí | ⬜ Pendiente | Puede tomar 24-48h de espera |
| 3.5 | Creación de app en Meta for Developers | 1d | 24/02/26 | 24/02/26 | 3.3 | P1 | 100% | 8h | No | Sí | ⬜ Pendiente | Configurar app y permisos |
| 3.6 | Configuración de credenciales y tokens | 1d | 25/02/26 | 25/02/26 | 3.5 | P1 | 100% | 8h | No | Sí | ⬜ Pendiente | Access tokens, API keys |
| 3.7 | Configuración de webhooks | 1d | 26/02/26 | 26/02/26 | 3.6 | P2 | 100% | 8h | No | Sí | ⬜ Pendiente | Endpoints para recibir mensajes |
| 3.8 | Pruebas de conexión con WhatsApp API | 1d | 27/02/26 | 27/02/26 | 3.7 | Ambos | 100% | 16h | No | Sí | ⬜ Pendiente | Envío y recepción de mensajes |
| 3.9 | Documentación de credenciales | 0.5d | 28/02/26 | 28/02/26 | 3.8 | P1 | 100% | 4h | No | No | ⬜ Pendiente | Guardar en gestor de contraseñas |
| **H1** | **💎 HITO: WhatsApp API Verificado** | **0d** | **28/02/26** | **28/02/26** | **3.9** | **-** | **-** | **0h** | **Sí** | **Sí** | ⬜ Pendiente | **Conexión WhatsApp funcional** |
| | | | | | | | | | | | |
| **4.0** | **FASE 4: CONFIGURACIÓN DE CHATWOOT** | **5d** | **03/03/26** | **07/03/26** | **H3** | **Equipo** | **100%** | **80h** | **No** | **Sí** | **Plataforma de gestión** |
| 4.1 | Instalación de Chatwoot en servidor | 1.5d | 03/03/26 | 04/03/26 | H3 | P2 | 100% | 12h | No | Sí | Cloud o servidor propio |
| 4.2 | Configuración inicial de la plataforma | 0.5d | 03/03/26 | 03/03/26 | H3 | P1 | 100% | 4h | No | No | Configuración básica |
| 4.3 | Integración con WhatsApp Business API | 1d | 05/03/26 | 05/03/26 | 4.1 | P1 | 100% | 8h | No | Sí | Conectar webhooks de WhatsApp |
| 4.4 | Configuración de equipos y usuarios | 0.5d | 05/03/26 | 05/03/26 | 4.1 | P2 | 100% | 4h | No | No | Roles: admin, agentes, supervisores |
| 4.5 | Personalización de interfaz | 1d | 06/03/26 | 06/03/26 | 4.3 | P2 | 100% | 8h | No | No | Branding, colores, logo |
| 4.6 | Configuración de etiquetas y categorías | 0.5d | 06/03/26 | 06/03/26 | 4.3 | P1 | 100% | 4h | No | No | Organización de conversaciones |
| 4.7 | Creación de respuestas rápidas | 0.5d | 07/03/26 | 07/03/26 | 4.5;4.6 | P1 | 100% | 4h | No | No | Templates de respuestas comunes |
| 4.8 | Configuración de automatizaciones | 0.5d | 07/03/26 | 07/03/26 | 4.5;4.6 | P2 | 100% | 4h | No | No | Reglas de asignación automática |
| 4.9 | Pruebas de bandeja de entrada omnicanal | 0.5d | 07/03/26 | 07/03/26 | 4.7;4.8 | Ambos | 100% | 8h | No | Sí | Verificar funcionamiento completo |
| **H2** | **💎 HITO: Chatwoot Operativo** | **0d** | **07/03/26** | **07/03/26** | **4.9** | **-** | **-** | **0h** | **Sí** | **Sí** | ⬜ Pendiente | **Plataforma lista para IA** |
| | | | | | | | | | | | |
| **5.0** | **FASE 5: DESARROLLO AGENTE IA** | **10d** | **10/03/26** | **21/03/26** | **H4** | **Equipo** | **100%** | **160h** | **No** | **Sí** | **Núcleo del sistema** |
| 5.1 | Evaluación de plataformas de IA | 1d | 10/03/26 | 10/03/26 | H4 | Ambos | 100% | 16h | No | Sí | Claude, GPT-4, Gemini - análisis |
| 5.2 | Selección y justificación de plataforma | 0.5d | 11/03/26 | 11/03/26 | 5.1 | P1 | 100% | 4h | No | Sí | Documento de decisión técnica |
| 5.3 | Configuración de cuenta y API keys | 0.5d | 11/03/26 | 11/03/26 | 5.1 | P2 | 100% | 4h | No | Sí | Credenciales de plataforma elegida |
| 5.4 | Estructuración de base de conocimiento | 1.5d | 12/03/26 | 13/03/26 | 5.2;5.3 | P1 | 100% | 12h | No | Sí | Formato JSON/DB optimizado para IA |
| 5.5 | Desarrollo de sistema de embeddings | 1d | 12/03/26 | 12/03/26 | 5.2;5.3 | P2 | 100% | 8h | No | No | Vector database si es necesario |
| 5.6 | Entrenamiento - Carreras profesionales | 1d | 14/03/26 | 14/03/26 | 5.4 | P1 | 100% | 8h | No | Sí | Fine-tuning con datos de carreras |
| 5.7 | Entrenamiento - Diplomados | 1d | 14/03/26 | 14/03/26 | 5.4 | P2 | 100% | 8h | No | Sí | Fine-tuning con datos de diplomados |
| 5.8 | Entrenamiento - Cursos cortos | 1d | 17/03/26 | 17/03/26 | 5.6;5.7 | P1 | 100% | 8h | No | No | Fine-tuning con datos de cursos |
| 5.9 | Configuración de intents y entidades | 1d | 17/03/26 | 17/03/26 | 5.6;5.7 | P2 | 100% | 8h | No | Sí | NLU: detección de intenciones |
| 5.10 | Desarrollo de flujos conversacionales | 1.5d | 18/03/26 | 19/03/26 | 5.8;5.9 | Ambos | 100% | 24h | No | Sí | Lógica de conversación con contexto |
| 5.11 | Integración del agente con Chatwoot API | 1d | 19/03/26 | 19/03/26 | 5.10 | P1 | 100% | 8h | No | Sí | Conexión bidireccional |
| 5.12 | Configuración de reglas de escalamiento | 0.5d | 20/03/26 | 20/03/26 | 5.11 | P2 | 100% | 4h | No | No | Cuándo pasar a agente humano |
| 5.13 | Sistema de logging y monitoreo | 1d | 20/03/26 | 20/03/26 | 5.11 | P1 | 100% | 8h | No | Sí | Registro de conversaciones y métricas |
| 5.14 | Pruebas iniciales del agente | 1d | 21/03/26 | 21/03/26 | 5.12;5.13 | Ambos | 100% | 16h | No | Sí | 20+ casos de prueba |
| **H3** | **💎 HITO: Agente IA Funcional** | **0d** | **21/03/26** | **21/03/26** | **5.14** | **-** | **-** | **0h** | **Sí** | **Sí** | ⬜ Pendiente | **IA respondiendo correctamente** |
| | | | | | | | | | | | |
| **6.0** | **FASE 6: INTEGRACIÓN ZOHO CRM** | **5d** | **24/03/26** | **28/03/26** | **H5** | **Equipo** | **100%** | **80h** | **No** | **Sí** | **Gestión de leads** |
| 6.1 | Evaluación del API de Zoho CRM | 1d | 24/03/26 | 24/03/26 | H5 | P1 | 100% | 8h | No | No | Documentación y capacidades |
| 6.2 | Configuración de credenciales Zoho | 0.5d | 24/03/26 | 24/03/26 | H5 | P2 | 100% | 4h | No | Sí | OAuth, API keys |
| 6.3 | Configuración de webhooks bidireccionales | 1d | 25/03/26 | 25/03/26 | 6.2 | P2 | 100% | 8h | No | Sí | Sincronización en tiempo real |
| 6.4 | Desarrollo de sincronización de leads | 1.5d | 25/03/26 | 26/03/26 | 6.2 | P1 | 100% | 12h | No | Sí | Creación automática de leads |
| 6.5 | Mapeo de campos entre sistemas | 1d | 26/03/26 | 26/03/26 | 6.3;6.4 | P2 | 100% | 8h | No | No | Nombre, email, teléfono, programa |
| 6.6 | Implementación de flujo de actualización | 1d | 27/03/26 | 27/03/26 | 6.5 | P1 | 100% | 8h | No | Sí | Estados: nuevo, contactado, interesado |
| 6.7 | Pruebas de integración bidireccional | 1d | 28/03/26 | 28/03/26 | 6.6 | Ambos | 100% | 16h | No | Sí | 15+ casos de uso reales |
| **H4** | **💎 HITO: Zoho CRM Integrado** | **0d** | **28/03/26** | **28/03/26** | **6.7** | **-** | **-** | **0h** | **Sí** | **Sí** | ⬜ Pendiente | **CRM sincronizado** |
| | | | | | | | | | | | |
| **7.0** | **FASE 7: PRUEBAS Y CONTROL DE CALIDAD** | **5d** | **31/03/26** | **04/04/26** | **H6** | **Equipo** | **100%** | **80h** | **No** | **Sí** | **Validación completa** |
| 7.1 | Diseño de casos de prueba | 1d | 31/03/26 | 31/03/26 | H6 | Ambos | 100% | 16h | No | Sí | 50+ casos de prueba documentados |
| 7.2 | Pruebas unitarias de componentes | 1d | 01/04/26 | 01/04/26 | 7.1 | P1 | 100% | 8h | No | Sí | Cada módulo individualmente |
| 7.3 | Pruebas de integración end-to-end | 1.5d | 01/04/26 | 02/04/26 | 7.1 | P2 | 100% | 12h | No | Sí | Flujo completo: WhatsApp→IA→CRM |
| 7.4 | Pruebas de carga y estrés | 1d | 02/04/26 | 02/04/26 | 7.2;7.3 | P1 | 100% | 8h | No | Sí | Simular 100+ conversaciones |
| 7.5 | Pruebas de usuario (UAT) | 1d | 03/04/26 | 03/04/26 | 7.4 | Ambos | 50% | 8h | No | Sí | 10-15 casos con usuarios reales |
| 7.6 | Documentación de errores encontrados | 0.5d | 03/04/26 | 03/04/26 | 7.5 | P1 | 100% | 4h | No | No | Bug tracking |
| 7.7 | Corrección de errores críticos | 1d | 04/04/26 | 04/04/26 | 7.6 | Ambos | 100% | 16h | No | Sí | Prioridad alta |
| 7.8 | Validación final del sistema | 0.5d | 04/04/26 | 04/04/26 | 7.7 | Ambos | 100% | 8h | No | Sí | Sign-off de calidad |
| **H5** | **💎 HITO: Sistema Validado** | **0d** | **04/04/26** | **04/04/26** | **7.8** | **-** | **-** | **0h** | **Sí** | **Sí** | ⬜ Pendiente | **QA aprobado** |
| | | | | | | | | | | | |
| **8.0** | **FASE 8: CAPACITACIÓN Y DOCUMENTACIÓN** | **3d** | **07/04/26** | **08/04/26** | **H7** | **Equipo** | **75%** | **24h** | **No** | **No** | **Preparación del equipo** |
| 8.1 | Creación de manual de usuario | 1d | 07/04/26 | 07/04/26 | H7 | P1 | 100% | 8h | No | No | Con capturas de pantalla |
| 8.2 | Documentación técnica de arquitectura | 1d | 07/04/26 | 07/04/26 | H7 | P2 | 100% | 8h | No | No | Diagramas y especificaciones |
| 8.3 | Guías de troubleshooting | 0.5d | 08/04/26 | 08/04/26 | 8.1;8.2 | P1 | 100% | 4h | No | No | Problemas comunes y soluciones |
| 8.4 | Preparación de materiales de capacitación | 0.5d | 08/04/26 | 08/04/26 | 8.1;8.2 | P2 | 100% | 4h | No | No | Presentaciones y videos |
| 8.5 | Sesión de capacitación - Equipo admin | 0.5d | 08/04/26 | 08/04/26 | 8.3;8.4 | Ambos | 100% | 8h | No | No | Capacitación práctica |
| 8.6 | Sesión de capacitación - Equipo ventas | 0.5d | 08/04/26 | 08/04/26 | 8.5 | Ambos | 100% | 8h | No | No | Capacitación práctica |
| 8.7 | Sesión de preguntas y resolución de dudas | 0.25d | 08/04/26 | 08/04/26 | 8.6 | Ambos | 50% | 4h | No | No | Q&A con el equipo |
| 8.8 | Entrega de materiales digitales | 0.25d | 08/04/26 | 08/04/26 | 8.7 | P1 | 50% | 2h | No | No | Drive/email con documentación |
| **H6** | **💎 HITO: Equipo Capacitado** | **0d** | **08/04/26** | **08/04/26** | **8.8** | **-** | **-** | **0h** | **Sí** | **No** | ⬜ Pendiente | **Personal entrenado** |
| | | | | | | | | | | | |
| **9.0** | **FASE 9: DESPLIEGUE Y PRODUCCIÓN** | **2d** | **09/04/26** | **09/04/26** | **H8** | **Equipo** | **100%** | **24h** | **No** | **Sí** | **Lanzamiento oficial** |
| 9.1 | Configuración final de entorno producción | 0.5d | 09/04/26 | 09/04/26 | H8 | P2 | 100% | 4h | No | Sí | Servidores, DNS, SSL |
| 9.2 | Migración de datos y configuraciones | 0.5d | 09/04/26 | 09/04/26 | 9.1 | P1 | 100% | 4h | No | Sí | Desde ambiente de pruebas |
| 9.3 | Verificación de servicios en producción | 0.25d | 09/04/26 | 09/04/26 | 9.2 | Ambos | 100% | 4h | No | Sí | Health checks de todos los servicios |
| 9.4 | Lanzamiento oficial del agente IA | 0.25d | 09/04/26 | 09/04/26 | 9.3 | Ambos | 100% | 4h | No | Sí | Activación del número de WhatsApp |
| 9.5 | Monitoreo post-lanzamiento (48h) | 2d | 09/04/26 | 10/04/26 | 9.4 | Ambos | 50% | 16h | No | No | Vigilancia intensiva |
| 9.6 | Ajustes menores si son necesarios | 0.5d | 09/04/26 | 09/04/26 | 9.4 | P1 | 100% | 4h | No | No | Correcciones rápidas |
| **H7** | **💎 HITO: GO-LIVE PRODUCCIÓN** | **0d** | **09/04/26** | **09/04/26** | **9.4** | **-** | **-** | **0h** | **Sí** | **Sí** | ⬜ Pendiente | **🚀 SISTEMA EN VIVO** |

---

## RESUMEN DE TOTALES

| Concepto | Valor |
|----------|-------|
| **Total de tareas** | 61 tareas |
| **Total de hitos** | 7 hitos |
| **Duración total** | 35 días laborables |
| **Horas totales** | 560 horas |
| **Tareas en ruta crítica** | 38 tareas (62%) |
| **Holgura promedio** | 0-2 días |

---

## NOTAS IMPORTANTES

1. **Días laborables:** Solo se cuentan lunes a viernes
2. **Dependencias:** Todas son tipo FC (Fin a Comienzo) salvo indicación contraria
3. **Recursos:** P1 y P2 pueden trabajar en paralelo
4. **Ruta crítica:** Tareas que no pueden retrasarse sin afectar fecha final
5. **Holgura:** Tiempo de margen antes de afectar la ruta crítica
6. **Buffer:** Se ha incluido tiempo de buffer en tareas de alta incertidumbre

---

**Versión:** 2.0  
**Fecha de creación:** 28/01/2026  
**Última actualización:** 28/01/2026
