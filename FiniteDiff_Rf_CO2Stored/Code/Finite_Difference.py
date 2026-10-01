import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

case_name = "Finite_Difference_Rf_CO2Stored"  #----------------------------input
# ---------------------------------------
# export folder
# ---------------------------------------
export_folder = r'C:\Users\oa2414\PycharmProjects\Share_Code'    #--------------------------input
os.makedirs(export_folder, exist_ok=True)

print("Export folder =", export_folder)

# -------------------------------------------------------
# Viscosity
# -------------------------------------------------------
water_viscosity = 0.3093 #cP
oil_viscosity = 0.18452029 #cP
gas_viscosity = 0.05759195 #cP

# -------------------------------------------------------
# Input for relative permeability curves
# -------------------------------------------------------

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


# -------------------------------------------------------
# Relative permeability functions
# -------------------------------------------------------

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


# Print Krw(o) and Krg(o) tables -------------------------
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
    if Sg <= Sgc:
        return 0.0
    denom = (1 - Swi - Sorg - Sgc)
    if denom <= 0:
        return 0.0
    val = Krgmax_go * (((Sg - Sgc) / denom) ** c)
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

# Gas-water -------------------------------------

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

# ----------------------------------------------------
# Baker interpolation for Kro
# ----------------------------------------------------
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


# Print three-phase interpolated oil relative permeability ----------------------

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


# -------------------------------------------------------
# Baker interpolation for Krw
# -------------------------------------------------------

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


# Print three-phase interpolated WATER relative permeability -----------------------------

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


# -------------------------------------------------------
# Baker interpolation for Krg
# -------------------------------------------------------

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


# Print three-phase interpolated GAS relative permeability ------------------------------------

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


# =======================================================
# Select relative permeability model
# =======================================================

def Kro(Sw: float, Sg: float) -> float:
    So = 1.0 - Sw - Sg

    # Choose one:
    return Kro_Baker(So, Sg, Sw)       # interpolated Kro -----------------------------------input


def Krw(Sw: float, Sg: float) -> float:
    So = 1.0 - Sw - Sg

    # Choose one:
    return Krw_o(Sw)                   # only oil-water Krw
    # return Krw_g(Sw)                 # only gas-water Krw
    # return Krw_Baker(Sw, Sg)         # interpolated Krw ----------------------------------input


def Krg(Sw: float, Sg: float) -> float:
    So = 1.0 - Sw - Sg

    # Choose one:
    return Krg_o(Sg)                   # only gas-oil Krg
    # return Krg_w(Sg)                 # only gas-water Krg
    # return Krg_Baker(Sw, Sg)         # interpolated Krg --------------------------------input

# Mobility ---------------------------
def lamda_w(Sw: float, Sg: float) -> float:
    return Krw(Sw, Sg) / water_viscosity

def lamda_o(Sw: float, Sg: float) -> float:
    return Kro(Sw, Sg) / oil_viscosity

def lamda_g(Sw: float, Sg: float) -> float:
    return Krg(Sw, Sg) / gas_viscosity

def lamda_t(Sw: float, Sg: float) -> float:
    return lamda_w(Sw, Sg) + lamda_o(Sw, Sg) + lamda_g(Sw, Sg)


