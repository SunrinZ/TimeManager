# -*- coding: utf-8 -*-def pop_up_box():
 
# Copyright (c) 2017-7-21 ZhengPeng All rights reserved.

def pop_up_box():
    """
    使用tkinter弹出输入框输入数字, 具有确定输入和清除功能, 可在函数内直接调用num(文本框的值)使用
    """

    import tkinter
    from datetime import datetime
    
    def inputint():
#		f=open("Login.txt","a+").read().decode('gbk','ignore')
		e=file("Login.txt",'a')
		str=datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" "+var.get().encode('utf-8')+"\n"
		e.write(str)
		e.close()
		root.destroy()
		print(var.get())
#        nonlocal num
#        try:
#            num = int(var.get().strip())
#        except:
#            num = 'Not a valid integer.'


#    def inputclear():
#		print("clear")
#        nonlocal num
#        var.set('')
#        num = ''

    num = 0
    root = tkinter.Tk(className='time recode')  # 弹出框框名
    root.geometry('270x60')     # 设置弹出框的大小 w x h

    var = tkinter.StringVar()   # 这即是输入框中的内容
    entry1 = tkinter.Entry(root, textvariable=var)  # 设置"文本变量"为var
    entry1.pack()   # 将entry"打上去"
    btn1 = tkinter.Button(root, text='Input', command=inputint)     
	# 按下此按钮(Input), 触发inputint函数
#    btn2 = tkinter.Button(root, text='Clear', command=inputclear)   
	# 按下此按钮(Clear), 触发inputclear函数

    # 按钮定位
#    btn2.pack(side='right')
    btn1.pack(side='right')

    # 上述完成之后, 开始真正弹出弹出框
    root.mainloop()
pop_up_box()