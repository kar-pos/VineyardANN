import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

from ANN1 import ANN1_fun
from ANN2 import ANN2_fun

#calculating
input1=[15,	274.5,	1372500,	860,	118035000,	53,	7274250]
input1=np.transpose(input1)
result1=ANN1_fun(input1)
print(result1)

input2=[18,	1.8,	9000,	100,	1.063829787]
input2=np.transpose(input2)
result2=ANN2_fun(input2)
