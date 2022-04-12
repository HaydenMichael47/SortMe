import sys

#print(sys.argv[1])

#read the file into a list
file1 = open('Sort Me.txt')
lines = file1.readlines()  
file1.close()

#remove empty space and extra characters   
for x in lines:
    if x.isspace():
        lines.remove(x)
    
for x in range(len(lines)):
    lines[x] = lines[x].rstrip()

for x in range(len(lines)):
    lines[x] = lines[x].replace(" ", "")

def sortList(fileStrings):
    fileStrings.sort(key= len) #sorts by length first

    tempList = []

    #now sort alpabetically
    indexHigh = 0
    currLength = len(fileStrings[0])
    #iterate through entire list
    for x in range(len(fileStrings)):
        for y in range(x+1,len(fileStrings)):
            if(len(fileStrings[y]) > len(fileStrings[x])): 
                indexHigh = y #find where length changes to define current scope
                break
        
        #sort current scope then return them to the list
        for i in range(x,indexHigh):
            tempList.append(fileStrings[i])

        tempList.sort()
        counter = 0
        for i in range(x,indexHigh):
            fileStrings[i] = tempList[counter]
            counter +=1

        #reset temp variables and update index
        tempList.clear()
        counter = 0
        x=indexHigh-1


    #After the list is properly sorted, output the results
   # for x in fileStrings:
        #print(x)

    return fileStrings

def reverseSort(fileStrings):
    fileStrings = sortList(fileStrings)
    fileStrings.reverse()
    
    
    return fileStrings




#Test the sort method
if(len(sys.argv)>1 and sys.argv[1] == "-r"):
    lines = reverseSort(lines)
    lines.append("Hello")
    for x in lines:
        print(x)
else:
    lines = sortList(lines)
    for x in lines:
        print(x)


