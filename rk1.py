from operator import itemgetter

class Row:
    def __init__(self, id, content, size, table_id):
        self.id = id
        self.content = content
        self.size = size
        self.table_id = table_id


class Table:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class RowTable:
    def __init__(self, table_id, row_id):
        self.table_id = table_id
        self.row_id = row_id

tables = [
    Table(1, 'таблица пользователей'),
    Table(2, 'журнал заказов'),
    Table(3, 'сводная таблица продаж'),

    Table(11, 'таблица (архивная) пользователей'),
    Table(22, 'журнал (архивный) заказов'),
    Table(33, 'сводная (архивная) таблица продаж'),
]

rows = [
    Row(1, 'Иванов;ivanov@mail.ru', 128, 1),
    Row(2, 'Петров;petrov@mail.ru', 96, 1),
    Row(3, 'Заказ №1001;2500 руб.', 64, 2),
    Row(4, 'Январь;150000 руб.', 256, 3),
    Row(5, 'Февраль;175000 руб.', 192, 3),
]

rows_tables = [
    RowTable(1, 1),
    RowTable(1, 2),
    RowTable(2, 3),
    RowTable(3, 4),
    RowTable(3, 5),

    RowTable(11, 1),
    RowTable(11, 2),
    RowTable(22, 3),
    RowTable(33, 4),
    RowTable(33, 5),
]


def main():
    one_to_many = [(r.content, r.size, t.name)
        for t in tables
        for r in rows
        if r.table_id == t.id]

    many_to_many_temp = [(t.name, rt.table_id, rt.row_id)
        for t in tables
        for rt in rows_tables
        if t.id == rt.table_id]

    many_to_many = [(r.content, r.size, table_name)
        for table_name, table_id, row_id in many_to_many_temp
        for r in rows if r.id == row_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for t in tables:
        t_rows = list(filter(lambda i: i[2] == t.name, one_to_many))
        if len(t_rows) > 0:
            t_sizes = [size for _, size, _ in t_rows]
            t_sizes_sum = sum(t_sizes)
            res_12_unsorted.append((t.name, t_sizes_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    for t in tables:
        if 'таблица' in t.name:
            t_rows = list(filter(lambda i: i[2] == t.name, many_to_many))
            t_rows_contents = [x for x, _, _ in t_rows]
            res_13[t.name] = t_rows_contents

    print(res_13)


if __name__ == '__main__':
    main()
