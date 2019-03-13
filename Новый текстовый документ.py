import random


class Person:
    def __init__(self, nm, hp, dmm, ar):
        self.nm = nm
        self.hp = hp
        self.dmm = dmm
        self.ar = ar
    def _Dm(self, dmm):
        if self.ar > 0:
            self.ar = self.ar - int(dmm*random.uniform(0.1, 1.0))
            if self.ar <= 0:
                self.ar = 0
        else:
            self.hp = self.hp - int(dmm*random.uniform(0.1, 1.0))
            if self.hp <= 0:
                self.hp = 0
        print("{} получил урон. {} здоровья и {} брони осталось".format(self.nm, self.hp, self.ar))
    def at(self, person):
        person._Dm(self.dmm)
class enm(Person):
    
    def __init__(self, nm, hp, dmm, ar):
        Person.__init__(self, nm, hp, dmm, ar)
class pl(Person):
        def __init__(self, nm, hp, dmm, ar):
            Person.__init__(self, nm, hp, dmm, ar)
class Fight:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def start(self, p1, p2):
        while p1.hp > 0 and p2.hp > 0:
            p1.at(p2)
            if p2.hp == 0:
                print("{} победил".format(p1.nm))
                break
            p2.at(p1)
            if p1.hp == 0:
                print("{} победил".format(p2.nm))
pl = pl("Дырик", 100, 33, 55)
enm = enm("НеДырик", 150, 11, 55)
nf = Fight(pl, enm)
nf.start(pl, enm)
input()