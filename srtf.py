import plotly.figure_factory as px
import pandas as pd
class process:
    def __init__(self,name=None,arrival=None,burst=None) -> None:
        self.name = name
        self.arrival_time = arrival
        self.burst_time = burst 
    def relay(self,time):
        print(f'{self.name} remaining time {self.burst_time} current time: {time} '.format())

number = int(input(' please enter the number of processes'))
processes = []
total_time = 0
for i in range(number):
    name = f'process{i}'.format()
    arrival = int(input(f'please enter Arrival time for {name}: '.format()))
    burst = int(input(f'please enter Burst time for {name}: '.format()))
    process1 = process(name=name,arrival= arrival,burst= burst)
    processes.append(process1)
    total_time += burst 
ready_queue = []
old  = 0
plotter = []
for i in range(1,total_time+1):
    ready_queue = [ j for j in processes if j.arrival_time <= i]
    ready_queue1 = [j for j in ready_queue if j.burst_time != 0]
    ready_queue1.sort(key=lambda x: x.burst_time)
    if ready_queue1:
        ready_queue1[0].burst_time -= 1
        if old != ready_queue1[0] and old != 0:


            plotter.append([old.name,old.arrival_time,i,])
            ready_queue1[0].arrival_time = i
        if i==total_time:
            
            plotter.append([ready_queue1[0].name,ready_queue1[0].arrival_time,i])

        old = ready_queue1[0]
    else:
        print(f'No process     current time {i}'.format())

df = pd.DataFrame([
    dict(Task=x,Start=y,Finish=z) for [x,y,z] in plotter
])

fig = px.create_gantt(df)
fig.update_xaxes(type='linear')
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()
print(df)

        
  

     



        