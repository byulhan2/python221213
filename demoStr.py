#demoStr.py

#print(dir(str()))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",7))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())
print("demo.ppt".startswith("ppt"))
print("demo.ppt".endswith("ppt"))

print("----공백문자 제거---")
u="<<< spam and ham >>>"
result = u.strip("<> ")
print(u)
print(result)

result = result.replace("spam", "spam egg")
print(result)

lst = result.split()
print(lst)
print("----다시합치기---")
print(" ".join(lst))

#반복적인 문구를 만드는 경우
names = ["전우치", "이순신", "박문수"]
for name in names:
    print("안녕하세요 {0} 입니다.".format(name))
    print("="*40)

