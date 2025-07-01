while True:
    try:
        x = int(input("Enter the value of X: "))
        y = int(input("Enter the value of Y: "))
    except ValueError:
        print("Enter a valid integer!")
        continue

    add = x + y
    subtract = x - y
    multiply = x * y
    if y != 0:
        divide = x / y
    else:
        divide = "Undefined Value"

    print("Addition:", add)
    print("Subtraction:", subtract)
    print("Multiplication:", multiply)
    print("Division:", divide)
    break

