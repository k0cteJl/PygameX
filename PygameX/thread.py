from collections.abc import Sequence

from thread import Thread

def run_task(target, args: Sequence = ()):
    task = Thread(target=target, args=args)
    task.start()
    return task