import tkinter as tk
from tkinter import messagebox
import csv
from pathlib import Path
import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"your_path\images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_gui1():
    subprocess.run(["python", "gui1.py"])

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the entered username and password match any entry in the CSV file
    if check_credentials(username, password):
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        open_gui1()
        window.destroy()  # Close the login window after opening gui1.py
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def check_credentials(username, password):
    # Read the usernames and passwords from the CSV file
    with open('user_credentials.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2 and row[0] == username and row[1] == password:
                return True
    return False

window = tk.Tk()

window.geometry("400x300")
window.title("Login Page")

# New color scheme
bg_color = "#3498db"
label_color = "#ffffff"
entry_color = "#ecf0f1"
button_color = "#2ecc71"

window.configure(bg=bg_color)

frame = tk.Frame(window, bg=bg_color)
frame.place(relx=0.5, rely=0.5, anchor="center")

label_username = tk.Label(frame, text="Username:", bg=bg_color, fg=label_color)
label_username.grid(row=0, column=0, pady=10)

username_entry = tk.Entry(frame, bg=entry_color)
username_entry.grid(row=0, column=1, pady=10)

label_password = tk.Label(frame, text="Password:", bg=bg_color, fg=label_color)
label_password.grid(row=1, column=0, pady=10)

password_entry = tk.Entry(frame, show="*", bg=entry_color)
password_entry.grid(row=1, column=1, pady=10)

login_button = tk.Button(frame, text="Login", command=validate_login, bg=button_color, fg=label_color)
login_button.grid(row=2, columnspan=2, pady=20)

window.mainloop()
