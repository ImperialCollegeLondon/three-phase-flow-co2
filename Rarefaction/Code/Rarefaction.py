import numpy as np
import pandas as pd
pd.options.display.float_format = '{:.4f}'.format
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
import sympy as sym
import os

# ---------------------------
# Viscosity
# ---------------------------
# Viscosity -- general condition
water_viscosity = 0.3093 #cP
oil_viscosity = 0.18452029 #cP
gas_viscosity = 0.05759195 #cP

# # Viscosity -- mutual equilibrium
# water_viscosity = 0.3093 #cP
# oil_viscosity = 0.394 #cP
# gas_viscosity = 0.203 #cP

# ---------------------------
# Paramaters for relative permeability curves
# ---------------------------

# Oil-Water --------------------------------
Sorw = 0.3
Swi = 0.2

# Water
Krwmax_ow = 0.6
a = 1.5

# Oil
Kromax = 0.9
b = 3

# Gas-Oil ----------------------------------
Sorg = 0

# Gas
c = 1
Sgc = 0
Krgmax_go = 0.9

# Oil
d = 3

# Gas-Water ----------------------------------

# Water
Krwmax_gw = 1
e = 1.5

# Gas
Krgmax_gw = 0.9
f = 5


# -------------------------------------------------------
# Baker interpolation parameters
# -------------------------------------------------------

Soi = 0.0
Sgr = 0.0


# ---------------------------
# Equations of relative permeabilities
# ---------------------------

# Oil-Water --------------------------------

def Krw_o(Sw: float) -> float:
    # กันกรณี Sw ต่ำกว่า Swi
    if Sw <= Swi:
        return 0.0
    denom = (1 - Swi - Sorw)
    if denom <= 0:
        return 0.0
    val = Krwmax_ow * (((Sw - Swi) / denom) ** a)
    return min(val, Krwmax_ow)
    # return min(val, 1.0000000)

# -------------------------------------------------------
# Print Krw(o) and Krg(o) tables
# -------------------------------------------------------

saturation_values = np.round(np.arange(0.0, 1.0001, 0.1), 2)

print("\nOil-water system: Sw and Krw(o)")
print("-" * 30)
print(f"{'Sw':>8} {'Krw(o)':>12}")

for Sw in saturation_values:
    krw_value = Krw_o(Sw)
    print(f"{Sw:8.2f} {krw_value:12.6f}")

# def Kro_w_Sw(Sw):
#     return Kromax * (((1-Sorw-Sw)/(1-Swi-Sorw))**b)

def Kro_w_So(So: float) -> float:
    # ถ้า So < Sorw ให้เป็น 0
    if So < Sorw:
        return 0.0
    denom = (1 - Swi - Sorw)
    if denom <= 0:
        return 0.0
    normalized_oil_saturation = (
        (So - Sorw) / denom
    )

    normalized_oil_saturation = np.clip(
        normalized_oil_saturation,
        0.0,
        1.0
    )
    return Kromax * normalized_oil_saturation**b

# Gas-Oil ----------------------------------

def Krg_o(Sg: float) -> float:
    # ถ้า Sg ต่ำกว่า Sgc ให้เป็น 0
    if Sg <= Sgc:
        return 0.0
    denom = (1 - Swi - Sorg - Sgc)
    if denom <= 0:
        return 0.0
    val = Krgmax_go * (((Sg - Sgc) / denom) ** c)
    # (ถ้าต้องการ cap ที่ Krgmax_go ก็ทำได้)
    return min(val, Krgmax_go)

print("\nGas-oil system: Sg and Krg(o)")
print("-" * 30)
print(f"{'Sg':>8} {'Krg(o)':>12}")

for Sg in saturation_values:
    krg_value = Krg_o(Sg)
    print(f"{Sg:8.2f} {krg_value:12.6f}")

# def Kro_g_Sg(Sg):
#     return Kromax * (((1-Swi-Sorg-Sg)/(1-Swi-Sorg-Sgc))**d)

def Kro_g_So(So: float) -> float:
    # ถ้า So < Sorg ให้เป็น 0
    if So < Sorg:
        return 0.0
    denom = (1 - Swi - Sorg - Sgc)
    if denom <= 0:
        return 0.0
    normalized_oil_saturation = (
        (So - Sorg) / denom
    )
    normalized_oil_saturation = np.clip(
        normalized_oil_saturation,
        0.0,
        1.0
    )
    return Kromax * normalized_oil_saturation**d

