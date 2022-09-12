"""
可视化画图的基本用法
Matplotlib属于第三方库，在绘图时主要运用其pyplot子模块并命名plt,语法如下:
import matplotlib.pyplot as plt
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x_data = [1,2,3,4]
y_data = [6,9,4,13]
plt.plot(x_data,y_data)#调用plt中的plot画折线图
plt.show()
