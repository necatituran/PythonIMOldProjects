from tkinter import Label, Tk    # import Label and Tk from tkinter
import time                # import time module

app_windows = Tk()       # create a Tk object
app_windows.title("Digital Clock")    # set the title of the window
app_windows.geometry("420x150")     # set the size of the window
app_windows.resizable(1, 1)      # make the window resizable

text_font = ("Boulder", 68, 'bold')   # set the font of the text
background = "#f2e750"      # set the background color
foreground = "#363529"
border_width = 25

label = Label(app_windows, font=text_font, background=background,
              foreground=foreground, bd=border_width)    # create a Label object
# row and column are 0-indexed  # set the position of the label
label.grid(row=0, column=1)


def digital_clock():        # function to display the digital clock
    # get the current local time from the PC
    text_input = time.strftime('%H:%M:%S')
    label.config(text=text_input)       # set the text of the label
    # run the function after 200 milliseconds
    label.after(200, digital_clock)


digital_clock()     # call the digital_clock function
app_windows.mainloop()   # start the application
