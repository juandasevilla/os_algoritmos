from process import Process
from operator import attrgetter

#sjf recibe la cola y el tiempo general
def sjf(queue, time):

    finish_process = []

    while queue:
        order_process = [process for process in queue if process.arrival_time <= time]

        if order_process:
            ready_process = min(order_process, key=lambda x: (x.burst_time, -x.priority))

            if ready_process.response_time is None:
                ready_process.response_time = time
            time += ready_process.burst_time
            ready_process.complete_time = time
            ready_process.waiting_time = ready_process.complete_time - ready_process.arrival_time - ready_process.burst_time
            ready_process.turn_around_time = ready_process.complete_time - ready_process.arrival_time
            finish_process.append(ready_process)
            queue.remove(ready_process)
        else:
            time = time + 1

    return finish_process, time


