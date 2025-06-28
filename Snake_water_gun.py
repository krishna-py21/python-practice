import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp turn: Snake 🐍 (s), Water 💧 (w), Gun 🔫 (g)")
randNO = random.randint(1, 3)
print(randNO)

if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

you = input("Your turn: Snake 🐍 (s), Water 💧 (w), Gun 🔫 (g): ")

a = gamewin(comp, you)

print(f"\nComputer chose: {comp}")
print(f"You chose: {you}")

if a == None:
    print("😐 The game is a tie!")
elif a:
    print("🎉 You won! Congratulations!")
else:
    print("😞 You lose! Better luck next time!")