# ---------- fractional flow ----------
def f1(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    if lt <= 1e-14:
        return 0.0
    return lamda_w(Sw, Sg) / lt   # water fractional flow

# f1 = fractional flow ของ water, fw =  λw / λt
# f3 = fractional flow ของ gas (CO2)
# คำนวณ total mobility (lt) : λt=λw+λo+λg

def f3(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    if lt <= 1e-14:
        return 0.0
    return lamda_g(Sw, Sg) / lt   # gas fractional flow

def f2(Sw: float, Sg: float) -> float:
    lt = lamda_t(Sw, Sg)
    if lt <= 1e-14:
        return 0.0
    return lamda_o(Sw, Sg) / lt   # oil fractional flow
# เพิ่ม f2 = fractional flow ของ oil เพื่อให้เห็นครบว่า f1 + f2 + f3 = 1

# ---------- find boundary saturation on So = 0 ----------
def find_boundary_saturation_So_zero(target_Fg: float, n_grid: int = 10001):
    """
    Find Sw, So, Sg on the boundary So = 0
    such that f3(Sw, Sg) = target_Fg.

    On So = 0:
        Sg = 1 - Sw
    """

    if target_Fg < 0.0 or target_Fg > 1.0:
        raise ValueError("target_Fg must be between 0 and 1")

    # Search along So = 0 line
    # So = 0 means Sw + Sg = 1
    Sw_min = Swi
    Sw_max = 1.0 - Sgc

    Sw_candidates = np.linspace(Sw_min, Sw_max, n_grid)
    Sg_candidates = 1.0 - Sw_candidates

    fg_values = np.array([
        f3(Sw, Sg)
        for Sw, Sg in zip(Sw_candidates, Sg_candidates)
    ])

    # Find Sw that gives fg closest to target_Fg
    idx = np.argmin(np.abs(fg_values - target_Fg))

    Sw_bc = Sw_candidates[idx]
    Sg_bc = Sg_candidates[idx]
    So_bc = 1.0 - Sw_bc - Sg_bc

    return {
        "Sw_bc": Sw_bc,
        "So_bc": So_bc,
        "Sg_bc": Sg_bc,
        "fw_bc": f1(Sw_bc, Sg_bc),
        "fo_bc": f2(Sw_bc, Sg_bc),
        "fg_bc": f3(Sw_bc, Sg_bc),
        "error_fg": abs(f3(Sw_bc, Sg_bc) - target_Fg),
    }

# ---------- numerical setting ----------
Nx = 1000
xD_max = 1.0
xD = np.linspace(0.0, xD_max, Nx)
dxD = xD[1] - xD[0]

CFL = 0.05

dtD = CFL * dxD

tD_final = 1.0

Nt = int(np.ceil(tD_final / dtD))

dtD = tD_final / Nt

print(f"Total number of time steps (Nt) = {Nt}")
print(f"dxD = {dxD:.6f}")
print(f"dtD = {dtD:.6f}")

# ---------- initial condition ----------
S1 = np.full(Nx, 0.70, dtype=float)   # Sw initial = 0.7 -------------------------------------input
S3 = np.zeros(Nx, dtype=float)       # Sg initial = 0.0
# S2 = 1 - S1 - S3 = 0.3

# ---------- left boundary condition ----------
F3_inlet = 1.0 # -----------------------------------------------------------------------------input
F2_inlet = 0.0
F1_inlet = 1.0 - F2_inlet - F3_inlet

# find boundary at So=0
bc = find_boundary_saturation_So_zero(F3_inlet)

S1_inlet = bc["Sw_bc"]
S2_inlet = bc["So_bc"]
S3_inlet = bc["Sg_bc"]

print("\nBoundary saturation on So = 0:")
print(f"Target Fw = {F1_inlet:.6f}")
print(f"Target Fo = {F2_inlet:.6f}")
print(f"Target Fg = {F3_inlet:.6f}")

print(f"Sw_boundary = {S1_inlet:.6f}")
print(f"So_boundary = {S2_inlet:.6f}")
print(f"Sg_boundary = {S3_inlet:.6f}")

print("\nCheck fractional flow at boundary saturation:")
print(f"fw_boundary = {bc['fw_bc']:.6f}")
print(f"fo_boundary = {bc['fo_bc']:.6f}")
print(f"fg_boundary = {bc['fg_bc']:.6f}")
print(f"error_fg    = {bc['error_fg']:.6e}")

# collecting results of all time steps
S1_history = [S1.copy()]
S3_history = [S3.copy()]
time_step_history = [0]
tD_history = [0.0]

# ---------- explicit forward difference ----------
# finite difference
# forward in time
# backward/upwind in space for flux difference

for n in range(Nt):
    S1_new = S1.copy()
    S3_new = S3.copy()

    for i in range(Nx):

        # ---------- F flow in ----------
        if i == 0:
            F1_in = F1_inlet
            F3_in = F3_inlet

        else:
            F1_in = f1(S1[i-1], S3[i-1])
            F3_in = f3(S1[i-1], S3[i-1])

        # ---------- F flow out ----------
        F1_out = f1(S1[i], S3[i])
        F3_out = f3(S1[i], S3[i])

        # ---------- explicit update ----------
        S1_new[i] = S1[i] + (dtD / dxD) * (F1_in - F1_out)
        S3_new[i] = S3[i] + (dtD / dxD) * (F3_in - F3_out)
        # Si,n+1 = Si,n + (delta t / delta x) * (F flow in - F flow out)

        if (S1_new[i] < -1e-8) or (S3_new[i] < -1e-8) or (S1_new[i] + S3_new[i] > 1.0 + 1e-8):
            print(f"Warning: nonphysical state at step={n}, cell={i}, "
                  f"S1={S1_new[i]}, S3={S3_new[i]}, S2={1 - S1_new[i] - S3_new[i]}")

    # right boundary: zero-gradient
    S1_new[-1] = S1_new[-2]
    S3_new[-1] = S3_new[-2]

    S1 = S1_new
    S3 = S3_new

    S1_history.append(S1.copy())
    S3_history.append(S3.copy())
    time_step_history.append(n + 1)
    tD_history.append((n + 1) * dtD)

# ---------- oil saturation ----------
S2 = 1.0 - S1 - S3

# ---------- x-axis as dimensionless velocity ----------
vD = xD / tD_final
# vD = xD / tD --> dimensionless velocity

# ---------- เลือก time step ที่ต้องการ plot เอง ----------
plot_steps = [0, int(Nt*0.1), int(Nt*0.3), int(Nt*0.6), Nt]
# plot_steps = [0, 50, 100, 300, Nt]

# กันกรณีเลือก step เกินช่วง
plot_steps = sorted(list(set([step for step in plot_steps if 0 <= step <= Nt])))

# ---------- plot ตาม time step ที่เลือก ----------
for step in plot_steps:
    S1_plot = S1_history[step]
    S3_plot = S3_history[step]
    S2_plot = 1.0 - S1_plot - S3_plot

    tD_now = tD_history[step]

    if tD_now == 0:
        continue

    vD = xD / tD_now

    # ---------- plot ----------
    plt.figure(figsize=(8, 5))
    plt.plot(vD, S1_plot, color='blue', label='S1 = Water')
    plt.plot(vD, S2_plot, color='green', label='S2 = Oil')
    plt.plot(vD, S3_plot, color='red', label='S3 = CO2 Gas')

    plt.xlabel('Dimensionless velocity, $v_D = x_D/t_D$')
    plt.ylabel('Saturation')
    plt.title(f'CO2 Injection at time step = {step}, $t_D$ = {tD_now:.5f}')
    plt.ylim(0, 1)
    plt.xlim(vD.min(), vD.max())
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # ---------------------------------------
    # Figure name
    # ---------------------------------------

    figure_name = (
        f"Saturation_tD_{tD_now * 10:.0f}_{case_name}"
    )

    figure_path = os.path.join(
        export_folder,
        figure_name + ".jpg"
    )

    plt.savefig(
        figure_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Figure Saturation_tD_{tD_now:.2f} saved to: {figure_path}")

    # plt.show()
    plt.close()


# ---------- export all results to excel ----------

export_step_stride = 10
# export every 10 time steps --> 0, 10, 20, 30, ...

sampled_steps = list(range(0, len(time_step_history), export_step_stride))

if sampled_steps[-1] != len(time_step_history) - 1:
    sampled_steps.append(len(time_step_history) - 1)

plot_steps_export = [0, int(Nt * 0.1), int(Nt * 0.3), int(Nt * 0.6), Nt]
plot_steps_export = sorted(list(set([step for step in plot_steps_export if 0 <= step <= Nt])))

plot_steps_export = [step for step in plot_steps_export if step != 0]

def build_export_df(step_list):
    export_rows = []

    for step in step_list:
        S1_export = S1_history[step]
        S3_export = S3_history[step]
        S2_export = 1.0 - S1_export - S3_export

        tD_now = tD_history[step]

        # ตอน tD = 0 จะคำนวณ vD ไม่ได้ ให้ใส่ NaN
        if tD_now == 0:
            vD_now = np.full_like(xD, np.nan, dtype=float)
        else:
            vD_now = xD / tD_now

        for i in range(Nx):
            export_rows.append({
                'time_step': time_step_history[step],
                'tD': tD_now,
                'cell_index': i,
                'xD': xD[i],
                'vD': vD_now[i],

                'F1_inlet': F1_inlet,
                'F2_inlet': F2_inlet,
                'F3_inlet': F3_inlet,

                'f1_water': f1(S1_export[i], S3_export[i]),
                'f2_oil': f2(S1_export[i], S3_export[i]),
                'f3_CO2_gas': f3(S1_export[i], S3_export[i]),

                'S1_water': S1_export[i],
                'S2_oil': S2_export[i],
                'S3_CO2_gas': S3_export[i]
            })

    return pd.DataFrame(export_rows)

df_export = build_export_df(sampled_steps)

# ---------- divide all time steps data into 3 groups ----------
sampled_time_steps = sorted(df_export['time_step'].unique())
# last_time_step = max(sampled_time_steps)
#
# cut_1 = last_time_step / 3
# cut_2 = 2 * last_time_step / 3
#
# df_sheet1 = df_export[df_export['time_step'] < cut_1].copy()
# # Sheet 1 : time step 0 to 1/3 of all time step
#
# df_sheet2 = df_export[(df_export['time_step'] >= cut_1) & (df_export['time_step'] < cut_2)].copy()
# # Sheet 2 : 1/3 of time step to 2/3 of all time step
#
# df_sheet3 = df_export[df_export['time_step'] >= cut_2].copy()
# # Sheet 3 : 2/3 ของ time step to last time step
#
# ---------- DataFrame for plot_steps ----------
df_sheet4 = build_export_df(plot_steps_export)
# Sheet 4 : selected time steps for plotting
#
# ---------- DataFrame for Sheet 5: one boundary point where So = 0 ----------
df_sheet5_boundary = pd.DataFrame([{
    'description': 'One boundary saturation point on So = 0',

    'F1_inlet': F1_inlet,
    'F2_inlet': F2_inlet,
    'F3_inlet': F3_inlet,

    'Sw_boundary_So0': S1_inlet,
    'So_boundary_So0': S2_inlet,
    'Sg_boundary_So0': S3_inlet,

    'fw_boundary_So0': bc['fw_bc'],
    'fo_boundary_So0': bc['fo_bc'],
    'fg_boundary_So0': bc['fg_bc'],

    'error_Fg_boundary': bc['error_fg'],

    'lambda_w_boundary': lamda_w(S1_inlet, S3_inlet),
    'lambda_o_boundary': lamda_o(S1_inlet, S3_inlet),
    'lambda_g_boundary': lamda_g(S1_inlet, S3_inlet),
    'lambda_t_boundary': lamda_t(S1_inlet, S3_inlet),
}])

# ---------- export Excel sheets ----------
excel_path = os.path.join(export_folder, 'Displacement.xlsx') #----------------------------------------input

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    # df_sheet1.to_excel(writer, sheet_name='0.33_timestep', index=False)
    # df_sheet2.to_excel(writer, sheet_name='0.67_timestep', index=False)
    # df_sheet3.to_excel(writer, sheet_name='1.00_timestep', index=False)
    df_sheet4.to_excel(writer, sheet_name='plot_steps', index=False)
    df_sheet5_boundary.to_excel(writer, sheet_name='Boundary_So0_point', index=False)

print(f"Excel file exported to: {excel_path}")

print(f"Export stride = every {export_step_stride} time steps")
print(f"Number of sampled time steps = {len(sampled_steps)}")
print(f"Plot steps exported in Sheet 4 = {plot_steps_export}")

# print("\nSheet 1 preview:")
# print(df_sheet1.head())
#
# print("\nSheet 2 preview:")
# print(df_sheet2.head())
#
# print("\nSheet 3 preview:")
# print(df_sheet3.head())

print("\nSheet 4 preview:")
print(df_sheet4.head())

print("\nSheet 5 boundary point preview:")
print(df_sheet5_boundary)

# =======================================================
# Recovery factor and dimensionless CO2 stored
# Calculated directly using dimensionless velocity vD
# =======================================================

# Initial oil saturation
Sw_initial = S1_history[0]
Sg_initial = S3_history[0]
So_initial = 1.0 - Sw_initial - Sg_initial

# Initial average oil saturation
# For a uniform initial condition, this is simply 1 - Swi_initial - Sgi
Soi = np.trapezoid(So_initial, x=xD) / xD_max

print("\nInitial oil saturation:")
print(f"Soi = {Soi:.8f}")


# Store calculated results
NPD_history = []
recovery_factor_history = []
NDS_history = []

average_oil_saturation_history = []
average_gas_saturation_history = []


for step in range(len(tD_history)):

    tD_now = tD_history[step]

    Sw_now = S1_history[step]
    Sg_now = S3_history[step]
    So_now = 1.0 - Sw_now - Sg_now

    # At tD = 0, vD = xD/tD is undefined
    # Physically, no oil has been recovered and no CO2 is stored yet
    if np.isclose(tD_now, 0.0):

        So_average = Soi
        Sg_average = 0.0

        NPD = 0.0
        recovery_factor = 0.0
        NDS = 0.0

    else:

        # ---------------------------------------------------
        # Dimensionless velocity:
        #
        # vD = xD / tD
        #
        # Integration limit:
        #
        # vD_max = xD_max / tD
        #
        # If xD_max = 1:
        # vD_max = 1 / tD
        # ---------------------------------------------------
        vD_now = xD / tD_now
        vD_max = xD_max / tD_now

        # ---------------------------------------------------
        # Average oil saturation:
        #
        # (1 / VD) integral_0^(1/tD) So dvD
        #
        # where VD = vD_max = 1/tD for xD_max = 1
        # ---------------------------------------------------
        integral_So_dvD = np.trapezoid(
            So_now,
            x=vD_now
        )

        So_average = integral_So_dvD / vD_max

        # ---------------------------------------------------
        # Pore volumes of oil recovered:
        #
        # NPD(tD) = Soi
        #           - (1/VD) integral_0^(1/tD) So dvD
        # ---------------------------------------------------
        NPD = Soi - So_average

        # ---------------------------------------------------
        # Recovery factor:
        #
        # Rf = NPD / Soi
        # ---------------------------------------------------
        if Soi > 1e-14:
            recovery_factor = NPD / Soi
        else:
            recovery_factor = np.nan

        # ---------------------------------------------------
        # Dimensionless pore volume of CO2 stored:
        #
        # NDS(tD) =
        # (1/VD) integral_0^(1/tD) Sg dvD
        # ---------------------------------------------------
        integral_Sg_dvD = np.trapezoid(
            Sg_now,
            x=vD_now
        )

        Sg_average = integral_Sg_dvD / vD_max
        NDS = Sg_average

    # Save results
    average_oil_saturation_history.append(So_average)
    average_gas_saturation_history.append(Sg_average)

    NPD_history.append(NPD)
    recovery_factor_history.append(recovery_factor)
    NDS_history.append(NDS)


# Convert lists to NumPy arrays
tD_results = np.asarray(tD_history, dtype=float)

average_oil_saturation_history = np.asarray(
    average_oil_saturation_history,
    dtype=float
)

average_gas_saturation_history = np.asarray(
    average_gas_saturation_history,
    dtype=float
)

NPD_history = np.asarray(
    NPD_history,
    dtype=float
)

recovery_factor_history = np.asarray(
    recovery_factor_history,
    dtype=float
)

NDS_history = np.asarray(
    NDS_history,
    dtype=float
)

# =======================================================
# Plot recovery factor versus tD
# =======================================================

figure_name = f"Recovery_factor_{case_name}"
plt.figure(figsize=(8, 5))
plt.plot(
    tD_results,
    recovery_factor_history,
    linewidth=2
)
plt.xlabel("Dimensionless time, $t_D$")
plt.ylabel("Recovery factor, $R_f$")
plt.title("Oil recovery factor versus dimensionless time")
plt.xlim(0.0, tD_final)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as JPG
figure_path = os.path.join(
    export_folder,
    figure_name + ".jpg"
)
plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)
print(f"Figure Recovery_factor saved to: {figure_path}")
# plt.show()
plt.close()


# =======================================================
# Plot recovery factor in percent versus tD
# =======================================================

recovery_factor_percent = recovery_factor_history * 100.0
figure_name = f"Percent_recovery_factor_{case_name}"
plt.figure(figsize=(8, 5))
plt.plot(
    tD_results,
    recovery_factor_percent,
    linewidth=2
)
plt.xlabel("Dimensionless time, $t_D$")
plt.ylabel("Recovery factor, %")
plt.title("Oil recovery factor versus dimensionless time")
plt.xlim(0.0, tD_final)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as JPG
figure_path = os.path.join(
    export_folder,
    figure_name + ".jpg"
)
plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)
print(f"Figure Percent_recovery saved to: {figure_path}")
# plt.show()
plt.close()


# =======================================================
# Plot dimensionless CO2 stored versus tD
# =======================================================

figure_name = f"N_DS_{case_name}"

plt.figure(figsize=(8, 5))
plt.plot(
    tD_results,
    NDS_history,
    linewidth=2
)
plt.xlabel("Dimensionless time, $t_D$")
plt.ylabel("Dimensionless pore volume stored, $N_{DS}$")
plt.title("Dimensionless CO$_2$ stored versus dimensionless time")
plt.xlim(0.0, tD_final)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as JPG
figure_path = os.path.join(
    export_folder,
    figure_name + ".jpg"
)
plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)
print(f"Figure N_DS saved to: {figure_path}")
# plt.show()
plt.close()


