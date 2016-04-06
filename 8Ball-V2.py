import random
print("Original code By insomnyawolf")
print("Recoded and optimized by ohmyginger")
print("Hi... Im the magic 8Ball")
quest = input("Whats your question?\n")
ans = []
#Negative ans
ans.append("Doubtful...")
ans.append("No")
ans.append("Never (╯°□°）╯︵ ┻━┻")
#Neutral ans
ans.append("Maybe...")
#possitive ans
ans.append("Yes")
ans.append("Not sure, likely yes :)")
ans.append("Yes, definitely!")
while True:
    if quest.lower() in ["stop", "quit", "exit"]:
        break
    print(random.choice(ans))
    quest = input("Whats your question?\n")
    print("\n")
#Bad Coded by:
#ohmyginger and insomnyawolf
