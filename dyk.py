import numpy as np
import matplotlib.pyplot as plt

# ================= 1. 实验已知参数 =================
d = 0.010          # 样品厚度 (m)
R = 110            # 加热器电阻 (Ω)
S = 0.009529       # 加热面积 (m^2)
alpha = 0.04       # 热电偶常数 (mV/K)
U0 = 18.0          # 加热电压 (V)

rho_plexi = 1196   # 有机玻璃密度 (kg/m^3)
rho_rubber = 1374  # 橡胶密度 (kg/m^3)

# ================= 2. 最新实验数据录入 =================
t = np.arange(1, 19) # 时间 1-18 min

# 有机玻璃数据
Delta_T_plexi = np.array([2.325, 3.150, 3.650, 3.925, 4.075, 4.175, 4.225, 4.250, 4.275, 4.275, 4.300, 4.300, 4.300, 4.325, 4.325, 4.350, 4.350, 4.350])
Delta_U_plexi = np.array([np.nan, 0.006, 0.015, 0.020, 0.021, 0.021, 0.023, 0.023, 0.024, 0.023, 0.022, 0.023, 0.023, 0.023, 0.023, 0.022, 0.022, 0.022])

# 橡胶数据
Delta_T_rubber = np.array([1.575, 1.675, 1.850, 1.900, 1.900, 1.900, 1.875, 1.850, 1.825, 1.800, 1.775, 1.750, 1.725, 1.675, 1.675, 1.650, 1.625, 1.600])
Delta_U_rubber = np.array([np.nan, 0.011, 0.019, 0.020, 0.021, 0.023, 0.023, 0.023, 0.023, 0.022, 0.022, 0.022, 0.023, 0.021, 0.021, 0.023, 0.021, 0.021])

# ================= 3. 数据计算 =================
# 计算热流量密度 qc (W/m^2)
qc = (U0**2) / (2 * S * R)

# --- 有机玻璃：选取 t=15~18 min 作为准稳态 ---
steady_idx_plexi = slice(14, 18) # 索引 14 到 17 对应 t=15,16,17,18
avg_Delta_T_plexi = np.mean(Delta_T_plexi[steady_idx_plexi])
avg_Delta_U_plexi = np.mean(Delta_U_plexi[steady_idx_plexi])
dT_dt_plexi = avg_Delta_U_plexi / (60 * alpha)

lambda_plexi = (qc * d) / (2 * avg_Delta_T_plexi)
c_plexi = qc / (rho_plexi * d * dT_dt_plexi)

# --- 橡胶：选取 t=4~6 min 作为准稳态 (因为此时 ΔT 恒定为 1.900) ---
steady_idx_rubber = slice(3, 6) # 索引 3 到 5 对应 t=4,5,6
avg_Delta_T_rubber = np.mean(Delta_T_rubber[steady_idx_rubber])
avg_Delta_U_rubber = np.mean(Delta_U_rubber[steady_idx_rubber])
dT_dt_rubber = avg_Delta_U_rubber / (60 * alpha)

lambda_rubber = (qc * d) / (2 * avg_Delta_T_rubber)
c_rubber = qc / (rho_rubber * d * dT_dt_rubber)

# ================= 4. 打印计算结果 =================
print(f"热流量密度 qc = {qc:.2f} W/m^2\n")
print(f"--- 有机玻璃 (选取 t=15~18min) ---")
print(f"稳态温差 ΔT = {avg_Delta_T_plexi:.3f} K")
print(f"导热系数 λ = {lambda_plexi:.4f} W/(m·K)")
print(f"比热容 c = {c_plexi:.1f} J/(kg·K)\n")
print(f"--- 橡胶 (选取 t=4~6min) ---")
print(f"稳态温差 ΔT = {avg_Delta_T_rubber:.3f} K")
print(f"导热系数 λ = {lambda_rubber:.4f} W/(m·K)")
print(f"比热容 c = {c_rubber:.1f} J/(kg·K)\n")

# ================= 5. 绘制 ΔT-t 曲线图 =================
plt.figure(figsize=(10, 6))
plt.plot(t, Delta_T_plexi, 'bo-', label='Plexiglass (有机玻璃)', linewidth=2)
plt.plot(t, Delta_T_rubber, 'ro-', label='Rubber (橡胶)', linewidth=2)

# 标记有机玻璃的准稳态区域 (t=15-18)
plt.axvspan(14.5, 18.5, color='blue', alpha=0.1)
plt.text(16.5, 4.1, 'Quasi-steady\n(Plexiglass)', ha='center', color='blue')

# 标记橡胶的准稳态区域 (t=4-6)
plt.axvspan(3.5, 6.5, color='red', alpha=0.1)
plt.text(5, 1.5, 'Quasi-steady\n(Rubber)', ha='center', color='red')

plt.title('Temperature Difference vs Time ($\Delta T - t$)', fontsize=14)
plt.xlabel('Time $t$ (min)', fontsize=12)
plt.ylabel('Temperature Difference $\Delta T$ (K)', fontsize=12)
plt.xticks(t)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()