# Apoyo metodológico y tecnológico

## DeepPrep

**Título:** DeepPrep: an accelerated, scalable and robust pipeline for neuroimaging preprocessing empowered by deep learning

**Autores:** Ren J, An N, Lin C, et al.

**Año:** 2025

**Revista:** Nature Methods

**DOI:** 10.1038/s41592-025-02599-1

**Repositorio oficial:** pBFSLab/DeepPrep

**Clasificación:** Metodología de neuroimagen computacional

**Tipo de imágenes:** RM estructural T1 y fMRI BOLD

**Funciones principales:**

- Segmentación cortical y subcortical.
- Reconstrucción de superficie cortical.
- Parcelación cerebral.
- Normalización espacial.
- Procesamiento automatizado de grandes volúmenes de imágenes.
- Generación de informes de control de calidad.

**Utilidad para MEMRISTORES:**

Puede apoyar una fase futura de segmentación, normalización y extracción
de medidas estructurales cerebrales.

**Limitación para el TFM actual:**

No estudia directamente enfermedad cerebral de pequeño vaso,
parkinsonismo vascular, Fazekas, lacunas, microhemorragias ni espacios
perivasculares.

**Decisión:** Conservar como respaldo metodológico.

**Título:** DeepPrep: an accelerated, scalable and robust pipeline for neuroimaging preprocessing empowered by deep learning

**Autores:** Ren J, An N, Lin C, et al.

**Año:** 2025

**Revista:** Nature Methods

**DOI:** 10.1038/s41592-025-02599-1

**Repositorio oficial:** https://github.com/pBFSLab/DeepPrep

**Tipo de artículo:** Comunicación breve / desarrollo y validación de software

**Clasificación:** Apoyo metodológico en neuroimagen computacional

**Objetivo del artículo:**

Presentar y validar DeepPrep, una tubería automatizada de preprocesamiento
de RM cerebral estructural T1 y fMRI basada en aprendizaje profundo.

**Funciones principales:**

- Segmentación cortical y subcortical.
- Reconstrucción de superficie cortical.
- Parcelación cerebral.
- Corrección de movimiento.
- Normalización espacial.
- Registro volumétrico y de superficies.
- Procesamiento de grandes lotes de estudios.
- Generación de informes de control de calidad.

**Resultados principales:**

- Evaluado en más de 55.000 estudios.
- Aproximadamente 10 veces más rápido que fMRIPrep.
- Mayor capacidad de procesamiento por lotes.
- Mejor tasa de finalización en cerebros clínicamente complejos.
- Resultados anatómicos y funcionales comparables o superiores en varias métricas.

**Relación con el TFM:**

No estudia directamente enfermedad cerebral de pequeño vaso ni
parkinsonismo vascular. Puede respaldar una futura fase de
segmentación, normalización y análisis volumétrico de estructuras
corticales y subcorticales.

**Limitaciones para el proyecto actual:**

- Se centra principalmente en T1 estructural y fMRI.
- No cuantifica Fazekas.
- No detecta automáticamente lacunas, microhemorragias ni EPVS.
- No procesa de forma específica DWI, ADC, SWI o DTI en la versión analizada.
- Los resultados requieren control visual experto.

**Decisión:** Conservar como respaldo metodológico.

## Rempe et al., 2025 — Desidentificación de imágenes médicas

**Referencia:**  
Rempe M, Heine L, Seibold C, Hörst F, Kleesiek J.  
De-identification of medical imaging data: a comprehensive tool for ensuring patient privacy.  
European Radiology. 2025;35:7809–7818.  
doi: 10.1007/s00330-025-11695-x

### Justificación metodológica

Este artículo respalda la fase de desidentificación y gobernanza de datos
del proyecto MEMRISTORES.

Los autores desarrollaron una herramienta abierta para desidentificar:

- imágenes DICOM de resonancia magnética;
- tomografía computarizada;
- archivos NIfTI;
- Whole Slide Images;
- datos crudos de RM Siemens Twix;
- imágenes con texto incrustado.

### Componentes del proceso

La herramienta combina:

- limpieza de metadatos;
- aplicación de perfiles DICOM;
- defacing;
- skull stripping;
- eliminación de texto incrustado;
- procesamiento de diferentes formatos de imagen médica.

### Relevancia para MEMRISTORES

En MEMRISTORES, la herramienta puede utilizarse antes de la conversión,
procesamiento y análisis de imágenes clínicas.

El flujo metodológico recomendado es:

```text
DICOM original restringido
→ desidentificación de metadatos
→ revisión de texto incrustado
→ defacing cuando exista cobertura facial
→ control de calidad de privacidad
→ asignación de identificador SUB-XXX
→ conversión a NIfTI
→ análisis de neuroimagen
```

### Nombre de registro
Rempe_2025_Deidentification_Medical_Imaging_Data.pdf