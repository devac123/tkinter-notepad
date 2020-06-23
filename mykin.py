import tkinter as  tk
from tkinter import ttk
from tkinter import colorchooser,filedialog,messagebox,font
import os
win = tk.Tk()
win.title("mynotepad project")
win.wm_iconbitmap('icon.ico')
win.geometry("1200x800")

toolbar = ttk.Label(win)
toolbar.pack(side = tk.TOP,fill = tk.X)

main_menu = tk.Menu()

font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar,width=16, textvariable =font_family,state ='readonly')
font_box['values']= font_tuples
font_box.current(0)
font_box.grid(row =0 ,column=0,padx=5)

#todo****** font size*********
size = tk.IntVar()
font_size = ttk.Combobox(toolbar,widt =14 ,textvariable = size,state=('readonly'))
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1)

#todo ******** bold buttuon*********
bold_icon = tk.PhotoImage(file='icons/icons8-bold-26.png')
bold_button = ttk.Button(toolbar , image = bold_icon )
bold_button.grid(row = 0,column = 2, padx = 4)

#todo ******** italic buttuon*********
italic_icon = tk.PhotoImage(file='icons/icons8-italic-26.png')
italic_btn = ttk.Button(toolbar , image = italic_icon)
italic_btn.grid(row = 0 ,column = 3)

#todo ******** underline buttuon*********
underline_icon = tk.PhotoImage(file='icons/icons8-underline-24.png')
underline_btn = tk.Button(toolbar,image=underline_icon,)
underline_btn.grid(row=0,column = 4,padx=4)

#todo ******** color chooser buttuon*********
color_icon = tk.PhotoImage(file = 'icons/icons8-color-wheel-30.png')
color_btn = ttk.Button(toolbar,image=color_icon)
color_btn.grid(row = 0,column = 5,padx=4)

#todo*********** left icon***********************
left_icon = tk.PhotoImage(file='icons/icons8-align-left-26.png')
left_btn = ttk.Button(toolbar,image =left_icon)
left_btn.grid(row =0 ,column =6)

#todo*********** right icon***********************
right_icon = tk.PhotoImage(file='icons/icons8-align-right-26.png')
right_btn =ttk.Button(toolbar,image=right_icon)
right_btn.grid(row =0 ,column =7,padx=4)
#todo*********** center icon***********************
center_icon = tk.PhotoImage(file='icons/icons8-align-center-26.png')
center_btn = ttk.Button(toolbar,image = center_icon)
center_btn.grid(row =0 ,column =8)

#todo**************text editor***************
text_editor = tk.Text(win)
text_editor.config(wrap = 'word' , relief=tk.FLAT)
scroll_bar =tk.Scrollbar(win)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

current_font_family = "Ariel"
current_font_size = 12

def changevalue(win):
    global current_font_family,current_font_size
    current_font_size = font_size.get()
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>",changevalue)
font_size.bind("<<ComboboxSelected>>",changevalue)

#todo************Button funcionality***************
#todo bold-Button______
# print(tk.font.Font(font=text_editor['font']).actual())
def bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_button.configure(command = bold)
#todo itali-Button______
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['weight'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))
italic_btn.configure(command =change_italic)
#todo itali-Button______
# print(tk.font.Font(font=text_editor['font']).actual())
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['weight'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
underline_btn.configure(command = change_underline)

#todo color chooser______
def color_chooser_ico():
    clor_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=clor_var[1])
color_btn.configure(command=color_chooser_ico)

#todo************** lignalignment ************
def align_left():
    text_contant = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_contant,'left')
left_btn.configure(command =align_left)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
right_btn.configure(command =align_right)

def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
center_btn.configure(command =align_center)
text_editor.configure (font = ('Arial',12))
#todo$$$$$$$$$$$$$$$$$$text-end$$$$$$$$$$$$$$$$$


#todo ********************stattus bar****
status_bar1 =ttk.Label(win,text="status_bar")
status_bar1.pack(side=tk.BOTTOM)
#
def status_bar(event = None):
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0,'end-1c').split())
        char = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar1.config(text =f'characters : {char},words :{words}')
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",status_bar)

