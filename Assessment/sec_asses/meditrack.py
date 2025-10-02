import sqlite3
import tkinter as tk
from tkinter import messagebox
import re

def init_db():
    conn = sqlite3.connect("meditrack.db")
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        contact TEXT,
        medical_history TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        specialization TEXT,
        contact TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        date TEXT,
        status TEXT,
        prescription TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS billing (
        bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER,
        consultation_fee REAL,
        medicine_cost REAL,
        tax REAL,
        total_amount REAL,
        FOREIGN KEY(appointment_id) REFERENCES appointments(appointment_id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    ''')
    
    cursor.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", 
                   ("shubham", "1234", "admin"))

    conn.commit()
    conn.close()
    print("Database initialized successfully")

def open_dashboard():
    dash = tk.Tk()
    dash.title("MediTrack Dashboard")
    dash.geometry("400x400")

    tk.Label(dash, text="Welcome to MediTrack!", font=("Arial", 16)).pack(pady=20)
    tk.Button(dash, text="Patients", width=20, command=open_patient_form).pack(pady=5)
    tk.Button(dash, text="Appointments", width=20, command=open_appointments_form).pack(pady=5)
    tk.Button(dash, text="Doctors", width=20, command=open_doctor_form).pack(pady=5)
    tk.Button(dash, text="Billing", width=20, command=open_billing_form).pack(pady=5)
    tk.Button(dash, text="Search Patients", width=20, command=search_patients).pack(pady=5)
    tk.Button(dash, text="Search Appointments", width=20, command=search_appointments).pack(pady=5)
    tk.Button(dash, text="Manage Patients", width=20, command=manage_patients).pack(pady=5)
    tk.Button(dash, text="Logout", width=20, command=dash.destroy).pack(pady=20)
    


    dash.mainloop()

def open_patient_form():
    pf = tk.Toplevel()  
    pf.title("Add Patient")
    pf.geometry("400x400")

    tk.Label(pf, text="Add New Patient", font=("Arial", 14)).pack(pady=10)

    tk.Label(pf, text="Name").pack()
    name_entry = tk.Entry(pf)
    name_entry.pack()

    tk.Label(pf, text="Age").pack()
    age_entry = tk.Entry(pf)
    age_entry.pack()

    tk.Label(pf, text="Gender").pack()
    gender_entry = tk.Entry(pf)
    gender_entry.pack()

    tk.Label(pf, text="Contact").pack()
    contact_entry = tk.Entry(pf)
    contact_entry.pack()

    tk.Label(pf, text="Medical History").pack()
    medhist_entry = tk.Entry(pf)
    medhist_entry.pack()

    def save_patient():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        contact = contact_entry.get()
        medhist = medhist_entry.get()

        if not name or not age or not contact:
            messagebox.showerror("Error", "Name, Age, Contact are required!")
            return

        try:
            age = int(age)
        except:
            messagebox.showerror("Error", "Age must be a number")
            return

        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO patients (name, age, gender, contact, medical_history) VALUES (?, ?, ?, ?, ?)",
            (name, age, gender, contact, medhist)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Patient {name} added!")
        pf.destroy()  

    tk.Button(pf, text="Save Patient", command=save_patient).pack(pady=20)

def open_appointments_form():
    appt = tk.Toplevel()
    appt.title("Add Appointment")
    appt.geometry("400x400")

    tk.Label(appt, text="Add New Appointment", font=("Arial", 14)).pack(pady=10)

    conn = sqlite3.connect("meditrack.db")
    cursor = conn.cursor()

    # Patients list
    cursor.execute("SELECT patient_id, name FROM patients")
    patients = cursor.fetchall()
    patient_dict = {f"{pid} - {name}": pid for pid, name in patients}
    patient_var = tk.StringVar()
    if patients:
        patient_var.set(list(patient_dict.keys())[0])
    tk.Label(appt, text="Select Patient").pack()
    tk.OptionMenu(appt, patient_var, *patient_dict.keys()).pack()

    # Doctors list
    cursor.execute("SELECT doctor_id, name FROM doctors")
    doctors = cursor.fetchall()
    doctor_dict = {f"{did} - {name}": did for did, name in doctors}
    doctor_var = tk.StringVar()
    if doctors:
        doctor_var.set(list(doctor_dict.keys())[0])
    tk.Label(appt, text="Select Doctor").pack()
    tk.OptionMenu(appt, doctor_var, *doctor_dict.keys()).pack()

    tk.Label(appt, text="Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(appt)
    date_entry.pack()

    tk.Label(appt, text="Status").pack()
    status_entry = tk.Entry(appt)
    status_entry.pack()

    tk.Label(appt, text="Prescription").pack()
    prescription_entry = tk.Entry(appt)
    prescription_entry.pack()

    def save_appointment():
        patient_id = patient_dict.get(patient_var.get())
        doctor_id = doctor_dict.get(doctor_var.get()) if doctors else None
        date = date_entry.get()
        status = status_entry.get()
        prescription = prescription_entry.get()

        if not patient_id or not date:
            messagebox.showerror("Error", "Patient and Date are required")
            return

        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO appointments (patient_id, doctor_id, date, status, prescription) VALUES (?, ?, ?, ?, ?)",
            (patient_id, doctor_id, date, status, prescription)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Appointment added!")
        appt.destroy()

    tk.Button(appt, text="Save Appointment", command=save_appointment).pack(pady=20)

def open_doctor_form():
    doc = tk.Toplevel()
    doc.title("Add Doctor")
    doc.geometry("400x350")

    tk.Label(doc, text="Add New Doctor", font=("Arial", 14)).pack(pady=10)

    tk.Label(doc, text="Name").pack()
    name_entry = tk.Entry(doc)
    name_entry.pack()

    tk.Label(doc, text="Specialization").pack()
    spec_entry = tk.Entry(doc)
    spec_entry.pack()

    tk.Label(doc, text="Contact").pack()
    contact_entry = tk.Entry(doc)
    contact_entry.pack()

    def save_doctor():
        name = name_entry.get()
        spec = spec_entry.get()
        contact = contact_entry.get()

        if not name:
            messagebox.showerror("Error", "Name is required!")
            return

        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO doctors (name, specialization, contact) VALUES (?, ?, ?)",
            (name, spec, contact)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Doctor {name} added!")
        doc.destroy()

    tk.Button(doc, text="Save Doctor", command=save_doctor).pack(pady=20)


def open_billing_form():
    bill = tk.Toplevel()
    bill.title("Add Billing")
    bill.geometry("400x400")

    tk.Label(bill, text="Billing Details", font=("Arial", 14)).pack(pady=10)

    conn = sqlite3.connect("meditrack.db")
    cursor = conn.cursor()

    # Appointment list
    cursor.execute("SELECT appointment_id, patient_id FROM appointments")
    appointments = cursor.fetchall()
    appt_dict = {f"Appointment {aid} (Patient {pid})": aid for aid, pid in appointments}
    appt_var = tk.StringVar()
    if appointments:
        appt_var.set(list(appt_dict.keys())[0])

    tk.Label(bill, text="Select Appointment").pack()
    tk.OptionMenu(bill, appt_var, *appt_dict.keys()).pack()

    tk.Label(bill, text="Consultation Fee").pack()
    consult_entry = tk.Entry(bill)
    consult_entry.pack()

    tk.Label(bill, text="Medicine Cost").pack()
    med_entry = tk.Entry(bill)
    med_entry.pack()

    tk.Label(bill, text="Tax (%)").pack()
    tax_entry = tk.Entry(bill)
    tax_entry.pack()

    def save_billing():
        appt_id = appt_dict.get(appt_var.get())
        try:
            consultation = float(consult_entry.get())
            medicine = float(med_entry.get())
            tax = float(tax_entry.get())
        except:
            messagebox.showerror("Error", "Please enter valid numbers for fees/cost/tax")
            return

        total = consultation + medicine + (consultation + medicine) * tax / 100

        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO billing (appointment_id, consultation_fee, medicine_cost, tax, total_amount) VALUES (?, ?, ?, ?, ?)",
            (appt_id, consultation, medicine, tax, total)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Billing saved! Total = {total}")
        bill.destroy()

    tk.Button(bill, text="Save Billing", command=save_billing).pack(pady=20)

def search_patients():
    sp = tk.Toplevel()
    sp.title("Search Patients")
    sp.geometry("400x400")

    tk.Label(sp, text="Enter Regex Pattern (Medical History)", font=("Arial", 12)).pack(pady=10)
    pattern_entry = tk.Entry(sp)
    pattern_entry.pack()

    result_box = tk.Text(sp, height=15, width=45)
    result_box.pack(pady=10)

    def perform_search():
        pattern = pattern_entry.get()
        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, medical_history FROM patients")
        patients = cursor.fetchall()
        conn.close()

        result_box.delete("1.0", tk.END)

        for name, medhist in patients:
            if re.search(pattern, medhist, re.IGNORECASE):
                result_box.insert(tk.END, f"{name} : {medhist}\n")

    tk.Button(sp, text="Search", command=perform_search).pack(pady=10)


def search_appointments():
    sa = tk.Toplevel()
    sa.title("Search Appointments")
    sa.geometry("400x400")

    tk.Label(sa, text="Enter Regex Pattern (Status/Prescription)", font=("Arial", 12)).pack(pady=10)
    pattern_entry = tk.Entry(sa)
    pattern_entry.pack()

    result_box = tk.Text(sa, height=15, width=45)
    result_box.pack(pady=10)

    def perform_search():
        pattern = pattern_entry.get()
        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute("SELECT appointment_id, status, prescription FROM appointments")
        appointments = cursor.fetchall()
        conn.close()

        result_box.delete("1.0", tk.END)

        for aid, status, pres in appointments:
            if re.search(pattern, status + " " + (pres or ""), re.IGNORECASE):
                result_box.insert(tk.END, f"Appointment {aid} : {status} / {pres}\n")

    tk.Button(sa, text="Search", command=perform_search).pack(pady=10)

def manage_patients():
    mp = tk.Toplevel()
    mp.title("Manage Patients")
    mp.geometry("500x400")

    conn = sqlite3.connect("meditrack.db")
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, name FROM patients")
    patients = cursor.fetchall()
    conn.close()

    patient_dict = {f"{pid} - {name}": pid for pid, name in patients}
    patient_var = tk.StringVar()
    if patients:
        patient_var.set(list(patient_dict.keys())[0])

    tk.Label(mp, text="Select Patient").pack()
    tk.OptionMenu(mp, patient_var, *patient_dict.keys()).pack()

    tk.Label(mp, text="Update Name").pack()
    name_entry = tk.Entry(mp)
    name_entry.pack()

    tk.Label(mp, text="Update Age").pack()
    age_entry = tk.Entry(mp)
    age_entry.pack()

    def update_patient():
        pid = patient_dict.get(patient_var.get())
        name = name_entry.get()
        age = age_entry.get()
        if not pid or not name or not age:
            messagebox.showerror("Error", "Patient & new data required")
            return
        try:
            age = int(age)
        except:
            messagebox.showerror("Error", "Age must be a number")
            return
        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE patients SET name=?, age=? WHERE patient_id=?", (name, age, pid))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Patient updated!")

    def delete_patient():
        pid = patient_dict.get(patient_var.get())
        if not pid:
            return
        conn = sqlite3.connect("meditrack.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM patients WHERE patient_id=?", (pid,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Patient removed!")

    tk.Button(mp, text="Update Patient", command=update_patient).pack(pady=5)
    tk.Button(mp, text="Delete Patient", command=delete_patient).pack(pady=5)


def login():
    u = entry_user.get()
    p = entry_pass.get()

    conn = sqlite3.connect("meditrack.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Login", "Login Successful")
        root.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Login", "Invalid Username/Password")

init_db()  

root = tk.Tk()
root.title("MediTrack Login")
root.geometry("400x250")

tk.Label(root, text="MediTrack Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()