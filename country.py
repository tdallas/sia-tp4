class Country():
    def __init__(self, name, area, gdp, inflation, life_expect, military, pop_growth, unemployement):
        self.name = name
        self.area = area
        self.gdp = gdp
        self.inflation = inflation
        self.life_expect = life_expect
        self.military = military
        self.pop_growth = pop_growth
        self.unemployement = unemployement

    def get_name(self):
        return self.name

    def get_area(self):
        return self.area

    def get_gdp(self):
        return self.gdp

    def get_inflation(self):
        return self.inflation

    def get_life_expect(self):
        return self.life_expect

    def get_military(self):
        return self.military

    def get_pop_growth(self):
        return self.pop_growth

    def get_unemployement(self):
        return self.unemployement