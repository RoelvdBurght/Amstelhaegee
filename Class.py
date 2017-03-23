class House:
    x = 2

class SingleHouse(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.value = 285000

class Bungalow(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 7.5
        self.value = 399000

class Maison(House):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 11
        self.height = 10.5
        self.value = 610000

# Shape 1 is a square, shape 2 is a circle
class Water:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

def dist(point1, point2):
    height = point1[0] - point2[0]
    width = point1[1] - point2[1]
    return sqrt(height^2 + width^2)

def distanceBetween(h1, h2):
    if h2.x + h2.width < h1.x and h2.y + h2.height < h1.y:
        return dist([h2.x + h2.width, h2.y + h2.height], [h1.x, h1.y])
    elif h2.x > h1.x + h1.width and h2.y + h2.height < h1.y:
        return dist([h2.x, h2.y + h2.height],[h1.x + h1.width, h1.y])
    elif h2.x > h1.x + h1.width and h2.y > h1.y + h1.height:
        return dist([h2.x, h2.y], [h1.x + h1.width, h1.y + h1.height])
    elif h2.x + h2.width < h1.x and h2.y > h1.y + h1.height:
        return dist([h2.x + h2.width, h2.y], [h1.x, h1.y + h1.height])
    elif h2.x >= h1.x and h2.y + h2.width < h1.y:
        return h1.y - (h2.y + h2.height)
    elif h2.x >= h1.x:
        return h2.y -(h1.y + h1.height)
    elif h2.x + h2.width < h1.x:
        return h1.x - (h2.x + h2.height)
    else:
        return h2.x - (h1.x + h1.width)