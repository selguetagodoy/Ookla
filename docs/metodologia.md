# Metodología

## Principio general

El objetivo es comparar la evolución de la performance de Internet sin ocultar los cambios de fuente y de estadístico. La base no trata Akamai y Ookla como una única serie homogénea.

## Familias de datos

### Akamai

Los valores históricos provienen de informes *State of the Internet — Connectivity*. Las métricas reflejan la metodología utilizada por Akamai en cada periodo y se conservan con su denominación de origen.

### Ookla

Ookla Open Data publica agregados trimestrales de tests en tiles geográficos. La documentación oficial indica que los tiles de `performance_mobile_tiles` corresponden a dispositivos móviles con localización GPS y conexión celular. Los tiles de `performance_fixed_tiles` corresponden a dispositivos con localización GPS y conexión no celular, como Wi-Fi o ethernet.

Los datos abiertos comienzan en Q1 2019. Ookla advierte además que los datos pueden ser reagregados posteriormente, por lo que una descarga realizada en fechas distintas puede presentar variaciones en conteos y métricas agregadas.

## Reglas de comparación

1. No se interpola ningún dato faltante.
2. `NA` representa ausencia de observación comparable o disponible.
3. El cambio entre Akamai y Ookla se trata como un quiebre metodológico.
4. El dato 2018 se conserva como referencia parcial y no se utiliza para inferir continuidad entre ambas fuentes.
5. El dato 2026 se identifica como provisional.
6. Los promedios OCDE y mundial deben interpretarse dentro de la cobertura disponible en cada año y fuente.

## Unidad

Las velocidades se expresan en Mbps.

## Reproducibilidad

El archivo `data/comparacion_anual_2008_2026.csv` contiene la tabla comparativa liviana utilizada para análisis y visualización. El script incluido en `scripts/` permite obtener automáticamente el último valor disponible por entidad.

## Limitaciones

Las diferencias entre proveedores, métodos de medición, cobertura geográfica, dispositivos observados y estadísticos publicados impiden interpretar toda la ventana 2008–2026 como una sola serie estrictamente comparable. El repositorio privilegia trazabilidad y transparencia metodológica por sobre la construcción artificial de una serie continua.
