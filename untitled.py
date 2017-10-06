NumbersList = []
min1= 0
min2 = 100000
NewList =[]
n = raw_input("Please enter number N =")
if n = 2:
    number1 = raw_input()
    score1 = raw_input()
    list1 = [number1,score1]
    number2= raw_input()
    score2 = raw_input()
    list2 = [number2,score2]
    NumberList=[list1,list2]

if n == 3:
    number1 = raw_input()
    score1 = raw_input()
    list1 = [number1,score1]
    number2= raw_input()
    score2 = raw_input()
    list2 = [number2,score2]
    NumberList=[list1,list2]
    number3= raw_input()
    score3 = raw_input()
    list3 = [number3,score3]
    NumberList=[list1,list2,list3]

if n==4:
    number1 = raw_input()
    score1 = raw_input()
    list1 = [number1,score1]
    number2= raw_input()
    score2 = raw_input()
    list2 = [number2,score2]
    NumberList=[list1,list2]
    number3= raw_input()
    score3 = raw_input()
    list3 = [number3,score3]
    number4 = raw_input()
    score4 = raw_input()
    list4 = [number4,score4]
    NumberList=[list1,list2,list3,list4]

if n==5:
    number1 = raw_input()
    score1 = raw_input()
    list1 = [number1,score1]
    number2= raw_input()
    score2 = raw_input()
    list2 = [number2,score2]
    NumberList=[list1,list2]
    number3= raw_input()
    score3 = raw_input()
    list3 = [number3,score3]
    number4 = raw_input()
    score4 = raw_input()
    list4 = [number4,score4]
    number5 = raw_input()
    score5 = raw_input()
    list5 = [number5,score5]
    NumberList=[list1,list2,list3,list4,list5]

for i in range(len(NumberList)):
    if NumberList[i][1] < min1:
        min1 = NumberList[i][1]
        Newlist =  List2
        List2 = NumberList[i]
        min2 = min1
    elif NumberList[i][1] = min1:
        Newlist = Newlist + [NumberList[i]]
  
for i in range(len(Newlist)):
    print Newlist[i][0] , Newlist[i][1]
               
