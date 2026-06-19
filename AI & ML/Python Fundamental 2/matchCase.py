color= input("Enter color: ")

match color:
    case "Red":
        print("Stop!")
    case "Yellow":
        print("Look!")
    case "Green":
        print("Go!")
    case _:
        print("Wrong Color!")