# Gas-Water ----------------------------------

def Krw_g(Sw: float) -> float:
    """
    Water relative permeability from the gas-water system

    krw(g)(Sw) =
        Krwmax_gw * ((Sw - Swi) / (1 - Swi))^e
    """

    if Sw <= Swi:
        return 0.0

    denom = 1.0 - Swi

    if denom <= 0.0:
        return 0.0

    normalized_Sw = (Sw - Swi) / denom

    normalized_Sw = np.clip(
        normalized_Sw,
        0.0,
        1.0
    )

    return Krwmax_gw * normalized_Sw**e

# def Krg_w_Sw(Sw):
#     return Krgmax_gw * (((1-Sw)/(1-Swi))**f)

def Krg_w(Sg: float) -> float:
    """
    Gas relative permeability from the gas-water system

    krg(w)(Sg) =
        Krgmax_gw * Sg^f / (1 - Swi)^f

    Since Sgc = 0 in the current case.
    """

    if Sg <= Sgc:
        return 0.0

    denom = 1.0 - Swi - Sgc

    if denom <= 0.0:
        return 0.0

    normalized_Sg = (Sg - Sgc) / denom

    normalized_Sg = np.clip(
        normalized_Sg,
        0.0,
        1.0
    )

    return Krgmax_gw * normalized_Sg**f

# ---------------------------
# Interpolation of Kr using Baker
# ---------------------------

# Kro ---------------------------------
def Kro_Baker(So: float, Sg: float, Sw: float) -> float:
    # Outside the physical saturation region
    if So < 0:
        return np.nan

    krow_val = Kro_w_So(So)
    krog_val = Kro_g_So(So)

    water_weight = max(Sw - Swi, 0.0)
    gas_weight = max(Sg - Sgc, 0.0)

    denom = water_weight + gas_weight

    # At Sw = Swi and Sg = Sgc:
    # no Baker interpolation is required; use the oil endpoint
    if np.isclose(denom, 0.0):
        return Kromax

    kro_interpolated = (
        water_weight * krow_val
        + gas_weight * krog_val
    ) / denom

    return kro_interpolated


# Print three-phase interpolated oil relative permeability ---------------------

# Water saturation values for columns
Sw_values = np.round(np.arange(Swi, 1.0001, 0.05), 2)

# Gas saturation values for rows
Sg_values = np.round(np.arange(Sgc, 1.0 - Swi + 0.0001, 0.05), 2)

# Create table
kro_table = pd.DataFrame(
    index=Sg_values,
    columns=Sw_values,
    dtype=float
)

for Sg in Sg_values:
    for Sw in Sw_values:
        So = 1.0 - Sw - Sg

        # Only calculate values inside the saturation triangle
        if So >= -1e-12:
            So = max(So, 0.0)
            kro_table.loc[Sg, Sw] = Kro_Baker(
                So=So,
                Sg=Sg,
                Sw=Sw
            )
        else:
            kro_table.loc[Sg, Sw] = np.nan

# Labels
kro_table.index.name = "SGAS"
kro_table.columns.name = "WATER SATURATION"

print("\n* - INTERPOLATED VALUE")
print("-" * 80)
print("3-PHASE OIL RELATIVE PERMEABILITIES TABLE")
print("-" * 80)
print(f"CONNATE WATER SATURATION = {Swi:.4f}\n")

# Print with 3 decimal places and leave invalid cells blank
print(
    kro_table.to_string(
        float_format=lambda x: f"{x:.3f}",
        na_rep=""
    )
)
print("\n")


# Krw -----------------------------------------------

def Krw_Baker(Sw: float, Sg: float) -> float:

    So = 1.0 - Sw - Sg

    # Outside physical saturation triangle
    if So < -1e-12:
        return np.nan

    So = max(So, 0.0)

    # Two-phase Krw values
    krwo_val = Krw_o(Sw)   # oil-water curve
    krwg_val = Krw_g(Sw)   # gas-water curve

    # Baker weights
    oil_weight = max(So - Soi, 0.0)
    gas_weight = max(Sg - Sgr, 0.0)

    denom = oil_weight + gas_weight

    # Special corner:
    # So = Soi and Sg = Sgr
    # For the current model this corresponds to pure/high water.
    if np.isclose(denom, 0.0):

        # Both two-phase curves meet at the water endpoint
        return max(krwo_val, krwg_val)

    krw_interpolated = (
        oil_weight * krwo_val
        + gas_weight * krwg_val
    ) / denom

    return float(
        np.clip(
            krw_interpolated,
            0.0,
            1.0
        )
    )

