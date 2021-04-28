# inFp, outFp = None, None

# inStr = ""

# inFp = open("C:/Users/ysokr/Desktop/ICT/data2.txt", "r", encoding="utf-8")

# outFp = open("C:/Users/ysokr/Desktop/ICT/data2_copy.txt",

#              "w", encoding="utf-8")

# while True:

#     outStr = inFp.readlines()

#     if outStr != "":

#         outFp.write(outStr)

#     else:
#         break

# inFp.close()

# outFp.close()

# print("----정상적으로 파일이 복사되었음---")



# 다른 방법으로 복붙 1

# inFp, outFp = None, None

# inStr = ""

# inFp = open("C:/Users/ysokr/Desktop/ICT/data2.txt", "r", encoding="utf-8")

# outFp = open("C:/Users/ysokr/Desktop/ICT/data2_copy1.txt",

#              "w", encoding="utf-8")

# inList = inFp.readlines()

# for inStr in inList:

#     outFp.writelines(inStr)

# inFp.close()

# outFp.close()

# print("----정상적으로 파일이 복사되었음 --- ")


# 다른 방법으로 복붙2

# inFp, outFp = None, None

# inStr = ""

# inFp = open("C:/Users/ysokr/Desktop/ICT/data2.txt", "r", encoding="utf-8")

# outFp = open("C:/Users/ysokr/Desktop/ICT/data2_copy2.txt",

#              "w", encoding="utf-8")

# inList = inFp.readlines()

# outFp.writelines(inList)

# inFp.close()

# outFp.close()

# print("----정상적으로 파일이 복사되었음 --- ")


# tkinter 기본코드

# import tkinter as tk

# root = tk.Tk()


# lbl = tk.Label(root, text="EduCoding", underline=3)
# lbl.pack()


# txt = tk.Entry(root)

# txt.pack()


# btn = tk.Button(root, text="OK", activebackground="red", width=5)
# btn.pack()


# root.mainloop()


# 텍스트 출력 위젯

# import tkinter as tk

# root = tk.Tk()

# label = tk.Label(root, text='Hello World')
# label.pack()

# root.mainloop()


# 버튼배우기

# import tkinter as tk

# root = tk.Tk()



# def func():

#     print('pushed')



# button = tk.Button(root, text='Push!', command=func)
# button.pack()

# root.mainloop()


# 버튼만들기


# import tkinter as tk

# root = tk.Tk()



# def func():

#     label.config(text='pushed')



# label = tk.Label(root, text='push Button')
# label.pack()


# button = tk.Button(root, text='Push!', command=func)
# button.pack()

# root.mainloop()


# 버튼 누르면 텍스트가번갈아가면서 출력되게

# import tkinter as tk

# root = tk.Tk()


# s = False



# def func():

#     global s

#     if s:

#         label.config(text='orange')

#         s = False

#     else:

#         label.config(text='apple')

#         s = True



# label = tk.Label(root, text='push Button')
# label.pack()


# button = tk.Button(root, text='Push!', command=func)
# button.pack()

# root.mainloop()


# 버튼이 떠나면 다시 바뀌는

# import tkinter as tk

# root = tk.Tk()



# def func():

#     label.config(text='Pushed')



# def func_event(ev):

#     label.config(text='push Button')



# label = tk.Label(root, text='push Button')
# label.pack()

# button = tk.Button(root, text='Push!', command=func)
# button.pack()

# button.bind('<Leave>', func_event)


# root.mainloop()


# 위의 예제문제 커서가 안으로 들어왔을 때도 추가// 풀었다 얏호

# import tkinter as tk

# root = tk.Tk()



# def func():

#     label.config(text='Pushed')



# def func_event(ev):

#     label.config(text='Leave')



# def func_event1(ev):

#     label.config(text='Enter')



# label = tk.Label(root, text='push Button')
# label.pack()


# button = tk.Button(root, text='Push!', command=func)
# button.pack()


# button.bind('<Leave>', func_event)

# button.bind('<Enter>', func_event1)


# root.mainloop()


# 버튼만들기 - Event Object

# import tkinter as tk

# root = tk.Tk()



# def func():

#     label.config(text='Pushed')



# def func_event_click(ev):

#     disp = str(ev.x) + '/' + str(ev.y)