#todo ***** filemenu **********
file_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
open_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
save_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
save_as_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
exit_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')

file = tk.Menu(main_menu, tearoff = 0)


#todo ***** edit menu**********
copy_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
paste_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
cut_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
clear_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')
find_icon = tk.PhotoImage(file = 'icons/icons8-file-48.png')

edit = tk.Menu(main_menu, tearoff = 0)


#todo ***** viewmenu **********
toolbar_icon = tk.PhotoImage(file = 'icons/wrench.png')
statusbar_icon = tk.PhotoImage(file = 'icons/wrench.png')

view = tk.Menu(main_menu, tearoff = 0)


#todo ********* color theme menue**********
blackTheme = tk.PhotoImage(file = 'icons/icons8-bookmark-48.png')
lightTheme= tk.PhotoImage(file = 'icons/icons8-bookmark-48.png')
greyTheme = tk.PhotoImage(file = 'icons/icons8-bookmark-48.png')
MonokaiTheme= tk.PhotoImage(file = 'icons/icons8-bookmark-48.png')
purpleTheme= tk.PhotoImage(file = 'icons/icons8-bookmark-48.png')

colortheme = tk.Menu(main_menu, tearoff = 0)
theme_choice = tk.StringVar()
color_theme = (blackTheme,lightTheme,greyTheme,MonokaiTheme,purpleTheme)

color_dict={
    'blacktheme':('#fff','#000'),
    'lightetheme':('#474747','#e0e0e0'),
    'greytheme':('#c4c4c4','#2d2d2d'),
    'monokaitheme':('#2d2d2d','#ffe8e8'),
    'purpletheme':('#d3b774','#474747')
}

#todo ****** cascading all menue*******
main_menu.add_cascade(label='File',menu =file)
main_menu.add_cascade(label='Edit',menu =edit)
main_menu.add_cascade(label='View',menu =view)
main_menu.add_cascade(label='Color theme',menu =colortheme)


#todo********* file commands***********
#todo*********new-file***********
url = ''
def new_file(event=None):
    text_editor.delete(1.0,tk.END)

file.add_command(label='New',image=file_icon,compound = tk.LEFT,accelerator ='ctrl+N',command = new_file)

#todo*********open file***********
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir =os.getcwd(),title = 'select-file',filetypes = (('Text-file','*.txt'),('all-types','*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except :
        return
    win.title(os.path.basename(url))
file.add_command(label='Open',image=file_icon,compound = tk.LEFT,accelerator ='ctrl+O',command = open_file)


#todo*********save-file***********
def save_file(event=None):
    global url
    if url:
        content = str(text_editor.get(1.0,tk.END))
        with open(url, 'w',encoding='utf-8') as fw:
            fw.write(content)
    else:
        url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes=(('Text-file', '*.txt'), ('all-types', '*.*')))
        content2 = text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close()


file.add_command(label='Save',image=file_icon,compound = tk.LEFT,accelerator ='ctrl+S',command =save_file)

#todo*********save-as-file***********
def saveas_file(event=None):
     global url
     content = text_editor.get(1.0,tk.END)
     url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt', filetypes=(('Text-file', '*.txt'), ('all-types', '*.*')))
     url.write(content)



file.add_command(label='Save_as',image=file_icon,compound = tk.LEFT,accelerator ='ctrl+alt+S',command=saveas_file)
#todo*********Exit-file***********
def exit_file(event=None):
    global url,text_change
    if text_change:
        mbox = messagebox.askyesnocancel('warning','Do you want to save the file ?')
        if mbox is True:
            if url:
                content = text_editor.get(1.0,tk.END)
                with open(url,'w',encoding= 'utf-8') as fw :
                    fw.write(content)
                    win.destroy()
            else:
                content2 = str(text_editor.get(1.0,tk.END))
                url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                               filetypes=(('Text-file', '*.txt'), ('all-types', '*.*')))
                url.write(content2)
                url.close()

        elif mbox is False:
            win.destroy()
    else:
        win.destroy()
