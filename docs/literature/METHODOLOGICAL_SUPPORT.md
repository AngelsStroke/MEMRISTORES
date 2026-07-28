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
## DeepPrep

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