class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def representation(self):
        print(f"I'm a {self.name}, usually I eat {self.eat}. Amount I like to sleep {self.sleep}")


class Horse(Animal):
    def __init__(self, name, eat, sleep, run):
        super().__init__(name, eat, sleep)
        self.run = run

    def special_force(self):
        print(f'I can run faster than your car at speed {self.run} km/h looser!')


class Cow(Animal):
    def __init__(self, name, eat, sleep, gives_milk):
        super().__init__(name, eat, sleep)
        self.gives_milk = gives_milk

    def special_force(self):
        print(f'I give {self.gives_milk} liters of milk everyday. Just feed me')


class Cat(Animal):
    def __init__(self, name, eat, sleep, hunting):
        super().__init__(name, eat, sleep)
        self.hunting = hunting

    def special_force(self):
        print(f'Once I brought {self.hunting} to my human. He screamed... stupid')


class Dog(Animal):
    def __init__(self, name, eat, sleep, catching):
        super().__init__(name, eat, sleep)
        self.catching = catching

    def special_force(self):
        print(f'I can bring you anything, just though it please! Through that {self.catching} now :(')


class Mole(Animal):
    def __init__(self, name, eat, sleep, dig):
        super().__init__(name, eat, sleep)
        self.dig = dig

    def special_force(self):
        print(f'Yes, I can not see, but I bet you can not make {self.dig} holes in a day!')


bucephalus = Horse('Bucephalus', 'Oat', '2.9', '160')
bucephalus.representation()
bucephalus.special_force()
print(isinstance(bucephalus, Animal))

flower = Cow('Flower', 'Grass', '3.9', '10')
flower.representation()
flower.special_force()
print(isinstance(flower, Animal))

thomas = Cat('Thomas', 'Wiskas', '12', 'Mouse')
thomas.representation()
thomas.special_force()
print(isinstance(thomas, Animal))

spike = Dog('Spike', 'Pedigry', '11', 'stick')
spike.representation()
spike.special_force()
print(isinstance(spike, Animal))

krtek = Mole('Krtek', 'insects', '10', '100')
krtek.representation()
krtek.special_force()
print(isinstance(krtek, Animal))


# 1a

class Human:
    def __init__(self, eat, sleep, work, study, procrastinate):
        self.eat = eat
        self.sleep = sleep
        self.work = work
        self.study = study
        self.procrastinate = procrastinate

    def main_activity(self):
        print(
            f"My main is {self.work}, also I'm learning {self.study}, "
            f"but to be honest most of the time I'm doing {self.procrastinate}, "
            f"and just eating {self.eat} and sleeping {self.sleep} hours")


class Centaur(Animal, Human):
    def __init__(self, name, eat, sleep, work, study, procrastinate, skill):
        Animal.__init__(self, name, eat, sleep)
        Human.__init__(self, eat, sleep, work, study, procrastinate)
        self.skill = skill

    def centaur_story(self):
        print(f"My name is {self.name}, I eat what forest gives, mostly {self.eat}, "
              f"usually I don't sleep much around {self.sleep} hours."
              f"My main works is to {self.work} the forest. "
              f"Every night I'm {self.study} the stars. I love to {self.procrastinate} during the day"
              f"I'm a great {self.skill}, and no one can win with me around")


the_myth = Centaur('Galion', 'berries', '6', 'protect', 'watch', 'daydream', 'archer')
the_myth.centaur_story()
