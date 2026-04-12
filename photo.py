import numpy as np
import matplotlib.pyplot as plt

# ================= 实验已知参数 =================
d = 0.010          # 样品厚度 (m)
R = 110            # 加热器电阻 (Ω)
S = 0.009529       # 加热面积 (m^2)
alpha = 0.04       # 热电偶常数 (mV/K)
U0 = 18.0          # 加热电压 (V) -> 【请核对：如果你的实际电压是19V，请在此处修改】

rho_plexi = 1196   # 有机玻璃密度 (kg/m^3)
rho_rubber = 1374  # 橡胶密度 (kg/m^3) -> 【请核对：根据手写笔迹辨认，若有误请修改】

# ================= 提取的实验数据 =================
# 时间 t (min)
t = np.arange(1, 19)

# 有机玻璃数据 (Plexiglass)
Ut_plexi = np.array([0.095, 0.129, 0.148, 0.158, 0.164, 0.167, 0.169, 0.170, 0.170, 0.172, 0.172, 0.173, 0.173, 0.173, 0.174, 0.175, 0.175, 0.175])
U_plexi = np.array([0.747, 0.749, 0.756, 0.768, 0.782, 0.796, 0.812, 0.830, 0.846, 0.863, 0.880, 0.897, 0.914, 0.932, 0.950, 0.967, 0.984, 1.001])

# 橡胶数据 (Rubber)
Ut_rubber = np.array([0.063, 0.085, 0.095, 0.097, 0.099, 0.100, 0.100, 0.100, 0.100, 0.100, 0.099, 0.099, 0.099, 0.099, 0.098, 0.098, 0.098, 0.098])
U_rubber = np.array([0.034, 0.046, 0.065, 0.086, 0.110, 0.131, 0.154, 0.177, 0.200, 0.223, 0.246, 0.269, 0.291, 0.314, 0.336, 0.357, 0.379, 0.400])

# ================= 数据计算 =================
# 1. 计算温差 ΔT
Delta_T_plexi = Ut_plexi / alpha
Delta_T_rubber = Ut_rubber / alpha

# 2. 计算热流量密度 qc (单位: W/m^2)
qc = (U0**2) / (2 * S * R)

# 3. 提取准稳态数据 (选取最后4分钟, 即第15-18分钟的数据作为准稳态区间计算)
steady_idx_start = -4

# 有机玻璃准稳态参数
avg_Delta_T_plexi = np.mean(Delta_T_plexi[steady_idx_start:])
delta_U_plexi_avg = np.mean(np.diff(U_plexi)[steady_idx_start-1:]) # 每分钟 ΔU 平均值
dT_dt_plexi = delta_U_plexi_avg / (60 * alpha) # 升温速率 K/s

# 橡胶准稳态参数
avg_Delta_T_rubber = np.mean(Delta_T_rubber[steady_idx_start:])
delta_U_rubber_avg = np.mean(np.diff(U_rubber)[steady_idx_start-1:])
dT_dt_rubber = delta_U_rubber_avg / (60 * alpha)

# 4. 计算导热系数 λ (W/(m·K)) 和 比热容 c (J/(kg·K))
lambda_plexi = (qc * d) / (2 * avg_Delta_T_plexi)
c_plexi = qc / (rho_plexi * d * dT_dt_plexi)

lambda_rubber = (qc * d) / (2 * avg_Delta_T_rubber)
c_rubber = qc / (rho_rubber * d * dT_dt_rubber)

# ================= 终端输出计算结果 =================
print(f"--- 统一计算结果 ---")
print(f"热流量密度 qc = {qc:.2f} W/m^2\n")

print(f"--- 有机玻璃 (Plexiglass) ---")
print(f"稳态温差 ΔT ≈ {avg_Delta_T_plexi:.3f} K")
print(f"导热系数 λ = {lambda_plexi:.4f} W/(m·K)")
print(f"比热容 c = {c_plexi:.1f} J/(kg·K)\n")

print(f"--- 橡胶 (Rubber) ---")
print(f"稳态温差 ΔT ≈ {avg_Delta_T_rubber:.3f} K")
print(f"导热系数 λ = {lambda_rubber:.4f} W/(m·K)")
print(f"比热容 c = {c_rubber:.1f} J/(kg·K)\n")

# ================= 绘图 (任务1) =================
plt.figure(figsize=(10, 6))

# 为了避免中文乱码，图表标签使用英文，可根据本地环境修改
plt.plot(t, Delta_T_plexi, 'bo-', label='Plexiglass (有机玻璃)', linewidth=2)
plt.plot(t, Delta_T_rubber, 'ro-', label='Rubber (橡胶)', linewidth=2)

# 标记准稳态区域
plt.axvspan(14.5, 18.5, color='gray', alpha=0.2, label='Quasi-steady State Region')

plt.title('Temperature Difference vs Time ($\Delta T - t$)', fontsize=14)
plt.xlabel('Time $t$ (min)', fontsize=12)
plt.ylabel('Temperature Difference $\Delta T$ (K)', fontsize=12)
plt.xticks(t)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()