import tkinter as tk
from tkinter import messagebox
import random
import string
# Function to generate password
def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero")
            return 
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
        password_display.config(state=tk.NORMAL)
        password_display.delete('1.0', tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length")
# Create main window
root = tk.Tk()
root.title("Password Generator")
# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root, width=30)
length_entry.pack()
# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
# Text widget to display generated password
password_display = tk.Text(root, height=3, width=50, state=tk.DISABLED)
password_display.pack(pady=10)
# Start the main tkinter loop
root.mainloop()
