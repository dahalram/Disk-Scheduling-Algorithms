import copy

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
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	res = 0
	max_d = max(tmp_req)
	min_d = abs(local_head - max_d)

	while(len(tmp_req) > 0):
		for r in tmp_req:
			res = abs(local_head - r)
			if (res < min_d):
				min_d = res
				max_d = r

		local_head = max_d
		tmp_req.remove(max_d)
		distance += min_d

		if (len(tmp_req) > 0):
			min_d = abs(local_head - max(tmp_req))
			max_d = max(tmp_req)
	return distance
	
print ('{} {}'.format("SSTF:", sstf(requests)))

def scan(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	end = 4999
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			distance += abs(local_head - i)
			local_head = i
			tmp_req.remove(i)

	distance += abs(local_head - end)
	local_head = end
	
	#tmp_c = max_d
	while max_d >= 0:
		if (max_d in tmp_req):
			distance += abs(local_head - max_d)
			local_head = max_d
			tmp_req.remove(max_d)
		max_d -= 1
	return distance
	
print ('{} {}'.format("SCAN:", scan(requests)))

def look(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			distance += abs(local_head - i)
			local_head = i
			tmp_req.remove(i)

	while max_d >= 0:
		if (max_d in tmp_req):
			distance += abs(local_head - max_d)
			local_head = max_d
			tmp_req.remove(max_d)
		max_d -= 1
	return distance	

print ('{} {}'.format("LOOK:", look(requests)))

def cscan(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	end = 4999
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			distance += abs(local_head - i)
			local_head = i
			tmp_req.remove(i)

	distance += abs(local_head - end)
	local_head = 0
	
	for i in range(0, max_d+1):
		if (i in tmp_req):
			distance += abs(local_head - i)
			local_head = i
			tmp_req.remove(i)
	return distance
print ('{} {}'.format("C-SCAN:", cscan(requests)))	

def clook(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			distance += abs(local_head - i)
			local_head = i
			tmp_req.remove(i)
	
	local_head = min(tmp_req)
	for i in range(0, max_d+1):
		if (i in tmp_req):
			distance += abs(local_head - i)
			local_head = i
			tmp_req.remove(i)
	return distance
print ('{} {}'.format("C-LOOK:", clook(requests)))

