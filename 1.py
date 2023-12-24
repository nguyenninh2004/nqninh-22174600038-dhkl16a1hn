import threading

def print_thread_name():
    print(f"Thread name: {threading.current_thread().name}")

t = threading.Thread(target=print_thread_name)
t.start()