# =======================================================
# Reservoir/model pore volume
# =======================================================

# Model dimensions
model_length = 150.0       # m
model_width = 5.0          # m
model_thickness = 5.0      # m
porosity = 0.25            # fraction

bulk_volume = (
    model_length
    * model_width
    * model_thickness
)

reservoir_pore_volume = (
    bulk_volume * porosity
)

print("\n" + "=" * 80)
print("RESERVOIR / MODEL PROPERTIES")
print("=" * 80)

print(f"Model length              = {model_length:.4f} m")
print(f"Model width               = {model_width:.4f} m")
print(f"Model thickness           = {model_thickness:.4f} m")
print(f"Porosity                   = {porosity:.6f}")
print(f"Bulk volume                = {bulk_volume:.6f} m^3")
print(
    f"Reservoir pore volume, PV = "
    f"{reservoir_pore_volume:.6f} m^3"
)


# =======================================================
# CO2 volume stored at reservoir conditions
#
# V_CO2,res = NDS * PV
# =======================================================

CO2_stored_reservoir_volume = (
    NDS_history * reservoir_pore_volume
)


# =======================================================
# CO2 volume stored at surface conditions
#
# Bg = reservoir volume / surface volume
#
# V_CO2,surface = V_CO2,reservoir / Bg
# =======================================================

