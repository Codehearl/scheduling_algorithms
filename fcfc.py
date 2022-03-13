from models.model import process , visualize , get_input

def scheduler(processes,total_time):
    ready_queue = []
    plotter = []
    
    processes.sort(key = lambda x: x.arrival_time)
    old = processes[0].arrival_time
    ready_queue = [j for j in processes if j.burst_time != 0]
    for j in ready_queue:
        new = old + j.burst_time
        plotter.append([j.name,old,new])
        old = j.arrival_time+j.burst_time
    return plotter 
processes ,total_time= get_input()
plotter = scheduler(processes,total_time)
visualize(plotter)