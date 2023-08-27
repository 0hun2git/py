# jumin = "820113-1234567"
# print(jumin[:])

# python = "Python is Amazing"
# print(python.lower()) # 소문자로
# print(python.upper()) # 대문자로
# print(python[0].isupper()) # 대문자인지? 참 거짓
# print(len(python)) # 문자 갯수
# print(python.replace("Python", "Java")) # 문자 수정
# index = python.index("n") # 문장에서 첫 번째 'n' 문자의 위치
# print(index)
# index = python.index("n", index + 1) # 문장에서 두 번째 'n' 문자의 위치
# print(index)

# a = ["a","b","c","d","e","f","g"]
# print(a.index("a"))
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())
# print(a.pop())

# a = {"a":"0hun2", 1:"0hun2"}
# print(a["a"])
# a["hello"] = "0hun2"
# a.update({4:"0hun2"})
# a.update({5:"0hun2"})
# print(a.values())
# print(a.get("a"))
# print(a.get(1))
# print(a.get(2))
# print(1 in a)
# print(a.keys())
# print(a.values())
# print(a.items())
# print(a.clear())
# a={}
# a["name"]="younghunkim" # 쓰기
# print(a["name"]) # 읽기
# a["name"]="younghunlee" # 덮어쓰기
# print(a["name"]) # 읽기
# del a["name"] # 지우기
# a.update({"age":20})
# print(a.get("age"))
# a.clear()
# print(a)

# a = (name, age, hobby) = ("0hun2", 20, "코딩")
# print(a[0])
# print(a[1])
# print(a[2])
# print(a)
# print(name)
# print(age)
# print(hobby)
# a={"a","a","b"}
# print(a)
# a=set(["a","b"])
# a.add("c")
# a.add("d")
# a.add("e")
# print(a)
# a=[]
# a.append("a")
# print(a)
# a.remove("a")
# print(a)
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account() # 호출
