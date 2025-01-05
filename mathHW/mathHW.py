import matplotlib.pyplot as plt
import math
import numpy as np



# x=np.linspace(-2, 2, 200)
# f1=6**x
# f2=6**x-9
# f3=6**(x+1)
# plt.figure()
# plt.plot(x,f1,"r",x,f2,"b",x,f3,"g")
# plt.show()

# x=np.linspace(-2, 2, 100)
# f1=1/np.exp(x)
# plt.figure()
# plt.plot(x,f1)
# plt.show()

# x=np.linspace(-2, 2, 100)
# f1=np.exp(x-3)+6
# plt.figure()
# plt.plot(x,f1)
# plt.show()

x=np.linspace(0.000001,10000.1, 100)
f1=np.log10(x)
g=np.log(x)
plt.figure()
plt.plot(x,f1,"r",x,g,"g")
plt.show()
