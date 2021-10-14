# 1 Basic
for x in range(0, 151):
    print(x)

# 2 Multiples of Five
for x in range(5, 1001):
    if x%5 == 0:
     print(x)

# 3 Counting,the Dojo Way
result = ""
for x in range(1, 101):
 if x % 5 == 0:
    result= "coding"
 if x % 10 == 0:
    result += " dojo"
 if result == "":
    result = str(x)
 print(result)
 result = ""

# 4 Whoa. That Sucker's Huge
Sum = 0
for x in range(0, 500001):
    if x % 2 != 0:
        Sum += x
print(Sum)

# 5 Countdown by Fours
for x in range(2018, 0, -4):
    print(x)

# 6 Flexible Counter
lowNum = int(input("Enter a low number: "))
highNum = int(input("Enter a high number: "))
mult = int(input("Enter a number to find its multiples : "))

for Int_Num in range(lowNum, highNum+1):
    if Int_Num % mult == int():
        print(Int_Num)