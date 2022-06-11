#!/usr/bin/env python
# coding: utf-8

# # Water quality modeling - BOD in rivers (II)
# 
# 
# 
# ## Introduction
# We have shown in [BOD in rivers (I)](BOD1.md) that Streeter-Phelps equation explains how DO concentration varies in steady-state rivers controlled by deoxygenation, reaeration, and advection due to river flow. However, Streeter-Phelps equation does not consider other mixing processes (e.g., dispersion), so that the upstream water are not affected by the point source pollution. Apparently this is not true in reality. In this lab, we will explore this additional mixing process and how they affect DO and BOD in the stream.
# 
# 
# ## BOD-DO deficit equations
# 
# The advection-diffusion process of DO and BOD variation is controlled by a set of partial differential equations (PDE), which can be simplified to be a set of second-order ordinary differential equations (ODE):
# ```{math}
# :label: gov1
# E\frac{d^2 L}{dx^2} - u\frac{dL}{dx} - k_d L = 0
# ```
# 
# ```{math}
# :label: gov2
# E\frac{d^2 D}{dx^2} - u\frac{dD}{dx} - k_a D + K_d L = 0
# ```
# where $E$ is longitudinal dispersion coefficient.
# 
# Some other important parameters in this system include: river discharge $Q$, mass discharge in wastewater (pollutant source) $W$, BOD concentration at the source $L_0$. They are connected through this equation:
# 
# ```{math}
# :label: L0
# L_0 = \frac{W}{Qm_1}
# ```
# with $m_1 = \sqrt{1+\frac{4k_d E}{u^2}}$.
# 
# 
# ## Solving BOD equation
# 
# Let's work on an example of wastewater BOD discharge into a coastal plain estuary (Example 6.7 in Book "Environmental Modeling: fate and transport of pollutants in water, air, and soil" authored by Dr. Jerald L. Schnoor).
# 
# Here is the list of parameters:
# * $E$ = 15 mi$^2$/day (dispersion coefficient)
# * $k_d$ = 0.15 /day (deoxygenation rate)
# * $k_a$ = 0.18 /day (reaeration rate)
# * $u$ = 3.57 mi/day (mean tidal velocity)
# * $W/Q$ = 18.5 mg/L (wastewater mass discharge / flow discharge)
# 
# To find out the relationship between BOD concentration and location ($L$ vs. $x$) at both upstream and downstream of the source ($-10$ mi $< x < 50$ mi), we will need to solve Eq. {eq}`gov1` with the following boundary condition:
# 
# ```{math}
# L = \begin{cases}
# 	0 & \textrm{for } x=-\infty \\
#   L_0 & \textrm{for } x=0 \\
#   0 & \textrm{for } x=\infty
#   \end{cases}
# ```
# 
# We will use `scipy.integrate.solve_bvp` to solve this boundary value problem (BVP). Here we have some incomplete instructions to get it started. However, you still need to google it to find out how to use `solve_bvp`.
# 
# Since we have a second-order ODE Eq. {eq}`gov1` for $L$, we can rewrite the second-order ODE to two first-order ODEs:
# 
# 
# ```{math}
# \frac{dL}{dx} = L_1
# ```
# 
# ```{math}
# \frac{dL_1}{dx}  = \frac{uL_1 + k_d L}{E}
# ```
# 
# 
# Here is how you can define these two equations in Python (this function return `dydt` with first dimension is $dL/dx$, and the second dimension is $dL_1/dx$):

# In[1]:


def L_eq(x, y):
    L, L1 = y
    dydt = [L1, (u*L1 + kd*L)/E]
    return dydt


# We need to solve this problem twice (upstream and downstream) since we have two boundary conditions for $x>0$ and $x<0$:

# In[2]:


def bc1(ya, yb):
    return np.array([ya[0], yb[0]-L0])

def bc2(ya, yb):
    return np.array([ya[0]-L0, yb[0]])


# The first boundary condition `bc1` is for $x<0$ and `bc2` is for $x>0$. You may see $L_0$ in the second term of `bc1` and in the first term of `bc2`. They are the source locations which represent the right hand side boundary for $x<0$ and the left hand side boundary for $x>0$.
# 
# ```{admonition} Box question 1
# Write your own program to solve this problem with the help of the above given codes.
# ```{hint} Since we can not define infinity in the program, let's select $-100$ miles and 500 miles as upstream and downstream infinity locations where the pollution from wastewater can not be detected (You can later change the left and right boundary and re-run your program to verify whether these values make sense).
# 
# Plot the BOD concentration as a function of $x$ with x-axis limit of $-10 \sim 50$ miles. Compare your plots with analytical solution ($+$ and $-$ are for $x<0$ and $>0$, respectively):
# ```{math}
# L = L_0 \exp\left(\frac{u x}{2E} (1\pm m_1) \right)
# ```
# 
# 
# 
# 
# ## Concurrently solving BOD and DO deficit equations
# 
# To solve both BOD and DO deficit equations concurrently, we need to solve a set of four first order equations:
# ```{math}
# \frac{dL}{dx} = L_1
# ```
# 
# ```{math}
# \frac{dL_1}{dx}  = \frac{uL_1 + k_d L}{E}
# ```
# 
# ```{math}
# \frac{dD}{dx} = D_1
# ```
# 
# ```{math}
# \frac{dD_1}{dx}  = \frac{uD_1 + k_a D - K_d L}{E}
# ```
# 
# 
# ## Take-home work
# 
# In this lab, we will solve above equations using `solve_bvp`, similar to what we did for BOD equation only. We will use the same parameters:
# 
# * $E$ = 15 mi$^2$/day (dispersion coefficient)
# * $k_d$ = 0.15 /day (deoxygenation rate)
# * $k_a$ = 0.18 /day (reaeration rate)
# * $u$ = 3.57 mi/day (mean tidal velocity)
# * $W/Q$ = 18.5 mg/L (wastewater mass discharge / flow discharge)
# 
# To help you start, there are several key steps you need to work out:
# 
# **step 1:**
# 
# Refer to `L_eq(x,y)`, define a new function for BOD and DO deficit equations.
# 
# **step 2:**
# 
# Use two sets of boundary conditions in your program:

# In[3]:


def bc3(ya, yb):
    return np.array([ya[0], yb[0]-L0, ya[2], yb[2]-D0])

def bc4(ya, yb):
    return np.array([ya[0]-L0, yb[0], ya[2]-D0, yb[2]])


# You will need to define $D_0$:
# 
# ```{math}
# D_0  = \frac{k_d W}{(k_a-k_d)Q}\left(\frac{1}{m_1}-\frac{1}{m_2}\right)
# ```
# 
# where $m_2 = \sqrt{1+\frac{4k_a E}{u^2}}$
# 
# **step 3:**
# 
# After you solve the problem, plot BOD vs. $x$ and DO deficit vs. $x$ on the same figure. Also plot the analytical solutions for comparison:
# ```{math}
# L = L_0 \exp\left(\frac{u x}{2E} (1\pm m_1) \right)
# ```
# 
# ```{math}
# D  = \frac{k_d W}{(k_a-k_d)Q}\left(\frac{1}{m_1} \exp \left[ \frac{u x}{2 E} (1\pm m_1) \right] - \frac{1}{m_2}\exp \left[\frac{u x}{2 E} (1\pm m_2)\right]\right)
# ```
# where $+$ and $-$ are for $x<0$ and $>0$, respectively.
# 
# **step 4:**
# 
# Label your $x$ and $y$ axes with variable names and their correct units, and add legend on the figure (i.e., BOD analytical, BOD model, DO deficit analytical, DO model).
