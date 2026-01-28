# 📘 GUÍA DE IMPORTACIÓN A MICROSOFT PROJECT

## Cómo importar la EDT a Microsoft Project

---

## 📋 ARCHIVOS GENERADOS

Has recibido los siguientes archivos para gestionar el proyecto:

1. **EDT_PROYECTO_AGENTE_IA.md** - Documento completo con toda la EDT en formato tabla
2. **EDT_PROYECTO_AGENTE_IA.csv** - Archivo CSV para importar a MS Project
3. **DIAGRAMA_GANTT_PROYECTO.md** - Visualización del cronograma y Gantt
4. **GUIA_IMPORTACION_MS_PROJECT.md** - Este documento

---

## 🚀 PASOS PARA IMPORTAR A MICROSOFT PROJECT

### OPCIÓN 1: Importación Directa de CSV

#### Paso 1: Abrir Microsoft Project
1. Abre **Microsoft Project** (versión 2016 o superior recomendada)
2. Crea un **nuevo proyecto en blanco**
3. Ve a **Archivo → Información del Proyecto**
4. Configura la **fecha de inicio: 03/02/2026**
5. Configura el **calendario: Estándar (Lunes a Viernes)**

#### Paso 2: Importar el archivo CSV
1. Ve a **Archivo → Abrir**
2. Cambia el tipo de archivo a **"Todos los archivos (*.*)"** o **"CSV (*.csv)"**
3. Selecciona el archivo **EDT_PROYECTO_AGENTE_IA.csv**
4. Aparecerá el **Asistente de importación**

#### Paso 3: Configurar el Asistente de Importación
1. **Pantalla 1:** Selecciona **"Nuevo mapa"** → Siguiente
2. **Pantalla 2:** Selecciona **"Tareas"** → Siguiente
3. **Pantalla 3:** Verifica que el delimitador sea **"Coma"**
4. **Pantalla 4:** Mapea las columnas de la siguiente manera:

| Columna CSV | Campo de MS Project |
|-------------|---------------------|
| WBS | WBS |
| Task Name | Name |
| Duration | Duration |
| Start Date | Start |
| Finish Date | Finish |
| Predecessors | Predecessors |
| Resource Names | Resource Names |
| Work (hours) | Work |
| Milestone | Milestone |
| Notes | Notes |

5. Haz clic en **Finalizar**

#### Paso 4: Verificar la importación
1. Verifica que todas las **tareas** se hayan importado correctamente
2. Verifica que las **dependencias** estén correctas
3. Verifica que los **hitos** estén marcados
4. Verifica que las **fechas** sean correctas

---

### OPCIÓN 2: Creación Manual en MS Project

Si la importación CSV presenta problemas, puedes crear el proyecto manualmente:

#### Paso 1: Configuración Inicial
```
Archivo → Información del Proyecto
- Fecha de inicio: 03/02/2026
- Calendario: Estándar
- Formato de fecha: DD/MM/AAAA
```

#### Paso 2: Crear la Estructura WBS
1. Ve a la vista **"Diagrama de Gantt"**
2. Crea la tarea principal: **"PROYECTO COMPLETO: AGENTE IA ISMM"**
3. Crea las 9 fases principales como **tareas de resumen**
4. Indenta las subtareas bajo cada fase

#### Paso 3: Configurar Duraciones
- Ingresa las duraciones en la columna **"Duración"**
- Usa el formato: **5d** para días, **0.5d** para medio día
- Para hitos, usa **0d**

#### Paso 4: Establecer Dependencias
- En la columna **"Predecesoras"**, ingresa los números de tarea
- Ejemplo: **"1.1.1"** para una dependencia simple
- Ejemplo: **"1.1.2;1.1.3"** para múltiples dependencias

#### Paso 5: Asignar Recursos
1. Ve a **Vista → Hoja de recursos**
2. Crea los recursos:
   - **Persona 1** (Capacidad: 100%)
   - **Persona 2** (Capacidad: 100%)
3. Vuelve a **Diagrama de Gantt**
4. Asigna recursos en la columna **"Nombres de recursos"**

---

## ⚙️ CONFIGURACIONES RECOMENDADAS EN MS PROJECT

### Configuración del Calendario

