from threading import Lock, Thread
lock = Lock()
g = 0

def add_one():
	global g
	lock.acquire()
	g += 1
	lock.release()


def add_two():
	global g
	lock.acquire()
	g += 2
	lock.release()


threads = []
for func in [add_one, add_two]:
	threads.append(Thread(target=func))
	threads[-1].start()

for thread in threads:
	thread.join()


print(g)



"""

This simply gives an output of 3, but now we are sure that the two 
functions are not changing the value of the global variable g 
simultaneously although they run on two different threads. 
Thus, Locks can be used to avoid inconsistent output by allowing
 only one thread to modify data at a time.

 """