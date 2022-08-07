from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from matplotlib.animation import FuncAnimation
from tkinter import ttk

window = Tk()
  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")

#Initialize a Label to display the User Input
label=Label(window, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(window, width= 40)
entry.focus_set()
entry.pack(pady=30)


lamda = 0.0
g = DoubleVar()
R = DoubleVar()
planet = IntVar()

fig1, ax= plt.subplots()

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
  

line,=ax.plot([],[],lw=2)
plt.grid()
    
xdata, ydata = [], [] 
t = 0.0
def plott_anm(t):
        global lamda
        global planet
        global g
        global R
        if planet == 1:
            R = 0
            g = 3.7
        elif planet == 2:
            R = 0.0
            g = 8.87
        elif planet == 3:
            R = 0.012
            g = 9.8                
        elif planet == 4:
            R = 0.011
            g = 3.71
        elif planet == 5:
            R = 0.028
            g = 24.92
        elif planet == 6:
            R = 0.026
            g = 10.44
        elif planet == 7:
            R = 0.016
            g = 8.87
        elif planet == 8:
            R = 0.017
            g = 11.15
        else:
            print("Restart and enter the correct Option")

        
        L = 67
        print("r is", R,"g is" ,g)

        #lamda = 1.8
        print('lamda', lamda)
        print('planet', planet)
        #g=9.8 
        
        # we will take the value of C1 and C2 to be equal to 1
        k_1=1
        k_2=1  

        x = k_1*np.cos(np.sqrt(g/L)*t - R*np.sin(lamda)*t) + k_2*np.cos(np.sqrt(g/L)*t + R*np.sin(lamda)*t)
        y = k_1*np.sin(np.sqrt(g/L)*t - R*np.sin(lamda)*t) - k_2*np.sin(np.sqrt(g/L)*t + R*np.sin(lamda)*t)
        xdata.append(x)
        ydata.append(y)
        
        line.set_data(xdata, ydata)


        return line

def anim():
    

    animation = FuncAnimation(fig1, plott_anm, frames = 1000,interval=200)
    

    

    
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig1,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()


    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
    
def printValue2():
    global planet

    planet = float(entry.get())



def printValue():
    global lamda
    
    lamda = float(entry.get())
    

def plot_static():
    global lamda
    global planet

    if planet == 1:
        R = 0
        g = 3.7
    elif planet == 2:
        R = 0.0
        g = 8.87
    elif planet == 3:
        R = 0.012
        g = 9.8                
    elif planet == 4:
        R = 0.011
        g = 3.71
    elif planet == 5:
        R = 0.028
        g = 24.92
    elif planet == 6:
        R = 0.026
        g = 10.44
    elif planet == 7:
        R = 0.016
        g = 8.87
    elif planet == 8:
        R = 0.017
        g = 11.15
    else:
        print("Restart and enter the correct Option")

    fig2, ax2 = plt.subplots()

    L = 100

    k_1=1
    k_2=1  
    t = np.arange(0,100,0.1)



    x = k_1*np.cos(np.sqrt(g/L)*t - R*np.sin([lamda])*t) + k_2*np.cos(np.sqrt(g/L)*t + R*np.sin(lamda)*t)
    y = k_1*np.sin(np.sqrt(g/L)*t - R*np.sin(lamda)*t) - k_2*np.sin(np.sqrt(g/L)*t + R*np.sin(lamda)*t)

    ax2.plot(x,y)


    
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig2,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    #toolbar = NavigationToolbar2Tk(canvas,
           #                        window)
    #toolbar.update()
    

    # placing the toolbar on the Tkinter window
    #canvas.get_tk_widget().pack()
input_lamda = Label(text="Enter Lamda",font=("Courier", 16)).place(x = 40,y = 70)

Button(
    window,
    text="enter", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack(side = TOP)

user_planet = Label(text = "Choose Valid Number option for planet:- \n 1. Mercury \n 2.Venus \n 3. Earth \n 4.Mars \n 5.Jupiter \n 6.Saturn \n 7.Uranus \n 8.Neptune ", height = 10, font=("Courier", 16)).place(x = 40,
                                               y = 100)

#user_planet_entry_area = Entry(width = 30,textvariable= planet).place(x = 300,                                                y = 150)
#planet_area= Entry(width = 30).place(x = 300,y = 150) 


Button(
    window,
    text="Choosen", 
    padx=10, 
    pady=5,
    command=printValue2
    ).pack(side = TOP)

# button that displays the plot
plot_button = Button(master = window, 
                     #command = partial(plot_static , lamda),
                     command = plot_static,
                     height = 2, 
                     width = 10,
                     text = "Plot")
anim_button = Button(master = window, 
                     #command = partial(plot_static , lamda),
                     command = anim,
                     height = 2, 
                     width = 10,
                     text = "animate")
Button(master = window, text='Quit', command=window.destroy).pack(side = BOTTOM)
  
# place the button 
# in main window
anim_button.pack(side=LEFT)
plot_button.pack(side=RIGHT)


window.mainloop()       

