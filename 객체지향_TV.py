# 파이썬 객체지향 특징
# 1.다중상속 지원
# 2.캡슐화||접근지원자 제대로 지원 안함
# 3.오버라이딩은 지원하나 오버로딩은 지원 안함(데이터 타입이 존재 안함, 디폴트매개변수 존재)
# 4.생성자 키워드 __init__
# 5. 기본생성자가 없음 인스턴스 필드는 생성자 내에 존재
# 6. 자신의 객체를 가리키는 포인터는 생성자||메소드 첫번째 인자로 존재(관례상 self로 사용)
class TV:
    def __init__(self,name,is_on,channel,volume): #def 함수만들기
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, cnl):
        self.channel = cnl
    def set_volume(self,vol):
        self.volume = vol
    def get_on(self):
        return self.is_on
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume
    def view_tv(self):
        power = "OFF", "ON"
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")
lg_tv = TV("LG",False,10,30) #bool 값을 바로 인덱스로 사용 가능
sam_tv = TV("삼성",True,20,70)
lg_tv.view_tv()
sam_tv.view_tv()