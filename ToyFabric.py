class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    @staticmethod
    def create(input_name, input_color, input_toy_type):
        new_toy = Toy(input_name, input_color, input_toy_type)
        print('Создаем игрушку\n')
        new_toy._purchasing()
        new_toy._stitching()
        new_toy._painting()
        print('\nИгрушка создана')
        return new_toy

    def _purchasing(self):
        print('Где мои деньги? Купил сырье для {}'.format(self.name.title()))

    def _stitching(self):
        print('Сшиваю {}'.format(self.name.title()))

    def _painting(self):
        print('Крашу {} в {} цвет'.format(self.name.title(), self.color))

    def test(self):
        print('Это я, {}'.format(self.name.title()))


sledge_mini = Toy.create('Sledge', 'Черный', 'Оператор')
sledge_mini.test()
input()