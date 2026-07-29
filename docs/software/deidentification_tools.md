## MEDE — Medical Image De-identification

**Repositorio:** https://github.com/TIO-IKIM/medical_image_deidentification

**Paquete:** `mede`

**Institución:** TIO-IKIM

**Tipo de herramienta:** Desidentificación local de imágenes médicas.

**Licencia:** Apache License 2.0 modificada con Commons Clause y
restricción de explotación comercial del código original.

### Modalidades compatibles

- Resonancia magnética.
- Tomografía computarizada.
- Ecografía.
- Whole Slide Images.
- Datos crudos de RM en formato Twix.
- Enhanced DICOM.

### Funciones principales

- Eliminación o modificación de metadatos DICOM.
- Aplicación de perfiles de desidentificación.
- Defacing de imágenes con cobertura facial.
- Skull stripping.
- Eliminación automática de texto incrustado.
- Refinamiento manual de texto o artefactos residuales.
- Renombrado de archivos.
- Procesamiento mediante Python o Docker.
- Multiprocesamiento.
- Soporte opcional de GPU.

### Instalación

```bash
pip install mede