

#objeto process, tiene todos los atributos que requiere mi proceso y metricas que se va a obtener
class Process:
    def __init__(self, name, burst_time, arrival_time,  queue, priority):
        self.name = name
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.queue = queue
        self.priority = priority
        self.waiting_time = 0
        self.complete_time = 0
        self.response_time = None
        self.turn_around_time = 0
        self.missing_time = burst_time
