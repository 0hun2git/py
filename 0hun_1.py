class yh:
    def __init__(self, id, pw, name, age):
        self.id = id
        self.name = name
        self.pw = pw
        self.age = age
    
    def signup(self):
        print("아이디: {0}\n패스워드: {1}\n이름: {2}\n나이: {3}".format(self.id, self.pw, self.name, self.age))

id = input("아이디를 입력하세요: ")
pw = input("패스워드를 입력하세요: ")
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
aaa= yh(id, pw, name, age)
aaa.signup()


# git init
# git config --global --add safe.directory D:/py
# git add 0hun_1.py
# git commit -m "update"
# git config --global user.email "0hun2git@gmail.com"
# git commit -m "update"
# git status
# git push origin