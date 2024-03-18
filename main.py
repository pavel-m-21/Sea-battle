#X - подбитые корабли, T — промахи
import random
import time
print("Приветствуем на игре морской бой!")
print()
class Board:

    computer_add = [
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
        [" - ", "  ", " C1", " C2", " C3", " C4", " C5", " C6", " ", " - "],
        [" - ", "X1", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X2", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X3", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X4", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X5", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X6", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]

    player_add = [
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
        [" - ", "  ", " C1", " C2", " C3", " C4", " C5", " C6", " ", " - "],
        [" - ", "X1", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X2", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X3", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X4", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X5", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", "X6", "| O", "| O", "| O", "| O", "| O", "| O", "|", " - ", " - "],
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "],
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]]

    def computer_table(self, x):
        print("Computer_Ships")
        print()
        for i in x[1:8]:
            for g in i[1:9]:
                print(g, end=" ")
            print()
        print()
        print("----------------------------")
        print()

    def player_table(self, x):
        print("Player_Ships")
        print()
        for i in x[1:8]:
            for g in i[1:9]:
                print(g, end=" ")
            print()
        print()

class Ship(Board):

    def __init__(self, q=0, g=0, c=0, z=0, f=0, j=0, r=0, t=0, o=0, s=0, p=0, w=0, v=0, l=0, h1=0, h2=0, h3=0, h4=0,
                 h5=0, h6=0, h7=0, h8=0):
        self.q = q
        self.g = g
        self.c = c
        self.z = z
        self.f = f
        self.j = j
        self.r = r
        self.t = t
        self.o = o
        self.s = s
        self.p = p
        self.w = w
        self.v = v
        self.l = l
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.h5 = h5
        self.h6 = h6
        self.h7 = h7
        self.h8 = h8
    def computer_board_ship_1(self):
        self.q = random.randint(2, 7)
        self.g = random.randint(2, 7)
        self.c = random.randint(0, 1)
        self.z = random.randint(0, 1)
        self.f = random.randint(0, 1)
        self.j = random.randint(0, 1)
        if self.c == 1:
            self.f = 1
            self.z = 0
            self.j = 0
        else:
            self.z = 1
            self.f = 0
            self.j = 1


        while True:
            if self.q + self.c + self.f <= 7 and self.g + self.z + self.j <= 7:
                Board.computer_add[self.q][self.g] = "| О"
                Board.computer_add[self.q + self.c][self.g + self.z] = Board.computer_add[self.q][self.g]
                Board.computer_add[self.q + self.c + self.f][self.g + self.z + self.j] = Board.computer_add[self.q][self.g]
                break
            else:
                self.q = random.randint(2, 7)
                self.g = random.randint(2, 7)
                self.c = random.randint(0, 1)
                self.z = random.randint(0, 1)
                self.f = random.randint(0, 1)
                self.j = random.randint(0, 1)
                if self.c == 1:
                    self.f = 1
                    self.z = 0
                    self.j = 0
                else:
                    self.z = 1
                    self.f = 0
                    self.j = 1

    def show_computer_ship_2(self, x, y, c, z):
        while True:
            if Board.computer_add[x][y] != Board.computer_add[self.q][self.g] and Board.computer_add[x + 1][y] != Board.computer_add[self.q][self.g] and \
                    Board.computer_add[x - 1][
                        y] != Board.computer_add[self.q][self.g] and Board.computer_add[x][y + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x][
                y - 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x + 1][y + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x - 1][
                y - 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x + 1][y - 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x - 1][
                y + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x + c][y + z] != Board.computer_add[self.q][self.g] and Board.computer_add[x + c + 1][
                y + z] != Board.computer_add[self.q][self.g] and \
                    Board.computer_add[x + c - 1][
                        y + z] != Board.computer_add[self.q][self.g] and Board.computer_add[x + c][z + y + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[x + c][
                y - 1 + z] != Board.computer_add[self.q][self.g] and Board.computer_add[x + c + 1][y + z + 1] != Board.computer_add[self.q][self.g] and \
                    Board.computer_add[x + c - 1][
                        y - 1 + z] != Board.computer_add[self.q][self.g] and Board.computer_add[x + 1 + c][y - 1 + z] != Board.computer_add[self.q][self.g] and \
                    Board.computer_add[c + x - 1][
                        y + 1 + z] != Board.computer_add[self.q][self.g]:
                if x + c <= 7 and y + z <= 7:
                    Board.computer_add[x][y] = Board.computer_add[self.q][self.g]
                    Board.computer_add[x + c][y + z] = Board.computer_add[self.q][self.g]
                    break
            else:
                x = random.randint(2, 7)
                y = random.randint(2, 7)
                c = random.randint(0, 1)
                z = random.randint(0, 1)

                if c == 1:
                    z = 0
                else:
                    z = 1

    def computer_board_ship_2(self):

        self.r = random.randint(2, 7)
        self.t = random.randint(2, 7)
        self.o = random.randint(0, 1)
        self.s = random.randint(0, 1)

        self.p = random.randint(2, 7)
        self.w = random.randint(2, 7)
        self.v = random.randint(0, 1)
        self.l = random.randint(0, 1)

        if self.o == 1:
            self.s = 0
        else:
            self.s = 1

        if self.v == 1:
            self.l = 0
        else:
            self.l = 1

        self.show_computer_ship_2(self.r, self.t, self.o, self.s)
        self.show_computer_ship_2(self.p, self.w, self.v, self.l)

    def show_computer_ship_3(self, d, a):
        while True:
            if Board.computer_add[d][a] != Board.computer_add[self.q][self.g] and Board.computer_add[d + 1][a] != Board.computer_add[self.q][self.g] and \
                    Board.computer_add[d - 1][
                        a] != Board.computer_add[self.q][self.g] and Board.computer_add[d][a + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[d][
                a - 1] != Board.computer_add[self.q][self.g] and Board.computer_add[d + 1][a + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[d + 1][
                a - 1] != Board.computer_add[self.q][self.g] and Board.computer_add[d - 1][a + 1] != Board.computer_add[self.q][self.g] and Board.computer_add[d - 1][
                a - 1] != Board.computer_add[self.q][self.g]:
                Board.computer_add[d][a] = Board.computer_add[self.q][self.g]
                break
            else:
                d = random.randint(2, 7)
                a = random.randint(2, 7)

    def computer_board_ship_3(self):

        self.h1 = random.randint(2, 7)
        self.h2 = random.randint(2, 7)
        self.h3 = random.randint(2, 7)
        self.h4 = random.randint(2, 7)
        self.h5 = random.randint(2, 7)
        self.h6 = random.randint(2, 7)
        self.h7 = random.randint(2, 7)
        self.h8 = random.randint(2, 7)

        self.show_computer_ship_3(self.h1, self.h2)
        self.show_computer_ship_3(self.h3, self.h4)
        self.show_computer_ship_3(self.h5, self.h6)
        self.show_computer_ship_3(self.h7, self.h8)

    def player_board_ship_1(self):
        x = random.randint(2, 7)
        y = random.randint(2, 7)
        c = random.randint(0, 1)
        z = random.randint(0, 1)
        f = random.randint(0, 1)
        j = random.randint(0, 1)
        if c == 1:
            f = 1
            z = 0
            j = 0
        else:
            z = 1
            f = 0
            j = 1

        if x + c + f <= 7 and y + z + j <= 7:
            Board.player_add[x][y] = "| ■"
            Board.player_add[x + c][y + z] = "| ■"
            Board.player_add[x + c + f][y + z + j] = "| ■"
        else:
            Board.player_add[x][y] = "| ■"
            Board.player_add[x - c][y - z] = "| ■"
            Board.player_add[x - c - f][y - z - j] = "| ■"

    def show_player_ship_2(self, x, y, c, z):
        while True:
            if Board.player_add[x][y] != "| ■" and Board.player_add[x + 1][y] != "| ■" and \
                    Board.player_add[x - 1][
                        y] != "| ■" and Board.player_add[x][y + 1] != "| ■" and Board.player_add[x][
                y - 1] != "| ■" and Board.player_add[x + 1][y + 1] != "| ■" and Board.player_add[x - 1][
                y - 1] != "| ■" and Board.player_add[x + 1][y - 1] != "| ■" and Board.player_add[x - 1][
                y + 1] != "| ■" and Board.player_add[x + c][y + z] != "| ■" and Board.player_add[x + c + 1][
                y + z] != "| ■" and \
                    Board.player_add[x + c - 1][
                        y + z] != "| ■" and Board.player_add[x + c][z + y + 1] != "| ■" and Board.player_add[x + c][
                y - 1 + z] != "| ■" and Board.player_add[x + c + 1][y + z + 1] != "| ■" and \
                    Board.player_add[x + c - 1][
                        y - 1 + z] != "| ■" and Board.player_add[x + 1 + c][y - 1 + z] != "| ■" and \
                    Board.player_add[c + x - 1][
                        y + 1 + z] != "| ■":
                if x + c <= 7 and y + z <= 7:
                    Board.player_add[x][y] = "| ■"
                    Board.player_add[x + c][y + z] = "| ■"
                    break
            else:
                x = random.randint(2, 7)
                y = random.randint(2, 7)
                c = random.randint(0, 1)
                z = random.randint(0, 1)

                if c == 1:
                    z = 0
                else:
                    z = 1


    def player_board_ship_2(self):
        x = random.randint(2, 7)
        y = random.randint(2, 7)
        c = random.randint(0, 1)
        z = random.randint(0, 1)

        p = random.randint(2, 7)
        w = random.randint(2, 7)
        v = random.randint(0, 1)
        l = random.randint(0, 1)

        if c == 1:
            z = 0
        else:
            z = 1

        if v == 1:
            l = 0
        else:
            l = 1

        self.show_player_ship_2(x, y, c, z)
        self.show_player_ship_2(p, w, v, l)

    def show_player_ship_3(self, x, y):
        while True:
            if Board.player_add[x][y] != "| ■" and Board.player_add[x + 1][y] != "| ■" and \
                    Board.player_add[x - 1][
                        y] != "| ■" and Board.player_add[x][y + 1] != "| ■" and Board.player_add[x][
                y - 1] != "| ■" and Board.player_add[x + 1][y + 1] != "| ■" and Board.player_add[x + 1][
                y - 1] != "| ■" and Board.player_add[x - 1][y + 1] != "| ■" and Board.player_add[x - 1][
                y - 1] != "| ■":
                Board.player_add[x][y] = "| ■"
                break
            else:
                x = random.randint(2, 7)
                y = random.randint(2, 7)


    def player_board_ship_3(self):

        x = random.randint(2, 7)
        y = random.randint(2, 7)
        c = random.randint(2, 7)
        z = random.randint(2, 7)
        f = random.randint(2, 7)
        j = random.randint(2, 7)
        p = random.randint(2, 7)
        n = random.randint(2, 7)

        self.show_player_ship_3(x, y)
        self.show_player_ship_3(c, z)
        self.show_player_ship_3(f, j)
        self.show_player_ship_3(p, n)

class Play(Ship):

    def computer_board(self):
        while True:
            x = int(input("Введите значение по 'X': "))
            c = int(input("Введите значение по 'C': "))
            if x > 6 or x < 1 or c > 6 or c < 1:
                print()
                print("Введите значение входящее в игровое поле")
                print()
            elif self.computer_add[x+1][c+1] == "| O":  #Тут "O" на английской раскладке
                self.computer_add[x+1][c+1] = "| T"
                print()
                print("У вас промах")
                print()
                self.player_table(self.player_add)
                self.computer_table(self.computer_add)
                break
            elif self.computer_add[x + 1][c + 1] == "| О":  #Тут "O" на русской раскладке
                self.computer_add[x + 1][c + 1] = "| X"
                if all([r != "| О" for h in Board.computer_add for r in h]):
                    print()
                    self.player_table(self.player_add)
                    self.computer_table(self.computer_add)
                    break
                print()
                print("Вы попали, сделайте еще ход")
                print()
                self.player_table(self.player_add)
                self.computer_table(self.computer_add)
                print()
            else:
                print()
                print("Клетка занята")
                print()
        print()

    def player_board(self):
        x = random.randint(2, 7)
        c = random.randint(2, 7)
        while True:
            if self.player_add[x][c] == "| O":
                self.player_add[x][c] = "| T"
                print(f"Ход компьютера 'X' - {x-1}, 'C' - {c-1} ")
                print("Компьютер промазал, ваш ход")
                print()
                self.player_table(self.player_add)
                self.computer_table(self.computer_add)
                break
            elif self.player_add[x][c] == "| ■":
                self.player_add[x][c] = "| X"
                print(f"Ход компьютера 'X' - {x-1}, 'C' - {c-1} ")
                if all([r != "| ■" for h in Board.player_add for r in h]):
                    print()
                    self.player_table(self.player_add)
                    self.computer_table(self.computer_add)
                    break
                print("Компьютер попал, еще ход")
                print()
                self.player_table(self.player_add)
                self.computer_table(self.computer_add)
                print()
                x = random.randint(2, 7)
                c = random.randint(2, 7)
            else:
                x = random.randint(2, 7)
                c = random.randint(2, 7)
        print()


a = Play()
a.computer_board_ship_1()
a.computer_board_ship_2()
a.computer_board_ship_3()
a.player_board_ship_1()
a.player_board_ship_2()
a.player_board_ship_3()
a.player_table(Board.player_add)
a.computer_table(Board.computer_add)

while True:
    a.computer_board()
    if all ([r != "| О" for h in Board.computer_add for r in h]):
        print("Поздравляю, вы победили!!!")
        break
    a.player_board()
    if all ([r != "| ■" for h in Board.player_add for r in h]):
        print("Компьютер победил!")
        break





