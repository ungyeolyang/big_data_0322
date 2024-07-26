# 정적메서드 : 클래스와 관련이 있어 클래스 안에 두기는 하지만 클래스, 인스턴스와는 무관
class Car:
    is_instance_cnt = 0 #클래스 안에 넣으면 static
    def __init__(self,size,model):
        self.speed = None # 생성자에 일단 만들어 놓아야함
        self.size = size
        self.model = model
        Car.is_instance_cnt += 1
        print(f"자동차 생산 대수 : {Car.is_instance_cnt}")
    def move(self,speed):
        self.speed = speed
        print(f"자동차 {self.size}&{self.model}가 시속 {self.speed}로 달립니다.")
    @staticmethod
    def check_type(code):
        if code >= 10: print("전기차 입니다.")
        elif code >= 20: print("가솔린차 입니다.")
        elif code >= 30: print("디젤차 입니다.")
        else : print("분류 코드가 없습니다.")

morning = Car("소형","모닝")
sonata = Car("중형","소나타")
morning.move(100)
sonata.move(120)
Car.check_type(20)


