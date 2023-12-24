import threading

def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(i)

def print_odd_numbers():
    for i in range(30, 51):
        if i % 2 != 0:
            print(i)

t1 = threading.Thread(target=print_even_numbers)
t2 = threading.Thread(target=print_odd_numbers)

t1.start()
t2.start()

t1.join()
t2.join()
