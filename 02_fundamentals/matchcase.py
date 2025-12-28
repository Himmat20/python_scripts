# match case conditions

# classical traffic lights case
color=input("Enter your color:")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("look")
    case "blue":
        print("sky")
    case _:#default case
        print("wrong color")