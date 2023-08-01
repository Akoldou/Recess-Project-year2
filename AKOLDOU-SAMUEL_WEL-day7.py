
# CONTEXT MANAGER AND MULTI- THREADING

"""def open_file(filename):
    file = open(filename,"r")
    def__enter__py(self):
        return file
    def__exit__(self, exc-type, exc_value, exc_tb):
        return __enter__, __exit__

with open_file("my_file.txt") as f:
    contents = f.read()
"""
    # demonstating context manager using time series

import time
class Timer:
    def __enter__(self):
        self.start_time = time.time()
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"The time for this execution{execution_time} seconds")

with Timer():
    time.sleep(2)

    # Multithreading and Multi processing
     # these are technics that can be used to improved the performance of a python
     #program
     #  multi porcessing ,this is a tecnique where multiple threads are created within a simple process
    # Multiprocessing is a technique where multiple threads are created.

# Example of Multithreading 

import threading

def task(name):
    print(f"Running task{name}")

# creating multiple threads
threads = []
for i in range (10):
    t = threading.Thread(target=task, args=(f"threads{i}",))
    threads.append(t)
    t.start()

    # wait for  all threads to finish 
    for t in threads:
        t.join() 

#  Demonstrating the use of Multiprocessing

"""import multiprocessing

def process_task(name):
    print(f"processing task{name}")
    # creating a pool of processes
pool = multiprocessing.Pool(processes=5) 
# Submittng multiple task to the pool
for i in range(6):
    pool.apply_async(process_task, args=(f"Process{i}",))
    # close the pool and wait for all processes to finish
pool.close()
pool.join() 
"""

# Demonstrating the use of mulltithreading and multiprocessing

import threading
import multiprocessing

def task(name):
    print(f"Running task{name}on thread {threading.current_thread().name} with process{multiprocessing.current_process().name}")
    
   # creating multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target =task, args=(f"Threads{i}",))
    threads.append(t)
    t.start()
# waiting for all threads to finish
for t in threads:
    t.join()
    

 EXERCISES
 

 # EXERCISE 1
    
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# E
with FileHandler('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

 
 # EXERCISE 2

"""import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
"""

 
     #  EXERCISE 3


import threading
import multiprocessing
import time

# Function to run for a specific duration
def run_function(duration):
    print(f"Running function for {duration} seconds")
    time.sleep(duration)
    print("Function execution completed")

# Create and start multiple threads
threads = []
durations = [1, 2, 3]  # Different durations for each thread
for duration in durations:
    thread = threading.Thread(target=run_function, args=(duration,))
    thread.start()
    threads.append(thread)

# Create and start multiple processes
processes = []
for duration in durations:
    process = multiprocessing.Process(target=run_function, args=(duration,))
    process.start()
    processes.append(process)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Wait for all processes to complete
for process in processes:
    process.join()

print("All threads and processes completed")








    