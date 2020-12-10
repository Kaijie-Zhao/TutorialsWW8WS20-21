# TASK: Effect of gradient energy and potential
increasing K and decreasing H have the same effect: the interface width goes down
decreasing K and increasing H has the opposite effect.
This all is in line with the analytica results that width ~ sqrt(K*H)




# TASK: Choice of time step width
increasing delta_t over the critical step width (for diffusion eq. solved with forward Euler scheme) creates a diverging solution with limitless growth of the numerical values.
In 1D, values of 80% of the critical time step already ruin the solution, this is possibly due to the fact, that the source term in the phase-field equation has an additional destabilizing effect.




# TASK:  Dependency on grid resolution
          energy(anal.)  energy(sim.)  PF-width(anal.)  PF-width(sim.)
K=1,H=1   0.943          0.876         1.414            1.329
K=4,H=1   1.886          1.854         2.828            2.795
K=16,H=1  3.771          3.756         5.657            5.641




# TASK: Phase-field in 2D

# Initial condition
def initialCond(psi0, N):
    """This is a definition of a function, which takes psi0 and N as parameters.
    Here we fill a circular domain with radius r, at center (cx,cy)"""
    r, cx, cy = 30, 50, 50
    r2 = r**2
    for i in range(N):
        for j in range(N):
            p2 = (i*dx-cx)**2 + (j*dx-cy)**2
            if p2 < r2:  # if point lies inside circle, fill it with 1.0
                psi0[i,j] = 1.0
    return psi0


# Model parameters --------------------------------------------
K = 1.0  # gradient energy coefficient
H = 1.0  # potential energy coefficient
Gamma = 1.0 # mobility parameter
L = 100.0  # side length of the (square) domain


# Numerical setup ---------------------------------------------
N = 101
#x = np.linspace(0, 100, N)
dx = L/(N-1)
dx2 = dx*dx

steps = 2500 # no. of time steps
delta_t = dx**2/(4*Gamma*K) # stable time step of the FCTS scheme (4 for 2D!)
print('stability limit:', delta_t)
delta_t = 0.8*delta_t

psi0 = -np.ones((N, N))     # create & initialize psi0 as (NxN) array with value -1
psi0 = initialCond(psi0, N) # set initial condition
psi = np.zeros((N, N))      # identical array for the update
psi_sav = np.zeros((steps,N,N)) # a (steps x (NxN)) array to store all time steps



# The time loop -----------------------------------------------
for n in range(steps):
    #tmp = -K*(psi0[2:] - 2*psi0[1:-1] + psi0[:-2])/dx**2 + H*df_dw(psi0[1:-1])
    tmp = -K*(psi0[2:,1:-1] + psi0[1:-1,2:] - 4*psi0[1:-1,1:-1] + psi0[:-2,1:-1] + psi0[1:-1,:-2]/dx2) \
         + H*df_dw(psi0[1:-1,1:-1])
    psi[1:-1, 1:-1] = psi0[1:-1, 1:-1] - Gamma*delta_t*tmp
    
    psi[0,:] = psi[1,:]     # Neumann condition at left,
    psi[N-1,:] = psi[N-2,:] # right
    psi[:,0] = psi[:,1]     # top
    psi[:,N-1] = psi[N-2]   # bottom boundary
    
    psi0 = np.copy(psi) # buffer actual time step
    
    psi_sav[n,:] = psi  # store result as another frame

    
# Plot the result --------------------------------------------
plt.imshow(psi, cmap = 'hot', vmin=0, vmax=1)
plt.colorbar()
plt.show()




# TASK: Random initial condition

# Initial condition
def initialCond(psi0, N):
    """Random initial filling"""
    #psi0 = uniform(-1,1,(N,N))
    psi0 = randint(-1,2,(N,N))
    return psi0


# Model parameters --------------------------------------------
K = 4.0  # gradient energy coefficient
H = 1.0  # potential energy coefficient
Gamma = 1.0 # mobility parameter
L = 100.0  # side length of the (square) domain


# Numerical setup ---------------------------------------------
N = 101
#x = np.linspace(0, 100, N)
dx = L/(N-1)
dx2 = dx*dx

steps = 5000 # no. of time steps
delta_t = dx**2/(4*Gamma*K) # stable time step of the FCTS scheme (4 for 2D!)
print('stability limit:', delta_t)
delta_t = 0.8*delta_t

psi0 = -np.ones((N, N))     # create & initialize psi0 as (NxN) array with value -1
psi0 = initialCond(psi0, N) # set initial condition
psi = np.zeros((N, N))      # identical array for the update
psi_sav = np.zeros((steps,N,N)) # a (steps x (NxN)) array to store all time steps



# The time loop -----------------------------------------------
for n in range(steps):
    #tmp = -K*(psi0[2:] - 2*psi0[1:-1] + psi0[:-2])/dx**2 + H*df_dw(psi0[1:-1])
    tmp = -K*(psi0[2:,1:-1] + psi0[1:-1,2:] - 4*psi0[1:-1,1:-1] + psi0[:-2,1:-1] + psi0[1:-1,:-2]/dx2) \
         + H*df_dw(psi0[1:-1,1:-1])
    psi[1:-1, 1:-1] = psi0[1:-1, 1:-1] - Gamma*delta_t*tmp
    
    psi[0,:] = psi[1,:]     # Neumann condition at left,
    psi[N-1,:] = psi[N-2,:] # right
    psi[:,0] = psi[:,1]     # top
    psi[:,N-1] = psi[N-2]   # bottom boundary
    
    psi0 = np.copy(psi) # buffer actual time step
    
    psi_sav[n,:] = psi  # store result as another frame

    
# Plot the result --------------------------------------------
plt.imshow(psi, cmap = 'hot', vmin=0, vmax=1)
plt.colorbar()
plt.show()