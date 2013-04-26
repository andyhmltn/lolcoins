#!/usr/bin/env python
import sys
import threading
import random
import time
import string
import hashlib

thread_list = []
charmap = string.lowercase + string.uppercase + string.digits

def start_string():
    return "".join([random.choice(charmap) for _ in xrange(0, 5)])

def worker():
	difficulty  = 5
	number      = 0
	buffer_     = "0"*difficulty
	found       = False
	prefix      = start_string()
	
	upper_bound = (5*(10**5)**10)
	i = 0

	print "Starting worker for " + prefix
	while True and i < upper_bound:
		coin = prefix + str(i)
		
		worker_hash = hashlib.sha512(coin).hexdigest()

		if worker_hash[0:difficulty] == buffer_:
			print "Generated 1 lolcoin: " + coin

			with open("coins.txt", "a") as coin_base:
				coin_base.write(coin+"\n")

			t = threading.Thread(target=worker)
			thread_list.append(t)

			t.daemon = True
			t.start()

			found = True		
		i += 1

for i in range(10):
	t = threading.Thread(target=worker)
	thread_list.append(t)

	t.daemon = True
	t.start()