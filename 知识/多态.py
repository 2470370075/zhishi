
class Bird():
    def fly(self):
        print('bird fly')

class Plane():
    def fly(self):
        print('plane fly')

b = Bird()
p = Plane()

def func(obj):
    obj.fly()

func(b)
func(p)