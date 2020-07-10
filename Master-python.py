class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

p1 = Polynomial(1, 2, 3) # x2 + 2x +3
p2 = Polynomial(3, 4, 3) # 3x2 +4x +3

def showLove(*tup):
    print(type(tup))
    print(*tup)
    for bitch in tup:
        for each in bitch:
            print(each)

bitches = ("Anie","Mary","Drizel")
showLove(bitches)
