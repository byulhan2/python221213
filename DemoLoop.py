# DemoLoop.py

value = 5
while value>0:
    print(value)
    value -= 1


lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i)

color={"apple":100, "kiwi":200, "banana":300}
for item in color.keys():
    print(item)

for item in color.values():
    print(item)



print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    #추가 탈출조건
    #다중 라인 주석 : ctr+/
    if i>5:
        break
    print(i)


print("---continue---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i%2==1:
        continue
    print(i)


print("---수열---")
print(list(range(10)))
print(list(range(2000,2023)))
print(list(range(1,101)))


print("----리스트 컴프리헨션----")
lst = list(range(1,11))
print([i**2 for i in lst if i>5])

tp=("apple", "kiwi", "banana")
print([len(i) for i in tp])

print("--- 필터링하는 경우---")
lst=[10,25,30]
iterL=filter(None,lst)
for item in iterL:
    print(item)

    