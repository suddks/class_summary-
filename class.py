# 클래스 정의
class Person:
    #속성(변수)
    blood_color = 'red'

    #메서드
    def __init__(self, name):
        #개발자가 직접 호출 안함 , initialize 
        self.name = name

    def singing(self):
        return f'{self.name}가 노래합니다. '
    
#인스턴스 생성
singer1 = Person('iu')

print(singer1.singing())

