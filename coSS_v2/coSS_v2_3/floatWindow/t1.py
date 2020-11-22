import tkinter as tk
from tkinter import Toplevel 

root = tk.Tk()
root.geometry('200x200')   # 设置窗格大小为200x200

# 构建函数，创建一个顶级窗口
def create_tl():
	toplevel = tk.Toplevel()
	toplevel.title('古诗')
	toplevel.overrideredirect(True).title("sucess").transient(True)
	poetry = '''
《静夜思》
李白
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
	'''
	tk.Label(toplevel, text=poetry).pack(padx=10,pady=10)

# 创建一个生成顶级窗口的Button按钮
tk.Button(root, text='古诗生成器', command=create_tl).pack(padx=10,pady=10)

root.mainloop()