import subprocess as sp
import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sp.call( 'cls', shell=True )    # clear screen

# ----------------------------------------------------------------------
# 
# Main script
#
# ----------------------------------------------------------------------
# create a population of 10,000 numbers
mu = [ 170,175 ]
sigma = [ 10,15 ]
population = [ np.random.randn(10000) * sigma[0] + mu[0]
             , np.random.randn(10000) * sigma[1] + mu[1] ]
mu = [ round( np.mean(population[0]) )
     , round( np.mean(population[1]) ) ]
sigma = [ round( np.std(population[0]), 4 )
        , round( np.std(population[1]), 4 ) ]
print( 'Population 0 mean = ' + str( round( mu[0], 2 ) ) )
print( 'Population 0 standard deviation = ' + str( round( sigma[0], 2 ) ) )
print( 'Population 1 mean = ' + str( round( mu[1], 2 ) ) )
print( 'Population 1 standard deviation = ' + str( round( sigma[1], 2 ) ) )
print( '' )

# draw a sample from the population with sample size of n
n = [ 23,67 ]
sample = list()
sample.append( np.random.choice( population[0], size = n[0] ) )
sample.append( np.random.choice( population[1], size = n[1] ) )
xbar = [ round( np.mean( sample[0] ), 2 )
       , round( np.mean( sample[1] ), 2 ) ]
sx = [ round( np.std( sample[0] ), 2 )
     , round( np.std( sample[1] ), 2 ) ]
sexbar = [ round( sigma[0] / ( np.sqrt(n[0]) ), 2 )
         , round( sigma[1] / ( np.sqrt(n[1]) ), 2 ) ]
sexbar = [ round( stats.sem( sample[0], ddof = 0 ), 4 )
         , round( stats.sem( sample[1], ddof = 0 ), 4 ) ] # use scipy function to
                                                # calculate sexbar
print( 'Sample 0 mean = ' + str( round( xbar[0], 2 ) ) )
print( 'Sample 0 standard deviation = ' + str( round( sx[0], 2 ) ) )
print( 'Standard error of sample 1 mean = ' + str( sexbar[0] ) )
print( 'Sample 1 mean = ' + str( round( xbar[1], 2 ) ) )
print( 'Sample 1 standard deviation = ' + str( round( sx[1], 2 ) ) )
print( 'Standard error of sample 2 mean = ' + str( sexbar[1] ) )
print( '' )

# ----------------------------------------------------------------------
# 
# Hypothesis test for inequality
#
# ----------------------------------------------------------------------
print( 'Assertion: Population 1 mean is not equal to ' + str( mu[0] ) )
print( 'H0: mu[0] = ' + str( mu[0] ) )
print( 'HA: mu[0] != ' + str( mu[0] ) )
print( 'xbar[1] = ' + str( xbar[1] ) + ' vs ' + 'mu[0] = ' + str( mu[0] ) +
       ', but this difference could be due to sampling variation' )

# calculate a 95% confidence interval
df = n[1] - 1
t = round( stats.t.ppf( 0.975, df ), 4 )
cilo = round( xbar[1] - ( t * sexbar[1] ), 4 )
cihi = round( xbar[1] + ( t * sexbar[1] ), 4 )
print( 'two-tailed 95% confidence interval = ' + str( xbar[1] ) + ' +/- ' +
       str( t ) + ' * ' + str( sexbar[1] ) )
print( 'two-tailed 95% confidence interval = (' + str( cilo ) +
       ', ' + str( cihi ) + ')' )

# calculate a p-value
t = ( xbar[1] - mu[0] ) / sexbar[1]
pvalue = round( ( 1 - stats.t.cdf( t, df ) ) * 2, 4 )
print( 'pvalue = ' + str( pvalue ) )