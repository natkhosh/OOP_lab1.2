class Glass:
    count = 0
    def __init__(self, name):
        self.name = name
        cls = type(self)
        cls.count += 1

    def __del__(self):
        cls = type(self)
        cls.count -= 1

    @classmethod
    def print_count(cls):
        print(cls.count)

g1 = Glass(12)
g2 = Glass(22)
g3 = Glass(32)
Glass.print_count()
print(g1.count)
print(g2.count)
print(g3.count)