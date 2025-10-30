def calculate_love_score(name1, name2):
    a = 0
    b = 0
    full_name = str(name1) + str(name2)
    for letter in full_name.lower():
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            a += 1
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            b += 1
    print(f"Love Score: {a}{b}.")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Francisco Rangel", "Isis Katayama")
