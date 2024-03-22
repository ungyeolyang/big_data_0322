# 파이썬에서는 연산자 오버로딩이 가능
# 각 연산자의 좌변과 우변에 어떤 객체가 오는지에 따라 다른 연산을 수행
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector2D(1,2)
v2 = Vector2D(2,3)
v3 = Vector2D(4,5)
v4 = v1 + v2 + v3
print(f"{v4.x},{v4.y}") # vetor2d의 +
print(100 + 200) # 기본적인 +