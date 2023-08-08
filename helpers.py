import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import ipytone
import ipywidgets as wg
import numpy as np
from scipy.signal import square, sawtooth
from scipy.io import wavfile
import time
from IPython.display import display
from matplotlib.widgets import Slider, Button

def sine_function(t,frequency,amp):
    return amp * np.sin(2 * np.pi * frequency * t) # this is the equation written in the cell above!

def interactive_sine(time_interval,
                    initial_amplitude,
                    initial_frequency,
                    t_max,
                    amp_max,
                    freq_max):
    # Create the figure and the line that we will manipulate
    fig, ax = plt.subplots(figsize=(8,6)) # creating the figure
    ax.set_ylim([-amp_max,amp_max]) # setting the minimum/maximum values for the y axis
    t = time_interval
    initial_sine = sine_function(t, initial_frequency, initial_amplitude) # evaluating the sine function at the points
    line, = ax.plot(t, initial_sine, lw=2) # plotting the sine function
    
    #######################################################################
    #### Everything below this line is just technical details         #####
    #### Feel free to read it if you want, but no need to understand! #####
    #######################################################################
    
    plt.grid() # overlaying a grid on the axes
    ax.set_xlabel('Time t [s]')
    ax.set_ylabel(r"A$\sin(2\pi ft)$")
    
    # adjust the main plot to make room for the sliders
    fig.subplots_adjust(left=0.25, bottom=0.25)
    
    # Make a horizontal slider to control the frequency.
    axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    freq_slider = Slider(
        ax=axfreq,
        label=r'Frequency $f$ [Hz]',
        valmin=1,
        valmax=freq_max,
        valinit=initial_frequency,
        valstep=1
    )
    
    # Make a vertically oriented slider to control the sample rate
    axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
    amp_slider = Slider(
        ax=axamp,
        label=r"Amplitude $A$",
        valmin=0.1,
        valmax=amp_max,
        valstep=0.1,
        valinit=initial_amplitude,
        orientation="vertical"
    )
    
    # The function to be called anytime a slider's value changes
    def update(val):
        line.set_ydata(sine_function(t,freq_slider.val,amp_slider.val))
        fig.canvas.draw_idle()
    
    
    # register the update function with each slider
    freq_slider.on_changed(update)
    amp_slider.on_changed(update)
    
    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')
    
    
    def reset(event):
        freq_slider.reset()
        amp_slider.reset()
    button.on_clicked(reset)
    
    plt.show()

