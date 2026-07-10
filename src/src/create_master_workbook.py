from artifact_tool import Workbook, SpreadsheetFile
import csv, os, textwrap, json

out_dir = "/mnt/data/acv_neuroimagen_github"
os.makedirs(out_dir, exist_ok=True)

wb = Workbook.create()

# ---------- Styles ----------
title_fmt = {
    "fill": "#17365D",
    "font": {"bold": True, "color": "#FFFFFF", "size": 14},
    "horizontal_alignment": "center",
    "vertical_alignment": "center",
}
header_fmt = {
    "fill": "#1F4E78",
    "font": {"bold": True, "color": "#FFFFFF"},
    "horizontal_alignment": "center",
    "vertical_alignment": "center",
    "wrap_text": True,
}
subheader_fmt = {
    "fill": "#D9EAF7",
    "font": {"bold": True, "color": "#17365D"},
    "wrap_text": True,
}
note_fmt = {
    "fill": "#FFF2CC",
    "font": {"color": "#7F6000"},
    "wrap_text": True,
}

# ---------- README sheet ----------
s = wb.worksheets.add("INSTRUCCIONES")
s.merge_cells("A1:H1")
s.get_range("A1").values = [["MATRIZ MAESTRA DE BIOMARCADORES NEURORRADIOLÓGICOS POST-ACV"]]
s.get_range("A1:H1").format = title_fmt
instructions = [
    ["Campo", "Regla operativa"],
    ["Identificador", "Usar ACV-0001, ACV-0002… Nunca nombres, cédula, historia clínica, teléfono, dirección ni fechas completas identificables en repositorios públicos."],
    ["Unidad de análisis", "Una fila por estudio de imagen. Si un paciente tiene varios controles, conservar el mismo patient_id y asignar study_id creciente (p. ej., ACV-0001-RM01, ACV-0001-RM02)."],
    ["Fuente primaria", "Registrar informe radiológico y, cuando exista acceso legítimo, revisión directa de las imágenes. No sustituir ausencia de secuencia por ausencia de lesión."],
    ["Valores faltantes", "NA = dato no disponible; NE = no evaluable por calidad/artefacto; NS = secuencia necesaria no realizada; 0 = evaluado y ausente; 1 = presente."],
    ["Trazabilidad", "Conservar texto original desidentificado, persona que codifica, fecha de codificación, versión del diccionario y fuente bibliográfica."],
    ["Control de calidad", "Idealmente doble lectura independiente y adjudicación de discrepancias. Registrar confianza: alta, moderada o baja."],
    ["Uso en GitHub", "Subir solo datos completamente anonimizados/pseudonimizados autorizados. No subir DICOM, capturas, informes íntegros ni fechas exactas sin aprobación ética y evaluación de riesgo de reidentificación."],
]
s.get_range(f"A3:B{2+len(instructions)}").values = instructions
s.get_range("A3:B3").format = header_fmt
s.get_range("A4:B10").format.wrap_text = True
s.get_range("A:A").format.column_width = 24
s.get_range("B:B").format.column_width = 95
s.freeze_panes.freeze_rows(3)

