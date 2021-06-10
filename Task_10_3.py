class Cell:
    def __init__(self, cells_amount):
        self.cells_amount = int(cells_amount)

    def __add__(self, other):
        self.cells_amount += other.cells_amount
        # return Cell(self.cells_amount + other.cells_amount)
        return self

    def __sub__(self, other):
        resulting_cells_amount = self.cells_amount - other.cells_amount
        if resulting_cells_amount > 0:
            return Cell(resulting_cells_amount)
        else:
            return "Новых клеток слишком много"

    def __mul__(self, other):
        return Cell(self.cells_amount * other.cells_amount)

    def __floordiv__(self, other):
        return Cell(self.cells_amount // other.cells_amount)

    def __str__(self):
        return f'{self.cells_amount} cells long'

    def make_order(self, amount_of_cells_in_row):
        rows_amount, add_to_last_row = \
            divmod(self.cells_amount, amount_of_cells_in_row)
        cell_as_string = ''
        for _ in range(rows_amount):
            cell_as_string += f'{"*" * amount_of_cells_in_row}\n'

        return cell_as_string.rstrip() + '*' * add_to_last_row


if __name__ == '__main__':
    c1 = Cell(46)
    c2 = Cell(20)

    c_add = c1 + c2

    print(c_add)
    print(c_add.make_order(12))


