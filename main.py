import matplotlib.pyplot as plt
import numpy as np 

def gen_x() :
  # Your code to generate the random variables goes here
  
  
# You should not need to add any code from here onwards.  This will simply create a series of 
# samples from X and draw a graph of them
xvals, yvals = np.zeros(100), np.zeros(100)
for i in range(100) : 
  xvals[i] = i+1
  yvals[i] = gen_x() 
  
plt.plot( xvals, yvals, 'ko' )
plt.savefig("xvalues.png")