# Print three-phase interpolated WATER relative permeability --------------------------------

So_values_krw = np.round(
    np.arange(0.0, 1.0001, 0.1),
    2
)

Sg_values_krw = np.round(
    np.arange(0.0, 1.0001, 0.1),
    2
)

krw_table = pd.DataFrame(
    index=Sg_values_krw,
    columns=So_values_krw,
    dtype=float
)


for Sg in Sg_values_krw:

    for So in So_values_krw:

        Sw = 1.0 - So - Sg

        # Only physical saturation states
        if Sw >= -1e-12:

            Sw = max(Sw, 0.0)

            krw_table.loc[Sg, So] = Krw_Baker(
                Sw=Sw,
                Sg=Sg
            )

        else:

            krw_table.loc[Sg, So] = np.nan


# Labels
krw_table.index.name = "SGAS"
krw_table.columns.name = "OIL SATURATION"


print("\n")
print("* - INTERPOLATED VALUE")
print("-" * 80)
print("3-PHASE WATER RELATIVE PERMEABILITIES TABLE")
print("-" * 80)

print(
    krw_table.to_string(
        float_format=lambda x: f"{x:.5f}",
        na_rep=""
    )
)

print("\n")

# Krg ---------------------------------------------------

def Krg_Baker(Sw: float, Sg: float) -> float:

    So = 1.0 - Sw - Sg

    # Outside physical saturation triangle
    if So < -1e-12:
        return np.nan

    So = max(So, 0.0)

    # Two-phase Krg values
    krgw_val = Krg_w(Sg)   # gas-water curve
    krgo_val = Krg_o(Sg)   # gas-oil curve

    # Baker weights
    water_weight = max(Sw - Swi, 0.0)
    oil_weight = max(So - Soi, 0.0)

    denom = water_weight + oil_weight

    # Special corner
    if np.isclose(denom, 0.0):

        # At the gas endpoint both curves should approach
        # their gas endpoint value.
        return max(krgw_val, krgo_val)

    krg_interpolated = (
        water_weight * krgw_val
        + oil_weight * krgo_val
    ) / denom

    return float(
        np.clip(
            krg_interpolated,
            0.0,
            1.0
        )
    )

# Print three-phase interpolated GAS relative permeability ----------------------------------

Sw_values_krg = np.round(
    np.arange(Swi, 1.0001, 0.1),
    2
)

So_values_krg = np.round(
    np.arange(0.0, 1.0 - Swi + 0.0001, 0.1),
    2
)

krg_table = pd.DataFrame(
    index=Sw_values_krg,
    columns=So_values_krg,
    dtype=float
)


for Sw in Sw_values_krg:

    for So in So_values_krg:

        Sg = 1.0 - Sw - So

        # Only physical saturation states
        if Sg >= -1e-12:

            Sg = max(Sg, 0.0)

            krg_table.loc[Sw, So] = Krg_Baker(
                Sw=Sw,
                Sg=Sg
            )

        else:

            krg_table.loc[Sw, So] = np.nan


# Labels
krg_table.index.name = "SWATER"
krg_table.columns.name = "OIL SATURATION"


print("\n")
print("* - INTERPOLATED VALUE")
print("-" * 80)
print("3-PHASE GAS RELATIVE PERMEABILITIES TABLE")
print("-" * 80)

print(
    krg_table.to_string(
        float_format=lambda x: f"{x:.5f}",
        na_rep=""
    )
)

print("\n")

# ---------------------------
# Preparing inputs for fractional flow analysis
# ---------------------------

# Rel perm ---------------------------------------------
def Kro(Sw: float, Sg: float) -> float:
    So = 1.0 - Sw - Sg

    # Choose one:
    return Kro_Baker(So, Sg, Sw)       # interpolated Kro -----------------------------------input


def Krw(Sw: float, Sg: float) -> float:
    So = 1.0 - Sw - Sg

    # Choose one:
    return Krw_o(Sw)               # only oil-water Krw --------------------------------input
    # return Krw_g(Sw)               # only gas-water Krw
    # return Krw_Baker(Sw, Sg)         # interpolated Krw ----------------------------------input


