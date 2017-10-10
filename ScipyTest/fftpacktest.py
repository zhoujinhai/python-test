# coding=utf-8
# scipy's 的傅里叶变换

import numpy as np
from scipy import fftpack
import matplotlib.pylab as plt

# 信号输入
time_step = 0.02
period = 5
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2*np.pi/period*time_vec) + 0.5*np.random.randn(time_vec.size)
# print(sig)

# 利用fftpack.fftfreq()函数生成样本序列
sample_freq = fftpack.fftfreq(sig.size, d=time_step)
sig_fft = fftpack.fft(sig)

# 只需要使用频谱为正的部分
pidxs = np.where(sample_freq > 0)
freqs = sample_freq[pidxs]
power = np.abs(sig_fft)[pidxs]

# 寻找信号频率
freq = freqs[power.argmax()]
print(np.allclose(freq, 1./period))  # 检查是否找到了正确的频率

# 将高频噪音从傅里叶转换过得信号中移除
sig_fft[np.abs(sample_freq) > freq] = 0

# 生成过滤过的信号
main_sig = fftpack.ifft(sig_fft)

# 查看结果
plt.figure()
plt.plot(time_vec, sig)
plt.plot(time_vec, main_sig, linewidth=3)
plt.xlabel('time [s]')
plt.ylabel('Amplitude')
plt.show()
