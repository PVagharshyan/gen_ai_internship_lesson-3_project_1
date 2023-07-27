import math

class Point2D:
    def __init__(self, x, y):
        self.x = x;
        self.y = y

    def __eq__(self, other):
        if not isinstance(self, other):
            raise TypeError("Type Error!!!!")
        return (
                self.x == other.x and
                self.y == other.y
                )
        
    def __hesh__(self):
        return math.sqrt(self.x**2 + self.y**2)

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(self, other):
            raise TypeError("Type Error!!!!")
        return (
                self.x == other.x and
                self.y == other.y and
                self.z == other.z
                )

    def __hesh__(self):
        return self.x**2 + self.y**2, self.z**2

class MetClass(type):
    def __new__(cls, name, bases, attrs):
        def __init__(self, *args):
            for i in args:
                if not (isinstance(i, float) or isinstance(i, int)):
                    raise ValueError('ordinates cannot contain any other value than numbers')
            self.vector = args
        
        def __eq__(self, other):
            if not type(self) == type(other):
                raise TypeError("Type Error!!!!")
            self_v = self.vector
            other_v = other.vector
            for i in range(len(self_v)):
                if not self_v[i] == other_v[i]: 
                    return False
            return True
        
        def __hash__(self):
            result = sum([i**2 for i in self.vector])
            return result

        def __str__(self):
            return f'{self.vector}'

        def __repr__(self):
            return f'class: {self.__class__.__name__}, vector:{self.vector}' 
        attrs.update({'__init__': __init__, '__eq__': __eq__, '__hash__': __hash__, '__str__': __str__, '__repr__':__repr__})
        return type.__new__(cls, name, bases, attrs)

class Point2D(metaclass=MetClass):
    pass

class Point3D(metaclass=MetClass):
    pass
