from sys import exit
from sys import argv
from random import randint
from textwrap import dedent

lord_of_the_rings, middle_earth, fellowship_of_the_ring, song = argv

# a list of items
fellowship_of_the_ring = ['Aragorn', 'Boromir', 'Gimli', 'Legolas',
'Hobbits', 'Gandalf']

# Scenes: Ruins, shire, rivendell, Journey, moria, anduin, mount doom, Finished
# Objects: Scene, Engine, Map
# Argv: Aragorn, Gimli, Legolas, Hobbits, Boromir, Gandalf

print("This game is based on the book:", lord_of_the_rings)
print("It takes place on:", middle_earth)
print("The crew we are gonna lead on consists:", fellowship_of_the_ring)


class Scene(object):

    def enter(self):
        print("You are a hobbit in Middle-Earth.")
        print("Spending your days whom some never heard.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Ruins(Scene):

    quips = [
        "You died.",
        "Shire is in ruins, Melkor rules Middle-Earth now. ",
        "You tried, but you were too small.",
        "Thanks for trying, please try next time."

    ]

    def enter(self):
        print(Ruins.quips[randint(0, 3)])
        exit(1)


class Shire(Scene):

    def enter(self):
        print("\nUnder a beautiful tree, you're reading a book.")
        print("Long awaited Wizard shows up in Shire.")
        print("He brought good news or bad news?")
        print("He is asking for you to take some ring and join him in Rivendell")
        print("join or reject? ")

        action = input("> ")

        if action == "join":
            print(dedent("""
            You take Samwise Gamgee with you and roll for Rivendell on foot.
            """))
            return "Rivendell"
        elif action == "reject":
            print(dedent("""
            You choose a cozy life in Shire, for some more time, until the
            darkness arrive and swallow you all little buggers!"""
            ))
            return "ruins"
        else:
            print(dedent("""
            That doesn't make any sense
            """))
            return "Shire"


class Rivendell(Scene):

    def enter(self):
        print("\nYou join the council in Rivendell, hosted by Elrond.")
        print("Elves, dwarves, humans, wizards here. And hobbits of course...")
        print("Somebody has to take the ring to Mount Doom.")
        print("Is it going to be you ?")

        print("no, destroy, yes? ")

        yes_man = False

        while True:
            choice = input("> ")

            if choice == "no":
                print("Go home, halfling, have a pleasant death.")
                return "ruins"
            elif choice == "destroy" and not yes_man:
                print("\nThe ring can only destroyed by the lava its forged in.")
                return "Rivendell"
            elif choice == "yes" and not yes_man:
                print("\nYou are the man! Way to go!!!")
                yes_man = True
                return "Journey"
            else:
                print("That doesn't make sense.")
                return "Rivendell"

class Journey(Scene):

    def enter(self):
        print("The fellowship of the ring has been founded.")

        for i in fellowship_of_the_ring:
            print(f"We have {i} ready for the Journey. ")
            print("2 men, 1 dwarf, 1 elf, 1 wizard and 4 hobbits.")
            print("And the story begins, road to Moria!")
            return "Moria"

class Moria(Scene):

    def enter(self):
        print("\nKhazad-Dum!!!")
        print("You unlock the moon door carved by half elves and half dwarves.")
        print("Halls of Moria welcomes you, gloomy.")
        print("...")
        print("You are on the bridge and Gandalf is the latter one.")
        print("Balrog grabs Gandalf by the foot.")
        print("Would you try to help Gandalf or run for your lives? ")
        print("stay, leave?")

        choice = input("> ")

        if choice == "stay":
            print("You fool! Balrog kills you all!!!")
            return "ruins"
        elif choice == "leave":
            print("\nGandalf fights Balrog.")
            print("What does he need to say in order to stop him? ")
            print("ysnp, fuckyou? ")
            choice = input("> ")

            if choice == "ysnp":
                print("\nGandalf saves you all, but ends himself.")
                return "Anduin"
            else:
                print("Balrog kills Gandalf first, and then eats you all. ")
                return "ruins"
        else:
            print("I don't know what that means. ")
            return "Moria"

class Anduin(Scene):

    def enter(self):
        print("You think about leaving the band and going to Mount Doom alone.")
        print("What will be your choice? ")
        print("leave, stay?")

        choice = input("> ")

        if choice == "leave":
            print("\nYou did the right thing Frodo!")
            return "MountDoom"
        elif choice == "stay":
            print("That wasn't a good idea, bye world!")
            return "ruins"
        else:
            print("I don't know what that means.")
            return "Anduin"


class MountDoom(Scene):

    def enter(self):
        print("You are on top of the moutain. ")
        print("Time to get rid of the ring, the precious...")
        print("What will you do? ")
        print("destroy, keep ")

        choice = input("> ")

        if choice == "destroy":
            print("I...I CAN'T DO IT!!!")
            print("WHY WOULD I DO IT???")
            print("IT'S MINE NOW! I OWN IT!!!")
            print("I WILL KEEP IT FOREVER!!!")
            return 'MountDoom'

        elif choice == "keep":
            print("OUCHHHH!!!")
            print("Gollum bites your finger off.")
            print("And down he falls to the cracks of Mount Doom. ")
            print("Middle-Earth is saved, Thanks Frodo(!) ")
            return 'Finished'

        else:
            print("I don't know what that means. ")
            return 'MountDoom'

class Finished(Scene):

    def enter(self):
        print("\nYou did it Frodo!")
        print("Into the West now...")

        #using another file (importing a file)
        txt = open(song)
        print(f"\nHere is your {song}: \n\t")
        print(txt.read())

        return 'finished'

class Map(object):

    # a dictionary
    scenes = {
        'Shire': Shire(),
        "ruins": Ruins(),
        'Rivendell': Rivendell(),
        'Anduin': Anduin(),
        'Finished': Finished(),
        'MountDoom': MountDoom(),
        'Moria': Moria(),
        "Journey": Journey(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Shire')
the_game = Engine(a_map)
the_game.play()
