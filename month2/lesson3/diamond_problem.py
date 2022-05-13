class A:
    def test(self):
        print('Its method test')


class B:
    def test(self):
        print('Its method test in class B')

    def test2(self):
        print('test2 in B')

class C(A):
    def test(self):
        print("Its method test in class C")

    def test2(self):
        print('test2 in C')

class D(B, C):
    def test2(self):
        print('test2 in D')
    pass


d1 = D()
d1.test()
print(D.mro())