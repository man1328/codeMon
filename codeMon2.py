"""
    Criteria for your Codémon. Your Codémon codes must include your unique trainer code.

Design your Codémon:
- What does your Code Monster look like?
- Where does it live? What does it eat?
- What skills does it have? What is it good at?
- What is it bad at? What is its weakness?
- How does it behave? Is it friendly, shy? Aggressive, calm?

Write a code to store your Codémon’s features. Consider including a brief description text for your monster. Choose
appropriate data types and data structures of your programming language. Add your monster’s data to it. - Beginner
suggestion: Define a set of variables to store the information. - Advanced suggestion: Define a class (or a set of
classes) to store the information. Add getter- and setter-methods (if applicable). If your chosen language favors a
different approach, go for it!

Improve your code by adding a function or method that displays the most important pieces of information.

Write some typical behaviors for your Codémon (functions/ methods). Suggestions: Does the monster make sounds? Does
it have special tricks or attacks it can perform? - Do the functions return data? Do they operate on the monster’s
properties? - Beginner: Show examples for the functions. - Advanced: Additionally write tests for your functions.

Add some more details on the typical behavior, the temperament, life, etc. of individuals of your type of monster.
Display it as Monster Wiki [aka codex] entry.

Draw your monster. - Draw it by hand, as ASCII-art, as pixel art, on a canvas, with or without the help of drawing
software or whatever you like. - Display the monster in a code.

Please respond below with how you'd prefer to receive your unique Trainer IDs! It may take up to 3 days to receive
your ID, so please reach out right away if you haven't received yours after that time. When your code is complete --
you can add it here: https://www.sololearn.com/Discuss/3236512/official-event-codmon-wiki-post-your-codmon-codes-here

"""


class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f"My name is {self.name}, I'm {self.age} years old, with a {self.color} coat."

    def speak(self):
        print("Bow Wow")

    def live(self):
        print("I live in the fourth dimension.  I come to the earth dimension when I need to eat, help my friends or "
              "get away from my reality.")

    def eat(self):
        print("I love eating anything that falls off of the humans plates.  I specially love eating the treats that "
              "have fallen from my buddy's birdo cage.")

    def weakness(self):
        x = ["Water", "Swimming", "Running"]
        print(f"WEAKNESS: {x}")

    def skills(self):
        x = ["Licks your fear away", "Farts paralyze anyone with in five feet", "Puppy dog eyes allow him to get away "
                                                                                "with anything"]
        print(f"SKILLS: {x}")

    def image(self):
        dog = r''' 
          ,_____ ,
          ,._ ,_. 7\
         j `-'     /
         |o_, o    \
        .`_y_`-,'   !
        |/   `, `._ `-,
        |_     \   _.'*\
          >--,-'`-'*_*'``---.
          |\_* _*'-'         '
         /    `               \
         \.         _ .       /
          '`._     /   )     /
           \  |`-,-|  /c-'7 /
            ) \ (_,| |   / (_
           ((_/   ((_;)  \_)))'''
        print(dog)

    def likes(self):
        x = ["I love sleeping in front of closed doors and not moving when someone is trying to get in or "
             "out of the door......jejeje", "Licking away my friends and families issues",  "Long sunbathing sessions "
             "in the backyard on warm sunny days", "Eating all the tomatoes from the plants in the backyard"]
        print(f"LIKES: {x}")

    def codeMonDex(self):
        # import module
        import webbrowser

        # open html file
        webbrowser.open('codeMonDex/index.html')


Thor = Dog("Thor", "Red & White", 6)
print(Thor)
Thor.speak()
Thor.eat()
Thor.live()
Thor.image()
Thor.weakness()
Thor.skills()
Thor.likes()
Thor.codeMonDex()
