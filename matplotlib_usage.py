
import matplotlib.pylab as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0,10,20)
y = x*x+2
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
# 控制画布的左, 下, 宽度, 高度 (从 0 到 1)
axes.plot(x,y,'r')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2) # 子图为 1 行，2 列
for ax in axes:
    ax.plot(x, y, 'r')
plt.show()

"""还能将一张图绘制在另一张图的内部
"""
fig = plt.figure() # 新建画板

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # 大画布
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # 小画布

# 大画布
axes1.plot(x, y, 'r')

# 小画布
axes2.plot(y, x, 'g')
plt.show()

"""
add_axes() 方法向我们设置的画板 figure 中添加画布 axes。
在 Matplotlib 中，还有一种添加画布的方式，
那就是plt.subplots()，它和 axes 都等同于画布。
方法 2：使用 plt.subplots() 添加画布
"""
fig, axes = plt.subplots()

axes.plot(x, y, 'r')
plt.show()


"""方法 3：使用 add_subplot() 添加画布
"""
fig = plt.figure() # 新建图形对象

fig.add_subplot()

plt.plot(x, y, 'r')
plt.show()



"""调节画布尺寸和显示精度
"""
fig, axes = plt.subplots(figsize=(16,9), dpi=50) # 通过 figsize 调节尺寸, dpi 调节显示精度

axes.plot(x, y, 'r')
"""设置图标题
"""
axes.set_title("title")
"""设置坐标轴名称
"""
axes.set_xlabel("x")
axes.set_ylabel("y")
"""设置图例
"""
axes.legend(["label1", "label2"])
plt.show()

"""绘制包含图标题、坐标轴标题以及图例的图形
"""
fig, axes = plt.subplots()

axes.set_xlabel('x label')
axes.set_ylabel('y label')
axes.set_title('title')

axes.plot(x, x**2)
axes.plot(x, x**3)
axes.legend(["y = x**2", "y = x**3"], loc=2)
#图例中的 loc 参数标记图例位置，1，2，3，4 依次代表：右上角、左上角、左下角，右下角；0 代表自适应
plt.show()

"""设置线的颜色、透明度
"""
fig, axes = plt.subplots()

axes.plot(x, x+1, color="red", alpha=0.5)
axes.plot(x, x+2, color="#1155dd")
axes.plot(x, x+3, color="#15cc55")
plt.show()

"""设置线型
"""
fig, ax = plt.subplots(figsize=(12,6))

# 线宽
ax.plot(x, x+1, color="blue", linewidth=0.25)
ax.plot(x, x+2, color="blue", linewidth=0.50)
ax.plot(x, x+3, color="blue", linewidth=1.00)
ax.plot(x, x+4, color="blue", linewidth=2.00)

# 虚线类型
ax.plot(x, x+5, color="red", lw=2, linestyle='-')
ax.plot(x, x+6, color="red", lw=2, ls='-.')
ax.plot(x, x+7, color="red", lw=2, ls=':')

# 虚线交错宽度
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])

# 符号
ax.plot(x, x+ 9, color="green", lw=2, ls='--', marker='+')
ax.plot(x, x+10, color="green", lw=2, ls='--', marker='o')
ax.plot(x, x+11, color="green", lw=2, ls='--', marker='s')
ax.plot(x, x+12, color="green", lw=2, ls='--', marker='1')

# 符号大小和颜色
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")


plt.show()


"""设置画布网格和坐标轴范围
"""
fig, axes = plt.subplots(1, 2, figsize=(10,5))

# 显示网格
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# 设置坐标轴范围
axes[1].plot(x, x**2, x, x**3)
axes[1].set_ylim([0, 60])
axes[1].set_xlim([2, 5])

plt.show()

"""绘制散点图、梯步图、条形图、面积图
"""
n = np.array([0,1,2,3,4,5])

fig, axes = plt.subplots(1, 4, figsize=(16,5))

axes[0].scatter(x, x + 0.25*np.random.randn(len(x)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
axes[3].set_title("fill_between")
plt.show()


"""绘制雷达图
"""
fig = plt.figure(figsize=(6,6))
ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, t, color='blue', lw=3)
plt.show()

"""绘制直方图
"""
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title("Default histogram")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Cumulative detailed histogram")
axes[1].set_xlim((min(n), max(n)))

plt.show()

# 生成示例数据
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

"""绘制等高线图
"""
fig, ax = plt.subplots()

cnt = ax.contour(Z, cmap=plt.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
plt.show()


"""绘制 3D 表面图
使用 Matplotlib 绘制 3D 图形的过程中，我们首先需要导入 Axes3D 类，并通过 projection='3d' 参数指定绘制 3D 图形。
"""
from mpl_toolkits.mplot3d.axes3d import Axes3D

fig = plt.figure(figsize=(14,6))

# 通过 projection='3d' 指定绘制 3D 图形
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)
plt.show()

"""绘制复杂一些的 3D 图
"""
fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=plt.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=plt.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=plt.cm.coolwarm)

ax.set_xlim3d(-np.pi, 2*np.pi)
ax.set_ylim3d(0, 3*np.pi)
ax.set_zlim3d(-np.pi, 2*np.pi)
plt.show()