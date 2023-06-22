import tkinter as tk
from tkinter import StringVar
import NaiveBayes

root = tk.Tk()
root.geometry('500x500')

questions = ["Pilih pekerjaan", "Pilih usia", "Pilih status", "Pilih penghasilan",
             "Pilih kendaraan", "Pilih kepemilikan", "Pilih kondisi atap"]
option = [['Wiraswasta', 'Tidak Bekerja', None, None], ['20-29', '30-40', None, None],
          ['Kawin', 'Belum Kawin', None, None], ['<1000', '2000-3000', '4000-5000', '>5000'],
          ['Motor', 'Mobil', 'Angkutan Umum', None], ['Orang tua', 'Pribadi', 'Menyewa', None],
          ['Asbes', 'Genteng', None, None]]
data = []

frame = tk.Frame(root, padx=10, pady=10, bg='#fff')
question_label = tk.Label(frame, height=5, width=28, bg='#ddd', font=('Verdana', 20), wraplength=500)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg='#fff', variable=v1, font=('Verdana', 20), 
                         command=lambda:checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg='#fff', variable=v2, font=('Verdana', 20),
                         command=lambda:checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg='#fff', variable=v3, font=('Verdana', 20),
                         command=lambda:checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg='#fff', variable=v4, font=('Verdana', 20),
                         command=lambda:checkAnswer(option4))

button_next = tk.Button(frame, text='Next', bg='Orange', font=('Verdana', 20),
                        command=lambda:displayNextQuestion())

frame.pack(fill='both', expand=True)
question_label.grid(row=0, column=0)

button_next.grid(row=6, column=0)

index = 0

# function to disable button
def disableButton(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

# function to check selected option
def checkAnswer(radio):
    global index

    data.append(radio['text'])
    
    index += 1
    disableButton('disable')

# function to display next question
def displayNextQuestion():
    global index, data

    option1.grid(sticky='W', row=1, column=0)
    option2.grid(sticky='W', row=2, column=0)
    option3.grid(sticky='W', row=3, column=0)
    option4.grid(sticky='W', row=4, column=0)

    if button_next['text'] == 'Restart':
        index = 0
        question_label['bg'] = '#ddd'
        button_next['text'] = 'Next'

    # final page
    if index == len(option):
        question_label['text'] = NaiveBayes.naiveBayes(data)
        button_next['text'] = 'Restart'
        option1.grid(sticky='W', row=0, column=3)
        option2.grid(sticky='W', row=0, column=3)
        option3.grid(sticky='W', row=0, column=3)
        option4.grid(sticky='W', row=0, column=3)
        
        if question_label['text'] == 'Layak':
            question_label['bg'] = 'light green'
        else:
            question_label['bg'] = 'orange red'

        data = []

    else:
        question_label['text'] = questions[index]

        disableButton('normal')
        opts = option[index]

        option1['text'] = opts[0]          

        if opts[1] == None:
            option2.grid(sticky='W', row=0, column=3)
        option2['text'] = opts[1]

        if opts[2] == None:
            option3.grid(sticky='W', row=0, column=3)
        option3['text'] = opts[2]
        
        if opts[3] == None:
            option4.grid(sticky='W', row=0, column=3)
        option4['text'] = opts[3]

        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(option)-1:
            button_next['text'] = 'Check Result'

displayNextQuestion()

root.mainloop()