import copy

head = 2150
requests = [2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]

print("\nThe total distance the disk arm moves for each algorithm is as follows:")
print("---------------------------")

def fcfs(requests):
	distance = 0
	local_head = head
	moves = []
	
	for r in requests:
		move = abs(local_head - r)
		moves.append(move)
		distance += move
		local_head = r
	
	moves = [str(a) for a in moves]
	print ('{} {}'.format('Total Moves: ', ','.join(moves)))
	
	return distance

print ('{} {}'.format("FCFS total:", fcfs(requests)))
print("---------------------------")

def sstf(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	res = 0
	max_d = max(tmp_req)
	min_d = abs(local_head - max_d)
	moves = []

	while(len(tmp_req) > 0):
		for r in tmp_req:
			res = abs(local_head - r)
			if (res < min_d):
				min_d = res
				max_d = r

		local_head = max_d
		tmp_req.remove(max_d)
		moves.append(min_d)
		distance += min_d

		if (len(tmp_req) > 0):
			min_d = abs(local_head - max(tmp_req))
			max_d = max(tmp_req)
	
	moves = [str(a) for a in moves]
	print ('{} {}'.format('Total Moves: ', ','.join(moves)))
		
	return distance
	
print ('{} {}'.format("SSTF total:", sstf(requests)))
print("---------------------------")

def scan(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	end = 4999
	moves = []
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			move = abs(local_head - i)
			moves.append(move)
			distance += move
			local_head = i
			tmp_req.remove(i)

	distance += abs(local_head - end)
	local_head = end
	
	#tmp_c = max_d
	while max_d >= 0:
		if (max_d in tmp_req):
			move = abs(local_head - max_d)
			moves.append(move)
			distance += move
			local_head = max_d
			tmp_req.remove(max_d)
		max_d -= 1

	moves = [str(a) for a in moves]
	print ('{} {}'.format('Total Moves: ', ','.join(moves)))
	
	return distance
	
print ('{} {}'.format("SCAN total:", scan(requests)))
print("---------------------------")

def look(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	moves = []
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			move = abs(local_head - i)
			moves.append(move)
			distance += move
			local_head = i
			tmp_req.remove(i)

	while max_d >= 0:
		if (max_d in tmp_req):
			move = abs(local_head - max_d)
			moves.append(move)
			distance += move
			local_head = max_d
			tmp_req.remove(max_d)
		max_d -= 1
	
	moves = [str(a) for a in moves]
	print ('{} {}'.format('Total Moves: ', ','.join(moves)))
		
	return distance	

print ('{} {}'.format("LOOK total:", look(requests)))
print("---------------------------")

def cscan(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	end = 4999
	moves = []
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			move = abs(local_head - i)
			moves.append(move)
			distance += move
			local_head = i
			tmp_req.remove(i)

	move = abs(local_head - end)
	moves.append(move)
	distance += move
	local_head = 0
	
	for i in range(0, max_d+1):
		if (i in tmp_req):
			move = abs(local_head - i)
			moves.append(move)
			distance += move
			local_head = i
			tmp_req.remove(i)

	moves = [str(a) for a in moves]
	print ('{} {}'.format('Total Moves: ', ','.join(moves)))
		
	return distance
print ('{} {}'.format("C-SCAN total:", cscan(requests)))
print("---------------------------")	

def clook(requests):
	local_head = head
	distance = 0
	tmp_req = copy.copy(requests)
	
	max_d = max(tmp_req)
	moves = []
	
	for i in range(local_head, max_d+1):
		if (i in tmp_req):
			move = abs(local_head - i)
			moves.append(move)
			distance += move
			local_head = i
			tmp_req.remove(i)
	
	local_head = min(tmp_req)
	for i in range(0, max_d+1):
		if (i in tmp_req):
			move = abs(local_head - i)
			moves.append(move)
			distance += move
			local_head = i
			tmp_req.remove(i)
	moves = [str(a) for a in moves]
	print ('{} {}'.format('Total Moves: ', ','.join(moves)))
	
	return distance
print ('{} {}'.format("C-LOOK total:", clook(requests)))
print("---------------------------")

