import Account

class Request(object):
    def __init__(self, name, course, proficiency, times):
        self.name = name
        self.course = course
        self.proficiency = proficiency
        self.times = times

    def __str__(self):
        return "( {0}, {1}, {2}, {3} )".format(self.name, self.course, self.proficiency, self.str_time())

    def __repr__(self):
        return self.__str__()

    def str_time(self):
        times = self.times
        mon = "|".join(times["Monday"])
        tue = "|".join(times["Tuesday"])
        wed = "|".join(times["Wednesday"])
        thu = "|".join(times["Thursday"])
        fri = "|".join(times["Friday"])
        sat = "|".join(times["Saturday"])
        sun = "|".join(times["Sunday"])
        return "M{0};T{1};W{2};TH{3};F{4};SA{5};SU{6}".format(mon, tue, wed, thu, fri, sat, sun)

    def get_course(self):
        return self.course

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
        return self.course == other.get_course() and self.times_match(other.get_times()) and abs(self.proficiency - other.get_proficiency()) < 3
