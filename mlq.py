from process import Process
from operator import attrgetter
from collections import deque
from psjf import psjf
from rr import rr
from sjf import sjf
from fcfs import fcfs
from readtxt import readtxt

#algoritmo mlq, recibe el process group y el esquema que va a seguir
def mlq(process_group, scheme):
    queue1 = deque()
    queue2 = deque()
    queue3 = deque()

    #itera los procesos para clasificarlos de acuerdo a su cola
    for process in process_group:
        if process.queue == 1:
            queue1.append(process)
        elif process.queue == 2:
            queue2.append(process)
        else:
            queue3.append(process)

    finish_process = []
    time = 0

    #de acuerdo al esquema utiliza esos algoritmos
    if scheme == "Scheme1":
        finished_queue1, time = rr(queue1,time,quantum=1)
        finish_process.extend(finished_queue1)
        finished_queue2, time = rr(queue2,time,quantum = 3)
        finish_process.extend(finished_queue2)
        finished_queue3, time = sjf(queue3,time)
        finish_process.extend(finished_queue3)
    elif scheme == "Scheme2":
        finish_queue1, time = rr(queue1,time,quantum=3)
        finish_process.extend(finish_queue1)
        finish_queue2, time = rr(queue2,time,quantum=5)
        finish_process.extend(finish_queue2)
        finish_queue3, time = fcfs(queue3,time)
        finish_process.extend(finish_queue3)
    elif scheme == "Scheme3":
        finish_queue1, time = rr(queue1,time,quantum=2)
        finish_process.extend(finish_queue1)
        finish_queue2, time = rr(queue2,time,quantum=3)
        finish_process.extend(finish_queue2)
        finish_queue3, time = psjf(queue3,time)
        finish_process.extend(finish_queue3)

    return finish_process
