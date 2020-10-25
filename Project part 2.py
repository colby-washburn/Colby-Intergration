# Name: Colby Washburn
# Date: September 1st 2020
# An intergration of everything I have learned
# Along with some research I have done about programming
# The Import random allows for random number generation
# Time allows for text over time
# ** does exponets, * does multiplication, / divides
# + adds, % does modulus, // does floor divison
import random
import time

print("Welcome to my Intergration Project!", sep='\n')


# Classes
class Fighter(object):
    health = 100
    strength = 9
    defence = 8
    fire_magic = 1
    lightning_magic = 1


class Fire_Mage(object):
    health = 85
    strength = 3
    defence = 5
    fire_magic = 9
    lightning_magic = 5


class Lightning_Mage(object):
    health = 85
    strength = 3
    defence = 5
    fire_magic = 5
    lightning_magic = 9


class Rouge(object):
    health = 75
    strength = 7
    defence = 10
    fire_magic = 2
    lightning_magic = 2


# Enemy Classes

class Guard(object):
    name = "Guard"
    health = 30
    strength = 5
    defence = 5


class Warden(object):
    name = "Leon the Warden"
    health = 100
    strength = 8
    defence = 6


class Guard_dog(object):
    name = "Zeus THE Guard Dog"
    health = 55
    strength = 8
    defence = 2


def game_over(character):
    if character.health < 1:
        print("You have died, Restart.")
        exit()


def hero_select():
    print("Select your class!")
    selection = input(
        "1. Fighter \n2. Fire Mage \n3. Ligtning Mage \n4. Rouge \n")

    if selection == "1":
        character = Fighter
        print("Hmmm Fighter, strong and straight forward, I like your choice")
        return character

    elif selection == "2":
        character = Fire_Mage
        print("Aye, a Fire Mage, fury of flame and destruction")
        return character

    elif selection == "3":
        character = Lightning_Mage
        print("Okay,good luck")
        return character

    elif selection == "4":
        character = Rouge
        print("Rouge.... so you have chosen hard mode? Yes?")
        return character

    else:
        print("Please select a class. 1 2 3 or 4 ")
        hero_select()


character = hero_select()


def enemy_select(Guard):
    enemyList = [Guard]
    chance = random.randint(0, 0)
    enemy = enemyList[chance]
    return enemy


def battlestate():
    enemy = enemy_select(Guard)
    print("He says 'You will die by my blade!'\n")
    while enemy.health > 0:
        combat = input("1. Dagger\n2. Fire Spell\n3. Electric Spell\n")

        if combat == "1":
            print("You swing your trusty dagger at the", enemy.name, )
            hitchance = random.randint(0, 10)
            if hitchance > 0:
                enemy.health = enemy.health - character.strength
                print("You swing and slash , you hit them!")

                if enemy.health > 0:
                    character.health = character.health - (
                            enemy.strength / character.defence)
                    print("The", enemy.name,
                          "swipes their sword at you, you now have",
                          character.health, "left")
                    print("Quick! Attack again!")
                else:
                    if enemy.name == "Guard":
                        enemy.health = 30
                        print("You have defeated the", enemy.name, "\n")
                        break
            else:
                print("You swing too low, YOU MISS!")
                character.health = character.health - (
                        enemy.strength / character.defence)
                print("The", enemy.name,
                      "swipes their sword at you, you now have",
                      character.health, "left")
                print("Quick! Hit them again!")

        elif combat == "2":
            print("You focus on your power, and hurl a fireball at",
                  enemy.name)
            hitchance = random.randint(0, 10)
            if hitchance > 0:
                enemy.health = enemy.health - character.fire_magic
                print("Your fireball gets thrown , you hit them!")

                if enemy.health > 0:
                    character.health = character.health - (
                            enemy.strength / character.defence)
                    print("The", enemy.name,
                          "swipes their sword at you, you now have",
                          character.health, "left")
                    print("Quick! Hit them again!")
                else:
                    if enemy.name == "Guard":
                        enemy.health = 30
                        print("You have BURNT the", enemy.name, "\n")
                        break
            else:
                print("You fly that ball of fire too far, YOU MISS!")
                character.health = character.health - (
                        enemy.strength / character.defence)
                print("The", enemy.name,
                      "swipes their sword at you, you now have",
                      character.health, "left")
                print("Quick! Hit them again!")

        elif combat == "3":
            print("You use your rage, and conduct a lightning bolt at",
                  enemy.name)
            hitchance = random.randint(0, 10)
            if hitchance > 0:
                enemy.health = enemy.health - character.lightning_magic
                print("Your bolt gets shot , you hit them!")

                if enemy.health > 0:
                    character.health = character.health - (
                            enemy.strength / character.defence)
                    print("The", enemy.name,
                          "swipes their sword at you, you now have",
                          character.health, "left")
                    print("Quick! Hit them again!")
                else:
                    if enemy.name == "Guard":
                        enemy.health = 30
                        print("You have ELECTROCUTED the", enemy.name, "\n")
                        break
            else:
                print("You sweep your bolt too far, YOU MISS!")
                character.health = character.health - (
                        enemy.strength / character.defence)
                print("The", enemy.name,
                      "swipes their sword at you, you now have",
                      character.health, "left")
                print("Quick! Hit them again!")

        else:
            print("Number not valid, pres 1, 2, or 3,")


