import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
        mean = 0 
        for i in range(100) : mean = mean + gen_x() 
        mean = mean/100 

       prob = 1/2*7/8 + 3/4*1/8
       var = prob*(1-prob)
       bar = np.sqrt( var / 100 )*scipy.stats.norm.ppf( (0.99+1)/2 )
       self.assertTrue( np.abs( mean - prob)<bar, "your function appears to be sampling from the wrong distribution"  )
