class A:
    def func(self):
        return 'A.func'


class B:
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'


class D(B, C):
    pass

