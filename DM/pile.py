class Pile:
    def __init__(self):
        self.elements = []

    def empiler(self, e):
        self.elements.append(e)

    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        else:
            return None

    def sommet(self):
        if not self.est_vide():
            return self.elements[-1]
        else:
            return None

    def est_vide(self):
        return len(self.elements) 