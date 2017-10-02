import os
import csv 
import filecmp 

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		l = []
		for each in reader:
			l.append(each)
		return l




#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	x= sorted(data, key= lambda k:k[col])
	return x[0]["First"]+ " " + x[0]["Last"]

	

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	classdict= {"Senior": 0, "Junior": 0, "Sophomore": 0, "Freshman": 0}
	
	for each in data: 
		if each["Class"] == "Senior":
			classdict["Senior"]+=1
		elif each["Class"]== "Junior":
			classdict["Junior"]+=1
		elif each["Class"]== "Sophomore":
			classdict["Sophomore"]+=1
		elif each["Class"]== "Freshman":
			classdict["Freshman"]+= 1
	sortedclass= sorted(classdict, key = lambda x:classdict[x], reverse= True)			
			
	alist= []		
	for each in sortedclass:
		alist.append((each,classdict[each]))
	return alist

# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	x = {}
	for each in a:
		y = each["DOB"]
		z= y.split("/")
		b= z[1]

		if b in x:
			x[b] += 1
		else:
			x[b]= 1

	lst= []
	for key in x.keys():
		d= (key, x[key])
		lst.append(d)


	bday = sorted(lst, key= lambda x: x[1], reverse= True)
	return int(bday[0][0])




# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest integer

	#Your code here:
	ages= []
	for each in a:
		y= each["DOB"]
		z= y.split("/")

		age = 2017 - int(z[2])
		ages.append(age)

	average = (sum(ages)/ len(ages))
	avg= int(average)
	return avg

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	x= sorted(a, key= lambda k:k[col])
	z= range(len(x))
	myfile= open("fileName.csv", 'w')
	# for each in range(len(x)):
	# 	final = x[each]["First"]+ "," + x[each]["Last"]+ "," + x[each]["Email"]+ "\n"
	# 	myfile.write(final)

	# 	print(final)
	# myfile.close()


		

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

