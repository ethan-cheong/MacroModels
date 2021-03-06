import math

class SolowGrowthModel:
    def __init__(self, N, K, n, s, d, z, alpha):
        '''
        Initialize variables
        '''
        self.N = N                                      # initial population
        self.K = K                                      # initial capital
        self.Y = z * ((K ** alpha ) * (N ** (1-alpha))) # Cobb-Douglas production function
        self.C = (1-s) * self.Y                         # initial consumption
        self.S = self.Y - self.C                        # initial savings
        self.I = self.S                                 # initial investment

        self.k = self.K / self.N                        # capital per worker
        self.n = n                                      # population growth rate
        self.s = s                                      # savings rate
        self.d = d                                      # depreciation rate
        self.z = z                                      # productivity
        self.alpha = alpha                              # share of labour
        self.year = 0

    def increment(self):
        '''
        Increase year by 1 and update aggregate variables
        '''
        self.year += 1                                              # increment year
        self.Y = self.z*self.K**self.alpha*(self.N**(1-self.alpha)) # increment income
        self.K = self.s*self.Y + (1-self.d)*self.K                  # increment capital
        self.N = self.N*(1+self.n)                                  # increment population
        self.k = self.K/self.N                                      # increment capital per population
        self.S = self.s*self.Y                                      # increment savings
        self.I = self.S                                             # increment investment
        self.C = self.Y-self.S                                      # increment consumption

    def steady_state(self):
        '''
        get steady state k*
        '''
        # Adopted this solution from quantecon, my solution was very inefficient because of a log operation
        return ((self.s * self.z) / (self.n + self.d))**(1 / (1 - self.alpha))

class OnePeriodMacroModel:
    def __init__(self, G, z, K, alpha):
        '''
        Initialize all variables
        '''
        self.G = G
        self.z = z
        self.K = K
        self.alpha = alpha

    def ppf(self, time_div):
        '''
        Return outputs to plot the PPF.
        time_div is the number of time divisions to use - a higher number
        results in higher resolution when plotting.
        '''
        l_list, C_list=[],[]

        i = 0
        while self.z * self.K ** self.alpha * (time_div - i) ** (1-self.alpha) - self.G > 0: # Calculate all positive C for each hour of labour worked, using PPF function
            C = self.z * self.K ** self.alpha * (time_div - i) ** (1-self.alpha) - self.G
            l_list.append(i)
            C_list.append(C)
            i += 1

        # This calculates value of l where C is 0 so that the ppf joins nicely with the x axis
        l_list.append(time_div - (self.G/(self.z*self.K**self.alpha))**(1/(1-self.alpha)))
        C_list.append(0)

        return {'l': l_list, 'C': C_list}

    def indifference_curve(self, utility_function='normal'):
        '''
        Return outputs to plot indifference curve at the optimal point.
        Takes 3 different utility functions: normal, perfect complements, perfect substitutes.
        The normal utility function can be parameterized
        '''
