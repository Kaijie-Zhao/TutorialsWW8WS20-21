# TASK: Import of constants

from math import pi




# TASK: Functions I

def convertF(TC):
    """
    A function definition: Converts from Centigrade to Fahrenheit
    TC: temperature in Centrigrade
    TF: temperature in Fahrenheit
    """
    TF = 9.0/5.0*TC + 32.0
    return TF # the return value

convertF(100)
print(convertF.__doc__) # this prints out the docstring of the fct.




# TASK: Functions II

def convertC(TF):
    """
    Converts from Fahrenheit to Centigrade
    TC: temperature in Centrigrade
    TF: temperature in Fahrenheit
    """
    TC = 5.0/9.0*(TF - 32.0)
    return TC


from temperature import convertF, convertC





# TASK: Display the second last element in the list days_of_week!

days_of_the_week[-2]




# TASK: Create a list, which contains all numbers between 0 and 20 divisible by 2 und 3!

a = range(0,20,2)
b = range(0,20,3)
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
print(c)


# OR:


c = []
for i in range(20):
    if i%2 == 0 and i%3 == 0:
        c.append(i)
print(c)




# TASK: Volume of a parallelepiped (rhomboid)

a = np.array([1, 0, 0])
b = np.array([0, 1, 0])
c = np.array([1, 1, 1])

V = np.dot(a,np.cross(b,c))

# OR:
C = np.zeros((3,3))
C[:,0] = a
C[:,1] = b
C[:,2] = c
np.linalg.det(C)




# TASK: Create a (5x5) matrix consisting of an outer frame and filled inner pixel

im = np.zeros((5,5))
im[:,0]  = 1
im[:,-1] = 1
im[0,:]  = 1
im[-1,:] = 1
im[2,2]  = 1

plt.imshow(im)
plt.colorbar()
plt.show()

