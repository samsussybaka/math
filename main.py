val1 = input("Enter the first value: ")
val2 = input("Enter the second value: ")

value1 = float(val1)
value2 = float(val2)

def formula():
    a = value1 * value1 + value2 * value2
    b = a * a
    c = b / a
    vatar = str(c)
    print("Valur of vatar is: " + vatar)

formula()