def Krg(Sw: float, Sg: float) -> float:
    So = 1.0 - Sw - Sg

    # Choose one:
    return Krg_o(Sg)               # only gas-oil Krg ---------------------------------input
    # return Krg_w(Sg)               # only gas-water Krg
    # return Krg_Baker(Sw, Sg)         # interpolated Krg ---------------------------------input

# Mobility = Kr / viscosity ----------------------------
def lamda_w(Sw: float, Sg: float) -> float:
    return Krw(Sw, Sg) / water_viscosity

def lamda_o(Sw: float, Sg: float) -> float:
    return Kro(Sw, Sg) / oil_viscosity

def lamda_g(Sw: float, Sg: float) -> float:
    return Krg(Sw, Sg) / gas_viscosity

def lamda_t(Sw: float, Sg: float) -> float:
    return lamda_w(Sw, Sg) + lamda_o(Sw, Sg) + lamda_g(Sw, Sg)

# Derivatives of Krw ------------------------------------
def dKrw_dSw(Sw: float, Sg: float) -> float:
    h = max(1e-6, 1e-4 * abs(Sw))
    return (Krw(Sw + h, Sg) - Krw(Sw - h, Sg)) / (2 * h)

def dKrw_dSg(Sw: float, Sg: float) -> float:
    h = max(1e-6, 1e-4 * abs(Sg) if Sg != 0 else 1e-6)
    return (Krw(Sw, Sg + h) - Krw(Sw, Sg - h)) / (2 * h)

# Derivatives of Krg -----------------------------------
def dKrg_dSg(Sw: float, Sg: float) -> float:
    h = max(1e-6, 1e-4 * abs(Sg) if Sg != 0 else 1e-6)
    return (Krg(Sw, Sg + h) - Krg(Sw, Sg - h)) / (2 * h)

def dKrg_dSw(Sw: float, Sg: float) -> float:
    h = max(1e-6, 1e-4 * abs(Sw))
    return (Krg(Sw + h, Sg) - Krg(Sw - h, Sg)) / (2 * h)

# Derivative of Kro -----------------------------------
def dKro_dSw(Sw: float, Sg: float) -> float:
    h = max(1e-6, 1e-4 * abs(Sw))
    return (Kro(Sw + h, Sg) - Kro(Sw - h, Sg)) / (2 * h)

def dKro_dSg(Sw: float, Sg: float) -> float:
    h = max(1e-6, 1e-4 * abs(Sg) if Sg != 0 else 1e-6)
    return (Kro(Sw, Sg + h) - Kro(Sw, Sg - h)) / (2 * h)

# Mobility derivatives --------------------------------
def lambda_w_w(Sw: float, Sg: float) -> float:
    return (1 / water_viscosity) * dKrw_dSw(Sw, Sg)

def lambda_w_g(Sw: float, Sg: float) -> float:
    return (1 / water_viscosity) * dKrw_dSg(Sw, Sg)

def lambda_g_g(Sw: float, Sg: float) -> float:
    return (1 / gas_viscosity) * dKrg_dSg(Sw, Sg)

def lambda_g_w(Sw: float, Sg: float) -> float:
    return (1 / gas_viscosity) * dKrg_dSw(Sw, Sg)

def Lamda_o_w(Sw: float, Sg: float) -> float:
    return (1 / oil_viscosity) * dKro_dSw(Sw, Sg)

def Lamda_o_g(Sw: float, Sg: float) -> float:
    return (1 / oil_viscosity) * dKro_dSg(Sw, Sg)

def lambda_t_w(Sw: float, Sg: float) -> float:
    # d(lambda_t)/dSw
    return lambda_w_w(Sw, Sg) + Lamda_o_w(Sw, Sg) + lambda_g_w(Sw, Sg)

def lambda_t_g(Sw: float, Sg: float) -> float:
    # d(lambda_t)/dSg
    return lambda_w_g(Sw, Sg) + Lamda_o_g(Sw, Sg) + lambda_g_g(Sw, Sg)

# -----------------------------
# test saturation
# -----------------------------
Sw = 0.3
Sg = 0.20
So = 1.0 - Sw - Sg

print("\nSaturation:")
print(f"Sw = {Sw:.2f}")
print(f"Sg = {Sg:.2f}")
print(f"So = {So:.2f}")

