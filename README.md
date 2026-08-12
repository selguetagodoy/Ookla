# Velocidades de Internet — Chile, Colombia y comparadores internacionales

Repositorio de análisis reproducible sobre la evolución de las velocidades de Internet fija y móvil, con foco en Colombia y Chile y comparación con Nueva Zelanda, el promedio OCDE y el promedio mundial.

## Alcance

La serie reúne información histórica de Akamai y Ookla entre 2008 y 2026. Las familias metodológicas se mantienen separadas y no se interpretan como una única serie homogénea.

- **Akamai** aporta observaciones históricas de conectividad entre 2008 y 2017.
- **Ookla** aporta observaciones de Speedtest y datos abiertos desde 2019. El dato 2018 disponible corresponde a una cobertura parcial del índice y se conserva con esa advertencia.
- **2026 es provisional** y corresponde a los trimestres disponibles al momento del corte.
- Los valores ausentes se mantienen como `NA`. No se interpolan.

## Comparadores principales

- Colombia
- Chile
- Nueva Zelanda
- Promedio OCDE
- Promedio mundial

## Estructura

```text
.
├── README.md
├── data/
│   └── comparacion_anual_2008_2026.csv
├── docs/
│   ├── metodologia.md
│   └── fuentes.md
└── scripts/
    ├── requirements.txt
    └── analizar_comparacion.py
```

## Lectura rápida

En 2026, la velocidad fija disponible en la base alcanza **399,46 Mbps en Chile**, **237,86 Mbps en Colombia**, **235,26 Mbps en Nueva Zelanda**, **271,23 Mbps en el promedio OCDE** y **153,16 Mbps en el promedio mundial**.

En móvil, Nueva Zelanda y el promedio OCDE presentan los valores más altos dentro de este conjunto comparado. Colombia registra **82,09 Mbps** y Chile **99,90 Mbps** en el corte provisional 2026.

Estas cifras no deben utilizarse para calcular una tasa de crecimiento continua entre Akamai y Ookla. El cambio de fuente implica un quiebre metodológico explícito.

## Reproducción

```bash
pip install -r scripts/requirements.txt
python scripts/analizar_comparacion.py
```

El script lee la base anual y genera una tabla resumen con los últimos valores disponibles por entidad.

## Fuente y trazabilidad

La documentación de fuentes y las principales decisiones metodológicas están en `docs/`. Ookla publica sus datos abiertos de performance en tiles trimestrales y señala que la cobertura parte en Q1 2019.

Este repositorio es un proyecto independiente de análisis. **No está afiliado ni respaldado por Ookla ni Akamai.** Los nombres y marcas pertenecen a sus respectivos titulares.

## Autor

**Sebastián Elgueta Godoy**  
Sociólogo. Análisis de datos, políticas públicas e infraestructura digital.
