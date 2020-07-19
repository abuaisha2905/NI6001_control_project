from PyDAQmx import Task
import PyDAQmx
import nidaqmx
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import threading
import time
from datetime import datetime
import nidaqmx.system
import multiprocessing

system = nidaqmx.system.System.local()
print(system.driver_version)
for device in system.devices:
    print(device)

df = pd.DataFrame(data=None)

class NI:


    def __init__(self, channel):
        self.ch = 'Dev1/' + channel
        self.read_data = np.array([])
        self.df = pd.DataFrame(data=None)


    def write(self, input_array=np.arange(1, 5, 0.0002)):
        print('witting stared', self.ch)

        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(self.ch)
            task.write(input_array, auto_start=True)
        print('witting ended', self.ch)

    def read(self):
        print('read 0 started ')

        for i in range(200):
            with nidaqmx.Task() as task:
                task.ai_channels.add_ai_voltage_chan(self.ch)
                task.read()
                self.read_data = np.append(self.read_data, task.read())
                #print('read 0 loop started ', i, task.read())
        print(self.read_data)

    def data_frame(self):
        self.df = pd.DataFrame(data=self.read_data, columns=[self.ch])
        print('data frame has been created for', self.ch)
        # df.boxplot()
        # plt.show()

    def append_data_frame(self):
        df[self.ch] = self.read_data

    def save_csv(self):

        date = str(datetime.now().strftime("%d-%m %H %M %S")) + '.csv'
        time.sleep(1)
        df.to_csv(date)
        print('saving finished for', self.ch)


    def graph(self):
        x = np.arange(0, len(self.read_data))
        y = self.read_data
        fig, axes = plt.subplots()
        axes.plot(x,y,'r-',label='input data',mew=3,lw=3, mec='b')
        axes.set_xlabel('X-Axis')
        axes.set_ylabel('Y-Axis')
        axes.set_title(self.ch)
        axes.grid(True)
        axes.legend()
        axes.legend(loc=0)
        plt.tight_layout()
        plt.show()





read1 = NI('ai1')
read2 = NI('ai0')
read1.append_data_frame()
read2.append_data_frame()
read1.save_csv()
read2.save_csv()



#read.graph()
