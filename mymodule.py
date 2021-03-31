class A:
    arg = 'python'

    def hello(self):
        return "Hello world"

    def __privat(self):
        return "this is a privat function"


class B(A):
    def __init__(self, name):
        self.name = name

    def hello(self):
        return "Hello world, it's {}".format(self.name)


class MyDict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)

