def hello_world():
    print("Hello world")

hello_world()

def todays_mood():
    mood = ":)"
    print("Today's mood: " + mood)

todays_mood()

def lunch_menu(pizza):
    print ("Today's menu: " + pizza)
lunch_menu("teriyaki")

def sum(a, b):
    return a + b
print(sum(2,3))

def product(a, b):
    return a * b
print(product(22,7))

def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

def what_time_is_it(hour):
    if hour == 2:
        return "Taco Time! 🌮"
    elif hour == 12:
        return "Peanut butter Jelly time!! 🥪"
    else:
        return "Nap Time 😴"
time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

def blackjack(score):
    if score == 21:
        return "Blackjack!"
    elif score > 21:
        return "Bust!"
    elif  17 <= score < 21:
        return "Nice hand!"
    elif  score < 17:
        return print("Hit me!")
    
# def get_odds(nums):
#     newLst = []
#     for i in nums:
#         if i % 2 != 0:
#             newLst.append(i)
#     return newLst

# nums = [2,5,1,8,6,5]
# odd_nums = get_odds(nums)
# print(odd_nums)

# def multiplication_table(num):
#     for i in range(1,11):
#         mult = num * i
#         print(mult)

# multiplication_table(7)

def list_to_number(digits):
    word = ""
    for i in digits:
        word += str(i)
    return map(str, digits)

digits = [1,0,3]
number = list_to_number(digits)
print(number)

# Write a function move_zeroes() that takes in an integer list nums and returns a new list with all the 0 values moved to the end of the list. 
# The relative non-zero elements in the original list should be maintained.

# Understand: We must analyze the original list, insert all non-zero numbers, and move every zero to the end of the array.
# Plan: Initialize a count and new list. We will iterate through the original list and as we see 0s, we iterate the count, else append the non-zero
# integer. After the loop, we will have our non-zero numbers in place, so we have another loop that uses the count of zeros we had as a range,
# and until that count of zeroes finish we keep adding zeroes to the end of the array. After both loops finish (non-nested), we return our new list answer.

def move_zeroes(nums):
    newLst, count = [], 0
    for i in nums:
        if i == 0:
            count += 1
        else:
            newLst.append(i)
    
    for i in range(count):
        newLst.append(0)
    
    return newLst

nums = [0,6,5,3,3,0,0]
new_nums = move_zeroes(nums)
print(new_nums)