print("\n")
intro_1 = "This is an adventure game, that depends on your choices"
intro_2 = "The game adapts to the way you play"
print(intro_1, end='\n')
print(intro_2)
time.sleep(4)
print("\n")


def display_intro():
    print("You awake in a small cell, barred doors and walls")
    time.sleep(3)
    print("There is a guard, he is guarding your door")
    time.sleep(3)
    print("He says to you 'Finally, you're awake'")


display_intro()


def Choice_1():
    print("\n What do you choose to do? \n")
    choice_1 = input(
        "1. Punch the guard in the head \n2. Grab his keys \n3. Talk to the guard \n")

    if choice_1 == "1":
        print(
            "The guard opens the door and draws their sword, Prepare yourself \n")
        battlestate()

    elif choice_1 == "2":
        print("You try to take the guard's keys")
        keyChance = random.randint(0, 5)
        if keyChance > 2:
            print(
                "You got the keys and open the door.... but the guard looks over and attacks")
            battlestate()
        else:
            print("The guard notices!\n He opens the door and atacks!")
            battlestate()
    elif choice_1 == "3":
        print("You talk to the guard, what do you say \n")
        print(
            "As soon as you open your mouth, the guard gets irritaed and walks off")
        print("You notice, the door was actually broken")
        print("The guard was just holding the door closed")
        print("You leave the cell")


Choice_1()


def first_Puzzle():
    print("\n Good you're out of the cell""\n""Now find the key!""\n")
    print("Where do you look for the key?")
    key_spot = ["Drawer or Key Rack"]
    for x in key_spot:
        print(x)
        puzzle_choice = input("1 or 2\n")
        if puzzle_choice == 1:
            drawer_puzzle()
        elif puzzle_choice == 2:
            key_rack()
        elif puzzle_choice != 1 or 2:
            print("Invalid Choice")

first_Puzzle()
def drawer_puzzle():
    print("You approach a locked drawer you notice some plates lock down as you press them")
    print("You see these plates with these numbers")
    for x in range(2, 20):
        print(x)
    print("What do you do?")
    button_press = input(
        "1. Press all the even numbers \n 2. Press all of the Odd numbers")
    if button_press == 2:
        print("The drawer opens and you find the key")
        Ending_1()
    elif button_press == 1:
        print("The drawer locks, you approach the key rack instead")
        key_rack()


def key_rack():
    print("You walk over to the key rack and see the keys to the gate")
    Leaving_1()


def Ending_1():
    print("You've escaped your holdings, and there is a riddle at the exit")
    riddle = random.randint(1, 5)
    if riddle == 1:
        print("What is")
        print(int(2 * 2))
        print("+")
        print(int(2 * 2))
        print("?")
        answer = input()
        if answer == 8:
            Leaving_1()
    elif riddle == 2:
        print("what is")
        print(int(20 % 30))
        print("+")
        print(int(20 % 30))
        print("?")
        answer = input()
        if answer == 40:
            Leaving_1()
    elif riddle == 3:
        print("what is")
        print(int(2 ** 2))
        print("+")
        print(int(2 ** 2))
        print("?")
        answer = input()
        if answer == 8:
            Leaving_1()
    elif riddle == 4:
        print("what is")
        print(int(8 // 8))
        print("+")
        print(int(8 // 8))
        print("?")
        answer = input()
        if answer == 2:
            Leaving_1()
    elif riddle == 5:
        print("What is larger?")
        print("200 or 2001?")
        print("Please use < or >")
        answer = input()
        if answer == "<":
            Leaving_1()

Ending_1()


def Leaving_1():
    print("You escape! Congrats")
    exit()


Leaving_1()
