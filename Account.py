class Account(object):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year
