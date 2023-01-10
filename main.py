# This is a sample Python script.
import math


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Roots:

    def Discriminant(self, a, b, c):
        Disc = b * b - 4 * a * c
        return Disc

    def Oneroot(self, a, b):
        root1 = -b / (2 * a)
        return root1

    def Tworoots(self, a, b, D):
        root1 = (-b + math.sqrt(D) / (2 * a)
        root2 = (-b - math.sqrt(D) / (2 * a)
        return sorted([root1, root2])
