import requests
import threading

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

urls = ["https://example.com/file1.txt", "https://example.com/file2.txt", "https://example.com/file3.txt"]
filenames = ["file1.txt", "file2.txt", "file3.txt"]

threads = []
for i in range(len(urls)):
    t = threading.Thread(target=download_file, args=(urls[i], filenames[i]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
