# Foucault Pendulum: a simple proof that earth rotates
The Foucault's pendulum is a normal pendulum which is big enough for earth's rotation to have effects on it's trajectories. We can use it to prove that the earth is not at rest and is rotating.

The original one was a  28kg bob from 67m string. The pendulum basically swings back and forth and changes the plane of oscillation while it swings. The first time it's motion was observed, pendulum seemed to change its plane of oscillation where in reality the earth’s rotation was the real cause of this observed trajectory

## Equation 
The equation of trajectory of the Foucalt Pendulum gives us the exact position of the bob at some particular time. It can be derivied by using Lagrange's Equation of motion.

And is given by

<img src="https://render.githubusercontent.com/render/math?math=\ddot{x} - 2\dot{y}\Omega\sin(\lambda) %2B\frac{gx}{l} = 0">

and 

<img src="https://render.githubusercontent.com/render/math?math=\ddot{y} %2B2\dot{x}\Omega\sin(\lambda) %2B\frac{gy}{l} = 0">.

**Note-** 
the motion along z-axis has been neglected as the string is very long and the value of z(the displacement along z-axis) is small as compared to the diplacement along other two directions.

## App 
We developed a small app using python which is labelled "cos_fin2.py", simply launch it and you will be able to use the simple interface to observe what trajectory is followed by focults pendulum on different planets at different latitudes. 

Various plots have been analysed in the attached jupyter notebook 

A detailed presentation can be seen here - (here)[https://docs.google.com/presentation/d/1zGPZZ6i7xeJ5kZhfs0uXpLLQkGKN2nGrfFmFf72jizM/edit?usp=sharing]
