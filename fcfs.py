from process import Process
from operator import attrgetter

def fcfs(queue,time):
    # ordeno los procesos de acuerdo a su tiempo de llegada, si es la misma prioridad mas alta
    order_process = sorted(queue, key=lambda x:(x.arrival_time, -x.priority))

    #itero los procesos y establecemos metricas
    for process in order_process:
        if time < process.arrival_time:
            time = process.arrival_time

        if process.response_time is None:
            process.response_time = time

        time = time + process.burst_time
        process.complete_time = time
        process.waiting_time = process.complete_time - process.arrival_time - process.burst_time
        process.turn_around_time = process.complete_time - process.arrival_time

    return order_process, time
