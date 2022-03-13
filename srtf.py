from models.model import process , visualize , get_input
# Creating a process object
total_time = 0

def scheduler(processes,total_time):
    ready_queue = []
    old  = 0
    plotter = []

    for i in range(1,total_time+1):
        #sorting the queue so that the shortest remaining time left gets on top and  removes any finished processes
        ready_queue = [ j for j in processes if j.arrival_time <= i]
        ready_queue1 = [j for j in ready_queue if j.burst_time != 0]
        ready_queue1.sort(key=lambda x:
        x.burst_time)
        if ready_queue1:
            ready_queue1[0].burst_time -= 1
            if old != ready_queue1[0] and old != 0:


                plotter.append([old.name,old.arrival_time,i,])
                ready_queue1[0].arrival_time = i
        
            if i==total_time:
                
                plotter.append([ready_queue1[0].name,ready_queue1[0].arrival_time,i])

            old = ready_queue1[0]

    return plotter


processes ,total_time= get_input()
plotter = scheduler(processes,total_time)
visualize(plotter)

        
  

     



        