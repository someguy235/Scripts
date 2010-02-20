#Sorts a classroom schedule into an easier to read format
#For figuring out when a room is free

input = open("Fall07.csv", "r")
output = open("Fall07sorted.csv", "w")

def time(x, y):
        return cmp(x[2][:2], y[2][:2])

def timeSort(list, day):
        list.sort(time)
        lineNum = 0
        for line in list:
                if lineNum == 0:
                        output.write(day + " , ")
                        lineNum = 1
                else:
                        output.write(" , ")
                        #lineNum = 1
                stringNum = 0
                for string in line:
                        if stringNum == 0:
                                stringNum = 1
                        else:
                                if (not '\n' in string):
                                        output.write(string + " , ")
                                else:
                                        output.write(string)
                                
def daySort(list):
        M = []
        T = []
        W = []
        R = []
        F = []
        for line in list:
                if ('M' in line[4]):
                        M.append(line)
                if ('T' in line[4]):
                        T.append(line)
                if ('W' in line[4]):
                        W.append(line)
                if ('R' in line[4]):
                        R.append(line)
                if ('F' in line[4]):
                        F.append(line)
        output.write(list[0][0] + "\n")
        timeSort(M, "Mon")
        timeSort(T, "Tue")
        timeSort(W, "Wed")
        timeSort(R, "Thu")        
        timeSort(F, "Fri")
        output.write("\n")
        
line = input.readline()
lineList = line.split(',')
curRoom = lineList[0]
lines = []
done = 0
while(done != 2):
        if (done == 1):
                done = 2
        if (lineList[0] != curRoom):
                daySort(lines)
                lines = []
                curRoom = lineList[0]
        lines.append(lineList)
        line = input.readline()
        lineList = line.split(',')
        if ((line == "") & (done != 2)):
                done = 1