# ---------- Master sheet ----------
master = wb.worksheets.add("MATRIZ_MAESTRA")
headers = [
    "patient_id","study_id","cohort_year","index_event_type","index_event_date_shifted",
    "age_at_event","sex","days_event_to_imaging","modality","field_strength_T",
    "sequence_T1","sequence_T2","sequence_FLAIR","sequence_DWI","sequence_ADC",
    "sequence_T2star_GRE","sequence_SWI","sequence_TOF_MRA","sequence_CTA","image_quality",
    "acute_infarct_present","acute_infarct_count","acute_infarct_laterality","acute_infarct_territory",
    "acute_infarct_location_detail","acute_infarct_max_diameter_mm","acute_infarct_volume_ml",
    "dwi_positive","adc_restriction","flair_positive","dwi_flair_mismatch",
    "hemorrhagic_transformation_present","hemorrhagic_transformation_ECASS","remote_ICH_present",
    "lacune_present","lacune_count","lacune_locations","recent_small_subcortical_infarct",
    "WMH_present","fazekas_periventricular","fazekas_deep","WMH_total_fazekas_max",
    "WMH_symmetry","WMH_location_detail","microbleed_present","microbleed_total_count",
    "microbleed_lobar_count","microbleed_deep_count","microbleed_infratentorial_count",
    "microbleed_distribution","cortical_superficial_siderosis","cSS_focal_or_disseminated",
    "PVS_present","PVS_basal_ganglia_grade","PVS_centrum_semiovale_grade",
    "brain_atrophy_present","global_cortical_atrophy_grade","medial_temporal_atrophy_right",
    "medial_temporal_atrophy_left","posterior_cortical_atrophy_grade","strategic_infarct_present",
    "strategic_infarct_location","old_cortical_infarct_present","old_subcortical_infarct_present",
    "old_infratentorial_infarct_present","encephalomalacia_gliosis","large_artery_stenosis_present",
    "stenosis_vessel","stenosis_percent_category","intracranial_atherosclerosis",
    "dolichoectasia","aneurysm_present","vascular_malformation_present",
    "total_CSVD_score_0_4","probable_CAA_Boston2_category","vascular_parkinsonism_pattern",
    "other_incidental_findings","radiology_text_deidentified","coder_summary",
    "coding_confidence","primary_reader","second_reader","adjudicated",
    "dictionary_version","coding_date","source_type","notes"
]
master.get_range("A1:CG1").values = [headers]  # 85 cols = CG
master.get_range("A1:CG1").format = header_fmt
master.freeze_panes.freeze_rows(1)
master.freeze_panes.freeze_columns(2)
master.get_range("A2:CG501").format.wrap_text = True
master.get_range("A:B").format.column_width = 16
master.get_range("C:CG").format.column_width = 15
for col in ["X","Y","AQ","BR","BS","BT","CG"]:
    master.get_range(f"{col}:{col}").format.column_width = 34

# data validation
binary_cols = ["K","L","M","N","O","P","Q","R","S","U","AC","AD","AF","AG","AI","AJ","AM","AS","AT","AY","BE","BF","BI","BJ","BK","BL","BM","BN","BO","BP","BQ","BS","BT","BU"]
for c in binary_cols:
    master.get_range(f"{c}2:{c}501").data_validation = {"rule":{"type":"list","values":["0","1","NA","NE","NS"]}}
master.get_range("F2:F501").data_validation = {"rule":{"type":"wholeNumber","operator":"between","formula1":0,"formula2":120}}
master.get_range("G2:G501").data_validation = {"rule":{"type":"list","values":["F","M","Otro/NR","NA"]}}
master.get_range("I2:I501").data_validation = {"rule":{"type":"list","values":["RM","TC","Angio-TC","Angio-RM","Otro"]}}
master.get_range("T2:T501").data_validation = {"rule":{"type":"list","values":["Adecuada","Limitada","No evaluable","NA"]}}
master.get_range("AE2:AE501").data_validation = {"rule":{"type":"list","values":["HI1","HI2","PH1","PH2","NA","NE"]}}
master.get_range("AO2:AP501").data_validation = {"rule":{"type":"list","values":["0","1","2","3","NA","NE","NS"]}}
master.get_range("BQ2:BQ501").data_validation = {"rule":{"type":"list","values":["Alta","Moderada","Baja"]}}
master.get_range("BU2:BU501").data_validation = {"rule":{"type":"list","values":["0","1","NA"]}}

# ---------- Dictionary ----------
d = wb.worksheets.add("DICCIONARIO_VARIABLES")
dict_headers = ["variable","dominio","tipo","valores_permitidos_unidad","definicion_operativa","secuencia_fuente","regla_de_codificacion","prioridad"]
d.get_range("A1:H1").values = [dict_headers]
d.get_range("A1:H1").format = header_fmt

