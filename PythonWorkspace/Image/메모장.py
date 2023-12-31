from tkinter import *
import datetime
import tkinter.messagebox as msbox

date = datetime.date.today()

win = Tk()
win.title("호노의_Memo")
win.geometry("600x370")

filename = str(date) + '.txt'

#함수 정의
def saveFile():
    file = open(filename, "w")
    ts = str(list_file.get(0, END))
    file.write(ts)
    file.close
    msbox.showinfo("알림", "정상적으로 저장되었습니다.")

def addList():
    index = txt.get("1.0", END)
    if index == '':
        return
    list_file.insert(END, txt.get("1.0", END))
    txt.delete("1.0", END)

def deleteList():
    index = list_file.curselection()
    list_file.delete(index)

# 제목 프레임
title_frame = Frame(win)
title_frame.pack()

date_text = Label(title_frame, text = date)
date_text.pack()

button_save = Button(title_frame, padx=5, pady=5, width=12, text="저장", command=saveFile)
button_save.pack(fill="both")

#리스트 프레임
list_frame = Frame(win)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 파일 프레임
file_frame = Frame(win)
file_frame.pack(padx=5,pady=5)

txt = Text(file_frame, width=50, heigh=3)
txt.pack(side="left", expand=True)
txt.insert(END, "내용을 입력하세요")

button_add = Button(file_frame, padx=5, pady=5, width=12, text="추가", command=addList)
button_add.pack(side="left")

button_del = Button(file_frame, padx=5, pady=5, width=12, text="삭제", command=deleteList)
button_del.pack(side="left")

win.mainloop()