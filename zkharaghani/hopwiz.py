# HopWiz game
# Game starts by counting from 1 and instead of each multiplication of number 3, say "Hop",
# instead of each multiplication of number 7, say "Wiz" and instead of each multiplication
# of numbers 3 and 7 (like 21,..) say "HopWiz".

for n in range(1, 100):
    print("HopWiz") if n % 15 == 0 else print("Hop") if n % 3 == 0 else print("Wiz") if n % 5 == 0 else print(n)

# **********************************************************
for num in range(1,100):
    decision = 'HopWiz' if not num % 21 else 'Hop' if not num % 3 else 'Wiz' if not num % 7 else str(num)
    print(decision)

# **********************************************************
# pythonic form of HopWiz game

for num in range(1, 100):
    decision = 'HopWiz' if num in range(0, 100, 21) else 'Hop' if num in range(0, 100, 3)\
        else 'Wiz' if num in range(0, 100, 7) else str(num)
    print(decision)
