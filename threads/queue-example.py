import threading
from queue import Queue
q = Queue()


def worker():
    while True:
        item = q.get()
        print(f'working on {item}')
        print(f'finished {item}')
        q.task_done()


threading.Thread(target=worker, daemon=True).start()

for item in range(20):
    q.put(item)

print('All task requests send\n', end='')

q.join()

print('all work completed')
