import random

rollDie = input("roll the die? yes or no: ")
if rollDie != "yes":
    rollDie = input("roll the die? yes or no: ")

while rollDie == "yes":
    if rollDie == "yes":
        diceNumbers = [
            "[-----]"
            "[     ]"
            "[  0  ]"
            "[     ]"
            "[-----]",
            "[-----]"
            "[0    ]"
            "[     ]"
            "[    0]"
            "[-----]",
            "[-----]"
            "[     ]"
            "[0 0 0]"
            "[     ]"
            "[-----]",
            "[-----]"
            "[0   0]"
            "[     ]"
            "[0   0]"
            "[-----]",
            "[-----]"
            "[0   0]"
            "[  0  ]"
            "[0   0]"
            "[-----]",
            "[-----]"
            "[0   0]"
            "[0   0]"
            "[0   0]"
            "[-----]",
        ]
        num = random.randint(1,6)
        print(diceNumbers[num-1])
        rollDie = input("roll the die? yes or no: ")

