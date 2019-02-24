import threading

num = 0
lock = threading.Lock()		# normal lock

lock.acquire()
num += 1
lock.acquire()				# this will block
num += 2
lock.release()


# with R Lock that problem doesn't happens
lock = threading.RLock()

lock.acquire()
num += 3
lock.acquire()				# this won't block
num += 4
lock.release()
lock.release()				# you need to call release once for each call to acquire

