def child(arg: int):
    pid = os.getpid()
    print('Запущена программа Child в процессе с PID ', pid, ' с аргументом ', arg, 'c PPID = ', os.getppid())
    time.sleep(arg)
    print('Завершена программа Child в процессе с PID ', pid, ' с аргументом ', arg)
    exit(rnd.randint(0,1))


child(sys.argv[1])