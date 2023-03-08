class Superhero:
    people = "people"

    def __init__(self ,name,nickname,superpower,health_points,catchphrase ):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return self.name

    def hpx2(self):
        return self.health_points * self.health_points

    def __str__(self):
        return f'его прозвище {self.nickname} , его суперспособность {self.superpower} , eго здровье {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


hero = Superhero("BATMAN", "летучая мышь", "технологии" , 100 , "на страже города !!!")

print(hero.names())
print(hero.hpx2())
print(hero.__str__())
print(hero.__len__())








