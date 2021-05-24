class Bmi:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def getBmi(self):
        return self.weight / self.height ** 2 * 10000


if __name__ ==