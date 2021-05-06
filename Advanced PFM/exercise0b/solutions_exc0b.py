# TASK: Manual 'Fit'

f = 2*(np.sin(x+np.pi/4)**2)-1 # after trial and error you could arrive at this function!
g = np.sin(2*x)
plt.plot(x, f, label='$sin(\alpha(x-x_0)^2$')
plt.plot(x, g, 'x', label='sin($2x$)')
plt.legend()
plt.show()

# or

f = 2*np.sin(x+pi/4)**2-1
g = np.sin(2*x)
plt.plot(x,f,label='approximation')
plt.plot(x,g, 'o', markerfacecolor='none', label='sin($2x$)')
plt.legend()
plt.show()




# TASK: Scaled display of data

plt.loglog(x, y, 'o',label='mammal data')
plt.loglog(x,5*x**0.8, label='fit')
plt.legend()
plt.xlabel('body weight [kg]')
plt.ylabel('brain weight [g]')
plt.grid(True)
plt.show()

