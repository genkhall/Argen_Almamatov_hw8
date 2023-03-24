import random
from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    SAVE_AND_DIE = 5
    STUN_BOSS = 6
    ACCEPT_DAMAGE = 7
    PRETEND_DIE = 8
    INCREASE_DAMAGE = 9
    MAGIC_FUNCTIONS = 10


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value >= 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = random.choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        if isinstance(ability, SuperAbility):
            self.__ability = ability
        else:
            raise ValueError('Wrong data type for ability')

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = random.randint(2, 5)  # 2,3,4,5
        boss.health -= self.damage * coefficient
        print(f'Warrior hits critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):

        boost_point = random.randint(5, 11)
        print(f"Boost: {boost_point}")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost_point


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes):
        pass


class Witcher(Hero):
    def __init__(self, name, health, damage=0):
        super().__init__(name, health, damage, SuperAbility.SAVE_AND_DIE)

    def apply_super_power(self, boss, heroes):

        for hero in heroes:
            if hero.health <= 0 and boss.health > 0:
                hero.health += self.health
                self.health = 0
                print(f'{self.name} to {hero.name}')


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUN_BOSS)

    def apply_super_power(self, boss, heroes):
        stun = [1, 2, 3]
        b = random.choice(stun)
        if b == 1:
            boss.damage = 0
            print("Stun Boss!!!")
        else:
            boss.damage = 50


class Golem(Hero):
    def __init__(self, name, health, damage, protection=0):
        super().__init__(name, health, damage, SuperAbility.ACCEPT_DAMAGE)

        self.__protection = protection


def apply_super_power(self, boss, heroes):
    for hero in heroes:
        if hero.health > 0:

            self.__protection = boss.damage // 5
            if boss.damage >= 1:
                hero.health = self.health + self.__protection
        else:
            hero.health -= boss.damage


class Tricky(Hero):
    def __init__(self, name, health, damage, ):
        super().__init__(name, health, damage, SuperAbility.PRETEND_DIE)

    def apply_super_power(self, boss, heroes):
        die_round = random.randint(1, 10)
        if die_round == 2:
            took_health = self.health
            self.health = 0
            if self.health == 0:
                self.damage = 0
                boss.damage = 0
            self.health += took_health


class Reaper(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.INCREASE_DAMAGE)

    def apply_super_power(self, boss, heroes):

        if self.health < 0.3 * self.health and boss.health > 0:
            return self.damage * 2
        elif self.health < 0.15 * self.health and boss.health > 0:
            return self.damage * 3


# class Hacker(Hero):
#     def __init__(self, name, health, damage):
#         super().__init__(name, health, damage, SuperAbility.HACK_HEALTH)
#
#     def apply_super_power(self, boss, heroes):
#         for hero in heroes:
#             if hero.health >= 0 and boss.health > 0:


class AntMan(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.MAGIC_FUNCTIONS)

    def apply_super_power(self, boss, heroes):
    #
    #  rounds = [1, 2, 3, 4, 5, 6]
    #    c= random.choice(rounds)
    #   increasing_point = randint(5, 100)
    #
    #
    # if c == 1 or 3 or 5:
    #     self.health += increasing_point
    #     self.damage += increasing_point


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('Boss won!!!')

    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if boss.defence != hero.ability and hero.health > 0:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start():
    boss = Boss('Rashan', 1000, 50)

    warrior = Warrior('Ahiles', 280, 10)
    doc = Medic('Estes', 250, 5, 15)
    magic = Magic('Merlin', 270, 15)
    berserk = Berserk('Thamus', 260, 10)
    assistant = Medic('Aibolit', 290, 5, 5)
    thor = Thor("Hulk", 300, 10)
    tricky = Tricky("Jimmey", 250, 10)
    golem = Golem("Sadam", 280, 5)
    witcher = Witcher("Dove", 300, 5)
    reaper = Reaper("Jnets", 50, 10)

    heroes_list = [warrior, doc, magic, berserk, assistant, thor, tricky, golem, witcher, reaper]

    show_statistics(boss, heroes_list)

    while not is_game_finished(boss, heroes_list):
        play_round(boss, heroes_list)


start()
