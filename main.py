from readtxt import readtxt
from mlq import mlq
from writetxt import write_text

def main():
    filename = 'mlq004.txt'
    process_group = readtxt(filename)

    scheme = "Scheme1"
    finished_processes = mlq(process_group, scheme)
    write_text(finished_processes, filename)

if __name__ == '__main__':
    main()