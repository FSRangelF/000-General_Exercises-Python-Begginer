def format_name(first_name, last_name):
  first = []
  last = []
  for i in range(0, len(first_name)):
    if i == 0:
      first.append(first_name[i].upper())
    else:
      first.append(first_name[i].lower())
  for i in range(0, len(last_name)):
    if i == 0:
      last.append(last_name[i].upper())
    else:
      last.append(last_name[i].lower())
  name = ""
  for char in first:
    name += char
  name += " "
  for char in last:
    name += char
  return name

def format_name2(first_name, last_name):
  if first_name == "" or last_name == "":
    return "Please provide a valid name."
  return f"{first_name.title()} {last_name.title()}"

print(format_name("franCisco","rAngel"))
print(format_name2("franCisco","rAngel"))
