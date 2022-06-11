# Particle Settling in Water (I)



## Problem description

Settling of sediment particles are an important physical process to the sediment suspension, mixing, and transport. Modeling of the settling velocity of a sediment particle is essential to the models of river mechanics and sediment related hydraulic design.

The velocity ($W$) of a single particle settling in water can be predicted by the equilibrium between its gravity, buoyancy, and drag forces, where gravitational force is $F_G = \rho_p g V$ (downward), buoyancy force $F_B = \rho gV$ (upward), and drag force $F_D$ (upward). When the particle is very small, the drag force is related to the viscosity of the water $\mu$, particle size, and the settling velocity, $F_D = 3\pi\mu D W$. In fluid mechanics, we call this the Stokes regime, and the drag is call Stokes drag. Once we know the particle size, the settling velocity can be easily calculated by applying free body diagram to the sediment particle.

```{admonition} Box question 1
Derive the equation for the settling velocity, and write a small program to calculate the settling velocity of sand particles with diameter ranging from 1 $\mu$m to 100 $\mu$m (taking $\rho_p = 1600$ kg/m$^3$, $\rho = 1000$ kg/m$^3$, $g = 9.81$ m/s$^2$, $\mu = \nu \rho = 1.0\times10^{-3}$ Pa s). Plot the settling velocity vs. sand diameter with appropriate label and units.
```

```{admonition} Box question 2
Box question 2: Here we restrict the sand particle to be tiny because we want to ensure the particle within the Stokes regime, i.e., $Re < 1$. In your code, add a few lines to calculate Reynolds number and check if Re in the above question is within the Stokes regime.
```
```{tip}
plotting a figure might be a good idea in solving Box question 2.
```

For large particles than what you just plotted, the Stokes law is not going to work, because the drag force is not controlled by viscosity of the water. The drag force is then replaced by this equation:

```{math}
:label: drag
F_D =  \frac{1}{2} \rho W^2 C_D A
```

In hydraulic engineering, simple empirical equations are used to predict settling velocity by modeling drag coefficient $C_D$ in  Eq. {eq}`drag`.  For example:

```{math}
:label: settling1
W = \frac{\nu}{d}\left[\sqrt{0.25\left(\frac{A}{B}\right)^{2/m}+\left(\frac{4}{3}\frac{d_*^3}{B}\right)^{1/m}} - \frac{1}{2}\left(\frac{A}{B}\right)^{1/m}\right]^m
```
where $d_*$ is dimensionless diameter, defined by:

```{math}
:label: dia
d_* = \left[ \frac{(G-1)g}{\nu^2} \right]^{1/3} d
```
with $G$ is the specific gravity (also known as relative density of the particle) $G=\rho_p/\rho$.


In Eq. {eq}`settling1`, model coefficients are: $A=32$, $B=1$, $m=1.5$.


## Take-home work

1. Write a program to calculate settling velocity of same sand particles from 200 $\mu$m and 1 mm using Eq. {eq}`settling1`. Plot the result on top of the figure you created in Box question 1.
2. Check Reynolds number and plot your result on top of the figure you created in Box question 2.
3. Try a different set of model coefficients and repeat the above procedure. $A = 26.4$, $B = 1.27$, $m = 1.0$.
4. Write a sub-function in your code to take arguments of particle diameter $d$ and model coefficients $A$, $B$, and $m$, so that you do not need to write Eq. {eq}`settling1` in your code.
5. Write a complete program with sub-function to calculate settling velocity of a different type of particle: Quartz ($\rho_p = 2650$ kg/m$^3$) for diameter 100 $\mu$m and 1 mm. Plot your results and compared the equation given in Book ``River Mechanics'' by Dr. Pierre Y. Jullien:

```{math}
:label: dia2
W = \frac{8 \nu}{d} \left[ \left(1+\frac{d_*^3}{72} \right)^{0.5} -1 \right]
```
