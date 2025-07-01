import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
} 

dice = []
total =0
num_of_dice = int(input("No of Dice: "))


for die in range(num_of_dice):
    dice.append(random.randint(1,6))
import random
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
} 

dice = []
total =0
num_of_dice = int(input("No of Dice: "))


for die in range(num_of_dice):
    dice.append(random.randint(1,6))
#for vertical dices fig
#for die in range(num_of_dice):
    # access the elements of the tuple
    #for line in dice_art.get(dice[die]):
     #   print(line)
    
#for horizontal dices fig
for i in range(5):
    for j in dice:
        print(dice_art.get(j)[i], end = "  ")
    print()

for die in dice:
    print(f"    Die:{die}", end ="    ")

print()

total = sum(dice)
print(f"Total:{total}")


for i in range(5):
    for j in dice:
        print(dice_art.get(j)[i], end = "  ")
    print()

for die in dice:
    print(f"    Die:{die}", end ="    ")

print()

total = sum(dice)
print(f"Total:{total}")
