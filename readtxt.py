from process import Process

def readtxt(filename):
    process_group = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#')or not line:
                continue
            data = line.strip().split(';')
            name = data[0]
            burst_time = int(data[1])
            arrival_time = int(data[2])
            queue = int(data[3])
            priority = int(data[4])
            process_group.append(Process(name, burst_time, arrival_time, queue, priority))

    return process_group
