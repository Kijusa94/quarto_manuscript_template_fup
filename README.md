# Plantilla de manuscrito/reporte (Quarto)

Plantilla mínima para generar manuscritos y reportes de clase usando Quarto. Incluye estructura recomendada, metadatos y ejemplos para exportar a HTML, PDF y Word.

## Requisitos
- Quarto instalado: https://quarto.org
- R, Python o otro motor soportado (según los snippets del proyecto)
- Dependencias (paquetes) opcionales según los ejemplos incluidos

## Instalación
1. Clonar el repositorio.
2. Abrir la carpeta del proyecto en tu IDE preferido.
3. Cree un nuevo entorno de Python. Ejecute en su terminal `python -m venv .venv`.
4. Activar el entorno.
5. Instalar `requirements.txt`. Use: `pip install -r requirements.txt`.

## Uso rápido
- Vista previa interactiva:
    - quarto preview .
- Renderizar a formato final:
    - quarto render 

## Personalización
- Editar el bloque YAML en los archivos .qmd para cambiar título, autor, fecha, etc.

## Estructura sugerida para el proyecto
- manuscript.qmd — documento principal
- sections/ — capítulos o secciones parciales
- figures/ — figuras y recursos
- tables/ — tablas en formatos .md o TeX.
- references.bib — bibliografía

## Contribución
Ajustes simples y mejoras en secciones, estilos y ejemplos son bienvenidos. Abrir issues o pull requests con cambios claros y pruebas de renderizado.

## Licencia
Vease archivo de licencia.
