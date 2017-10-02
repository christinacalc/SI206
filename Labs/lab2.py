import operator 
f = open("TheVictors.txt", "r")
words = list(f.read().split())
d = {}
for i in words:
	if i in d: 
		d[i]+= 1
	else:
		d[i] = 1


top_words= sorted(d.items(), key= lambda x: x[1], reverse= True)
answer = top_words[:15]

for key,value in answer:
	print(key, value)