import random
print("Coded by:\nohmyginger\ninsomnyawolf")
print("Dice")
print("\n")
quest = input("Roll?\n")
print("\n")
ans = ["1", "2", "3", "4", "5", "6"]
while True:
    if quest.lower() in ["stop", "quit", "exit"]:
        break
    print(random.choice(ans))
    quest = input("Roll again?\n")
    print("\n")
#Bad Coded by:
#ohmyginger and insomnyawolf