# Replace this with the correct CO2 formation volume factor
# at the pressure and temperature of the simulation.
#
# Units:
# reservoir m^3 / surface m^3
Bg = 0.0027018 #--------------------------------------------------------------------------------------input

if Bg <= 0.0:
    raise ValueError("Bg must be greater than zero.")

CO2_stored_surface_volume = (
    CO2_stored_reservoir_volume / Bg
)


# =======================================================
# CO2 mass stored
#
# Method 1:
# mass = reservoir volume * reservoir density
# =======================================================

# Replace with the CO2 density corresponding to the
# same reservoir pressure and temperature used for Bg.
CO2_density_reservoir = 700.0       # kg/m^3 -------------------------------------------------------- input

if CO2_density_reservoir <= 0.0:
    raise ValueError(
        "CO2_density_reservoir must be greater than zero."
    )

CO2_stored_mass_kg = (
    CO2_stored_reservoir_volume
    * CO2_density_reservoir
)

CO2_stored_mass_tonnes = (
    CO2_stored_mass_kg / 1000.0
)


# =======================================================
# Optional mass cross-check using surface volume
#
# mass_surface_check =
# surface volume * surface density
# =======================================================

# Replace with the density at the surface/standard
# conditions used in the definition of Bg.
CO2_density_surface = 1.869         # kg/m^3, -------------------------------------------------- input

