def life_in_weeks(age):
    total = 52*90
    current = 52*int(age)
    left = total - current
    print(f"You have {left} weeks left")

x = input("type your age: ")
life_in_weeks(age=x)
