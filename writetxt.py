

def write_text(finish_process, original_filename):

    output_filename = original_filename.split('.')[0] + '_output.txt'

    with open(output_filename, 'w') as f:
        f.write("# archivo: " + output_filename + "\n")
        f.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n")

        for process in finish_process:
            f.write(f"{process.name}; {process.burst_time}; {process.arrival_time}; {process.queue}; {process.priority}; "
                     f"{process.waiting_time}; {process.complete_time}; {process.response_time}; {process.turn_around_time}\n")

        # Calcular y escribir los promedios
        avg_wt = sum(p.waiting_time for p in finish_process) / len(finish_process)
        avg_ct = sum(p.complete_time for p in finish_process) / len(finish_process)
        avg_rt = sum(p.response_time for p in finish_process) / len(finish_process)
        avg_tat = sum(p.turn_around_time for p in finish_process) / len(finish_process)

        f.write(f"WT={avg_wt}; CT={avg_ct}; RT={avg_rt}; TAT={avg_tat};\n")