1. **Herramientas → Cambiar calendario laboral**
2. Configura:
   - Lunes a Viernes: **8:00 AM - 12:00 PM, 1:00 PM - 5:00 PM** (8 horas)
   - Sábado y Domingo: **No laborables**
3. Agrega **festivos locales** si aplica

### Configuración de Opciones

1. **Archivo → Opciones → Programación**
2. Configura:
   - Horas por día: **8**
   - Horas por semana: **40**
   - Días por mes: **20**
   - Tipo de tarea predeterminado: **Duración fija**

### Formato de Columnas

Agrega estas columnas a la vista de Gantt:
- **WBS** (Estructura de Desglose del Trabajo)
- **Predecesoras** (Dependencias)
- **Recursos** (Asignaciones)
- **Trabajo** (Horas estimadas)
- **Comienzo** (Fecha de inicio)
- **Fin** (Fecha de finalización)
- **% completado** (Para seguimiento)

---

## 🎨 PERSONALIZACIÓN DE LA VISTA DE GANTT

### Formato de Barras

1. **Formato → Estilos de barra**
2. Personaliza los colores:
   - **Tareas de resumen:** Azul oscuro
   - **Tareas normales:** Azul claro
   - **Hitos:** Rombo rojo
   - **Ruta crítica:** Rojo

### Líneas de Cuadrícula

1. **Formato → Líneas de cuadrícula**
2. Activa:
   - Líneas de fecha actual
   - Líneas de hitos
   - Líneas de la ruta crítica

### Etiquetas de Barras

1. **Formato → Estilos de barra → Texto**
2. Configura para mostrar:
   - **Izquierda:** Nombre del recurso
   - **Derecha:** % completado
   - **Arriba:** Duración

---

## 📊 VISTAS ÚTILES EN MS PROJECT

### Vista de Diagrama de Gantt
- **Uso:** Visualización general del cronograma
- **Acceso:** Vista → Diagrama de Gantt

### Vista de Uso de Recursos
- **Uso:** Ver carga de trabajo por persona
- **Acceso:** Vista → Uso de recursos

### Vista de Red
- **Uso:** Ver dependencias entre tareas
- **Acceso:** Vista → Diagrama de red

### Vista de Línea de Tiempo
- **Uso:** Presentación ejecutiva de hitos
- **Acceso:** Vista → Línea de tiempo

---

## 🔍 VERIFICACIÓN DE LA RUTA CRÍTICA

### Activar la Ruta Crítica

1. **Formato → Tareas críticas**
2. Las tareas críticas se mostrarán en **rojo**
3. Verifica que coincidan con las marcadas en la EDT

### Análisis de la Ruta Crítica

En este proyecto, **todas las fases están en la ruta crítica** porque:
- No hay paralelización completa entre fases
- Cada fase depende de la anterior
- Cualquier retraso afecta la fecha final

**Tareas NO críticas:**
- 1.2.2 Estructuración de diplomados
- 1.2.4 Creación de FAQs
- 1.3.2 Validación de portafolio
- 1.4.2 Configuración inicial Chatwoot
- 1.5.5 Sistema de embeddings
- 1.7.4 Pruebas de carga

---

## 📈 SEGUIMIENTO DEL PROYECTO

### Actualización Semanal

1. **Actualizar % completado** de cada tarea
2. **Marcar hitos** alcanzados
3. **Registrar fechas reales** de inicio y fin
4. **Comparar** con la línea base

### Crear Línea Base

1. **Proyecto → Establecer línea base**
2. Selecciona **"Línea base"**
3. Aplica a **"Proyecto completo"**
4. Esto te permitirá comparar el plan vs. la realidad

### Informes Recomendados

1. **Informe → Resumen del proyecto**
   - Estado general del proyecto
   
2. **Informe → Tareas críticas**
   - Tareas que no pueden retrasarse
   
3. **Informe → Tareas retrasadas**
   - Tareas que van detrás del cronograma
   
4. **Informe → Carga de trabajo**
   - Distribución de horas por recurso

---

## 🚨 SOLUCIÓN DE PROBLEMAS COMUNES

### Problema 1: Las fechas no coinciden

**Causa:** Calendario mal configurado  
**Solución:**
1. Verifica que el calendario sea de Lunes a Viernes
2. Verifica que no haya festivos no deseados
3. Recalcula el proyecto: **Proyecto → Calcular proyecto**

