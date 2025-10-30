def is_leap_year(year):
    """Return True if the input year is Leap and False otherwise."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

test = [2000, 2020, 2024, 2400, 1700, 1989, 2100]

for item in test:
  print(f"{item} -> {is_leap_year(item)}")
  
