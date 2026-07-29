## Substantia Nigra Neuromelanin MRI

**Repositorio:** https://github.com/emmabiondetti/substantia-nigra-neuromelanin

**Autora:** Emma Biondetti

**Tipo de herramienta:** Análisis cuantitativo de imágenes de RM sensibles a neuromelanina

**Lenguajes y dependencias:**

- Shell.
- MATLAB.
- NiftyReg.
- NIfTI Toolbox para MATLAB.

### Datos necesarios

- Imagen de RM sensible a neuromelanina de la sustancia negra.
- Imagen estructural T1 de toda la cabeza.
- Segmentación manual opcional de la sustancia negra.
- Datos en formato NIfTI.

### Funciones principales

- Corregistro de imagen sensible a neuromelanina con T1.
- Registro de T1 a una plantilla cerebral.
- Transformación de segmentaciones manuales al espacio común.
- Creación de mapas probabilísticos de la sustancia negra.
- Cálculo de señal relativa de neuromelanina.
- Evaluación de territorios asociativo, límbico y sensorimotor.

### Utilidad para MEMRISTORES

- Estudiar la integridad de la sustancia negra.
- Cuantificar la señal de neuromelanina por subregiones.
- Explorar diferencias entre parkinsonismo vascular y enfermedad de Parkinson.
- Investigar pacientes con patología vascular y neurodegenerativa coexistente.
- Añadir biomarcadores nigroestriatales en una fase futura.

### Relación con el TFM

La relación es indirecta pero estratégicamente importante.

No cuantifica enfermedad cerebral de pequeño vaso, pero permite estudiar
un biomarcador nigral que podría ayudar a distinguir un parkinsonismo
predominantemente vascular de un proceso neurodegenerativo o mixto.

### Limitaciones

- Requiere una secuencia específica sensible a neuromelanina.
- No funciona únicamente con T1, T2, FLAIR, DWI o SWI convencionales.
- Requiere MATLAB y NiftyReg.
- Puede necesitar segmentación manual.
- No calcula Fazekas, lacunas, microhemorragias ni EPVS.
- No genera un diagnóstico clínico automático.
- La licencia del repositorio debe verificarse antes de copiar o redistribuir el código.

**Decisión:** Conservar como herramienta futura para análisis de sustancia
negra y diferenciación entre parkinsonismo vascular, degenerativo y mixto.

Substantia_Nigra_Neuromelanin_MRI_Analisis_Nigral_Parkinsonismo