rows = []
def add(var, domain, typ, vals, definition, seq, rule, priority="Núcleo"):
    rows.append([var,domain,typ,vals,definition,seq,rule,priority])

# Core metadata
add("patient_id","Identificación","Texto","ACV-0001…","Código pseudonimizado estable por paciente.","Matriz clínica","Asignación ascendente; nunca reutilizar.","Crítica")
add("study_id","Identificación","Texto","ACV-0001-RM01…","Código único por estudio.","Matriz clínica","Mismo patient_id, número de estudio ascendente.","Crítica")
add("days_event_to_imaging","Temporal","Entero","días","Intervalo entre evento índice y adquisición.","Matriz/fecha desplazada","Usar fecha desplazada coherente o diferencia ya calculada.","Crítica")
add("modality","Adquisición","Categórica","RM/TC/Angio-TC/Angio-RM","Modalidad principal.","Cabecera del estudio","No inferir.","Crítica")
add("field_strength_T","Adquisición","Numérica","1.5/3/otro/NA","Intensidad de campo del equipo RM.","DICOM/informe","NA si no consta.","Complementaria")
add("image_quality","Calidad","Ordinal","Adecuada/Limitada/No evaluable","Calidad global para calificación visual.","Todas","Registrar causa en notas.","Crítica")

# Acute stroke
add("acute_infarct_present","Lesión índice","Binaria","0/1/NA/NE/NS","Lesión isquémica aguda o reciente compatible con evento índice.","DWI/ADC ± FLAIR","1 solo si está descrita u observada.","Crítica")
add("acute_infarct_territory","Lesión índice","Categórica múltiple","ACA/ACM/ACP/vertebrobasilar/lacunar/frontera/otro","Territorio vascular dominante.","DWI/FLAIR/T2","Separar múltiples territorios con |.","Crítica")
add("acute_infarct_location_detail","Lesión índice","Texto controlado","lóbulos, ganglios basales, tálamo, cápsula, tronco, cerebelo…","Localización anatómica detallada.","DWI/ADC/FLAIR","Usar nomenclatura anatómica, lado y profundidad.","Crítica")
add("dwi_flair_mismatch","Lesión índice","Binaria","0/1/NA/NE/NS","DWI positiva sin hiperintensidad FLAIR correspondiente.","DWI+FLAIR","Solo evaluable si ambas secuencias existen y son interpretables.","Complementaria")
add("hemorrhagic_transformation_ECASS","Complicación","Ordinal","HI1/HI2/PH1/PH2","Clasificación radiológica de transformación hemorrágica.","TC o GRE/SWI","Codificar solo si puede aplicarse ECASS; de otro modo NA/NE.","Complementaria")

