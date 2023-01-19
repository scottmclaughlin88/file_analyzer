from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from weather_project import get_days_above_temperatures,get_days_below_temperatures
from plagariasm_checker import get_longest_matching_words


#
# def get_days_above():
#     label2.config(text=get_days_above_temperatures(entry1.get()))

# def get_days_below():
#     min_result.config(text=get_days_below_temperatures(min_entry.get()))
def add_file():
    global files_added
    files_added += 1
    new_file_frame = Frame(window)
    new_file_frame.pack()
    file2_label = Label(new_file_frame,text=f'File {files_added}',font=('Arial',20))
    file2_label.pack(side=LEFT)

    #Add input box
    file2_entry = Entry(new_file_frame)
    file2_entry.pack(side=LEFT)

    button_explore2 = Button(new_file_frame,
                            text = "Browse Files",
                            command = lambda: browseFile(file2_entry))
    file_widgets.append(file2_entry)
    button_explore2.pack(side=LEFT)
    button_analyze_file = Button(new_file_frame,text='Analyze',command=lambda: analyze_file(file2_entry.get()))
    button_analyze_file.pack(side=LEFT)

def get_matching_words():
    try:
        files = []
        for entry in file_widgets:
            print(entry.get())
            open(entry.get(),'r')
            files.append(entry.get())
        file1 = open(file1_entry.get(),'r')
    except:
        messagebox.showerror('Check fail','Please provide two text files')
    else:
        plagiarism_result.config(text=get_longest_matching_words(file1_entry.get(), files))

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = r"C:\Users\scott\OneDrive\Python\Coding Projects",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    fileparts = filename.split('/')                                                        
    file1_entry.delete(0,END)
    file1_entry.insert(0,fileparts[-1])

def browseFiles2():
    filename = filedialog.askopenfilename(initialdir = r"C:\Users\scott\OneDrive\Python\Coding Projects",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    fileparts = filename.split('/')                                                        
    file2_entry.delete(0,END)
    file2_entry.insert(0,fileparts[-1])

def browseFile(file2_entry):
    filename = filedialog.askopenfilename(initialdir = r"C:\Users\scott\OneDrive\Python\Coding Projects",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    fileparts = filename.split('/')                                                        
    file2_entry.delete(0,END)
    file2_entry.insert(0,fileparts[-1])

def analyze_file(filename):
    filler_words = []
    with open('filler_words.txt','r') as file:
        data = file.read()
        filler_words = data.split()
    common_words = {}
    with open(filename, 'r') as file:
        data = file.read()
    for punc in ',.;:\'"':
        data = data.replace(punc, '')
    words = data.split()
    for word in words:
        word = word.lower()
        if word in common_words:
            common_words[word] += 1
        elif word not in filler_words:
            common_words[word] = 1
    common_words = sorted(common_words.items(), key=lambda item:item[1], reverse=True)
    messagebox.showinfo('Common words',f'{common_words[0]}\n{common_words[1]}\n{common_words[2]}')
    
window = Tk()
window.geometry('800x400')
window.title('Data Analysis')

files_added = 1
file_widgets = []

# frame = Frame(window)
# frame.pack()

plagiarism_frame1 = Frame(window)
plagiarism_frame1.pack(side=TOP)
plagiarism_frame2 = Frame(window)
plagiarism_frame2.pack(side=TOP)


#Adding objects
# label1 = Label(window,text='Days above temp',font=('Arial',30))
# label1.pack()
# label2 = Label(window,text='',font=('Arial',30))
# label2.pack()

# #Add input box
# entry1 = Entry(window)
# entry1.pack()

# #Create a button
# button1 = Button(window,text='Get max',command=get_days_above)
# button1.pack()

# min_label1 = Label(window,text='Days below',font=('Arial',30))
# min_label1.pack()
# min_result = Label(window,text='',font=('Arial',30))
# min_result.pack()

# #Add input box
# min_entry = Entry(window)
# min_entry.pack()

# #Create a button
# get_min = Button(window,text='Get min',command=get_days_below)
# get_min.pack()

file1_label = Label(plagiarism_frame1,text='File 1',font=('Arial',20))
file1_label.pack(side=LEFT)
file1_entry = Entry(plagiarism_frame1)
file1_entry.pack(side=LEFT)
button_explore = Button(plagiarism_frame1,
                        text = "Browse Files",
                        command = browseFiles)
button_explore.pack(side=LEFT)
button_analyze_file = Button(plagiarism_frame1,text='Analyze',command=lambda: analyze_file(file1_entry.get()))
button_analyze_file.pack(side=LEFT)

button_explore.pack(side=LEFT)
button_add_file = Button(window,text='Add file',command=add_file)
button_add_file.pack()


#Find most common word
# button_common_word = Button(plagiarism_frame1,text='Common word',command=get_common_word)
# button_common_word.pack()

# file2_label = Label(plagiarism_frame2,text='File 2',font=('Arial',20))
# file2_label.pack(side=LEFT)

# #Add input box
# file2_entry = Entry(plagiarism_frame2)
# file2_entry.pack(side=LEFT)

# button_explore2 = Button(plagiarism_frame2,
#                         text = "Browse Files",
#                         command = browseFiles2)
# button_explore2.pack(side=LEFT)

#Create a button
find_pl = Button(window,text='Get plagiarism',command=get_matching_words)
find_pl.pack()

plagiarism_result = Label(window,text='',font=('Arial',30))
plagiarism_result.pack()

window.mainloop()