# function2.py

print("---불변형식---")


print("---가변형식---")
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

print("---이름을 해석하는 순서---")
# 함수정의(LGB)
def func1(a):
    x=1
    return x+a

#호출
print(func1(1))

#함수정의
x=5
def func2(a):
    return x+a

print(func2(1))
