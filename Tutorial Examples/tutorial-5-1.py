veryCoolMeter = 0

input = input("How cool are you?")

if input == "epic gamer":
    veryCoolMeter = 99
elif input == "gamer":
        veryCoolMeter = 88
elif input == "epic":
        veryCoolMeter = 77
else:
    veryCoolMeter = 10

print("Your coolness meter rating (out of 99) is " + str(veryCoolMeter))