print("\nMobility derivatives:")
print(f"lambda_w_w = {lambda_w_w(Sw, Sg):.4f}")
print(f"lambda_w_g = {lambda_w_g(Sw, Sg):.4f}")
print(f"lambda_g_g = {lambda_g_g(Sw, Sg):.4f}")
print(f"lambda_g_w = {lambda_g_w(Sw, Sg):.4f}")
print(f"lambda_o_w = {Lamda_o_w(Sw, Sg):.4f}")
print(f"lambda_o_g = {Lamda_o_g(Sw, Sg):.4f}")
print(f"lambda_t_w = {lambda_t_w(Sw, Sg):.4f}")
print(f"lambda_t_g = {lambda_t_g(Sw, Sg):.4f}")

# -------------------------------
# Fractional Flow
# -------------------------------
def fw(Sw: float, Sg: float) -> float:
    return lamda_w(Sw, Sg) / lamda_t(Sw, Sg)

def fg(Sw: float, Sg: float) -> float:
    return lamda_g(Sw, Sg) / lamda_t(Sw, Sg)

def f11(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    return (lambda_w_w(Sw, Sg) * lt - lamda_w(Sw, Sg) * lambda_t_w(Sw, Sg)) / (lt**2)

def f13(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    return (lambda_w_g(Sw, Sg) * lt - lamda_w(Sw, Sg) * lambda_t_g(Sw, Sg)) / (lt**2)

def f31(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    return (lambda_g_w(Sw, Sg) * lt - lamda_g(Sw, Sg) * lambda_t_w(Sw, Sg)) / (lt**2)

def f33(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    return (lambda_g_g(Sw, Sg) * lt - lamda_g(Sw, Sg) * lambda_t_g(Sw, Sg)) / (lt**2)

print(f"f11 = {f11(Sw, Sg):.4f}")
print(f"f13 = {f13(Sw, Sg):.4f}")
print(f"f31 = {f31(Sw, Sg):.4f}")
print(f"f33 = {f33(Sw, Sg):.4f}")

# -------------------------------------------
# Find Elliptic Region
# -------------------------------------------

# output folder for PyCharm / Windows
export_folder = r"C:\Users\oa2414\PycharmProjects\Share_Code"  #----------------------------------input
os.makedirs(export_folder, exist_ok=True)


def discriminant_value(Sw: float, Sg: float) -> float:
    return (f11(Sw, Sg) - f33(Sw, Sg))**2 + 4.0 * f13(Sw, Sg) * f31(Sw, Sg)


def find_elliptic_region(
    Sw_min=Swi, Sw_max=1.0, dSw=0.001,
    Sg_min=0.0, Sg_max=1-Swi, dSg=0.001,
    eps_lt=1e-12
):
    Sw_vals = np.arange(Sw_min, Sw_max + 1e-12, dSw)
    Sg_vals = np.arange(Sg_min, Sg_max + 1e-12, dSg)

    hits = []

    for Sg in Sg_vals:
        for Sw in Sw_vals:
            So = 1.0 - Sw - Sg

            if So < 0:
                continue

            lt = lamda_t(Sw, Sg)
            if (not np.isfinite(lt)) or lt <= eps_lt:
                continue

            v11 = f11(Sw, Sg)
            v13 = f13(Sw, Sg)
            v31 = f31(Sw, Sg)
            v33 = f33(Sw, Sg)

            if not all(np.isfinite(v) for v in [v11, v13, v31, v33]):
                continue

            disc = (v11 - v33)**2 + 4.0 * v13 * v31

            if disc < 0.0:
                hits.append([Sw, Sg, So, v11, v13, v31, v33, disc])

    return pd.DataFrame(
        hits,
        columns=["Sw", "Sg", "So", "f11", "f13", "f31", "f33", "discriminant"]
    )


df_ell = find_elliptic_region(
    Sw_min=0.2, Sw_max=1.0, dSw=0.001,
    Sg_min=0.0, Sg_max=0.8, dSg=0.001
)

out_file = os.path.join(export_folder, "Elliptic_region.csv")
df_ell.to_csv(out_file, index=False)

print("Saved to:", out_file)
print("Number of elliptic points:", len(df_ell))
print(df_ell.head())

# -------------------------------------------
# Plot elliptic region on ternary diagram
# Layout:
#   So  -> left bottom
#   Sw  -> right bottom
#   SCO2/Sg -> top
# -------------------------------------------

def ternary_xy(Sw, Sg, So):
    """
    So  vertex = (0, 0)
    Sw  vertex = (1, 0)
    Sg/SCO2 vertex = (0.5, sqrt(3)/2)
    """
    x = Sw + 0.5 * Sg
    y = (np.sqrt(3) / 2.0) * Sg
    return x, y


def draw_ternary_axes(ax, tick_step=0.1):
    h = np.sqrt(3) / 2.0

    # vertices
    V_So = np.array([0.0, 0.0])
    V_Sw = np.array([1.0, 0.0])
    V_Sg = np.array([0.5, h])

    # triangle boundary
    ax.plot([V_So[0], V_Sw[0]], [V_So[1], V_Sw[1]], color="black", lw=1.5)
    ax.plot([V_Sw[0], V_Sg[0]], [V_Sw[1], V_Sg[1]], color="black", lw=1.5)
    ax.plot([V_Sg[0], V_So[0]], [V_Sg[1], V_So[1]], color="black", lw=1.5)

    # grid lines every 10%
    vals = np.arange(tick_step, 1.0, tick_step)

    for v in vals:
        # constant Sg: horizontal line
        x1, y1 = ternary_xy(0, v, 1-v)
        x2, y2 = ternary_xy(1-v, v, 0)
        ax.plot([x1, x2], [y1, y2], color="lightgray", lw=0.6, zorder=0)

        # constant Sw
        x1, y1 = ternary_xy(v, 0, 1-v)
        x2, y2 = ternary_xy(v, 1-v, 0)
        ax.plot([x1, x2], [y1, y2], color="lightgray", lw=0.6, zorder=0)

        # constant So
        x1, y1 = ternary_xy(0, 1-v, v)
        x2, y2 = ternary_xy(1-v, 0, v)
        ax.plot([x1, x2], [y1, y2], color="lightgray", lw=0.6, zorder=0)

    # axis labels
    ax.text(-0.06, -0.055, "Oil", ha="right", va="top", fontsize=20)
    ax.text(1.06, -0.055, "Water", ha="left", va="top", fontsize=20)
    ax.text(0.5, h + 0.06, "CO₂", ha="center", va="bottom", fontsize=20)

    # tick labels 0,10,...,100
    tick_vals = np.arange(0, 1.01, tick_step)

    for v in tick_vals:
        label = f"{int(round(v * 100))}"

        # Sw ticks along bottom: So=1-Sw, Sg=0
        x, y = ternary_xy(v, 0, 1-v)
        ax.text(x, y - 0.035, label, ha="center", va="top", fontsize=15)

        # So ticks along left edge: Sw=0, Sg=1-So
        x, y = ternary_xy(0, 1-v, v)
        ax.text(x - 0.035, y, label, ha="right", va="center", fontsize=15)

        # Sg/SCO2 ticks along right edge: So=0, Sw=1-Sg
        x, y = ternary_xy(1-v, v, 0)
        ax.text(x + 0.035, y, label, ha="left", va="center", fontsize=15)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(-0.10, h + 0.12)
    ax.axis("off")


# ------------------------------------------------
# Eigenvalue (Velocity - vD+ and vD-)
# ------------------------------------------------
def vD_positive(Sw: float, Sg: float) -> float:
    disc = (f11(Sw, Sg) - f33(Sw, Sg))**2 + 4.0 * f13(Sw, Sg) * f31(Sw, Sg)
    if disc < 0:
        return np.nan
    return 0.5 * (f11(Sw, Sg) + f33(Sw, Sg)) + 0.5 * np.sqrt(disc)


def vD_negative(Sw: float, Sg: float) -> float:
    disc = (f11(Sw, Sg) - f33(Sw, Sg))**2 + 4.0 * f13(Sw, Sg) * f31(Sw, Sg)
    if disc < 0:
        return np.nan
    return 0.5 * (f11(Sw, Sg) + f33(Sw, Sg)) - 0.5 * np.sqrt(disc)

# เลือกว่า จะใช้ vD+ (Fast path) หรือ vD- (Slow path)
def vD(Sw: float, Sg: float, family: str = "positive") -> float:
    if family == "positive":
        return vD_positive(Sw, Sg)
    elif family == "negative":
        return vD_negative(Sw, Sg)
    else:
        raise ValueError("family must be 'positive' or 'negative'")

# ------------------------------
# slope: dSg/dSw, traced with delta Sw
# ------------------------------
def slope_dSg_dSw(Sw: float, Sg: float, family: str = "positive") -> float:
    vd = vD(Sw, Sg, family)

    if not np.isfinite(vd):
        return np.nan

    denom = vd - f33(Sw, Sg)

    if abs(denom) < 1e-12:
        return np.nan  # vertical slope / singular

    return f31(Sw, Sg) / denom

# ------------------------------
# slope: dSw/dSg, traced with delta Sg (inverse)
# ------------------------------
def slope_dSw_dSg(Sw: float, Sg: float, family: str = "positive") -> float:
    vd = vD(Sw, Sg, family)

    if not np.isfinite(vd):
        return np.nan

    denom = f31(Sw, Sg)

    if abs(denom) < 1e-12:
        return np.nan  # horizontal slope / singular

    return (vd - f33(Sw, Sg)) / denom


# -----------------------
# Trace rarefaction path
# -----------------------

def is_valid_saturation(Sw, Sg, tol=1e-12):
    So = 1.0 - Sw - Sg
    return (
        np.isfinite(Sw)
        and np.isfinite(Sg)
        and np.isfinite(So)
        and Sw >= -tol
        and Sg >= -tol
        and So >= -tol
        and Sw <= 1.0 + tol
        and Sg <= 1.0 + tol
        and Sw + Sg <= 1.0 + tol
    )


def trace_rarefaction(
    Sw0: float,
    Sg0: float,
    family: str = "positive",        # "positive" or "negative"
    step_mode: str = "dSw_dSg",      # "dSw_dSg" or "dSg_dSw"
    delta_value: float = 0.001,
    max_steps: int = 10000,
    sign: int = 1                    # +1 or -1
):
    rows = []

    Sw = float(Sw0)
    Sg = float(Sg0)
    delta_step = sign * abs(delta_value)

    for step in range(max_steps):

        if not is_valid_saturation(Sw, Sg):
            break

        So = 1.0 - Sw - Sg

        disc = discriminant_value(Sw, Sg)
        if (not np.isfinite(disc)) or disc < 0:
            break

        vd = vD(Sw, Sg, family)
        if not np.isfinite(vd):
            break

        if step_mode == "dSw_dSg":
            direction = slope_dSw_dSg(Sw, Sg, family)

            if not np.isfinite(direction):
                break

            Sg_next = Sg + delta_step
            Sw_next = Sw + direction * delta_step

        elif step_mode == "dSg_dSw":
            direction = slope_dSg_dSw(Sw, Sg, family)

            if not np.isfinite(direction):
                break

            Sw_next = Sw + delta_step
            Sg_next = Sg + direction * delta_step

        else:
            raise ValueError("step_mode must be 'dSw_dSg' or 'dSg_dSw'")

        So_next = 1.0 - Sw_next - Sg_next

        rows.append({
            "step": step,
            "Sg": Sg,
            "Sw": Sw,
            "So": So,

            "Kro": Kro(Sw, Sg),
            "Krg": Krg(Sw, Sg),
            "Krw": Krw(Sw, Sg),

            "lambda_w": lamda_w(Sw, Sg),
            "lambda_o": lamda_o(Sw, Sg),
            "lambda_g": lamda_g(Sw, Sg),
            "lambda_t": lamda_t(Sw, Sg),

            # derivatives
            "lambda_w_w": lambda_w_w(Sw, Sg),
            "lambda_w_g": lambda_w_g(Sw, Sg),

            "lambda_g_g": lambda_g_g(Sw, Sg),
            "lambda_g_w": lambda_g_w(Sw, Sg),

            "lambda_o_w": Lamda_o_w(Sw, Sg),
            "lambda_o_g": Lamda_o_g(Sw, Sg),

            "lambda_t_w": lambda_t_w(Sw, Sg),
            "lambda_t_g": lambda_t_g(Sw, Sg),

            # Jacobian
            "f11": f11(Sw, Sg),
            "f13": f13(Sw, Sg),
            "f31": f31(Sw, Sg),
            "f33": f33(Sw, Sg),

            "delta": disc,
            "vD": vd,
            "direction": direction,

            "Sw_next": Sw_next,
            "Sg_next": Sg_next,
            "So_next": So_next,
        })

        if not is_valid_saturation(Sw_next, Sg_next):
            break

        Sw = Sw_next
        Sg = Sg_next

    return pd.DataFrame(rows)

# -----------------------------------------------------------------------------------------
# INPUT for tracing
# -----------------------------------------------------------------------------------------
# varying Sg used with negative and dSg_dSw
# varying Sw used with positive and dSw_dSg

Sw_tracing = 0.8   #---------------------------------------------------------------------------input
Sg_tracing = 0.05   #---------------------------------------------------------------------------input

family = "negative"     #-----------------------------------------------------------------------input
                        # Direction: "positive" (vertical, fast path, use delta Sg) or "negative" (horizontal, slow path, use delta Sw)
step_mode = "dSg_dSw"   #-----------------------------------------------------------------------input
                        # "dSw_dSg" เดินด้วย delta Sg, หรือ "dSg_dSw" เดินด้วย delta Sw
delta_value = 0.0005

# trace both directions
df_path_pos = trace_rarefaction(
    Sw0=Sw_tracing,
    Sg0=Sg_tracing,
    family=family,
    step_mode=step_mode,
    delta_value=delta_value,
    sign=+1
)

df_path_neg = trace_rarefaction(
    Sw0=Sw_tracing,
    Sg0=Sg_tracing,
    family=family,
    step_mode=step_mode,
    delta_value=delta_value,
    sign=-1
)

# combine paths
df_path = pd.concat([df_path_neg, df_path_pos], ignore_index=True)
df_path = df_path.drop_duplicates(subset=["Sw", "Sg", "So"])

if step_mode == "dSw_dSg":
    df_path = df_path.sort_values("Sg").reset_index(drop=True)
else:
    df_path = df_path.sort_values("Sw").reset_index(drop=True)

df_path["step"] = np.arange(len(df_path))

print(df_path.head())
print(df_path.tail())
print("Number of tracing points:", len(df_path))


# -----------------------
# Save to Excel (with sheet name)
# -----------------------

def make_sheet_name(family: str, Sw: float, Sg: float) -> str:
    prefix = "D+" if family == "positive" else "D-"

    Sw_str = f"{Sw:.3f}".rstrip('0').rstrip('.')
    Sg_str = f"{Sg:.3f}".rstrip('0').rstrip('.')

    name = f"{prefix}_Sg{Sg_str}_Sw{Sw_str}"

    return name[:31]  # Excel limit

# path file
out_path = os.path.join(
    export_folder,
    f"Rarefaction_{family}_{step_mode}_Sw{Sw_tracing}_Sg{Sg_tracing}.xlsx"
)

sheet_name = make_sheet_name(family, Sw_tracing, Sg_tracing)

# save
with pd.ExcelWriter(out_path, engine="xlsxwriter") as writer:
    df_path.to_excel(writer, sheet_name=sheet_name, index=False)

print("Saved rarefaction path to:", out_path)
print("Sheet name:", sheet_name)

# Plot --------------------------
fig, ax = plt.subplots(figsize=(9, 8))
draw_ternary_axes(ax, tick_step=0.1)

# plot elliptic region
if len(df_ell) > 0:
    xs_ell, ys_ell = [], []
    for _, row in df_ell.iterrows():
        x, y = ternary_xy(row["Sw"], row["Sg"], row["So"])
        xs_ell.append(x)
        ys_ell.append(y)

    ax.scatter(xs_ell, ys_ell, s=2, color="lightblue", alpha=0.45, label="Elliptic region")

# plot rarefaction path
xs, ys = [], []
for _, row in df_path.iterrows():
    x, y = ternary_xy(row["Sw"], row["Sg"], row["So"])
    xs.append(x)
    ys.append(y)

ax.plot(xs, ys, color="red", linewidth=2.0, label=f"Rarefaction {family}, {step_mode}")
ax.scatter(
    *ternary_xy(Sw_tracing, Sg_tracing, 1-Sw_tracing-Sg_tracing),
    color="black",
    s=40,
    zorder=5,
    label="Start point"
)

ax.set_title("Rarefaction Path on Ternary Diagram", fontsize=14, pad=18)
ax.legend(loc="upper right", fontsize=9, frameon=True)

plot_path = os.path.join(export_folder, f"Rarefaction_{family}_{step_mode}_Sw{Sw_tracing}_Sg{Sg_tracing}.png")
plt.savefig(plot_path, dpi=300, bbox_inches="tight")
plt.show()

print("Saved rarefaction plot to:", plot_path)