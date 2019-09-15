import Account

class Request(object):
    def __init__(self, name, class, proficiency, times):
        self.name = name
        self.class = class
        self.proficiency = proficiency
        self.times = times

    def __str__(self):
        return "({0}, {1}, {2}, {3})".format(self.name, self.class, self.proficiency, self.times)

    def get_class(self):
        return self.class

    def get_proficiency(self):
        return self.proficiency

    def get_times(self):
        return self.times

    def times_match(self, other_times):
        for day, times in self.times.items():
            other_value = other_times[day]
            for time in times:
                if time in other_value:
                    return True
        return False

    def match(self, other):
        return self.class == other.get_class() && times_match(self, other.get_times()) and abs(self.proficiency - other.get_proficiency()) < 3
