#menuly created by bhatt ji

import pymysql
import tkinter as tk
from tkinter import messagebox
import re
import os

try:
    db = pymysql.connect(host="localhost", user="root", password="", database="patient")
    print("Connected to database")
except Exception as e:
    print(e)

cr = db.cursor()

try:
    table_p = ("""CREATE TABLE IF NOT EXISTS patients(id INT AUTO_INCREMENT PRIMARY KEY,name TEXT,age INT)""")
    try:
        cr.execute(table_p)
        db.commit()
        print("done")
    except Exception as e:
        print(e)
    

    table_a = ("""CREATE TABLE IF NOT EXISTS appointments(id INT AUTO_INCREMENT PRIMARY KEY,patient_id INT,doctor TEXT,date TEXT,time TEXT,notes TEXT,FOREIGN KEY(patient_id) REFERENCES patients(id))""")
    try:
        cr.execute(table_a)
        db.commit()
        print("done")
    except Exception as e:
        print(e)
   

    table_u = ("""CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY,username varchar(100) unique,password varchar(100),role VARCHAR(50))""")
    try:
        cr.execute(table_u)
        db.commit()
        print("done")
    except Exception as e:
        print(e)

    table_b = "create table if not exists bill(id int auto_increment primary key,patient_id int ,amount float ,description TEXT,date TEXT,FOREIGN KEY(patient_id) REFERENCES patients(id))"
    try:
        cr.execute(table_b)
        db.commit()
        print("done")
    except Exception as e:
        print(e)

    cr.execute("select * from users where username='admin'")
    if not cr.fetchone():
        cr.execute("insert into users(username,password,role) VALUES(%s,%s,%s)",
                   ("admin", "admin123", "Admin"))
        db.commit()
        print("Default admin created")

except Exception as e:
    print("error in table ", e)

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self):
        try:
            cr.execute("INSERT INTO patients(name, age) VALUES (%s,%s)", (self.name, self.age))
            db.commit()
            messagebox.showinfo("patient saved")
        except Exception as e:
            messagebox.showerror("Cannot save patient: ",e)

class Appointment:
    def __init__(self, pid, doctor, date, time, notes):
        self.pid = pid
        self.doctor = doctor
        self.date = date
        self.time = time
        self.notes = notes

    def save(self):
        try:
            cr.execute("insert into appointments(patient_id, doctor, date, time, notes) VALUES (%s,%s,%s,%s,%s)",
                       (self.pid, self.doctor, self.date, self.time, self.notes))
            db.commit()
            messagebox.showinfo("appointment saved")
        except Exception as e:
            messagebox.showerror("Cannot save appointment: ",e)

def login_page():
    login = tk.Tk()
    login.title("login")
    login.geometry("400x350")

    tk.Label(login, text="Username:").place(x=30, y=40)
    username_entry = tk.Entry(login)
    username_entry.place(x=100, y=40)

    tk.Label(login, text="Password:").place(x=30, y=60)
    password_entry = tk.Entry(login)
    password_entry.place(x=100, y=70)

    def check_login():
        u = username_entry.get()
        p = password_entry.get()
        cr.execute("select role from users where username=%s AND password=%s", (u, p))
        data = cr.fetchone()
        if data:
            role = data[0]
            messagebox.showinfo("Login Success",u)
            login.destroy()
            main_screen(role)
        else:
            messagebox.showerror("wrong username or password")

    tk.Button(login, text="Login", command=check_login, bg="green", fg="white").place(x=100, y=130)
    login.mainloop()