# STRIVE-2 SVD
add("lacune_present","CSVD","Binaria","0/1/NA/NE","Cavidad subcortical redonda u ovoide, típicamente 3–15 mm, con señal similar a LCR y halo FLAIR posible, compatible con infarto/hemorragia subcortical antigua.","T1/T2/FLAIR","Excluir espacios perivasculares y cavidades corticales.","Crítica")
add("recent_small_subcortical_infarct","CSVD","Binaria","0/1/NA/NE/NS","Infarto reciente pequeño en territorio de una arteriola perforante.","DWI/ADC/FLAIR","Registrar independientemente de lacuna antigua.","Núcleo")
add("fazekas_periventricular","WMH","Ordinal","0–3","Grado visual de hiperintensidades periventriculares.","FLAIR/T2","0 ausente; 1 casquetes/línea fina; 2 halo liso; 3 extensión irregular a sustancia blanca profunda.","Crítica")
add("fazekas_deep","WMH","Ordinal","0–3","Grado visual de hiperintensidades profundas.","FLAIR/T2","0 ausente; 1 focos puntiformes; 2 confluencia inicial; 3 grandes áreas confluentes.","Crítica")
add("microbleed_present","Microhemorragias","Binaria","0/1/NA/NE/NS","Foco pequeño, redondo/ovoide, hipointenso con blooming en secuencia sensible a susceptibilidad, no explicado por mimetizadores.","SWI o T2*-GRE","Aplicar MARS/BOMBS; excluir vasos, calcificación, hierro fisiológico y artefactos.","Crítica")
add("microbleed_distribution","Microhemorragias","Categórica","lobar/deep/infratentorial/mixed","Distribución anatómica global.","SWI/T2*-GRE","Lobar estricta, profunda, infratentorial o mixta.","Crítica")
add("cortical_superficial_siderosis","Hemorragia crónica","Binaria","0/1/NA/NE/NS","Depósito lineal de hemosiderina en surcos corticales.","SWI/T2*-GRE","Diferenciar de vasos y artefacto.","Núcleo")
add("PVS_basal_ganglia_grade","PVS","Ordinal","0–4/NA/NE","Carga visual de espacios perivasculares en ganglios basales.","T2","Usar escala semicuantitativa definida en protocolo local; registrar corte de referencia.","Núcleo")
add("PVS_centrum_semiovale_grade","PVS","Ordinal","0–4/NA/NE","Carga visual de espacios perivasculares en centrum semiovale.","T2","Misma escala y corte de referencia para toda la cohorte.","Núcleo")
add("total_CSVD_score_0_4","Carga total CSVD","Entero","0–4/NA","Suma pragmática de lacunas, microbleeds, WMH moderada-grave y PVS BG moderados-graves.","RM multimodal","1 punto por cada componente conforme al algoritmo definido en LEYENDA_ESCALAS.","Crítica")

# Atrophy & patterns
add("global_cortical_atrophy_grade","Atrofia","Ordinal","0–3/NA/NE","Grado visual global de ensanchamiento sulcal y pérdida de volumen.","T1/FLAIR/TC","Aplicar escala visual elegida de forma consistente.","Complementaria")
add("medial_temporal_atrophy_right","Atrofia","Ordinal","0–4/NA/NE","Atrofia temporal medial derecha.","T1 coronal","Escala MTA de Scheltens; considerar ajuste por edad en análisis.","Complementaria")
add("medial_temporal_atrophy_left","Atrofia","Ordinal","0–4/NA/NE","Atrofia temporal medial izquierda.","T1 coronal","Escala MTA de Scheltens; considerar ajuste por edad en análisis.","Complementaria")
add("strategic_infarct_present","Fenotipo cognitivo","Binaria","0/1/NA/NE","Infarto en localización potencialmente estratégica para cognición/conducta.","T1/T2/FLAIR/DWI","Registrar localización específica; evitar concluir causalidad automática.","Núcleo")
add("vascular_parkinsonism_pattern","Fenotipo motor","Categórica","ninguno/compatible/no concluyente/NA","Patrón radiológico compatible con parkinsonismo vascular, no diagnóstico clínico.","RM","Basar en carga vascular y localización; requiere correlación clínica.","Exploratoria")
add("probable_CAA_Boston2_category","CAA","Categórica","no aplicable/no probable/probable/posible según protocolo","Categoría derivada solo cuando edad, clínica y marcadores requeridos están disponibles.","SWI/GRE + clínica","No calcular con imagen aislada incompleta; documentar criterios.","Exploratoria")

# QA
add("radiology_text_deidentified","Trazabilidad","Texto","texto libre","Extracto del informe sin identificadores.","Informe","Eliminar nombres, IDs, fechas exactas y centros si generan riesgo.","Crítica")
add("coder_summary","Trazabilidad","Texto","texto libre","Resumen estandarizado de hallazgos codificados.","Todas","Describir positivos, negativos evaluables y limitaciones.","Crítica")
add("coding_confidence","Calidad","Ordinal","Alta/Moderada/Baja","Confianza del codificador.","Todas","Alta: secuencias adecuadas + hallazgo claro; moderada: limitación menor; baja: ambigüedad/solo informe.","Crítica")

