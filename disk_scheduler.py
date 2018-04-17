head = 2150
requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]

print("\nThe total distance the disk arm moves for each algorithm is as follows:")
print("---------------------------")
 
def fcfs(requests):
	distance = 0
	local_head = head
	
	for r in requests:
		distance += abs(local_head - r)
		local_head = r
	return distance

print ('{} {}'.format("FCFS:", fcfs(requests)))

def sstf(requests):
	pass

def scan(requests):
	pass

def look(requests):
	pass

def cscan(requests):
	pass

def clook(requests):
	pass


