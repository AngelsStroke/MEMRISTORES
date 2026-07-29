## HD-SEQ-ID

**Repositorio:** https://github.com/CCI-Bonn/HD-SEQ-ID

**Publicación asociada:** Mahmutoglu MA, Preetha CJ, Meredig H, et al.
Deep Learning-based Identification of Brain MRI Sequences Using a Model
Trained on Large Multicentric Study Cohorts. Radiology: Artificial
Intelligence. 2023.

**DOI:** 10.1148/ryai.230095

**Tipo de herramienta:** Clasificación automática de secuencias de RM
cerebral mediante aprendizaje profundo.

### Secuencias identificadas

- T1 sin contraste.
- T1 con contraste.
- T2.
- FLAIR.
- SWI.
- ADC.
- DWI de bajo valor b.
- DWI de alto valor b.
- T2* y secuencias relacionadas con perfusión DSC.

### Entrada

- Archivos NIfTI 3D o 4D.
- Carpeta con imágenes `.nii.gz`.

### Salida

- Archivo `predictions.csv`.
- Etiqueta de secuencia estimada.
- Copias NIfTI opcionalmente renombradas con la clase predicha.

### Utilidad para MEMRISTORES

- Organizar automáticamente secuencias de RM cerebral.
- Verificar disponibilidad de DWI, ADC, SWI y FLAIR.
- Estandarizar nombres de archivos provenientes de diferentes centros.
- Preparar imágenes para DeepPrep, nnU-Net PVS y otros modelos.
- Apoyar la extracción automatizada de variables de disponibilidad.
- Reducir errores de selección de secuencias en cohortes grandes.

### Variables futuras sugeridas

- `T1_available`
- `T1_postcontrast_available`
- `T2_available`
- `FLAIR_available`
- `DWI_low_b_available`
- `DWI_high_b_available`
- `ADC_available`
- `SWI_available`
- `sequence_id_predicted_class`
- `sequence_id_confidence`
- `sequence_id_manual_qc`
- `sequence_id_corrected_class`

### Fortalezas

- Entrenado con datos multicéntricos procedentes de numerosos centros.
- Compatible con variabilidad de equipos y parámetros de adquisición.
- Diferencia DWI de bajo y alto valor b.
- Identifica SWI y ADC.
- Disponible para CPU y GPU.
- Genera resultados en CSV.
- Puede utilizarse sin renombrar los archivos originales.

### Limitaciones

- Fue desarrollado principalmente con protocolos de tumores cerebrales.
- Las secuencias no incluidas se fuerzan dentro de una de las nueve clases.
- Puede clasificar erróneamente TOF, Scout, ASL, DTI u otras secuencias.
- No distingue individualmente los mapas de perfusión DSC.
- No procesa directamente DICOM.
- No evalúa calidad diagnóstica.
- No segmenta lesiones de enfermedad cerebral de pequeño vaso.
- No calcula Fazekas, lacunas, microhemorragias ni EPVS.
- Requiere validación visual antes de utilizar las predicciones.
- El código de entrenamiento no está disponible.

### Flujo propuesto

```text
DICOM anonimizado
→ conversión a NIfTI
→ HD-SEQ-ID
→ predictions.csv
→ control manual
→ selección de T1/T2/FLAIR/SWI/DWI/ADC
→ modelos de análisis específicos
→ MASTER_DATASET
```

### Nombre de registro
HD_SEQ_ID_Clasificacion_Automatica_Secuencias_RM_Cerebral