d.get_range(f"A2:H{1+len(rows)}").values = rows
d.get_range("A1:H1").format = header_fmt
d.get_range(f"A2:H{1+len(rows)}").format.wrap_text = True
widths = [30,22,16,28,55,25,65,16]
for i,w in enumerate(widths):
    col = chr(65+i)
    d.get_range(f"{col}:{col}").format.column_width = w
d.freeze_panes.freeze_rows(1)

# ---------- Scales legend ----------
l = wb.worksheets.add("LEYENDA_ESCALAS")
legend_headers = ["escala_marcador","categoría","criterio_operativo","comentario_metodológico"]
l.get_range("A1:D1").values = [legend_headers]
l.get_range("A1:D1").format = header_fmt
legend = [
    ["Valores faltantes","0","Marcador evaluado y ausente.","No equivale a NA, NE o NS."],
    ["Valores faltantes","1","Marcador presente.","Debe poder rastrearse al informe o imagen."],
    ["Valores faltantes","NA","Dato no disponible.","No consta o no fue proporcionado."],
    ["Valores faltantes","NE","No evaluable.","Secuencia existe, pero calidad/artefacto impide decidir."],
    ["Valores faltantes","NS","Secuencia no realizada/no disponible.","Ej.: microbleeds no calificables sin SWI/T2*-GRE."],
    ["Fazekas periventricular","0","Ausente.","FLAIR/T2."],
    ["Fazekas periventricular","1","Casquetes o revestimiento fino.","No confundir con halo completo."],
    ["Fazekas periventricular","2","Halo liso.","Separado de confluencia profunda."],
    ["Fazekas periventricular","3","Irregular, extendiéndose a sustancia blanca profunda.","Carga avanzada."],
    ["Fazekas profunda","0","Ausente.","FLAIR/T2."],
    ["Fazekas profunda","1","Focos puntiformes.","Leve."],
    ["Fazekas profunda","2","Confluencia inicial.","Moderada."],
    ["Fazekas profunda","3","Grandes áreas confluentes.","Grave."],
    ["Total CSVD 0–4","Lacuna","1 punto si existe ≥1 lacuna.","Definición STRIVE-2."],
    ["Total CSVD 0–4","Microbleed","1 punto si existe ≥1 microbleed.","Requiere GRE/SWI."],
    ["Total CSVD 0–4","WMH","1 punto si Fazekas profunda 2–3 o periventricular 3.","Regla original pragmática."],
    ["Total CSVD 0–4","PVS-BG","1 punto si PVS en ganglios basales grado 2–4 (moderado-grave según escala adoptada).","Fijar escala de PVS antes de análisis final."],
    ["MARS microbleeds","Lobar","Corteza y sustancia blanca subcortical lobar.","Contar por regiones y lado."],
    ["MARS microbleeds","Profunda","Ganglios basales, tálamo, cápsulas y sustancia blanca profunda/periventricular.","Registrar conteo."],
    ["MARS microbleeds","Infratentorial","Tronco encefálico y cerebelo.","Registrar conteo."],
    ["ECASS HT","HI1","Pequeñas petequias periféricas sin efecto de masa.","Transformación hemorrágica."],
    ["ECASS HT","HI2","Petequias confluentes sin efecto de masa.","Transformación hemorrágica."],
    ["ECASS HT","PH1","Hematoma ≤30% del área infartada con leve efecto de masa.","Transformación hemorrágica."],
    ["ECASS HT","PH2","Hematoma >30% del área infartada con efecto de masa significativo.","Transformación hemorrágica."],
]
l.get_range(f"A2:D{1+len(legend)}").values = legend
l.get_range("A1:D1").format = header_fmt
l.get_range(f"A2:D{1+len(legend)}").format.wrap_text = True
for col,w in zip(["A","B","C","D"],[26,18,70,50]):
    l.get_range(f"{col}:{col}").format.column_width = w
