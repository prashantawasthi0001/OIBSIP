import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# ---------------- DATABASE ---------------- #

try:
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        category TEXT,
        date TEXT
    )
    """)
    conn.commit()

except Exception as e:
    print("Database Error:", e)


# ---------------- BMI FUNCTION ---------------- #

def calculate_bmi():

    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if name == "":
            messagebox.showerror("Error", "Enter Name")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be positive.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "orange"

        elif bmi < 25:
            category = "Normal"
            color = "green"

        elif bmi < 30:
            category = "Overweight"
            color = "blue"

        else:
            category = "Obese"
            color = "red"

        result.config(
            text=f"BMI : {bmi:.2f}\nCategory : {category}",
            fg=color
        )

        try:
            cursor.execute(
                "INSERT INTO bmi(name,weight,height,bmi,category,date) VALUES(?,?,?,?,?,?)",
                (
                    name,
                    weight,
                    height,
                    bmi,
                    category,
                    datetime.now().strftime("%Y-%m-%d %H:%M")
                )
            )
            conn.commit()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")


# ---------------- GRAPH ---------------- #

def show_graph():

    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Enter Name")
        return

    try:
        cursor.execute(
            "SELECT date,bmi FROM bmi WHERE name=?",
            (name,)
        )

        rows = cursor.fetchall()

        if len(rows) == 0:
            messagebox.showinfo("No Data", "No records found.")
            return

        dates = []
        bmi = []

        for row in rows:
            dates.append(row[0])
            bmi.append(row[1])

        plt.figure(figsize=(6,4))
        plt.plot(dates, bmi, marker="o")
        plt.title(name + " BMI Trend")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x450")
root.configure(bg="#eaf4ff")

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial",20,"bold"),
    bg="#eaf4ff",
    fg="navy"
)
title.pack(pady=15)

tk.Label(root,text="Name",bg="#eaf4ff",font=("Arial",12)).pack()
name_entry = tk.Entry(root,font=("Arial",12))
name_entry.pack(pady=5)

tk.Label(root,text="Weight (kg)",bg="#eaf4ff",font=("Arial",12)).pack()
weight_entry = tk.Entry(root,font=("Arial",12))
weight_entry.pack(pady=5)

tk.Label(root,text="Height (m)",bg="#eaf4ff",font=("Arial",12)).pack()
height_entry = tk.Entry(root,font=("Arial",12))
height_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate BMI",
    bg="green",
    fg="white",
    font=("Arial",12),
    command=calculate_bmi
).pack(pady=15)

tk.Button(
    root,
    text="Show BMI Trend",
    bg="blue",
    fg="white",
    font=("Arial",12),
    command=show_graph
).pack()

result = tk.Label(
    root,
    text="",
    bg="#eaf4ff",
    font=("Arial",15,"bold")
)
result.pack(pady=20)

root.mainloop()

conn.close()