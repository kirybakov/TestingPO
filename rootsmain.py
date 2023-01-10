class Roots:

    def Discriminant(self, a, b, c):
        Disc = b * b - 4 * a * c
        return Disc

    def Oneroot(self, a, b):
        root1 = -b / (2 * a)
        return root1

    def Tworoots(self, a, b, Disc):
        root1 = (-b + Disc ** 0.5) / (2 * a)
        root2 = (-b - Disc ** 0.5) / (2 * a)
        return sorted([root1, root2]) 
