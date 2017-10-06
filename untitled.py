boolean1 = "False"
count = 0
s = ""
list1 = []
string1 = raw_input("please enter the word =")
k = raw_input("please enter the integer k =")
k = int(k)
length = len(string1)
length = int(length)
segments = length / k

for i in range(segments):
    for x in range(k):
        for y in range(len(s)):
            if string1[i] == s[y]:
               boolean1 = "True"
        if boolean1 == "False":
            s = s + string1[count]
        count = count + 1
    list1 =  list1 + [s]
    s = ""
    boolean1 = "False"
for i in range(len(list1)):
    print list1
