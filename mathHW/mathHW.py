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

# x=np.linspace(0.000001,10000.1, 100)
# f1=np.log10(x)
# g=np.log(x)
# plt.figure()
# plt.plot(x,f1,"r",x,g,"g")
# plt.show()

# import math
# 100000*math.exp(0.075*4.5)

# import math
# t=(math.log(8/5))/(0.12)
# print(t)

# import math
# t=math.log(1.02,8/5)
# print(t)

# import math
# Q=500*math.exp(0.195*12)
# print(Q)

# import math
# t=math.log(20)/0.195
# print(t)

# import math
# T=10000*(1+0.055/4)**(11/3)*4
# print(T)

# import math
# T=10000*(1+0.055/12)**(11/3)*12
# print(T)

# import math
# Q=10000*math.exp(0.055*(3/11))
# print(Q)

# import math
# t=math.log(2,1.03)/4
# print(t)

# import math
# t=math.log(2,1.01)/12
# print(t)

# import math
# t=math.log(2)/0.12
# print(t)

# import math
# t=math.log(6.4)/5
# print(t)

# import math
# t=math.log(8)/0.37
# print(t)

x=np.linspace(0.000001,10000.1, 100)
f1=np.log10(x)
g=np.log(x)
plt.figure()
plt.plot(x,f1,"r",x,g,"g")
plt.show()