CO2_stored_mass_surface_check_kg = (
    CO2_stored_surface_volume
    * CO2_density_surface
)

CO2_stored_mass_surface_check_tonnes = (
    CO2_stored_mass_surface_check_kg / 1000.0
)

mass_difference_percent = np.zeros_like(
    CO2_stored_mass_kg,
    dtype=float
)

nonzero_mass = CO2_stored_mass_kg > 1e-14

mass_difference_percent[nonzero_mass] = (
    (
        CO2_stored_mass_surface_check_kg[nonzero_mass]
        - CO2_stored_mass_kg[nonzero_mass]
    )
    / CO2_stored_mass_kg[nonzero_mass]
    * 100.0
)


# =======================================================
# Print conversion properties
# =======================================================

print("\n" + "=" * 80)
print("CO2 CONVERSION PROPERTIES")
print("=" * 80)

print(
    f"Gas formation volume factor, Bg       = "
    f"{Bg:.8f} reservoir m^3/surface m^3"
)

print(
    f"CO2 density at reservoir conditions   = "
    f"{CO2_density_reservoir:.6f} kg/m^3"
)

print(
    f"CO2 density at surface conditions     = "
    f"{CO2_density_surface:.6f} kg/m^3"
)


# =======================================================
# Plot CO2 volume at reservoir conditions
# =======================================================
figure_name = f"CO2Stored_res_{case_name}"
plt.figure(figsize=(8, 5))

