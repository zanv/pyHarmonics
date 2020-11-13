#!/usr/bin/env python3

## Referencias:
## https://www.qsl.net/py4zbz/teoria/espectro.htm
## https://asecuritysite.com/comms/plot04?a1=1.0&a2=0&a3=0.4&a4=0&a5=0.2
## https://stackoverflow.com/questions/38953369/how-do-you-plot-the-total-summation-of-harmonics-in-python
## "harmonics.py": https://mindchasers.com/dev/python-harmonics
##
## Usage:
##   python3 harmonics.py -n 3
##   python3 harmonics.py -n 5 -f 3
##   python3 harmonics.py -n 1000 -f 3 -s triangle
##
## GIT Repository: https://github.com/zanv/pyHarmonics



import matplotlib.pyplot as plt
import numpy as np

## preparação dos dados:
freq   = int(input("Fundamental frequency (default = 1Hz): ") or "1")
cycles = int(input("Number of cycles (default = 4 cycles): ") or "4")
nharm  = int(input("Number of harmonics (default = 4): ") or "4")
ampl   = int(input("Signal amplitude (default = 1): ") or "1")
htype  = input("Type of harmonics (odd or even)(default = odd): ") or "odd"

print(f"Chosen values: f = {freq}Hz.    N = {cycles} cycle(s),    A = {ampl}")

cycles = cycles*2

## build a set of x values from zero to 4π in increments of 0.1 radians.
## The x-values are stored in a numpy array. Numpy's arange() function has three arguments: start, stop, step.
## Then we define a variable y as the sine of x using numpy's sin() function.
x  = np.arange(0, cycles*np.pi, 0.01)   # start, stop, step

## Amplitude da frequencia fundamental
y = ampl*np.sin(x)   ## y = amplitude do seno
z = ampl*np.cos(x)   ## z = amplitude do cosseno

for i in range(nharm+2):
    if (i > 0):  ## evita a divisão por i=0
        ya = ampl*np.sin(x*i)/i   ## ya = amplitude auxiliar
        if (htype == "odd"):
            if ((i > 1) and (i % 2 != 0)):  ## soma apenas as frequencias ímpares
                plt.plot(x,ya)
                y = y + ya
        elif (htype == "even"):
            if ((i > 1) and (i % 2 == 0)):  ## soma apenas as frequencias pares
                plt.plot(x,ya)
                y = y + ya
        else:
            if (i > 1):  ## soma apenas as frequencias pares
                plt.plot(x,ya)
                y = y + ya


plt.plot(x,y)

plt.title(f"Plot of sin(x) and cos(x), x = 0 to {cycles}π")   # título do gráfico
plt.xlabel(f"x values from 0 to {cycles}π")     # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.legend(['sin(x)', 'cos(x)'])        # legend entries as seperate strings in a list

plt.show()      ## show the finished plot
