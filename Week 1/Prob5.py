num1 = int(input("Hey I'm Mr Calculator give me a number!\n"))
num2 = int(input("Ooooooweee that's a great number. Give me another!\n"))
opera = str(input("Now enter xeither a to add, m to minus, d to divide, t to multiply or s to square\n2"))

if opera == "a":
    print(num1 + num2)
elif opera == "m":
    print(num1 - num2)
elif opera == "d":
    print(num1 / num2)
elif opera == "t":
    print(num1 * num2)
elif opera == "s":
    print(num1 ** num2)
else:
    print("woahhhhhhhh that's not a recognized input")