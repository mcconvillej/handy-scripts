import visa #initialise pyvisa
import numpy
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.pyplot as plt

rm = visa.ResourceManager()
print(rm.list_resources())
k237 = rm.list_resources()[2] # or k237 = whatever
print(k237.query('*IDN?'))
k237.write('F0,1X') #SVMI sweep
k237.write('P1X') #filter
k237.write('Q4,20,30,1,3,1000,60000X') #sweep command
k237.write('B10,1,X') #bias level command
k237.write('L.05,0X') #compliance
k237.write('T1,0,0,0X') #triggers

action = input('Operate? Type Y/N : ')
if action != 'Y':
    exit()
    
k237.write('N1X') #operate
k237.wait_for_srq()#wait for sweep to finish
source_data=k237.query_ascii_values('G1,2,2', container=numpy.array) #get data
measure_data=k237.query_ascii_values('G4,2,2', container=numpy.array)

host = host_subplot(111)#plot V,I over time- NB only actually want some points...

par = host.twinx()#need 2 y axes

host.set_xlabel("Time (a.u.)")
host.set_ylabel("Voltage")
par.set_ylabel("Current")

p1, = host.plot(source_data, label="Voltage")
p2, = par.plot(measure_data, label="Current")

leg = plt.legend()

host.yaxis.get_label().set_color(p1.get_color())
leg.texts[0].set_color(p1.get_color())

par.yaxis.get_label().set_color(p2.get_color())
leg.texts[1].set_color(p2.get_color())

plt.show()

leave_program = 'N'
while leave_program != 'Y':
    leave_program = input('Exit program? Type Y/N : ')
exit()
