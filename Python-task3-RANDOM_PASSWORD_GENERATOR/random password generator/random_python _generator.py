import tkinter as tk
from tkinter import messagebox
import string
import secrets


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror(
                "Error",
                "Password length must be at least 4!"
            )
            return

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        # At least one character from each category
        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(special)
        ]

        all_characters = lowercase + uppercase + digits + special

        for _ in range(length - 4):
            password.append(secrets.choice(all_characters))

        secrets.SystemRandom().shuffle(password)

        final_password = ''.join(password)

        # Show password in output box
        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number!"
        )


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# Main Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#1e1e2f")


# Title
title = tk.Label(
    root,
    text="RANDOM PASSWORD GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="#00ffcc"
)
title.pack(pady=30)


# Length Label
length_label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
length_label.pack()


# Length Entry
length_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=20,
    justify="center"
)
length_entry.pack(pady=10)


# Generate Button
generate_button = tk.Button(
    root,
    text="GENERATE PASSWORD",
    font=("Arial", 12, "bold"),
    bg="#00cc99",
    fg="white",
    width=22,
    command=generate_password
)
generate_button.pack(pady=15)


# Password Label
password_label = tk.Label(
    root,
    text="Generated Password:",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="white"
)
password_label.pack(pady=5)


# Password Output
password_entry = tk.Entry(
    root,
    font=("Arial", 14, "bold"),
    width=30,
    justify="center"
)
password_entry.pack(pady=10)


# Copy Button
copy_button = tk.Button(
    root,
    text="COPY PASSWORD",
    font=("Arial", 11, "bold"),
    bg="#3366ff",
    fg="white",
    width=18,
    command=copy_password
)
copy_button.pack(pady=15)


# Footer
footer = tk.Label(
    root,
    text="Oasis Infobyte Internship Project",
    font=("Arial", 9),
    bg="#1e1e2f",
    fg="#aaaaaa"
)
footer.pack(side="bottom", pady=15)


root.mainloop()