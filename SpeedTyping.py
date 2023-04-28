from tkinter import *
from timeit import default_timer as timer
import random


def game():
    # Start game by clearing the start frame and showing the word frame
    start_frame.pack_forget()
    word_frame.pack()
    
    # Clear entry field and show a new random word
    entry.delete(0, END)
    word_label.config(text=random.choice(words), font=("Helvetica", 24, "bold"))

    # Start the timer
    global start_time
    start_time = timer()

def check_result(event=None):
    input_text = entry.get().strip()
    expected_text = word_label.cget("text")

    if input_text == expected_text:
        # Calculate and show the typing speed
        end_time = timer()
        time_taken = end_time - start_time
        typing_speed = len(expected_text) / time_taken
        typing_speed_label.config(text=f"Your typing speed is {round(typing_speed, 2)} characters per second")
        
        # Start a new game
        game()
    else:
        # Show an error message
        error_label.config(text="Wrong input, try again")

    
# Define words for testing
words = ['programming', 'coding', 'algorithm', 'systems', 'python', 'software']

# Create window
window = Tk()
window.title("Typing Speed Test")
window.geometry("600x400")

# Create start frame
start_frame = Frame(window)
start_frame.pack(pady=20)

start_label = Label(start_frame, text="Let's test your typing speed!", font=("Helvetica", 24))
start_label.pack(padx=20, pady=10)

start_button = Button(start_frame, text="Start", font=("Helvetica", 16), command=game)
start_button.pack(pady=20)

# Create word frame
word_frame = Frame(window)

word_label = Label(word_frame, text="", font=("Helvetica", 24, "bold"))
word_label.pack(pady=10)

entry = Entry(word_frame, font=("Helvetica", 18))
entry.pack(pady=10)
entry.bind("<Return>", check_result)

error_label = Label(word_frame, text="", fg="red")
error_label.pack(pady=10)

typing_speed_label = Label(word_frame, text="", font=("Helvetica", 18))
typing_speed_label.pack(pady=10)

# Pack word frame but keep it hidden initially
word_frame.pack_forget()

# Start the GUI
window.mainloop()