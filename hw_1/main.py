#!/usr/bin/python3
import os
import random as rnd
import time


def child(arg: int):
    pid = os.getpid()
    print('Запущена программа Child в процессе с PID ', pid, ' с аргументом ', arg, 'c PPID = ', os.getppid())
    time.sleep(arg)
    print('Завершена программа Child в процессе с PID ', pid, ' с аргументом ', arg)
    exit(rnd.randint(0,1))


def parent(n: int):
    processes = []
    for i in range(n):
        child_pid = os.fork()
        if child_pid == 0:
            arg = rnd.randint(5, 10)
            os.execl("/child.py", str(arg))
        else:
            processes.append(child_pid)

    while processes:
        child_pid, exit_code = os.wait()
        if child_pid == 0:
            time.sleep(1)
        else:
            if child_pid in processes:
                processes.remove(child_pid)


def main():
    n = int(input())
    parent(n)


main()