l.freeze_panes.freeze_rows(1)

# ---------- Sources ----------
src = wb.worksheets.add("FUENTES")
src_headers = ["tema","referencia","uso_en_matriz","url_doi"]
src.get_range("A1:D1").values = [src_headers]
src.get_range("A1:D1").format = header_fmt
sources = [
    ["Estándares CSVD","Duering M, et al. Neuroimaging standards for research into small vessel disease—advances since 2013 (STRIVE-2). Lancet Neurol. 2023.","Definiciones de lacuna, WMH, PVS, microbleeds, infartos subcorticales recientes y estándares de reporte.","https://doi.org/10.1016/S1474-4422(23)00131-X"],
    ["Carga total CSVD","Staals J, et al. Stroke subtype, vascular risk factors, and total MRI brain small-vessel disease burden. Neurology. 2014.","Puntuación total pragmática 0–4.","https://doi.org/10.1212/WNL.0000000000000837"],
    ["Microbleeds MARS","Gregoire SM, et al. The Microbleed Anatomical Rating Scale (MARS). Neurology. 2009.","Definición, localización y recuento anatómico de microbleeds.","https://doi.org/10.1212/WNL.0b013e3181c34a7d"],
    ["Microbleeds BOMBS","Cordonnier C, et al. Improving interrater agreement about brain microbleeds: development of BOMBS. Stroke. 2009.","Apoyo para identificación y reducción de desacuerdo interobservador.","https://doi.org/10.1161/STROKEAHA.108.526996"],
    ["WMH Fazekas","Fazekas F, et al. MR signal abnormalities at 1.5 T in Alzheimer's dementia and normal aging. AJR. 1987; y revisiones posteriores.","Gradación visual periventricular y profunda 0–3.","https://doi.org/10.2214/ajr.149.2.351"],
    ["Transformación hemorrágica","Clasificación ECASS de transformación hemorrágica.","HI1, HI2, PH1, PH2.","https://doi.org/10.1161/01.STR.30.11.2280"],
]
src.get_range(f"A2:D{1+len(sources)}").values = sources
src.get_range("A1:D1").format = header_fmt
src.get_range(f"A2:D{1+len(sources)}").format.wrap_text = True
for col,w in zip(["A","B","C","D"],[24,70,55,48]):
    src.get_range(f"{col}:{col}").format.column_width = w
src.freeze_panes.freeze_rows(1)

# ---------- Patient summaries ----------
psum = wb.worksheets.add("RESUMEN_PACIENTES")
psum_headers = ["patient_id","study_id","resumen_neurorradiologico","biomarcadores_clave","limitaciones","estado_revision"]
psum.get_range("A1:F1").values = [psum_headers]
psum.get_range("A1:F1").format = header_fmt
psum.get_range("A2:F501").format.wrap_text = True
for col,w in zip(["A","B","C","D","E","F"],[16,18,65,55,45,20]):
    psum.get_range(f"{col}:{col}").format.column_width = w
psum.get_range("F2:F501").data_validation = {"rule":{"type":"list","values":["Pendiente","Codificado","Segunda lectura","Adjudicado"]}}
psum.freeze_panes.freeze_rows(1)

# tables where useful
master.tables.add("A1:CG501", True, "MasterNeuroimaging")
d.tables.add(f"A1:H{1+len(rows)}", True, "VariableDictionary")
l.tables.add(f"A1:D{1+len(legend)}", True, "ScaleLegend")
src.tables.add(f"A1:D{1+len(sources)}", True, "SourcesTable")
psum.tables.add("A1:F501", True, "PatientSummaries")

# Export workbook
xlsx_path = os.path.join(out_dir, "matriz_maestra_biomarcadores_neurorradiologicos_ACV.xlsx")
SpreadsheetFile.export_xlsx(wb).save(xlsx_path)