#     label.config(text=disp)



# label = tk.Label(root, text='p B')
# label.pack()


# button = tk.Button(root, text='Push!', command=func)
# button.pack()


# button.bind('<Button-1>', func_event_click)

# root.mainloop()


# 라디오 버튼 만들기

# import tkinter as tk

# root = tk.Tk()



# def func1():

#     lbl.config(text="Choice 1")



# def func2():

#     lbl.config(text="Choice 2")



# def func3():

#     lbl.config(text="Choice 3")



# def func4():

#     label.config(text='Push Choice')



# sel = tk.IntVar()

# sel.set(1)


# lbl = tk.Label(root, text="EduCoding", underline=3)
# lbl.pack()


# rb1 = tk.Radiobutton(root, text="Choice 1", variable=sel,

#                      value=1, command=func1)


# rb1.pack()

# rb2 = tk.Radiobutton(root, text="Choice 2", variable=sel,

#                      value=2, command=func2)

# rb2.pack()


# rb3 = tk.Radiobutton(root, text="Choice 3", variable=sel,

#                      value=3, command=func3)

# rb3.pack()


# button = tk.Button(root, text='Push Choice!', command=func4)
# button.pack()


# root.mainloop()


# 슬라이더 만들기

# import tkinter as tk

# root = tk.Tk()


# val = tk.IntVar()

# val.set(0)



# def func(scl):

#     label.config(text="Value = %d" % int(scl))



# label = tk.Label(root, text='value = %d' % val.get())
# label.pack()


# s = tk.Scale(root, label='Scale', orient='h', from_=0, to=100,

#              showvalue=False, variable=val, command=func)
# s.pack()


# root.mainloop()


# 텍스트 박스 만들기

# import tkinter as tk

# root = tk.Tk()



# def func(ev):

#     label.config(text=e.get())



# label = tk.Label(root, text='Input Text')
# label.pack()


# e = tk.Entry(root)
# e.pack()


# e.bind('<Return>', func)


# root.mainloop()



# FUI 텍스트 계산기

import tkinter as tk

root = tk.Tk()

a_input = tk.Entry(root)
a_input.pack()

b_input = tk.Entry(root)
b_input.pack()

sel = tk.IntVar()
sel.set(1)

rb1 = tk.Radiobutton(root,
                     text="Button +",
                     variable=sel,
                     value=1)
rb2 = tk.Radiobutton(root,
                     text="Button -",
                     variable=sel,
                     value=2)
rb3 = tk.Radiobutton(root,
                     text="Button *",
                     variable=sel,
                     value=3)
rb4 = tk.Radiobutton(root,
                     text="Button /",
                     variable=sel,
                     value=4)
rb1.pack()
rb2.pack()
rb3.pack()
rb4.pack()



def calc(a, b, sel):
    if sel == 1:
        return a + b
    elif sel == 2:
        return a - b
    elif sel == 3:
        return a*b
    elif sel == 4:
        return a/b
    else:
        return "알 수 없는 연산자"

def onClick():
    a = int(a_input.get())
    b = int(b_input.get())
    selector = sel.get()
    result = func1(a, b, selector)
    result_label.config(text=cal)

button = tk.Button(root, text='Result', command=onClick )
button.pack()

result_label = tk.Label(root, text='결과가 출력됩니다')
result_label.pack()

root.mainloop()


# 라디오 버튼 만들기 답안

# import tkinter as tk


# def printmy():

#     print(var.get())


# def func1():

#     lbl.config(text="Option 1")


# def func2():

#     lbl.config(text="Option 2")


# def func3():

#     lbl.config(text="Option 3")


# root = tk.Tk()

# lbl = tk.Label(root, text="EduCoding", underline=3)
# lbl.pack()

# var = tk.IntVar(root, 0)


# rb1 = tk.Radiobutton(root, text="Choice 1", variable=var,

#                      value=1, command=func1)


# rb1.pack()

# rb2 = tk.Radiobutton(root, text="Choice 2", variable=var,

#                      value=2, command=func2)

# rb2.pack()


# rb3 = tk.Radiobutton(root, text="Choice 3", variable=var,

#                      value=3, command=func3)

# rb3.pack()


# button = tk.Button(root, text='Print choice', command=printmy)
# button.pack()


# root.mainloop()

