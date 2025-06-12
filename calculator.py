def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def mod(n1, n2):
    return n1 % n2

print("select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n"
      "5. modulus\n")


number= int(input("Select operation (1-5): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if number == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif number == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif number == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif number == 4:
    print(n1, "/", n2, "=", div(n1, n2))
elif number == 5:
    print(n1, "%", n2, "=", mod(n1, n2))   
else:
    print("Invalid input")