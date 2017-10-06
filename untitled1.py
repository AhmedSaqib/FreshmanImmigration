number = raw_input("please enter number=")
operation = raw_input("Please enter operation (*,/,+,-) =")
number1 = raw_input("please enter second number=")

if operation == "+":
    number3 = int(number) + int(number1)

if operation == "-":
    number3 = int(number) - int(number1)

if operation == "*":
    number3 = int(number) * int(number1)

if operation == "/":
    number3 = int(number) / (int(number1)*1.0)


print "final answer is =", number3

number4 = raw_input("if anymore operations on previous number then enter number else enter -1 =")
if number4 != -1:
    while number4 != "-1":
        operation = raw_input("Please enter operation (*,/,+,-) =")
        if operation == "+":
            number3 = int(number3) + int(number4)

        if operation == "-":
            number3 = int(number3) - int(number4)

        if operation == "*":
            number3 = int(number3) * int(number4)

        if operation == "/":
            number3 = int(number3) / (int(number4)*1.0)
        
        print "final answer is =", number3

        number4 = raw_input("if anymore operations on previous number then enter number else enter -1 =")

print "Thank you for using this calculator"
