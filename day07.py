class PrettyMixin:
    def time_print(self):
        import datetime
        print(datetime.date.today())

    def dump(self):
        import pprint
        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.time_print()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.gender = "female"
t.gender = "male"
t.dump()