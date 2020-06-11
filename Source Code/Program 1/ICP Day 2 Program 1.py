weightlist = []
N = int(input("total number of students:"))
for i in range(0, N):
    print("Enter weight in lbs", i , ":")
    weight = int(input())
    weightlist.append(weight)
print("weight list is", weightlist)
kilo = [item/2.2 for item in weightlist]
print (kilo)




