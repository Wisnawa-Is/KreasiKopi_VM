from customtkinter import *
from PIL import Image
from orderMenu import *

root = CTk()
root.title("Kreasi Kopi")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{600}x{500}")
x = (screen_width - 600) // 2
y = (screen_height - 500) // 2
root.configure(fg_color="#FFE0BC")
root.geometry(f"+{x}+{y}")
root.resizable(False, False)
current_menu = 'start'
size = ''
            
startpage(root, current_menu, size)

root.mainloop()

