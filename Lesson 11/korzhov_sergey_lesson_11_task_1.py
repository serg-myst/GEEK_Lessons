class Date:

    def __init__(self, param):
        self.param = param

    @classmethod
    def get_date_param(cls, param):
        date_list = param.split('-')
        date, month, year = date_list[0], date_list[1], date_list[2]
        cls.valid_date(month, 'm')
        cls.valid_date(year, 'y')
        return int(date), int(month), int(year)

    @staticmethod
    def valid_date(value, typo):
        if typo == 'y':
            if len(value) < 4 or int(value) < 2000:
                raise ValueError('Год должен быть в формате yyyy и больше 2000')
        if typo == 'm':
            if int(value) <= 0 or int(value) > 12:
                raise ValueError('Месяц должен быть в пределах 1 - 12')


d, m, y = Date.get_date_param('27-04-2021')
print(d, m, y)