### Problema 2: Las dependencias no funcionan

**Causa:** Formato incorrecto de predecesoras  
**Solución:**
1. Usa el **número de ID de tarea**, no el WBS
2. Para múltiples predecesoras usa **punto y coma**: `2;3`
3. Verifica que no haya dependencias circulares

### Problema 3: Los recursos están sobreasignados

**Causa:** Más de 8 horas asignadas por día  
**Solución:**
1. Ve a **Vista → Uso de recursos**
2. Identifica los días con >8 horas
3. Usa **Herramientas → Redistribuir recursos**

### Problema 4: La importación CSV falla

**Causa:** Formato de fecha incorrecto  
**Solución:**
1. Abre el CSV en Excel
2. Cambia el formato de fechas a **DD/MM/AAAA**
3. Guarda y vuelve a importar

---

## 📱 EXPORTACIÓN Y COMPARTIR

### Exportar a PDF

1. **Archivo → Exportar → Crear PDF/XPS**
2. Selecciona el rango de fechas
3. Configura la orientación: **Horizontal**
4. Ajusta para que quepa en páginas

### Exportar a Excel

1. **Archivo → Guardar como**
2. Tipo: **Libro de Excel (*.xlsx)**
3. Selecciona las columnas a exportar

### Compartir en línea

1. **Archivo → Compartir**
2. Opciones:
   - **SharePoint**
   - **OneDrive**
   - **Project Online**

---

## 🎯 MEJORES PRÁCTICAS

### 1. Actualización Regular
- Actualiza el proyecto **semanalmente** como mínimo
- Registra el progreso real de las tareas
- Ajusta las estimaciones si es necesario

### 2. Comunicación
- Comparte el Gantt con el equipo
- Usa la **línea de tiempo** para presentaciones ejecutivas
- Exporta informes de estado semanales

### 3. Gestión de Cambios
- Documenta cualquier cambio en el alcance
- Actualiza la línea base si hay cambios aprobados
- Mantén un registro de cambios

### 4. Gestión de Riesgos
- Monitorea las tareas de la ruta crítica
- Identifica retrasos tempranamente
- Ten planes de contingencia para tareas de alto riesgo

---

## 📚 RECURSOS ADICIONALES

### Documentación de Microsoft Project
- [Guía oficial de MS Project](https://support.microsoft.com/es-es/project)
- [Tutoriales en video](https://support.microsoft.com/es-es/office/aprendizaje-de-project)

### Plantillas Útiles
- Plantilla de informe de estado
- Plantilla de seguimiento de riesgos
- Plantilla de registro de cambios

---

## ✅ CHECKLIST DE IMPORTACIÓN

Antes de considerar la importación completa, verifica:

- [ ] Todas las 9 fases están creadas
- [ ] Las 80+ tareas están importadas
- [ ] Los 9 hitos están marcados correctamente
- [ ] Las dependencias están configuradas
- [ ] Los 2 recursos están creados y asignados
- [ ] El calendario está configurado (Lun-Vie)
- [ ] La fecha de inicio es 03/02/2026
- [ ] La fecha de fin es 09/04/2026
- [ ] La duración total es 47 días
- [ ] La ruta crítica está visible
- [ ] Las horas totales suman 752h

---

## 🆘 SOPORTE

Si tienes problemas con la importación:

1. **Revisa esta guía** completa
2. **Consulta la documentación** de MS Project
3. **Contacta al gerente del proyecto** para asistencia
4. **Considera usar la opción manual** si el CSV falla

---

## 📝 NOTAS FINALES

### Importante:
- Este cronograma asume **trabajo continuo** de lunes a viernes
- **No incluye festivos** - agrégalos manualmente según tu país
- Las estimaciones son **conservadoras** - pueden ajustarse según experiencia del equipo
- Se recomienda agregar un **buffer de 1 semana** al final para contingencias

### Próximos Pasos:
1. ✅ Importar la EDT a MS Project
2. ✅ Configurar el calendario con festivos locales
3. ✅ Crear la línea base del proyecto
4. ✅ Compartir el cronograma con el equipo
5. ✅ Iniciar el seguimiento semanal

---

**Documento creado:** 27 de enero de 2026  
**Versión:** 1.0  
**Autor:** Antigravity AI  
**Para:** Proyecto Agente IA ISMM
