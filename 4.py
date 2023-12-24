import threading

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_factorial(start, end):
    result = 1
    for i in range(start, end+1):
        result *= i
    return result

n = 10
num_threads = 4
chunk_size = n // num_threads

threads = []
results = []
for i in range(num_threads):
    start = i * chunk_size + 1
    end = (i+1) * chunk_size
    t = threading.Thread(target=lambda r, f, s, e: r.append(f(s, e)), args=(results, calculate_factorial, start, end))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_result = 1
for r in results:
    final_result *= r

print(f"The factorial of {n} is {final_result}")
