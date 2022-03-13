import plotly.figure_factory as px
import pandas as pd
class process:
    def __init__(self,name=None,arrival=None,burst=None) -> None:
        self.name = name
        self.arrival_time = arrival
        self.burst_time = burst 
def get_input():
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
    return processes, total_time

def visualize(plotter):
    df = pd.DataFrame([
        dict(Task=x,Start=y,Finish=z) for [x,y,z] in plotter 
    ])

    fig = px.create_gantt(df)
    fig.update_xaxes(type='linear')
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    fig.show()
    print(df)