number = input("Enter your number: ")
numberTwo = input("Enter your second number: ")
numberSymbol = input("Enter what to do here ")

def calculator():
    if numberSymbol == "-":
        print(int(number) - int(numberTwo)) # if its minus, then it will subtract the two numbers
    if numberSymbol == "+": 
        print(int(number) + int(numberTwo)) #If its plus, then it will add the two numbers
    if numberSymbol == "*":
        print(int(number) * int(numberTwo)) #If its multiply, then it will multiply the two numbers
    if numberSymbol == "/":
        print(int(number) / int(numberTwo)) #If its divide, then it will divide the two numbers
    if numberSymbol == "%":
        print(int(number) % int(numberTwo)) #If its modulus, then it will get the remainder of the two numbers
    if numberSymbol == "**":
        print(int(number) ** int(numberTwo)) #If its power, then it will get the power of the two numbers
    if numberSymbol == "//":
        print(int(number) // int(numberTwo)) #If its floor division, then it will get the floor division of the two numbers

if __name__ == "__main__":
    while True:
        calculator()
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != "yes":
            break