plt.plot(
    tD_results,
    CO2_stored_reservoir_volume,
    linewidth=2
)

plt.xlabel("Dimensionless time, $t_D$")
plt.ylabel(
    "CO$_2$ stored at reservoir conditions, m$^3$"
)
plt.title(
    "CO$_2$ volume stored at reservoir conditions"
)
plt.xlim(0.0, tD_final)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as JPG
figure_path = os.path.join(
    export_folder,
    figure_name + ".jpg"
)
plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)
print(f"Figure CO2Stored_res saved to: {figure_path}")
# plt.show()
plt.close()


# =======================================================
# Plot CO2 volume at surface conditions
# =======================================================
figure_name = f"CO2Stored_surface_{case_name}"
plt.figure(figsize=(8, 5))

plt.plot(
    tD_results,
    CO2_stored_surface_volume,
    linewidth=2
)

plt.xlabel("Dimensionless time, $t_D$")
plt.ylabel(
    "CO$_2$ stored at surface conditions, m$^3$"
)
plt.title(
    "CO$_2$ volume stored at surface conditions"
)
plt.xlim(0.0, tD_final)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as JPG
figure_path = os.path.join(
    export_folder,
    figure_name + ".jpg"
)
plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)
print(f"Figure CO2Stored_surface saved to: {figure_path}")
# plt.show()
plt.close()


