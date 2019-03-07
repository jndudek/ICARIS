from tkinter import *
import sys
#import numpy as np

test = [["Circuit 1", 'R', 1, 'V', 1], ["Circuit 2", 'V', 2, 'R', 1], ["Circuit 3", 'R', 2, 'V', 3],
        ["Circuit 4", 'V', 4, 'R', 2], ["Circuit 5", 'R', 3, 'V', 5], ["Circuit 6", 'V', 1, 'R', 3],
        ["Circuit 7", 'R', 4, 'V', 2], ["Circuit 8", 'V', 3, 'R', 4], ["Circuit 9", 'R', 5, 'V', 4],
        ["Circuit 10", 'V', 5, 'R', 5]]
def export(input_components):
    sum = 0
    i = 1
    j = 1
    netlist = open("%s.cir" % (input_components[0]), "a+")
    netlist.write("** ICARIS generated Circuit **\r\n")
    while (i < len(input_components)-2):
        if (input_components[i] == 'R'):
            netlist.write("r%d %d %d %d\r\n" % (j, j, j-1, input_components[i + 1]))
        if (input_components[i] == 'V'):
            netlist.write("v%d %d %d dc %d\r\n" % (j, j, j-1, input_components[i + 1]))
        i += 2
        j += 1
    if (input_components[i] == 'R'):
        netlist.write("r%d %d 0 %d\r\n" % (j, j-1,  input_components[i + 1]))
    if (input_components[i] == 'V'):
        netlist.write("v%d %d 0 dc %d\r\n" % (j, j-1, input_components[i + 1]))
    netlist.write(".END")
    netlist.close()

k = 0
while (k < len(test)):
    #print(test[k])
    export(test[k])
    k += 1