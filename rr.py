from process import Process
from operator import attrgetter
from collections import deque


def rr(queue, time, quantum):
    finish_process = []

    # filtra procesos que están en la cola
    queue = deque(sorted(queue, key=attrgetter('arrival_time')))

    while queue:
        # Filtrar los procesos que han llegado hasta el tiempo actual
        arriving_processes = [proc for proc in queue if proc.arrival_time <= time]

        if not arriving_processes:
            # Si no hay procesos que han llegado, incrementa el tiempo
            time += 1
            continue

        # Toma el primer proceso de los que han llegado
        current_process = arriving_processes[0]
        queue.remove(current_process)

        if current_process.response_time is None:
            current_process.response_time = time
        # Calcular el tiempo a gastar
        time_spend = min(current_process.missing_time, quantum)
        current_process.missing_time -= time_spend
        time += time_spend

        # Verifica si el proceso ha terminado
        if current_process.missing_time == 0:
            current_process.complete_time = time
            current_process.waiting_time = current_process.complete_time - current_process.arrival_time - current_process.burst_time
            current_process.turn_around_time = current_process.complete_time - current_process.arrival_time
            finish_process.append(current_process)
        else:
            # Reagregar el proceso a la cola al final
            queue.append(current_process)

    return finish_process, time