# =======================================================
# Plot CO2 mass stored in tonnes
# =======================================================
figure_name = f"CO2Stored_mass_{case_name}"
plt.figure(figsize=(8, 5))

plt.plot(
    tD_results,
    CO2_stored_mass_tonnes,
    linewidth=2
)

plt.xlabel("Dimensionless time, $t_D$")
plt.ylabel("CO$_2$ mass stored, tonnes")
plt.title("Mass of CO$_2$ stored")
plt.xlim(0.0, tD_final)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save as JPG
figure_path = os.path.join(
    export_folder,
    figure_name + ".jpg"
)
plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)
print(f"Figure CO2Stored_mass saved to: {figure_path}")
# plt.show()
plt.close()

# =======================================================
# Selected tD values for summary
# =======================================================

selected_tD_values = np.round(
    np.arange(
        0.0,
        tD_final + 0.0001,
        0.1
    ),
    2
)


# =======================================================
# Build complete summary
# =======================================================

summary_rows = []

for target_tD in selected_tD_values:

    # Find the numerical time nearest to target tD
    step = int(
        np.argmin(
            np.abs(tD_results - target_tD)
        )
    )

    summary_rows.append({
        "time_step":
            time_step_history[step],

        "target_tD":
            target_tD,

        "actual_tD":
            tD_results[step],

        "initial_oil_saturation_Soi":
            Soi,

        "average_oil_saturation":
            average_oil_saturation_history[step],

        "oil_recovered_NPD":
            NPD_history[step],

        "recovery_factor":
            recovery_factor_history[step],

        "recovery_factor_percent":
            recovery_factor_percent[step],

        "average_gas_saturation":
            average_gas_saturation_history[step],

        "NDS_dimensionless_PV_stored":
            NDS_history[step],

        "reservoir_pore_volume_m3":
            reservoir_pore_volume,

        "CO2_stored_reservoir_m3":
            CO2_stored_reservoir_volume[step],

        "Bg_reservoir_m3_per_surface_m3":
            Bg,

        "CO2_stored_surface_m3":
            CO2_stored_surface_volume[step],

        "CO2_density_reservoir_kg_m3":
            CO2_density_reservoir,

        "CO2_mass_stored_kg":
            CO2_stored_mass_kg[step],

        "CO2_mass_stored_tonnes":
            CO2_stored_mass_tonnes[step],

        "CO2_density_surface_kg_m3":
            CO2_density_surface,

        "CO2_mass_surface_check_kg":
            CO2_stored_mass_surface_check_kg[step],

        "mass_difference_percent":
            mass_difference_percent[step]
    })


results_summary = pd.DataFrame(summary_rows)


# =======================================================
# Print complete summary
# =======================================================

print("\n" + "=" * 180)
print("OIL RECOVERY AND CO2 STORAGE SUMMARY")
print("=" * 180)

