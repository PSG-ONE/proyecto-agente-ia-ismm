# 📊 Guía: Crear Diagrama de Gantt en Notion

## 🎯 **Objetivo**
Crear un diagrama de Gantt interactivo en Notion para el Proyecto de Agente IA usando la vista Timeline.

---

## ✅ **PASO 1: Crear la Base de Datos en Notion**

### 1.1 Abrir Notion
- Ve a tu workspace de Notion
- Crea una nueva página o usa una existente

### 1.2 Crear Base de Datos
1. Escribe `/database` y selecciona **"Database - Full page"**
2. O haz clic en **"+ New"** → **"Database"**
3. Nombra la base de datos: **"EDT - Proyecto Agente IA"**

---

## 📥 **PASO 2: Importar el CSV**

### 2.1 Importar Datos
1. En la esquina superior derecha de la base de datos, haz clic en **"⋮"** (tres puntos)
2. Selecciona **"Merge with CSV"** o **"Import"**
3. Selecciona el archivo: `EDT_PROYECTO_NOTION.csv`
4. Notion detectará automáticamente las columnas

### 2.2 Verificar Importación
Deberías ver:
- ✅ 96 tareas importadas
- ✅ Columnas: Tarea, Fase, Inicio, Fin, Duración, Recursos, Estado, Hito, Prioridad, Notas

---

## 🔧 **PASO 3: Configurar las Propiedades**

### 3.1 Ajustar Tipos de Columnas

Haz clic en cada encabezado de columna y configura:

| Columna | Tipo de Propiedad | Configuración |
|---------|-------------------|---------------|
| **Tarea** | Título | (ya configurado) |
| **Fase** | Select | Crear opciones: Fase 1, Fase 2, ..., Fase 9 |
| **Inicio** | Date | Formato: DD/MM/YYYY |
| **Fin** | Date | Formato: DD/MM/YYYY |
| **Duración (días)** | Number | Formato: Number |
| **Recursos** | Multi-select | Opciones: Persona 1, Persona 2, Ambos, Equipo |
| **Estado** | Status | Opciones: No iniciado, En progreso, Completado, Bloqueado |
| **Hito** | Checkbox | ☑ para hitos |
| **Prioridad** | Select | Opciones: Alta, Media, Baja |
| **Notas** | Text | (ya configurado) |

### 3.2 Agregar Propiedad Timeline (IMPORTANTE)

1. Haz clic en **"+ Add a property"**
2. Selecciona **"Date"**
3. Nómbrala: **"Timeline"**
4. Haz clic en el encabezado **"Timeline"** → **"Edit property"**
5. Activa **"Date range"** (rango de fechas)
6. Esta será la propiedad que usaremos para el Gantt

### 3.3 Copiar Fechas a Timeline

Necesitas copiar las fechas de "Inicio" y "Fin" a la columna "Timeline":

**Opción A: Manual**
- Para cada tarea, haz clic en "Timeline"
- Selecciona la fecha de inicio y fin

**Opción B: Fórmula (más rápido)**
- Notion no permite copiar automáticamente, pero puedes usar la vista para verificar

---

## 📅 **PASO 4: Crear la Vista Timeline (Gantt)**

### 4.1 Agregar Vista Timeline

1. En la parte superior de la base de datos, haz clic en **"+ Add a view"**
2. Selecciona **"Timeline"**
3. Nómbrala: **"Diagrama de Gantt"**

### 4.2 Configurar la Vista Timeline

1. Haz clic en **"..."** (tres puntos) en la vista Timeline
2. Selecciona **"Layout"**
3. Configura:
   - **Date property:** Timeline
   - **Show:** By month (o by week para más detalle)
   - **Color by:** Fase (para ver cada fase con un color diferente)

### 4.3 Ajustar Visualización

- **Zoom:** Usa los botones de zoom para ver todo el proyecto (Feb-Abr 2026)
- **Agrupación:** Agrupa por "Fase" para ver las 9 fases separadas
- **Filtros:** Puedes filtrar por Estado, Prioridad, Recursos, etc.

---

## 🎨 **PASO 5: Personalizar el Gantt**

### 5.1 Colores por Fase

1. Haz clic en **"..."** → **"Properties"**
2. Selecciona **"Color by: Fase"**
3. Cada fase tendrá un color diferente automáticamente

### 5.2 Mostrar Hitos

1. Crea un filtro: **"Hito is checked"**
2. Los hitos aparecerán como puntos en el timeline
3. Puedes usar un emoji 💎 en el nombre de los hitos para destacarlos

### 5.3 Agrupar por Fase

