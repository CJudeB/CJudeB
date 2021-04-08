class Mcgyver:
    def __init__(self, name, doing, speed):
        self.name = name
        self.doing = doing
        self.speed = speed

    def Bright_Idea(self):
        print("\n" f"{self.name} was getting some awesome {self.doing} while driving at {self.speed}.")

    def Blame_Apple(self):
        print("\n" f"{self.name} is disappointed with Find my Phone service." "\n")


Darwin_Award = Mcgyver('Mcgyver', 'land scape photography', 110)
Darwin_Award.Bright_Idea()
Darwin_Award.Blame_Apple()


