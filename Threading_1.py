import threading
from queue import Queue
import time

# This is the lock, making sure we only allow 1 variable modification at a time.
print_lock = threading.Lock()

# This creates the queue and threader
q=Queue()






# This is a job that will be done by a worker in the queue
def exampleJob(worker):
	time.sleep(5) # work for 5 seconds
	with print_lock:
		print(threading.current_thread().name,worker)






# This creates workers, puts them in the queue, and does jobs.
def threader():
	while True:
		
		# Gets a worker from the queue
		worker = q.get()

		# Run example job using this worker we just added to the queue
		exampleJob(worker)

		# finished task
		q.task_done()






# This creates threads or 'workers'
for x in range(10): #Creating 10 workers
	t=threading.Thread(target=threader)

	# classifying as daemon, so they will die when the main thread dies.
	t.deamon=True

	# begins the thread, MUST come AFTER the daemon definition statement.
	t.start()





start=time.time()





# Assigning 20 jobs.
for worker in range(20):
	q.put(worker)




# wait until main thread terminates.
q.join()





# Calculates and prints how long it took to do every job assigned. Using threads the time is fractional.
print('Entire job took:',time.time() - start)