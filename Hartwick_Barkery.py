# Jared Jackson
# 10/14/19
# This will collect and present data from Hartwick Bakery
cookies = []
candies = []


# The following 2 functions will enable there user to enter input data for the sales
def cookies_input():
    print("Okay then, enter the amount of sales for cookies for each of the six months. Press enter after each value")
    for cookie in range(0, 6):
        cookie = int(input(">>>"))
        print("Received")
        cookies.append(cookie)


def candies_input():
    print("Now, enter the amount of sales for candy. Press enter after each value")
    for candy in range(0, 6):
        candy = int(input(">>>"))
        print("Received")
        candies.append(candy)


# The following 2 functions will calculate the average of the sales for the cookies and candy
def cookies_average():
    av_co = (cookies[0] + cookies[1] + cookies[2] + cookies[3] + cookies[4] + cookies[5]) / 6
    print(av_co)


def candies_average():
    av_ca = (candies[0] + candies[1] + candies[2] + candies[3] + candies[4] + candies[5]) / 6
    print(av_ca)


# I decided to create another function that would just return the value to pop_op.
# I had the function return the value, and it wouldn't print the value
# So after asking two people, I said conyo

def cookies_av_pop():
    av_co = (cookies[0] + cookies[1] + cookies[2] + cookies[3] + cookies[4] + cookies[5]) / 6
    return av_co


def candies_av_pop():
    av_ca = (candies[0] + candies[1] + candies[2] + candies[3] + candies[4] + candies[5]) / 6
    return av_ca


# The following 2 functions will calculate the maximum value of the cookies and the candy
def co_max():
    cookies.sort()
    print("Here is the maximum value of cookies sold in the list:")
    print(cookies[5])


def ca_max():
    candies.sort()
    print("Here is the maximum value of candy sold in the list:")
    print(candies[5])


def co_min():
    cookies.sort()
    print("Here is the minimum value of cookies sold in the list: ")
    print(cookies[0])


def ca_min():
    candies.sort()
    print("Here is the minimum value of candy sold in the list:")
    print(candies[0])


def pop_op():
    if cookies_av_pop() > candies_av_pop():
        print("Candy is nasty. According to the statistical data, cookies are way better than candy.")
    elif cookies_av_pop() < candies_av_pop():
        print("Apparently people like candy more, based on the data, you've given me")
        print("Are you happy with that?")


def new_co():
    cookies.clear()
    cookies_input()
    print("These are the new values for the sales of cookies per month:")
    print(cookies, "\n")


def new_ca():
    candies.clear()
    candies_input()
    print("These are the values for the sales of candy per month:")
    print(candies, "\n")


start = input("""Hello there, do you have data values for me? *Yes or No*
>>>""").title()
if start == "Yes" or start == "Y":
    print("\n")
else:
    print("Fine, goodbye! You're depriving me of food. You meanie")
    print("Program Terminated")
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()
    input()

# this is the def call for the user to input values for the cookie sales
# I've set it up so that the user can retype the values if they mess up
# while entering the values for the cookies and candy
cookies_input()
print("Thank you")
print(f"""These are the sales for each month:
{cookies}""")
correct1 = input("""Is this correct? *Yes or No*
>>>""").title()
if correct1 == "Yes" or correct1 == "Y":
    print("Moving on")
elif correct1 == "No" or correct1 == "N":
    print("Alright, here you go")
    new_co()


candies_input()
print("Thank you, again")
print(f"""And these were your values for the sales of candy for each month:
{candies}""")
correct2 = input("""Is this correct? *Yes or No*
>>>""").title()
if correct2 == "Yes" or correct2 == "Y":
    print("Moving on")
elif correct2 == "No" or correct2 == "N":
    print("Alright, here you go")
    new_ca()


# this is the def call that will average the inout values of the cookies and candy
print("Okay, now with that information, I can give you the average of the sales for the 6 month period")
print("Here is the average value of cookies sold per month:")
cookies_average()
input("Press Enter")
print("And here is the average value of candies sold per month")
candies_average()
input("Press Enter\n")

print("Now for the next piece of data")
co_max()
input("Press Enter")
ca_max()
input("Press Enter\n")
ca_min()
input("Press Enter")
co_min()

print("And now for the final evaluation of data:")
pop_op()
print("Well, thank you for the data, I have been well fed")