# CSV headers template
csv_path = os.path.join(out_dir, "matriz_maestra_template.csv")
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    csv.writer(f).writerow(headers)

dict_csv_path = os.path.join(out_dir, "diccionario_variables.csv")
with open(dict_csv_path, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(dict_headers)
    w.writerows(rows)

# README for GitHub
readme = """# Matriz maestra de biomarcadores neurorradiológicos post-ACV

Repositorio de trabajo para codificación estandarizada y reproducible de hallazgos neurorradiológicos posteriores a un evento cerebrovascular.

## Estructura
- `matriz_maestra_template.csv`: tabla principal, una fila por estudio.
- `diccionario_variables.csv`: definiciones operativas y reglas de codificación.
- `matriz_maestra_biomarcadores_neurorradiologicos_ACV.xlsx`: versión de trabajo con validaciones, leyendas y fuentes.

## Identificación
Los pacientes se codifican de forma ascendente: `ACV-0001`, `ACV-0002`, etc.
Cada estudio usa un identificador propio: `ACV-0001-RM01`, `ACV-0001-RM02`.

## Valores faltantes
- `0`: evaluado y ausente.
- `1`: presente.
- `NA`: dato no disponible.
- `NE`: no evaluable por calidad o artefacto.
- `NS`: secuencia necesaria no realizada/no disponible.

## Principios
1. No inferir ausencia de lesión cuando falta la secuencia necesaria.
2. Conservar trazabilidad entre texto radiológico desidentificado y variable codificada.
3. Separar hallazgos observados, inferencias y correlación clínica.
4. Usar doble lectura y adjudicación cuando sea posible.
5. No publicar identificadores, DICOM, informes íntegros, fechas exactas ni combinaciones con riesgo de reidentificación sin aprobación ética.

## Referencias principales
- STRIVE-2 (Duering et al., 2023): https://doi.org/10.1016/S1474-4422(23)00131-X
- Total CSVD score (Staals et al., 2014): https://doi.org/10.1212/WNL.0000000000000837
- MARS (Gregoire et al., 2009): https://doi.org/10.1212/WNL.0b013e3181c34a7d
- BOMBS (Cordonnier et al., 2009): https://doi.org/10.1161/STROKEAHA.108.526996

## Estado
Plantilla inicial. Los registros de pacientes se incorporarán únicamente después de desidentificación y revisión metodológica.
"""
readme_path = os.path.join(out_dir, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)

# data governance checklist
governance = """# Lista mínima de gobernanza antes de publicar datos

- Confirmar aprobación ética o determinación formal de exención.
- Definir responsable del tratamiento, finalidad y base jurídica.
- Mantener la tabla de correspondencia entre identidad y código fuera del repositorio.
- Aplicar desplazamiento o generalización de fechas.
- Evaluar combinaciones raras: edad extrema, localidad, fechas, hospital, hallazgos infrecuentes.
- Publicar solo el conjunto mínimo necesario.
- Documentar control de acceso, versiones, cambios y retiro de registros.
- No publicar imágenes DICOM sin desidentificación específica de cabeceras y revisión de información incrustada.
- Establecer licencia de datos solo después de confirmar que existe derecho para compartirlos.
"""
gov_path = os.path.join(out_dir, "GOBERNANZA_DATOS.md")
with open(gov_path, "w", encoding="utf-8") as f:
    f.write(governance)

# Verify workbook key areas
print(wb.inspect({"kind":"table","range":"INSTRUCCIONES!A1:B10","include":"values,formulas","table_max_rows":12,"table_max_cols":4}).ndjson)
print(wb.inspect({"kind":"match","search_term":"#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A","options":{"use_regex":True,"max_results":100},"summary":"formula error scan"}).ndjson)

print({
    "xlsx": xlsx_path,
    "csv": csv_path,
    "dictionary": dict_csv_path,
    "readme": readme_path,
    "governance": gov_path
})
