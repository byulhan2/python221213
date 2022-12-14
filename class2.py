# class1.py


class person:
        #클래스 멤버 변수(일종의 공통 데이터로 사용)
        num_person=0
        #초기화 메서드
        def __init__(self):
            self.name="default name"
            person.num_person += 1
        #인스턴스 메서드
        def print(self):
            print("my name is {0}".format(self.name))


#인스턴스 생성
p1 = person()
p2 = person()
p1.name = "전우치"
print("인스턴스 갯수:{0}".format(person.num_person))

#런타임시에 추가
person.title ="new title"
print(p1.title)
print(p2.title)
print(person.title)