# GitHub MRI Topic — Índice de herramientas para MEMRISTORES

**Página fuente:** https://github.com/topics/mri

**Tipo de recurso:** Índice general de repositorios relacionados con resonancia magnética.

## Interpretación

La página `github.com/topics/mri` no corresponde a una sola herramienta.
Es un catálogo dinámico que reúne repositorios de:

- preprocesamiento de RM;
- control de calidad;
- segmentación anatómica;
- segmentación de lesiones;
- difusión y tractografía;
- visualización;
- reconstrucción;
- clasificación mediante inteligencia artificial;
- proyectos educativos.

La etiqueta `MRI` no garantiza que un repositorio sea cerebral, clínico,
validado o útil para enfermedad cerebral de pequeño vaso.

## Herramientas prioritarias para MEMRISTORES

### Nivel A — prioritarias

- MRIQC  
  https://github.com/nipreps/mriqc

- nnU-Net Perivascular Spaces  
  https://github.com/wpham17/nnUNet-Perivascular-Spaces

- TrueNet  
  https://github.com/v-sundaresan/truenet

- HyperMapp3r  
  https://github.com/AICONSlab/HyperMapp3r

- HD-SEQ-ID  
  https://github.com/CCI-Bonn/HD-SEQ-ID

- 3D Slicer  
  https://github.com/Slicer/Slicer

- DeepPrep  
  https://github.com/pBFSLab/DeepPrep

### Nivel B — estratégicas para fases futuras

- Brainchop  
  https://github.com/neuroneural/brainchop

- ENIGMA  
  https://github.com/MICA-MNI/ENIGMA

- Substantia Nigra Neuromelanin  
  https://github.com/emmabiondetti/substantia-nigra-neuromelanin

- MRI Toolkit  
  https://github.com/scientificcomputing/mri-toolkit

### Nivel C — educativas o experimentales

- Brain MRI 3D Renderer  
  https://github.com/Ftoutou/brain-mri-3d-renderer

- Brain MRI Modality Classification  
  https://github.com/gihuncho/brain-mri-modality-classification

- T2-DWI  
  https://github.com/ntnu-mr-cancer/T2-DWI

## Pipeline propuesto

```text
DICOM anonimizado
→ conversión a NIfTI
→ organización BIDS
→ HD-SEQ-ID
→ MRIQC
→ DeepPrep / FastSurfer / Brainchop
→ TrueNet / HyperMapp3r
→ nnU-Net PVS
→ 3D Slicer
→ extracción de estadísticas
→ MASTER_DATASET
```

### Nombre de registro
MRI_GITHUB_TOOLS_INDEX.md