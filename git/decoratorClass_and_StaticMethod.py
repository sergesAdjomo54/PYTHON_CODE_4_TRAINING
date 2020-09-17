from typing import Any


class Student:
    school = 'ING_ODT'  # variable de classe

    def __init__(self, m1, m2, m3):
        self.m1 = m1  # variable d'instance
        self.m2 = m2  # variable d'instance
        self.m3 = m3  # variable d'instance

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def avg(self):  # methode d'instance car on utilise le mot clef {self}
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getScholl(cls):  # methode de classe on utilise le mot clef {cls}
        return cls.school

    @staticmethod  # methode Static en utilise aucun mot clef
    def info():
        print("This is a static method...")


s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(Student.getScholl())

# La fonction info demande un param  car il n'ya pas de lien avec la classe
# pour resoudre le probleme on insere un {decorator} au nivau de la classe info


# 693467167
