# The following code displays a message(s) about the acidity of a solution:
# ph = float(input("Enter the ph level: "))

# if ph < 7.0:
#     print("It's acidic!")
# elif ph < 4.0:
#     print("It's a strong acid!")

def acid_test(ph):
    if ph < 7.0:
        print("It's acidic!")
    elif ph < 4.0:
        print("It's a strong acid")

# a. What message(s) are displayed when the user enters 6.4?
acid_test(6.4)

# b. What message(s) are displayed when the user enters 3.6?
acid_test(3.6)

# c. Make a small change to one line of the code so that both messages
# are displayed when a value less than 4 is entered.

def acid_test(ph):
    if ph < 7.0:
        print("It's acidic!")
    if ph < 4.0:
        print("It's a strong acid")

acid_test(3.9)