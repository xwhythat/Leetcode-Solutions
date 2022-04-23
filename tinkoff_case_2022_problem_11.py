class Standings:
    def __init__(self, number_of_teams):
        self.num = number_of_teams
        self.table = [[None for i in range(self.num)] for i in range(self.num)]

    def show(self):
        """
        Вывод всей таблицы
        """
        return self.table

    def get_result(self, i, j):
        """
        Получить количество очков, полученных i-й командой в игре с j-й командой
        """
        if self.table[i][j] is None:
            return "Команды не играли между собой"
        else:
            return self.table[i][j]

    def put_result(self, i, j, result):
        """
        Запись результата игры i-й и j-й команды.
        Запись в поле self.table[i][j] автоматически вносит тот же результат в поле self.table[j][i]
        """
        if not result in (0, 1, 3):
            return "Некорректный результат"
        else:
            if self.table[i][j] is None:
                if result == 3:
                    self.table[i][j] = 3
                    self.table[j][i] = 0
                elif result == 0:
                    self.table[i][j] = 0
                    self.table[j][i] = 3
                else:
                    self.table[i][j] = self.table[j][i] = 1

    def fill_team(self, n, results):
        """
        results - массив результатов n-й команды со всеми остальными командами
        """
        m = 0
        for i in range(self.num):
            if i != n:
                self.put_result(n, i, results[m])
                m += 1

    def score(self, team):
        sum = 0
        for i in range(len(team)):
            if team[i] is not None:
                sum += team[i]

        return sum


# def filling(standings, i, j, tables=[]):
#     if i == 5:
#         tables.append(standings.table)
#         return
#
#
#
#     for value in (0, 1, 3):
#         if i != j and standings.table[i][j] is None:
#             standings.put_result(i, j, value)
#         if j + 1 < len(standings.table):
#             filling(standings, i, j + 1, tables)
#         elif j + 1 == len(standings.table) and standings.score(standings.table[i]) == 6:
#             filling(standings, i + 1, 0, tables)
#         else:
#             standings.table[i] = [None for n in range(6)]
#             j = 0


def array_copy(arr):
    result = []
    for i in range(len(arr)):
        result.append(arr[i].copy())

    return result


def filling(standings, i, j, tables=[]):
    if i == 5:
        tables.append(standings.table.copy())
        return

    if standings.score(standings.table[i]) > 6:
        return

    if standings.score(standings.table[i]) != 6 and j == standings.num:
        return

    if j == standings.num and standings.score(standings.table[i]) == 6:
        filling(standings, i + 1, 0, tables)
        return

    if standings.table[i][j] is not None:
        filling(standings, i, j + 1, tables)
        return

    if i == j:
        filling(standings, i, j + 1, tables)
        return

    for value in (0, 1, 3):
        copy_table = array_copy(standings.table)
        standings.put_result(i, j, value)
        filling(standings, i, j + 1, tables)
        standings.table = copy_table





My_Standings = Standings(6)
tables = []
print(filling(My_Standings, 0, 0, tables))

def result(line):
    result = 0
    for i in range(len(line)):
        if line[i] is not None:
            result += line[i]

    return result

def show_table(tables):
    for i in range(len(table)):
        print(table[i])
    print("\n")




sums = {-1}
for table in tables:
    sums.add(sum(table[5][:-1]))

print(sums)

for table in tables:
    if result(table[5]) in sums:
        print("Кол-во очков равно {}:".format(result(table[5])))
        show_table(table)

        sums.remove(result(table[5]))