file.add_command(label='Exit',image=file_icon,compound = tk.LEFT,accelerator ='ctrl+Q',command = exit_file)

#todo********* edit commands ***********
def find_func(event=None):

    def find():
        word =find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches =0

        if word:
            satrt_possison = '1.0'
            while True:
                satrt_possison= text_editor.search(word,satrt_possison,stopindex= tk.END)
                if not satrt_possison:
                    break
                end_pos = (f"{satrt_possison}+{len(word)}c")
                text_editor.tag_add('match',satrt_possison,end_pos)
                matches +=1
                satrt_possison =end_pos
                text_editor.tag_config('match',foreground ='red',background="yellow")


    def replace():
        word =find_input.get()
        replace = Replace.get()
        content = text_editor.get(1.0,tk.END)
        new_cont = content.replace(word,replace)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_cont)
        pass


    find_dilouge = tk.Toplevel()
    find_dilouge.geometry("500x230")
    find_dilouge.title('Find and replace')
    find_dilouge.resizable(0,0)

    findframe = ttk.LabelFrame(find_dilouge,text='find/replace')
    findframe.pack(pady=20)

    text_find_label = ttk.Label(findframe,text = 'Find: ')
    text_replace_variable = ttk.Label(findframe,text = 'Replace: ')

    find_input = ttk.Entry(findframe,width=30)
    Replace = ttk.Entry(findframe,width=30)

    find_button = ttk.Button(findframe,text = 'Find',command = find)
    Replace_button =ttk.Button(findframe,text = 'Replace',command =replace)

    text_find_label.grid(row =0,column =0 , padx=4,pady=4)
    text_replace_variable.grid(row =1,column =0 , padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4)
    Replace.grid(row=1,column=1,padx=4,pady=4)

    find_button.grid(row=2,column=0,padx=8,pady=4)
    Replace_button.grid(row=2,column = 1,padx=8,pady=4)

    find_dilouge.mainloop()

edit.add_command(label='Copy',image=copy_icon,compound = tk.LEFT,accelerator ='ctrl+C',command = lambda :text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound = tk.LEFT,accelerator ='ctrl+V',command = lambda :text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound = tk.LEFT,accelerator ='ctrl+X',command = lambda :text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear',image=clear_icon,compound = tk.LEFT,accelerator ='ctrl+alt+X',command = lambda :text_editor.delete(1.0,tk.END))
edit.add_command(label='find',image=find_icon,compound = tk.LEFT,accelerator ='ctrl+shift+S',command =find_func )


#todo********* toolbar commands ***********
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar = tk.BooleanVar()
show_tool_bar.set(True)

def hide_toolbar():
    global show_tool_bar
    if show_tool_bar:
         toolbar.pack_forget()
         show_tool_bar = False
    else:
        text_editor.pack_forget()
        status_bar1.pack_forget()
        toolbar.pack(side = tk.TOP,fill =tk.X)
        text_editor.pack(fill = tk.BOTH,expand =True)
        status_bar1.pack(side = tk.BOTTOM)
        show_tool_bar = True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bar1.pack_forget()
        show_status_bar =False
    else:
        status_bar1.pack(side =tk.BOTTOM)
        show_status_bar =True
    pass

view.add_checkbutton(label='toolbar',onvalue = True,offvalue =0, variable= show_tool_bar ,image=toolbar_icon,compound = tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Satatusbar',onvalue = 1,offvalue = False, variable=show_status_bar ,image=toolbar_icon,compound = tk.LEFT,command=hide_statusbar)

#todo****** color radio button*******

def chnge_theme():
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,foreground =fg_color)


count1 = 0
for col in color_dict:
    colortheme.add_radiobutton(label=col,image = color_theme[count1], variable = theme_choice,compound = tk.LEFT,command =chnge_theme)
    count1 +=1

win.bind("<Control-n>",new_file)
win.bind("<Control-o>",open_file)
win.bind("<Control-q>",exit_file)
win.bind("<Control-s>",save_file)
win.bind("<Control-Alt-s>",saveas_file)
win.config(menu=main_menu)
win.mainloop()
