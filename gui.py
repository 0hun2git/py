# tkinter

from tkinter import *

# 윈도우
root = Tk()
root.title("0hun2")
root.geometry("640x720+100+300")
root.resizable(False,False)

# 버튼
btn1 = Button(root, text="Click")
btn1.pack()
btn2 = Button(root, padx=5, pady=10, text="Click")
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="Click")
btn3.pack()
btn4 = Button(root, width=10, height=3, text="Click")
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", text="Click")
btn5.pack()
photo = PhotoImage(file="image.png")
btn6 = Button(root, image=photo)
btn6.pack()
def btncmd():
    print("클릭")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

# 레이블
label1=Label(root,text="0hun2")
label1.pack()
label2=Label(root,image=photo)
label2.pack()
def change():
    label1.config(text="younghun")
    global photo2
    photo2=PhotoImage(file="image.png")
    label2.config(image=photo2)
btn7 = Button(root, text="클릭", command=change)
btn7.pack()

# 텍스트 박스(여러줄 입력), 엔트리(한줄 입력)
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END,"글자를 입력하세요.")

e = Entry(root, width=30) # Entry 한줄입력
e.pack()
e.insert(0, "한 줄만 입력해요.")

def btncmd2():
    print(txt.get("1.0",END)) # 1번재 라인 0번쨰 글자
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)
btn8 = Button(root, text="클릭", command=btncmd2)
btn8.pack()

# 리스트 박스
listbox = Listbox(root, selectmode="extended", height=0) # single 하나, extended 여러개, height=3(3개만)
listbox.insert(0,"사과")
listbox.insert(0,"딸기")
listbox.insert(0,"바나나")
listbox.insert(0,"수박")
listbox.insert(0,"포도")
listbox.pack()

def btncmd3():
    listbox.delete(0) # 삭제
    listbox.delete(END)
    print(listbox.size()) # 갯수
    print(listbox.get(0,2)) # 값
    print(listbox.curselection()) # 선택된 항목 위치로 반환

btn9 = Button(root, text="클릭", command=btncmd3)
btn9.pack()

root.mainloop()