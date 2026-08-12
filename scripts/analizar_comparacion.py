from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "comparacion_anual_2008_2026.csv"


def main() -> None:
    df = pd.read_csv(DATA, na_values=["NA"])

    fixed = df[[
        "year",
        "colombia_fixed_mbps",
        "chile_fixed_mbps",
        "new_zealand_fixed_mbps",
        "oecd_fixed_mbps",
        "world_fixed_mbps",
    ]].copy()

    mobile = df[[
        "year",
        "colombia_mobile_mbps",
        "chile_mobile_mbps",
        "new_zealand_mobile_mbps",
        "oecd_mobile_mbps",
        "world_mobile_mbps",
    ]].copy()

    latest_fixed = fixed.dropna(how="all", subset=fixed.columns[1:]).iloc[-1]
    latest_mobile = mobile.dropna(how="all", subset=mobile.columns[1:]).iloc[-1]

    print("Último corte disponible — fija")
    print(latest_fixed.to_string())
    print("\nÚltimo corte disponible — móvil")
    print(latest_mobile.to_string())


if __name__ == "__main__":
    main()
