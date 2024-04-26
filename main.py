from queue import Queue
import time
import random

class Request:
    def __init__(self, id):
        self.id = id

def generate_request(queue):
    request_id = random.randint(1, 1000)
    request = Request(request_id)
    queue.put(request)
    print(f"Заявка {request.id} створена.")

def process_request(queue):
    if not queue.empty():
        request = queue.get()
        print(f"Заявка {request.id} оброблена.")
    else:
        print("Черга порожня.")

def main():
    request_queue = Queue()

    try:
        while True:
            generate_request(request_queue)
            process_request(request_queue)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Програма завершена.")

if __name__ == "__main__":
    main()
