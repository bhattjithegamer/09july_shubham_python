
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import re
import csv
from datetime import datetime

DB_NAME = "meditrack.db"
INVOICE_CSV = "invoices.csv"

# ---------------------------
# ડેટાબેસ / સ્કીમા ઇનિશિયલાઇઝ
# ---------------------------
def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cr = conn.cursor()
        # users table
        cr.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                role TEXT
            )
        """)
        # patients table
        cr.execute("""
            CREATE TABLE IF NOT EXISTS patients(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                phone TEXT,
                disease TEXT,
                notes TEXT
            )
        """)
        # appointments table
        cr.execute("""
            CREATE TABLE IF NOT EXISTS appointments(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                doctor TEXT,
                date TEXT,
                time TEXT,
                type TEXT,
                notes TEXT,
                FOREIGN KEY(patient_id) REFERENCES patients(id)
            )
        """)
        # billing table
        cr.execute("""
            CREATE TABLE IF NOT EXISTS billing(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                appointment_id INTEGER,
                consultation REAL,
                medicines REAL,
                tax REAL,
                total REAL,
                date TEXT,
                FOREIGN KEY(patient_id) REFERENCES patients(id),
                FOREIGN KEY(appointment_id) REFERENCES appointments(id)
            )
        """)
        conn.commit()

        # Create a default admin if not exists
        cr.execute("SELECT * FROM users WHERE username='admin'")
        if not cr.fetchone():
            cr.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)",
                       ("admin", "admin123", "Admin"))
            conn.commit()
        conn.close()
    except Exception as e:
        print("DB Init Error:", e)

# ---------------------------
# OOP: Models
# ---------------------------
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @staticmethod
    def authenticate(username, password):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("SELECT username, role FROM users WHERE username=? AND password=?", (username, password))
            row = cr.fetchone()
            conn.close()
            if row:
                return User(row[0], row[1])
            else:
                return None
        except Exception as e:
            print("Auth Error:", e)
            return None

    @staticmethod
    def add_user(username, password, role):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)", (username, password, role))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Add user error:", e)
            return False

class Patient:
    def __init__(self, id=None, name="", age=0, phone="", disease="", notes=""):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.disease = disease
        self.notes = notes

    def save(self):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            if self.id:
                cr.execute("""UPDATE patients SET name=?, age=?, phone=?, disease=?, notes=? WHERE id=?""",
                           (self.name, self.age, self.phone, self.disease, self.notes, self.id))
            else:
                cr.execute("""INSERT INTO patients(name, age, phone, disease, notes) VALUES(?,?,?,?,?)""",
                           (self.name, self.age, self.phone, self.disease, self.notes))
                self.id = cr.lastrowid
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Patient save error:", e)
            return False

    @staticmethod
    def get_all():
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("SELECT id,name,age,phone,disease,notes FROM patients")
            rows = cr.fetchall()
            conn.close()
            return [Patient(*row) for row in rows]
        except Exception as e:
            print("Get all patients error:", e)
            return []

    @staticmethod
    def get_by_id(pid):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("SELECT id,name,age,phone,disease,notes FROM patients WHERE id=?", (pid,))
            row = cr.fetchone()
            conn.close()
            if row:
                return Patient(*row)
            return None
        except Exception as e:
            print("Get patient error:", e)
            return None

    @staticmethod
    def delete(pid):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("DELETE FROM patients WHERE id=?", (pid,))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Delete patient error:", e)
            return False

class Appointment:
    def __init__(self, id=None, patient_id=None, doctor="", date="", time="", type_="Consultation", notes=""):
        self.id = id
        self.patient_id = patient_id
        self.doctor = doctor
        self.date = date
        self.time = time
        self.type = type_
        self.notes = notes

    def save(self):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            if self.id:
                cr.execute("""UPDATE appointments SET patient_id=?, doctor=?, date=?, time=?, type=?, notes=? WHERE id=?""",
                           (self.patient_id, self.doctor, self.date, self.time, self.type, self.notes, self.id))
            else:
                cr.execute("""INSERT INTO appointments(patient_id, doctor, date, time, type, notes) VALUES(?,?,?,?,?,?)""",
                           (self.patient_id, self.doctor, self.date, self.time, self.type, self.notes))
                self.id = cr.lastrowid
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print("Appointment save error:", e)
            return False

    @staticmethod
    def get_by_patient(pid):
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("SELECT id,patient_id,doctor,date,time,type,notes FROM appointments WHERE patient_id=?", (pid,))
            rows = cr.fetchall()
            conn.close()
            return [Appointment(*row) for row in rows]
        except Exception as e:
            print("Get appointments error:", e)
            return []

    @staticmethod
    def get_all():
        try:
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("SELECT id,patient_id,doctor,date,time,type,notes FROM appointments")
            rows = cr.fetchall()
            conn.close()
            return [Appointment(*row) for row in rows]
        except Exception as e:
            print("Get all appointments error:", e)
            return []

class Billing:
    def __init__(self, id=None, patient_id=None, appointment_id=None, consultation=0.0, medicines=0.0, tax=0.0, total=0.0, date=None):
        self.id = id
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.consultation = consultation
        self.medicines = medicines
        self.tax = tax
        self.total = total
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_total(self):
        try:
            subtotal = float(self.consultation) + float(self.medicines)
            self.tax = round(subtotal * 0.05, 2)  # 5% tax as example
            self.total = round(subtotal + self.tax, 2)
        except Exception as e:
            print("Calculate total error:", e)
            raise

    def save(self):
        try:
            self.calculate_total()
            conn = sqlite3.connect(DB_NAME)
            cr = conn.cursor()
            cr.execute("""INSERT INTO billing(patient_id, appointment_id, consultation, medicines, tax, total, date)
                          VALUES(?,?,?,?,?,?,?)""",
                       (self.patient_id, self.appointment_id, self.consultation, self.medicines, self.tax, self.total, self.date))
            conn.commit()
            conn.close()
            # Save to CSV invoice
            self.save_to_csv()
            return True
        except Exception as e:
            print("Billing save error:", e)
            return False

    def save_to_csv(self):
        try:
            header = ["bill_id", "patient_id", "appointment_id", "consultation", "medicines", "tax", "total", "date"]
            row = [self.id or "", self.patient_id, self.appointment_id, self.consultation, self.medicines, self.tax, self.total, self.date]
            # append mode
            with open(INVOICE_CSV, "a", newline='') as f:
                writer = csv.writer(f)
                # write header if file empty
                f.seek(0)
                if f.tell() == 0:
                    writer.writerow(header)
                writer.writerow(row)
        except Exception as e:
            print("CSV save error:", e)

# ---------------------------
# Utility: regex search
# ---------------------------
def regex_search_patients(pattern):
    try:
        allp = Patient.get_all()
        prog = re.compile(pattern, re.IGNORECASE)
        filtered = [p for p in allp if prog.search(p.name or "") or prog.search(p.disease or "") or prog.search(p.notes or "")]
        return filtered
    except re.error as re_err:
        raise re_err
    except Exception as e:
        print("Regex search error:", e)
        return []

# ---------------------------
# GUI: Tkinter
# ---------------------------
class MediTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MediTrack - સરળ દર્દી વ્યવસ્થાપન")
        self.user = None
        self.build_login_screen()

    def build_login_screen(self):
        for w in self.root.winfo_children():
            w.destroy()
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack()

        tk.Label(frame, text="Users name (ઉપયોગકર્તાનું નામ):").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(frame, text="Password (પાસવર્ડ):").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(frame, text="Login (પ્રવેશ)", command=self.login).grid(row=2, column=0, pady=10)
        tk.Button(frame, text="New User (નવો વપરાશકર્તા)", command=self.new_user_prompt).grid(row=2, column=1)

    def login(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()
        if not u or not p:
            messagebox.showwarning("Warning", "બધી જાણકારી ભરો")
            return
        user = User.authenticate(u, p)
        if user:
            self.user = user
            messagebox.showinfo("સુવિચાર", f"સ્વાગત {user.username} ({user.role})")
            self.build_main_screen()
        else:
            messagebox.showerror("ભૂલ", "અમાન્ય username અથવા password")

    def new_user_prompt(self):
        # Only admin can add new users - but for simplicity allow creation after asking for admin password
        admin_pass = simpledialog.askstring("Admin pass", "Admin પાસવર્ડ નાખો (ડિફોલ્ટ admin123)", show="*")
        if admin_pass != "admin123":
            messagebox.showerror("બેપીર", "અમાન્ય admin પાસવર્ડ")
            return
        uname = simpledialog.askstring("Username", "નવું username નહિ નાખો")
        pwd = simpledialog.askstring("Password", "નવો password નાખો", show="*")
        role = simpledialog.askstring("Role", "Role નાંખો (Admin/Receptionist/Doctor)")
        if uname and pwd and role:
            ok = User.add_user(uname, pwd, role)
            if ok:
                messagebox.showinfo("બધુ સારું", "નવો વપરાશકર્તા બનાવી દીધો")
            else:
                messagebox.showerror("ભૂલ", "વપરાશકર્તા બનાવવામાં ભૂલ આવી")

    def build_main_screen(self):
        for w in self.root.winfo_children():
            w.destroy()
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Patient Menu
        patient_menu = tk.Menu(menubar, tearoff=0)
        patient_menu.add_command(label="Add Patient", command=self.add_patient_screen)
        patient_menu.add_command(label="List Patients", command=self.list_patients_screen)
        menubar.add_cascade(label="Patient", menu=patient_menu)

        # Appointment Menu
        appt_menu = tk.Menu(menubar, tearoff=0)
        appt_menu.add_command(label="New Appointment", command=self.new_appointment_screen)
        appt_menu.add_command(label="List Appointments", command=self.list_appointments_screen)
        menubar.add_cascade(label="Appointment", menu=appt_menu)

        # Billing
        menubar.add_command(label="Billing", command=self.billing_screen)

        # Reports
        menubar.add_command(label="Search (Regex)", command=self.search_screen)

        # Logout
        menubar.add_command(label="Logout", command=self.logout)

        # Default home
        home = tk.Label(self.root, text=f"MediTrack: Logged in as {self.user.username} ({self.user.role})", padx=10, pady=10)
        home.pack()

    def logout(self):
        self.user = None
        messagebox.showinfo("Logout", "લોગઆઉટ થઈ ગયું")
        self.build_login_screen()

    # ---------------------------
    # Patient screens
    # ---------------------------
    def add_patient_screen(self):
        win = tk.Toplevel(self.root)
        win.title("Add / Edit Patient")
        tk.Label(win, text="Name:").grid(row=0, column=0, sticky="w")
        name_e = tk.Entry(win)
        name_e.grid(row=0, column=1)

        tk.Label(win, text="Age:").grid(row=1, column=0, sticky="w")
        age_e = tk.Entry(win)
        age_e.grid(row=1, column=1)

        tk.Label(win, text="Phone:").grid(row=2, column=0, sticky="w")
        phone_e = tk.Entry(win)
        phone_e.grid(row=2, column=1)

        tk.Label(win, text="Disease:").grid(row=3, column=0, sticky="w")
        disease_e = tk.Entry(win)
        disease_e.grid(row=3, column=1)

        tk.Label(win, text="Notes:").grid(row=4, column=0, sticky="w")
        notes_e = tk.Entry(win)
        notes_e.grid(row=4, column=1)

        def save_patient():
            try:
                name = name_e.get().strip()
                age = int(age_e.get().strip()) if age_e.get().strip() else 0
                phone = phone_e.get().strip()
                disease = disease_e.get().strip()
                notes = notes_e.get().strip()
                if not name:
                    messagebox.showwarning("Warning", "નામ જરૂરી છે")
                    return
                p = Patient(None, name, age, phone, disease, notes)
                ok = p.save()
                if ok:
                    messagebox.showinfo("Saved", "Patient સાચવ્યો")
                    win.destroy()
                else:
                    messagebox.showerror("Error", "સાચવવામાં ભૂલ")
            except ValueError:
                messagebox.showerror("Error", "age માં નંબર મૂકવો")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Save", command=save_patient).grid(row=5, column=0, pady=10)
        tk.Button(win, text="Close", command=win.destroy).grid(row=5, column=1)

    def list_patients_screen(self):
        win = tk.Toplevel(self.root)
        win.title("List Patients")
        cols = ("id", "name", "age", "phone", "disease", "notes")
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=100)
        tree.pack(expand=True, fill="both")

        def load():
            for i in tree.get_children():
                tree.delete(i)
            for p in Patient.get_all():
                tree.insert("", "end", values=(p.id, p.name, p.age, p.phone, p.disease, p.notes))
        load()

        def edit_selected():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Warning", "પહેલી પસંદગી કરો")
                return
            item = tree.item(sel[0])["values"]
            pid = item[0]
            p = Patient.get_by_id(pid)
            if not p:
                messagebox.showerror("Error", "Patient ન મળ્યો")
                return
            # open edit window
            ew = tk.Toplevel(win)
            ew.title("Edit Patient")
            tk.Label(ew, text="Name:").grid(row=0, column=0)
            name_e = tk.Entry(ew); name_e.grid(row=0, column=1); name_e.insert(0, p.name)
            tk.Label(ew, text="Age:").grid(row=1, column=0)
            age_e = tk.Entry(ew); age_e.grid(row=1, column=1); age_e.insert(0, p.age)
            tk.Label(ew, text="Phone:").grid(row=2, column=0)
            phone_e = tk.Entry(ew); phone_e.grid(row=2, column=1); phone_e.insert(0, p.phone)
            tk.Label(ew, text="Disease:").grid(row=3, column=0)
            disease_e = tk.Entry(ew); disease_e.grid(row=3, column=1); disease_e.insert(0, p.disease)
            tk.Label(ew, text="Notes:").grid(row=4, column=0)
            notes_e = tk.Entry(ew); notes_e.grid(row=4, column=1); notes_e.insert(0, p.notes)

            def save_edit():
                try:
                    p.name = name_e.get().strip()
                    p.age = int(age_e.get().strip()) if age_e.get().strip() else 0
                    p.phone = phone_e.get().strip()
                    p.disease = disease_e.get().strip()
                    p.notes = notes_e.get().strip()
                    p.save()
                    messagebox.showinfo("Saved", "Patient બદલી ને સાચવ્યો")
                    ew.destroy()
                    load()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            tk.Button(ew, text="Save", command=save_edit).grid(row=5, column=0)
            tk.Button(ew, text="Close", command=ew.destroy).grid(row=5, column=1)

        def delete_selected():
            sel = tree.selection()
            if not sel:
                messagebox.showwarning("Warning", "પહેલી પસંદગી કરો")
                return
            item = tree.item(sel[0])["values"]
            pid = item[0]
            if messagebox.askyesno("Confirm", "શું તમે ખરેખર કાઢી નાખવા માંગો છો?"):
                Patient.delete(pid)
                load()

        btnf = tk.Frame(win)
        btnf.pack()
        tk.Button(btnf, text="Edit", command=edit_selected).pack(side="left", padx=5)
        tk.Button(btnf, text="Delete", command=delete_selected).pack(side="left", padx=5)
        tk.Button(btnf, text="Refresh", command=load).pack(side="left", padx=5)

    # ---------------------------
    # Appointment screens
    # ---------------------------
    def new_appointment_screen(self):
        win = tk.Toplevel(self.root)
        win.title("નવા એપોઇન્ટમેન્ટ")

        tk.Label(win, text="Patient ID:").grid(row=0, column=0)
        pid_e = tk.Entry(win); pid_e.grid(row=0, column=1)

        tk.Label(win, text="Doctor:").grid(row=1, column=0)
        doc_e = tk.Entry(win); doc_e.grid(row=1, column=1)

        tk.Label(win, text="Date (YYYY-MM-DD):").grid(row=2, column=0)
        date_e = tk.Entry(win); date_e.grid(row=2, column=1)

        tk.Label(win, text="Time (HH:MM):").grid(row=3, column=0)
        time_e = tk.Entry(win); time_e.grid(row=3, column=1)

        tk.Label(win, text="Type:").grid(row=4, column=0)
        type_e = tk.Entry(win); type_e.grid(row=4, column=1); type_e.insert(0, "Consultation")

        tk.Label(win, text="Notes:").grid(row=5, column=0)
        notes_e = tk.Entry(win); notes_e.grid(row=5, column=1)

        def save_appt():
            try:
                pid = int(pid_e.get().strip())
                # check patient exists
                if not Patient.get_by_id(pid):
                    messagebox.showerror("Error", "Patient ID ખોટો છે")
                    return
                ap = Appointment(None, pid, doc_e.get().strip(), date_e.get().strip(), time_e.get().strip(), type_e.get().strip(), notes_e.get().strip())
                ap.save()
                messagebox.showinfo("Saved", "Appointment સાચવ્યો")
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Patient ID number રાખો")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Save", command=save_appt).grid(row=6, column=0)
        tk.Button(win, text="Close", command=win.destroy).grid(row=6, column=1)

    def list_appointments_screen(self):
        win = tk.Toplevel(self.root)
        win.title("List Appointments")
        cols = ("id", "patient_id", "doctor", "date", "time", "type", "notes")
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=100)
        tree.pack(expand=True, fill="both")

        def load():
            for i in tree.get_children():
                tree.delete(i)
            for a in Appointment.get_all():
                tree.insert("", "end", values=(a.id, a.patient_id, a.doctor, a.date, a.time, a.type, a.notes))
        load()

        tk.Button(win, text="Refresh", command=load).pack()

    # ---------------------------
    # Billing screen
    # ---------------------------
    def billing_screen(self):
        win = tk.Toplevel(self.root)
        win.title("Billing / Invoice")

        tk.Label(win, text="Patient ID:").grid(row=0, column=0)
        pid_e = tk.Entry(win); pid_e.grid(row=0, column=1)

        tk.Label(win, text="Appointment ID (optional):").grid(row=1, column=0)
        appt_e = tk.Entry(win); appt_e.grid(row=1, column=1)

        tk.Label(win, text="Consultation fee:").grid(row=2, column=0)
        cons_e = tk.Entry(win); cons_e.grid(row=2, column=1)

        tk.Label(win, text="Medicines fee:").grid(row=3, column=0)
        med_e = tk.Entry(win); med_e.grid(row=3, column=1)

        def make_bill():
            try:
                pid = int(pid_e.get().strip())
                if not Patient.get_by_id(pid):
                    messagebox.showerror("Error", "Patient ન મળ્યો")
                    return
                apid = appt_e.get().strip()
                apid = int(apid) if apid else None
                consultation = float(cons_e.get().strip()) if cons_e.get().strip() else 0.0
                medicines = float(med_e.get().strip()) if med_e.get().strip() else 0.0
                bill = Billing(None, pid, apid, consultation, medicines)
                bill.calculate_total()
                # show summary and ask confirm
                msg = f"Subtotal: {consultation + medicines}\nTax(5%): {bill.tax}\nTotal: {bill.total}\n\nSave invoice?"
                if messagebox.askyesno("Confirm", msg):
                    ok = bill.save()
                    if ok:
                        messagebox.showinfo("Saved", f"Invoice saved. Total: {bill.total}")
                        win.destroy()
                    else:
                        messagebox.showerror("Error", "Invoice સાચવવામાં ભૂલ")
            except ValueError:
                messagebox.showerror("Error", "નંબરમાં ખોટ છે")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Generate & Save Invoice", command=make_bill).grid(row=4, column=0, pady=10)
        tk.Button(win, text="Close", command=win.destroy).grid(row=4, column=1)

    # ---------------------------
    # Search screen (Regex)
    # ---------------------------
    def search_screen(self):
        win = tk.Toplevel(self.root)
        win.title("Regex Search Patients / Disease")
        tk.Label(win, text="Regex pattern:").grid(row=0, column=0)
        pat_e = tk.Entry(win); pat_e.grid(row=0, column=1)

        cols = ("id", "name", "age", "phone", "disease", "notes")
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=100)
        tree.grid(row=2, column=0, columnspan=2)

        def do_search():
            pattern = pat_e.get().strip()
            if not pattern:
                messagebox.showwarning("Warning", "pattern નાખો")
                return
            try:
                results = regex_search_patients(pattern)
                for i in tree.get_children():
                    tree.delete(i)
                for p in results:
                    tree.insert("", "end", values=(p.id, p.name, p.age, p.phone, p.disease, p.notes))
            except re.error:
                messagebox.showerror("Regex Error", "અમાન્ય regex pattern")

        tk.Button(win, text="Search", command=do_search).grid(row=1, column=0, pady=5)
        tk.Button(win, text="Close", command=win.destroy).grid(row=1, column=1, pady=5)

# ---------------------------
# Run app
# ---------------------------
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = MediTrackApp(root)
    root.geometry("700x400")
    root.mainloop()
