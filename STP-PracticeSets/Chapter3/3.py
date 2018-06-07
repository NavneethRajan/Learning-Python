#   Write a program that prints a message
#   if a variable is less than or equal to 10,
#   another message if the variable is greater than 10 but less than or equal to 25,
#   and another message if the variable is greater than 25

x = 16

if x <= 10:
    print("x is less than or equal to 10")
# On further thought I guess the "x > 10" on the next line was not needed
elif x > 10 and x <= 25:
    print("x is greater than 10 but less than or equal to 25")
else:
    print("x is greater than 25")
