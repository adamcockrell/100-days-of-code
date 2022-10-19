# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

while(len(two_digit_number) != 2):
    print("I SAID TWO DIGITS")
    two_digit_number = input("Type a two digit number: ")

else:
    result = int(two_digit_number[0]) + int(two_digit_number[1])
    print(result)