columns_to_print = [
    "time_step",
    "actual_tD",
    "average_oil_saturation",
    "oil_recovered_NPD",
    "recovery_factor",
    "recovery_factor_percent",
    "NDS_dimensionless_PV_stored",
    "CO2_stored_reservoir_m3",
    "CO2_stored_surface_m3",
    "CO2_mass_stored_kg",
    "CO2_mass_stored_tonnes"
]

print(
    results_summary[
        columns_to_print
    ].to_string(
        index=False,
        float_format=lambda value: f"{value:.8f}"
    )
)


# =======================================================
# Print final-time result separately
# =======================================================

final_step = len(tD_results) - 1

print("\n" + "=" * 80)
print("FINAL-TIME RESULT")
print("=" * 80)

print(f"Time step                     = {time_step_history[final_step]}")
print(f"Dimensionless time, tD        = {tD_results[final_step]:.8f}")

print(
    f"Average oil saturation        = "
    f"{average_oil_saturation_history[final_step]:.8f}"
)

print(
    f"Oil recovered, NPD            = "
    f"{NPD_history[final_step]:.8f} PV"
)

print(
    f"Recovery factor               = "
    f"{recovery_factor_history[final_step]:.8f}"
)

print(
    f"Recovery factor               = "
    f"{recovery_factor_percent[final_step]:.6f} %"
)

print(
    f"Dimensionless CO2 stored, NDS = "
    f"{NDS_history[final_step]:.8f} PV"
)

print(
    f"CO2 stored at reservoir cond. = "
    f"{CO2_stored_reservoir_volume[final_step]:.8f} m^3"
)

print(
    f"CO2 stored at surface cond.   = "
    f"{CO2_stored_surface_volume[final_step]:.8f} m^3"
)

print(
    f"CO2 mass stored               = "
    f"{CO2_stored_mass_kg[final_step]:.8f} kg"
)

print(
    f"CO2 mass stored               = "
    f"{CO2_stored_mass_tonnes[final_step]:.8f} tonnes"
)

print(
    f"Mass from surface cross-check = "
    f"{CO2_stored_mass_surface_check_tonnes[final_step]:.8f} tonnes"
)

print(
    f"Mass calculation difference   = "
    f"{mass_difference_percent[final_step]:.6f} %"
)


# =======================================================
# Export complete summary to Excel
# =======================================================

export_folder = (
    r"C:\Users\oa2414\PycharmProjects"
    r"\3-phase_finite_diff"
) #-----------------------------------------------------------------------------------------------------input

os.makedirs(export_folder, exist_ok=True)

summary_excel_path = os.path.join(
    export_folder,
    "Oil_recovery_CO2_storage_summary.xlsx"
)

all_time_results = pd.DataFrame({
    "time_step": time_step_history,
    "tD": tD_results,

    "initial_oil_saturation_Soi":
        np.full(len(tD_results), Soi),

    "average_oil_saturation":
        average_oil_saturation_history,

    "oil_recovered_NPD":
        NPD_history,

    "recovery_factor":
        recovery_factor_history,

    "recovery_factor_percent":
        recovery_factor_percent,

    "average_gas_saturation":
        average_gas_saturation_history,

    "NDS_dimensionless_PV_stored":
        NDS_history,

    "reservoir_pore_volume_m3":
        np.full(
            len(tD_results),
            reservoir_pore_volume
        ),

    "CO2_stored_reservoir_m3":
        CO2_stored_reservoir_volume,

    "Bg_reservoir_m3_per_surface_m3":
        np.full(len(tD_results), Bg),

    "CO2_stored_surface_m3":
        CO2_stored_surface_volume,

    "CO2_density_reservoir_kg_m3":
        np.full(
            len(tD_results),
            CO2_density_reservoir
        ),

    "CO2_mass_stored_kg":
        CO2_stored_mass_kg,

    "CO2_mass_stored_tonnes":
        CO2_stored_mass_tonnes,

    "CO2_density_surface_kg_m3":
        np.full(
            len(tD_results),
            CO2_density_surface
        ),

    "CO2_mass_surface_check_kg":
        CO2_stored_mass_surface_check_kg,

    "mass_difference_percent":
        mass_difference_percent
})


with pd.ExcelWriter(
    summary_excel_path,
    engine="openpyxl"
) as writer:

    all_time_results.to_excel(
        writer,
        sheet_name="All_time_steps",
        index=False
    )

    results_summary.to_excel(
        writer,
        sheet_name="Selected_tD",
        index=False
    )


print("\nSummary exported to:")
print(summary_excel_path)