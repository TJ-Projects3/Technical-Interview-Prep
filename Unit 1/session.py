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
