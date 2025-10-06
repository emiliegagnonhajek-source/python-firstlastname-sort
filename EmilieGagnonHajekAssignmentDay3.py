def sortName(firstName, lastName, sortorder="firstlast"):
    if sortorder == "firstlast":
        return f"{firstName} {lastName}"
    elif sortorder == "lastfirst":
        return f"{lastName} {firstName}"
    else:
        return "Invalid choice. Defaulting to 'first last'."

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

sortOrder = input("Press 1 to print 'first last' name -OR- Press 2 to print 'last first' name: ")

if sortOrder == "1":
    print(sortName(firstName, lastName, "firstlast"))
elif sortOrder == "2":
    print(sortName(firstName, lastName, "lastfirst"))
else:
    print("Invalid choice. Defaulting to 'first last'.")
    print(sortName(firstName, lastName, "firstlast"))