def main_screen(user_role):
    screen = tk.Tk()
    screen.title("MediTrack App")
    screen.geometry("1000x600")
    screen.config(bg="light blue")

    tk.Label(screen, text="Name", bg="light blue", fg="red").place(x=50, y=50)
    name_entry = tk.Entry(screen)
    name_entry.place(x=150, y=50)

    tk.Label(screen, text="Age", bg="light blue", fg="red").place(x=50, y=80)
    age_entry = tk.Entry(screen)
    age_entry.place(x=150, y=80)

    tk.Label(screen, text="Patient ID", bg="light blue", fg="red").place(x=50, y=120)
    patient_id_entry = tk.Entry(screen)
    patient_id_entry.place(x=150, y=120)

    tk.Label(screen, text="Doctor", bg="light blue", fg="red").place(x=50, y=160)
    doctor_entry = tk.Entry(screen)
    doctor_entry.place(x=150, y=160)

    tk.Label(screen, text="Date", bg="light blue", fg="red").place(x=50, y=190)
    date_entry = tk.Entry(screen)
    date_entry.place(x=150, y=190)

    tk.Label(screen, text="Time", bg="light blue", fg="red").place(x=50, y=220)
    time_entry = tk.Entry(screen)
    time_entry.place(x=150, y=220)

    tk.Label(screen, text="Notes", bg="light blue", fg="red").place(x=50, y=250)
    notes_entry = tk.Entry(screen)
    notes_entry.place(x=150, y=250)

    tk.Label(screen, text="Amount", bg="light blue", fg="red").place(x=50, y=300)
    amount_entry = tk.Entry(screen)
    amount_entry.place(x=150, y=300)

    tk.Label(screen, text="Tax (%)", bg="light blue", fg="red").place(x=50, y=330)
    tax_entry = tk.Entry(screen)
    tax_entry.insert(0, "10")  
    tax_entry.place(x=150, y=330)

    tk.Label(screen, text="Description", bg="light blue", fg="red").place(x=50, y=330)
    desc_entry = tk.Entry(screen)
    desc_entry.place(x=150, y=330)

    from datetime import datetime

    def save_patient():
        try:
            name = name_entry.get()
            age = int(age_entry.get())
            p = Patient(name, age)
            p.save()
            messagebox.showinfo("Success", "Patient saved successfully!")
        except ValueError:
            messagebox.showerror("error","please enter a valid number for age.")
        except Exception as e:
            messagebox.showerror(e)

    tk.Button(screen, text="Save Patient", command=save_patient, bg="green", fg="white").place(x=350, y=50)


    def update_patient():
        pid = patient_id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        try:
            cr.execute("UPDATE patients SET name=%s, age=%s WHERE id=%s", (name, age, pid))
            db.commit()
            messagebox.showinfo("Success", "Patient updated")
        except Exception as e:
            messagebox.showerror(e)
    tk.Button(screen, text="Update Patient", command=update_patient, bg="orange", fg="black").place(x=350, y=80)


    def search_patient():
        pid = patient_id_entry.get()
        try:
            cr.execute("SELECT * FROM patients WHERE id=%s", (pid,))
            data = cr.fetchone()
            if data:
                name_entry.delete(0,'end')
                age_entry.delete(0,'end')
                name_entry.insert(0, data[1])
                age_entry.insert(0, data[2])
                messagebox.showinfo("Found","Patient Found:\nID: {}\nName: {}\nAge: {}".format(data[0], data[1], data[2]))
            else:
                messagebox.showwarning("patient not found")
        except Exception as e:
            messagebox.showerror(e)
    tk.Button(screen, text="Search Patient", command=search_patient, bg="blue", fg="white").place(x=450, y=50)

    def save_appointment():
        pid = patient_id_entry.get()
        doctor = doctor_entry.get()
        date = date_entry.get()
        time = time_entry.get()
        notes = notes_entry.get()
        
        if pid.strip() == "" or doctor.strip() == "" or date.strip() == "" or time.strip() == "":
            messagebox.showwarning("Warning", "Fill required fields")
            return
        
        a = Appointment(pid, doctor, date, time, notes)
        a.save()
    tk.Button(screen, text="Save Appointment", command=save_appointment, bg="purple", fg="white").place(x=350, y=160)

    def show_visits():
        pid = patient_id_entry.get().strip()
        if not pid:
            messagebox.showwarning("Warning", "Enter Patient ID")
            return
        try:
            cr.execute("SELECT doctor,date,time,notes FROM appointments WHERE patient_id=%s", (pid,))
            visits = cr.fetchall()
            if not visits:
                messagebox.showwarning("No Visits", "No visits found")
                return

            display_text = ""
            for v in visits:
                display_text += str(v) + "\n"

            messagebox.showinfo("visit history", display_text)

        except Exception as e:
            messagebox.showerror("cant see",e)

    tk.Button(screen, text="Show Visits", command=show_visits, bg="brown", fg="white").place(x=350, y=190)


    def search_by_notes():
        pattern = notes_entry.get().strip()
        if not pattern:
            messagebox.showwarning("Warning", "Enter pattern to search")
            return

        try:
            cr.execute("SELECT * FROM appointments")
            all_appointments = cr.fetchall()

            matched = [a for a in all_appointments if re.search(pattern, a[5], re.IGNORECASE)]
            if not matched:
                messagebox.showinfo("No Match", "No matching records found")
                return

            display_text = ""
            for m in matched:
                display_text += str(m) + "\n"   
            messagebox.showinfo("Matched Appointments", display_text)
        except Exception as e:
            messagebox.showerror("error", str(e))

    tk.Button(screen, text="Search Notes", command=search_by_notes, bg="pink", fg="black").place(x=350, y=220)

    def save_bill():
        pid = patient_id_entry.get()
        amount = amount_entry.get()
        tax = tax_entry.get()
        desc = desc_entry.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if pid == "" or amount == "":
            messagebox.showwarning("Warning", "Enter Patient ID and Amount")
            return

        try:
            total = float(amount) + (float(amount) * float(tax) / 100)
            cr.execute("INSERT INTO bill(patient_id, amount, description, date) VALUES (%s,%s,%s,%s)",
                       (pid, total, desc, date))
            db.commit()
            messagebox.showinfo("Success", f"Bill saved with tax.\nTotal: ₹{total}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_bills():
        pid = patient_id_entry.get()
        if not pid:
            messagebox.showwarning("Warning", "Enter Patient ID")
            return
        cr.execute("SELECT * FROM bill WHERE patient_id=%s", (pid,))
        bills = cr.fetchall()
        if bills:
            msg = ""
            for b in bills:
                msg += f"ID: {b[0]} | Amount: {b[2]} | Desc: {b[3]} | Date: {b[4]}\n"
            messagebox.showinfo("Bill History", msg)
        else:
            messagebox.showinfo("No Bills", "No bills found")

    tk.Button(screen, text="Save Bill", command=save_bill, bg="dark green", fg="white").place(x=350, y=300)
    tk.Button(screen, text="Show Bills", command=show_bills, bg="teal", fg="white").place(x=450, y=300)

    screen.mainloop()

login_page()
