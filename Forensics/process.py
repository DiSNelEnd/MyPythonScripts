import psutil
import os
import signal

def get_running_proccesses() -> list:
    processes_iter = psutil.process_iter()
    processes = []

    for process in processes_iter:
        processes.append(
            {
                'name': process.name(),
                'pid': process.pid,
                'memory used': process.memory_info().vms / 1024**2,
            }
        )
    
    processes = sorted(processes, key=lambda d: d['memory used'], reverse=True)
    return processes

def kill_process_win() -> None:
     pid = int(input("Enter pid :) > "))
     os.kill(pid, signal.SIGBREAK)

     print(f"Process {pid} dead :)")

def create_prosess_file():
    processes = get_running_proccesses()
    for process in processes:
        with open('process.txt', 'at', encoding='utf-8') as f:
            f.write(f"{process['pid']} {process['name']} {process['memory used']}\n" )
    
    print("Created a file process.txt :)")

def killing_processes():
    cond = input("Do you want to kill process y/n? :) > ")

    if cond == 'y':
        kill_process_win()
        cond = input("Want more y/n? :) > ")

        if cond == 'y':
            kill_process_win()

    print("End :)")


cond = input("Create process file y/n? :) > ")

if cond == 'y':
    create_prosess_file()

killing_processes()

