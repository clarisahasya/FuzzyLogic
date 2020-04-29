import csv

def loadData():
	data = []
	with open('influencers.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count=0
		for row in csv_reader:
			if (line_count != 0):
				data.append(row)
			line_count += 1
	return data

def saveData(target):
	with open('chosen.csv', mode='w', newline='') as csv_file:
	    csv_writer = csv.writer(csv_file)
	    for index in target:
	    	csv_writer.writerow([index])
	return csv_writer

def followerCount(fol):
	low, avg, high = 0, 0, 0
	if (fol <= 20000):
		low = 1
	elif (fol > 30000) :
		low = 0
	elif (fol > 20000 and fol <= 30000):
		low = (30000 - fol)/(30000 - 20000)

	if (fol <= 20000 and fol > 60000):
		avg = 0
	elif (fol > 20000 and fol <= 30000):
		avg = (fol - 20000)/(30000 - 20000)
	elif (fol > 30000 and fol <= 55000):
		avg = 1
	elif (fol > 55000 and fol <= 60000):
		avg = (60000 - fol)/(60000 - 55000)

	if (fol <= 50000):
		high = 0
	elif (fol > 70000) :
		high = 1
	elif (fol > 50000 and fol <= 70000):
		high = (fol - 50000)/(70000 - 50000)

	return [low, avg, high]

def engagementRate(rate):
	low, avg, high = 0.0, 0.0, 0.0
	if (rate <= 2):
		low = 1.0
	elif (rate > 3.5) :
		low = 0.0
	elif (rate > 2 and rate <= 3.5):
		low = (3.5 - rate)/(3.5 - 2)

	if (rate <= 2  and rate > 6.5):
		avg = 0.0
	elif (rate > 2 and rate <= 3.5):
		avg = (rate - 2)/(3.5 - 2)
	elif (rate > 3.5 and rate <= 6):
		avg = 1.0
	elif (rate > 6 and rate <= 6.5):
		avg = (6.5 - rate)/(6.5 - 6)

	if (rate <= 5):
		high = 0.0
	elif (rate > 7) :
		high = 1.0
	elif (rate > 5 and rate <= 7):
		high = (rate - 5)/(7 - 5)

	return [low, avg, high]

def inference(fol,rate):
	na, mi, me = [], [], []

	na.append(max(fol[0],rate[0])) #low, low
	na.append(max(fol[0],rate[1])) #low, average
	na.append(max(fol[1],rate[0])) #average, low

	mi.append(max(fol[0],rate[2])) #low, high
	mi.append(max(fol[1],rate[1])) #average, average
	mi.append(max(fol[2],rate[0])) #high, low

	me.append(max(fol[1],rate[2])) #average, high
	me.append(max(fol[2],rate[1])) #high, average
	me.append(max(fol[2],rate[2])) #high, high

	nano = max(na[0],na[1],na[2])
	micro = max(mi[0],mi[1],mi[2])
	medium = max(me[0],me[1],me[2])

	return [nano, micro, medium]

def sugeno(inf):
	s = ((40*inf[0]) + (60*inf[1]) + (70*inf[2])) / (inf[0]+inf[1]+inf[2])
	return s

def sorting(defuzzy,index):
	sort = [x for _, x in sorted(zip(defuzzy,index), reverse=True)]
	return sort


#MAIN PROGRAM
follower, engagement, inf, defuzzy, index = [], [], [], [], []
data = loadData()
for row in data:
	follower = followerCount(int(row[1]))
	engagement = engagementRate(float(row[2]))X
	inf = inference(follower,engagement)
	defuzzy.append(sugeno(inf))
	index.append(row[0])
# print("defuzzy",defuzzy)
# print("===========================================================================")
hasil = sorting(defuzzy,index)
twenty = hasil[:20]
print('*20 Influencers Terbaik*')
for twen in twenty:
	print(twen)
saveData(twenty)
