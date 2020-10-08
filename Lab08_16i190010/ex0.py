import matplotlib.pyplot as plt
import numpy as np
z=np.linspace(-5.0,5.0,2000)
hinge=[]
logistic=[]
sq_hinge=[]
for i in z:
    p1=max(0,1-i)
    p2=np.log(1+(np.exp(-i)))
    p3=(max(0,1-i))**2
    hinge.append(p1)
    logistic.append(p2)
    sq_hinge.append(p3)
print logistic
plt.plot(z, hinge, 'r', label='Hinge loss')
plt.plot(z, logistic, 'b', label='Logistic loss')
plt.plot(z, sq_hinge, 'g', label='Squared hinge loss')
plt.legend(loc='upper right', numpoints=1)
plt.title("Behaviour of different loss functions")
plt.xlabel("z")
plt.ylabel("loss")
plt.show()
plt.savefig("output_ex0.png")