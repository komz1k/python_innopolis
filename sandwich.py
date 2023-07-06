class Ingridient:
    def __init__(self, calories: float, mass: float):
        print("Вызывается метод __init__ у Ingridient")
        self._mass = mass
        self._calories = calories

    def prepare(self) -> float:
        """Подготавливает еду к употреблению"""
        return self._calories

    def get_calories(self) -> float:
        """Возвращает калории"""
        return self._calories

    def get_mass(self) -> float:
        """Возвращает массу"""
        return self._mass


class Bread(Ingridient):
    def prepare(self) -> float:
        self._calories += 10
        self._mass += 0.8
        return super().prepare()


class Tomato(Ingridient):
    def __init__(self, calories: float, mass: float, color: str):
        print("Вызывается метод __init__ у Tomato")
        self._color = color
        super().__init__(calories, mass)

    def prepare(self) -> float:
        self._mass += 0.8
        return super().prepare()


class Soup(Ingridient):
    def __init__(self, calories: float, mass: float, salinity: float):
        print("Вызывается метод __init__ у Soup")
        self._salinity = salinity
        super().__init__(calories, mass)


def cook(ings: list[Ingridient]):
    for ing in ings:
        print(type(ing))
        print(ing.prepare())
        print(ing.get_mass())


def main():
    bread = Bread(100, 50)
    soup = Soup(200, 100, 0.5)
    tomato = Tomato(100, 100, "RED")

    cook([bread, soup, tomato])


if __name__ == '__main__':
    main()
