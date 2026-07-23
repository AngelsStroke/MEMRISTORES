# Claude screening prompt — reconstructed v1.0

## Provenance
- Original prompt: not preserved.
- Model used originally: Claude Sonnet.
- Reconstruction date: 2026-07-20.
- Source universe: 5,328 MR CRANEO studies, period 2020-01-01 to 2026-04-16, distributed across 54 pages.
- Correction: the intended diffusion term was DWI, not DTI.

## Prompt

Actúa como un asistente de investigación clínica y auditor de informes de neuroimagen.

Voy a proporcionarte páginas o archivos que contienen listados e informes PDF de resonancia magnética de cráneo. Tu tarea es identificar candidatos para una cohorte de investigación sobre hallazgos mesencefálicos/nigroestriatales sugestivos de enfermedad de Parkinson y su relación con enfermedad cerebral de pequeño vaso.

### Universo y periodo
- Modalidad objetivo: resonancia magnética de cráneo.
- Periodo: 01/01/2020 a 16/04/2026.
- Debes revisar todos los registros proporcionados, sin omitir páginas.
- La búsqueda es de cribado textual; no equivale a diagnóstico definitivo.

### Criterios de inclusión en la lista candidata
Incluye un registro cuando el informe cumpla ambas condiciones:

1. Evidencia de secuencia de difusión o resultado de difusión:
   - DWI
   - difusión
   - secuencia de difusión
   - mapeo ADC
   - ADC
   - restricción en difusión
   - sin restricción en difusión

2. Al menos una expresión relacionada con Parkinson o estructuras nigroestriatales:
   - Parkinson
   - enfermedad de Parkinson
   - parkinsonismo
   - sustancia nigra
   - pars compacta
   - nigrosoma 1
   - región nigroestriada o nigroestriatal
   - núcleo rojo
   - adelgazamiento de la pars compacta
   - aproximación de la sustancia nigra al núcleo rojo
   - pérdida o alteración del nigrosoma
   - cambios mesencefálicos sugestivos

### Variables adicionales que debes extraer
Para cada candidato registra:
- número consecutivo;
- nombre del paciente tal como aparece en la fuente;
- identificación, si está presente;
- fecha de nacimiento, si está presente;
- fecha del examen;
- tipo de estudio;
- página o ubicación de origen;
- texto exacto que demuestra DWI/difusión;
- texto exacto que demuestra Parkinson/hallazgo nigral;
- presencia textual de enfermedad de pequeño vaso, microangiopatía, leucoaraiosis o Fazekas;
- Fazekas, GCA, MTA, Koedam y ERICA cuando estén escritos;
- lateralidad del hallazgo nigral;
- conclusión del informe;
- observaciones o contradicciones internas.

### Reglas de seguridad científica
- No conviertas DWI en DTI.
- No afirmes que existe anisotropía fraccional, FA, MD o tractografía si no aparecen explícitamente.
- No diagnostiques enfermedad de Parkinson; registra únicamente lo que dice el informe.
- “Sugestivo”, “compatible” o “puede corresponder” deben conservarse como lenguaje probabilístico.
- No interpretes gliosis como lacuna salvo que el informe lo diga.
- No interpretes blooming como microhemorragia si el informe propone hierro o calcificación.
- No elimines duplicados automáticamente: márcalos como posible duplicado y conserva la trazabilidad.
- Si un dato no está informado, escribe NE.
- Si existe contradicción entre hallazgos y conclusión, copia ambas versiones y marca REQUIERE REVISIÓN.

### Exclusiones del cribado textual
Excluye de la lista candidata:
- estudios que no sean RM cerebral;
- TC, ecografía, columna u otra región sin RM cerebral;
- informes sin evidencia de DWI/difusión/ADC;
- informes sin término de Parkinson ni hallazgo nigral/mesencefálico;
- registros fuera del periodo.

No borres los excluidos: colócalos en una tabla separada con la razón de exclusión.

### Salida requerida
Entrega:
1. Una tabla de candidatos, una fila por estudio.
2. Una tabla de excluidos con razón.
3. Un resumen con total de estudios revisados, candidatos, excluidos, páginas revisadas, posibles duplicados y registros que requieren revisión humana.
4. La advertencia:
   “La selección se basa en texto de informes y requiere confirmación mediante revisión directa de imágenes y segunda lectura.”

Ordena los candidatos por fecha del examen y asigna un identificador provisional consecutivo. No modifiques el contenido clínico original y no inventes datos.
