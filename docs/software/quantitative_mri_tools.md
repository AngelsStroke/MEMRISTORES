# MRI Toolkit

**Repositorio:** https://github.com/scientificcomputing/mri-toolkit

**Paquete Python:** mritk

**Licencia:** MIT

**Tipo de herramienta:** Posprocesamiento y análisis cuantitativo de RM

### Funciones principales

- Inspección de encabezados NIfTI.
- Revisión de matriz afín, dimensiones y tamaño de vóxel.
- Visualización ortogonal en terminal.
- Visualización interactiva con Napari.
- Estadísticas por regiones y máscaras.
- Generación de máscaras intracraneales y de LCR.
- Procesamiento de secuencias Look-Locker y Mixed.
- Creación de mapas T1 híbridos.
- Conversión de mapas T1 a R1.
- Cálculo de mapas de concentración de contraste.

### Utilidad para MEMRISTORES

- Verificar archivos NIfTI después de la conversión DICOM.
- Calcular estadísticas de regiones ya segmentadas.
- Obtener volúmenes, medias, medianas y percentiles.
- Integrar resultados de máscaras generadas con DeepPrep, FastSurfer,
  3D Slicer o ITK-SNAP.
- Automatizar análisis cuantitativos mediante línea de comandos.
- Explorar futuras líneas de investigación con mapas T1, R1 y contraste.

### Limitaciones

- No diagnostica enfermedad cerebral de pequeño vaso.
- No calcula Fazekas automáticamente.
- No detecta lacunas, microhemorragias o EPVS por sí solo.
- No identifica parkinsonismo vascular.
- Requiere máscaras o segmentaciones previas para análisis regional.
- No sustituye DeepPrep, FastSurfer, QSIPrep ni 3D Slicer.

### Comandos básicos

### Comandos básicos

```bash
pip install mritk
mritk info archivo.nii.gz
mritk info archivo.nii.gz --json
mritk show archivo.nii.gz
mritk napari archivo.nii.gz
mritk stats
mritk seg
mritk mask
mritk looklocker
mritk mixed
mritk hybrid
mritk t1-to-r1
mritk concentration
```

### Nombre de registro

`MRI_Toolkit_Analisis_Cuantitativo_NIfTI_T1_R1_Estadisticas`