1. Haz clic en **"..."** → **"Group by"**
2. Selecciona **"Fase"**
3. Ahora verás las tareas agrupadas por fase en el Gantt

---

## 📊 **PASO 6: Vistas Adicionales Útiles**

### 6.1 Vista Tabla (para edición)

- Mantén la vista **"Table"** para editar datos fácilmente
- Usa la vista **"Timeline"** para visualizar el Gantt

### 6.2 Vista Kanban (opcional)

1. Crea una vista **"Board"**
2. Agrupa por **"Estado"**
3. Útil para seguimiento diario de tareas

### 6.3 Vista Calendario (opcional)

1. Crea una vista **"Calendar"**
2. Usa la propiedad **"Inicio"**
3. Útil para ver fechas de inicio de tareas

---

## 🔄 **PASO 7: Sincronizar Fechas con Timeline**

Como Notion no permite copiar automáticamente fechas entre propiedades, tienes dos opciones:

### Opción A: Usar solo la propiedad Timeline
1. Elimina las columnas "Inicio" y "Fin"
2. Usa solo "Timeline" con rango de fechas
3. Más simple pero pierdes las fechas individuales

### Opción B: Mantener ambas (RECOMENDADO)
1. Mantén "Inicio", "Fin" y "Timeline"
2. Usa "Inicio" y "Fin" para referencia
3. Usa "Timeline" para el Gantt
4. Actualiza manualmente cuando cambien fechas

---

## ✅ **VERIFICACIÓN FINAL**

Después de configurar, deberías tener:

- ✅ **Vista Timeline** mostrando todas las tareas en un Gantt
- ✅ **9 Fases** con colores diferentes
- ✅ **9 Hitos** marcados en el timeline
- ✅ **Fechas:** 03/02/2026 - 09/04/2026
- ✅ **Agrupación por Fase** para mejor organización
- ✅ **Filtros** por Estado, Prioridad, Recursos

---

## 🎯 **VENTAJAS DEL GANTT EN NOTION**

✅ **Interactivo:** Haz clic en cualquier tarea para ver detalles  
✅ **Colaborativo:** Comparte con tu equipo en tiempo real  
✅ **Flexible:** Cambia fechas arrastrando las barras  
✅ **Integrado:** Conecta con otras bases de datos de Notion  
✅ **Accesible:** Desde web, desktop y móvil  
✅ **Sin costo:** Incluido en el plan gratuito de Notion  

---

## 🚀 **PRÓXIMOS PASOS**

1. ✅ Importar el CSV a Notion
2. ✅ Configurar las propiedades
3. ✅ Crear la vista Timeline
4. ✅ Personalizar colores y agrupación
5. ✅ Compartir con el equipo
6. ✅ Actualizar el estado de las tareas conforme avanza el proyecto

---

## 💡 **TIPS ADICIONALES**

### Dependencias entre Tareas
- Notion no tiene dependencias nativas como MS Project
- **Solución:** Usa la columna "Notas" para indicar dependencias
- O crea una columna "Predecesoras" tipo Relation

### Recursos y Asignación
- Usa la columna "Recursos" tipo Multi-select
- O crea una relación con una base de datos de "Equipo"

### Seguimiento de Progreso
- Agrega una columna "Progreso (%)" tipo Number
- Actualiza manualmente el porcentaje completado

### Ruta Crítica
- Marca las tareas críticas con una etiqueta especial
- O usa un filtro para mostrar solo tareas de alta prioridad

---

## 📱 **ACCESO MÓVIL**

El Gantt de Notion funciona en:
- ✅ Web (notion.so)
- ✅ Desktop (Windows/Mac)
- ✅ Móvil (iOS/Android)
- ✅ Tablet (iPad/Android)

---

## 🆘 **SOLUCIÓN DE PROBLEMAS**

### Las fechas no se importan correctamente
- Verifica que el formato sea YYYY-MM-DD en el CSV
- Reimporta el archivo

### No veo la vista Timeline
- Asegúrate de tener una propiedad tipo "Date" con rango activado
- Crea la vista Timeline manualmente

### Las tareas no aparecen en el Gantt
- Verifica que todas las tareas tengan fechas en la columna "Timeline"
- Revisa los filtros activos

---

## 📞 **SOPORTE**

Si tienes problemas:
1. Revisa la [documentación oficial de Notion](https://www.notion.so/help/guides/creating-a-timeline-view)
2. Consulta la comunidad de Notion
3. Verifica que el CSV esté bien formateado

---

**¡Listo! Ahora tienes un Gantt profesional en Notion para tu Proyecto de Agente IA.** 🎉
