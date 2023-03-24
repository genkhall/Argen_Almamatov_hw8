from decouple import config
import random





def casino():
    money = config("MY_MONEY", cast=int)
    while True:
        slot_of_win = random.randint(1, 31)
        choose_slot = int(input("Choose one number : "))
        put_money = int(input("сколько поставить : "))

        if choose_slot > 30:
            print("Недопустимое значение")
        if put_money > money:
            print("Недостаточно средств")

        if choose_slot == slot_of_win:
            money += put_money * 2
        else:
            money -= put_money
        print(f'slot of win {slot_of_win}')

        want_play = input("Хотите еще сыграть? y/n")
        if want_play == "y":
            print(f"your money : {money} ")
            continue
        if want_play == "n":
            print(f"your money :{money}")
            break


if __name__ == "__main__":
    casino()
