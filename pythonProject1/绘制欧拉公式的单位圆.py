import matplotlib.pyplot as plt
import numpy as np

# 生成 x 的值
x = np.linspace(0, 2 * np.pi, 1000)

# 计算 e^ix 的值
z = np.exp(1j * x)

# 提取实部和虚部
re = np.real(z)
im = np.imag(z)

# 绘制单位圆
plt.figure(figsize=(6, 6))
plt.plot(re, im, label='$e^{ix} = \cos(x) + i\sin(x)$')
plt.xlabel('Re')
plt.ylabel('Im')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('represent $e^{ix}$')
plt.show()

