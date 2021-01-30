import numpy as np
import pandas as pd

# Population N grows at a rate n, following
# N' = (1+n)N


# Consumers receive Y as income, and save s.
# C = (1-s)Y, s < 1
# S = sY  (S = current savings)


# Output produced by 
# Y = zF(K, N)
# Output per worker equals
# Y/N = zf(k) Where k=capital per worker and Y/N = output per worker

# Depreciation rate 0<d<1
# K' = (1-d)K + I 

# We know that Y = C + I
# so Y = (1-s)Y + K' - (1-d)K
# K' = sY + (1-d)K

# This solves to K' = szF(K,N) + (1-d)K
# We eventually get k'(1+n) = szf(k) + (1-d)k
# We arrive at the key equation
# k' = szf(k)/(1+n) + (1-d)k/(1+n)


# Automatically plot the steady state line.
# In the long run, all aggregate quantities (C, I, K, Y) grow at rate N.

# Function: Increment year by 1 every second (maybe canchange speed), calculate all the values.
