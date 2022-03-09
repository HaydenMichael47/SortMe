
file1 = open('Sort Me.txt')
lines = file1.readlines()  #[]
file1.close()
#with open('Sort Me.txt') as f:
 #   for line in f:
  #      if not line.isspace():
   #         lines.append(line)

    #lines = f.readlines()
    
    
for x in lines:
    if x.isspace():
        lines.remove(x)
    
for x in range(len(lines)):
    lines[x] = lines[x].rstrip()
    


for x in range(len(lines)):
    lines[x] = lines[x].replace(" ", "")

def sort(fileStrings):
    fileStrings.sort(key= len) #sorts by length first

    tempList = []

    #now sort alpabetically
    #indexLow = 0
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

        tempList.clear()
        counter = 0
        x=indexHigh-1



    for x in fileStrings:
        print(x)



sort(lines)


