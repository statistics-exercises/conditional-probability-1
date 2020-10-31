# Simulating conditional variables

Consider the following information about the Bernoulli random variables X and Y.

![](https://render.githubusercontent.com/render/math?math=P(X=1|Y=0)=\frac{1}{2}\qquad\P(X=0|Y=1)=\frac{1}{4}\qquad\P(Y=1)=\frac{1}{8})

Use this information, together with what you have learned about generating Bernoulli random variables in this course to write a function to generate variables from the distribution sampled by the variable X.  The function you write should be called `gen_x`.  In the code I have written in `main.py` I have used this function to generate a series of random variables from the distribution and have plotted a graph showing the values generated.
