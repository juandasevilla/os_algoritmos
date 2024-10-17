from process import Process
from operator import attrgetter

#algoritmo psjf recibe la cola y el tiempo general
def psjf(queue, time):

    finish_process = []

    #mientras halla algo en cola o algun proceso con tiempo restante se ejecuta el ciclo
    while queue or any(process.missing_time > 0 for process in queue):
        #ordena los procesos si ya llegaron
        order_process = [process for process in queue if process.arrival_time <= time]
        if order_process:
            ready_process = min(order_process, key=lambda p: (p.missing_time, -p.priority))
            if ready_process.response_time is None:
                ready_process.response_time = time
            ready_process.missing_time -= 1
            time += 1
            if ready_process.missing_time == 0:
                ready_process.complete_time = time
                ready_process.waiting_time = ready_process.complete_time - ready_process.arrival_time - ready_process.burst_time
                ready_process.turn_around_time = ready_process.complete_time - ready_process.arrival_time
                finish_process.append(ready_process)
                queue.remove(ready_process)
        else:
            time = time + 1

    return finish_process, time


