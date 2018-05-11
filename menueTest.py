from tkinter import *


def return_table():

    table = 'test.dbf'

    return table


def return_surname():

    surname = entry.get()

    return surname


def create_list():

    surname = return_surname()
    table = return_table()

    print (surname + ' ' + table)


def main():

    master = Tk()
    master.geometry('{}x{}'.format(400, 125))
    master.title('Assign a Player to a Team')

    entry = Entry(master, width = 50)
    entry.grid(row = 0, column = 0, columnspan = 5)

    surname_button = Button(master, text='Go', command=create_list)
    surname_button.grid(row = 0, column = 7, sticky = W)

    mainloop()


main()