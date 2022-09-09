import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# TAB1
connection = sqlite3.connect('PatientenDatenbank.db')
THD = "THD"
Versicherungsnummer = "Versicherungsnummer"
vorName = "Vorname"
Nachname = "Nachname"
Versicherungstyp = "Versicherungstyp"
Adresse = "Adresse"
Geburtsdatum = "Geburtsdatum"
Geschlecht = "Geschlecht"

# TAB2
connection = sqlite3.connect('RechnungenDatenbank.db')
THD_LEISTUNGEN = "THD_LEISTUNGEN"
Leistungsnummer = "Leistungsnummer"
Leistungsname = "Leistung"
Privat = "Privatpreis"
Kassen = "Kassenpreis"


class main:
    def __init__(self, mainwindow):
        mainwindow.title("Patientenverwaltung")
        mainwindow.resizable(width=False, height=False)
        mainwindow.geometry("400x550")

        # Tab erschaffung
        tabControl = ttk.Notebook(mainwindow)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Patienten')
        tabControl.add(tab2, text='Leistungen')
        tabControl.add(tab3, text='Rechnungen')
        tabControl.pack(expand=1, fill="both")

        Tab1(tab1)
        Tab2(tab2)


class windowtab1():
    def __init__(self, tab1):
        global versicherungFeld, vornameFeld, nachnameFeld, versicherungstypFeld, adresseFeld, geburtsdatumFeld, geschlechtFeld
        global list
        global THD, vorName, Nachname, Adresse, Versicherungstyp, Geburtsdatum, Geschlecht
        global platzhalter1, miniwindow

        # --------------------------Datenbank-------------------------------------------------#
        # connection = sqlite3.connect('PatientenDatenbank.db')
        connection.execute(
            " CREATE TABLE IF NOT EXISTS " + THD + " ( " + Versicherungsnummer + " INTEGER PRIMARY KEY AUTOINCREMENT, "
             + Versicherungstyp + " TEXT,  " + vorName + " TEXT, "
            + Nachname + " TEXT, " + Adresse + " TEXT, " + Geburtsdatum + " TEXT, " + Geschlecht + " TEXT);")

        # --------------------------Text vor dem Eingabefeld-------------------------------------------------#
        alabel = tk.Label(tab1, text='Patientenverwaltung', width=20, bg='gray35')
        alabel.config(font=("System", 20))
        alabel.grid(row=0, columnspan=2, padx=20, pady=5)
        versicherunglabel = tk.Label(tab1, text="Versicherungsnummer:", width=20, anchor='w', font=("System", 12)).grid(
            column=0, row=1, padx=0, pady=0)
        vornameLabel = tk.Label(tab1, text="Vorame:", width=20, anchor='w', font=("System", 12)).grid(column=0, row=2,
                                                                                                      padx=0, pady=0)
        nachnameLabel = tk.Label(tab1, text="Nachname:", width=20, anchor='w', font=("System", 12)).grid(column=0,
                                                                                                         row=3, padx=0,
                                                                                                         pady=0)
        versicherungstypLabel = tk.Label(tab1, text="Versicherungstyp:", width=20, anchor='w',
                                         font=("System", 12)).grid(column=0, row=4, padx=0, pady=0)
        adresseLabel = tk.Label(tab1, text="Adresse:", width=20, anchor='w', font=("System", 12)).grid(column=0, row=5,
                                                                                                       padx=0, pady=0)
        geburtsdatumLabel = tk.Label(tab1, text="Geburtsdatum:", width=20, anchor='w', font=("System", 12)).grid(
            column=0, row=6, padx=0, pady=0)
        geschlechtLabel = tk.Label(tab1, text="Geschlecht:", width=20, anchor='w', font=("System", 12)).grid(column=0,
                                                                                                             row=7,
                                                                                                             padx=0,
                                                                                                             pady=0)

        versicherungFeld = tk.Entry(tab1, width=20)
        vornameFeld = tk.Entry(tab1, width=20)
        nachnameFeld = tk.Entry(tab1, width=20)
        versicherungstypFeld = tk.Entry(tab1, width=20)
        adresseFeld = tk.Entry(tab1, width=20)
        geburtsdatumFeld = tk.Entry(tab1, width=20)
        geschlechtFeld = tk.Entry(tab1, width=20)

        # Positionierung
        versicherungFeld.grid(row=1, column=1, padx=0, pady=0)
        vornameFeld.grid(row=2, column=1, padx=0, pady=0)
        nachnameFeld.grid(row=3, column=1, padx=0, pady=0)
        versicherungstypFeld.grid(row=4, column=1, padx=0, pady=0)
        adresseFeld.grid(row=5, column=1, padx=0, pady=0)
        geburtsdatumFeld.grid(row=6, column=1, padx=0, pady=0)
        geschlechtFeld.grid(row=7, column=1, padx=0, pady=0)


class Tab1():
    def __init__(self, tab1):

        windowtab1(tab1)
        # Buttons
        Button(tab1, text="Hinzufügen", width=11, command=lambda: self.hinzufuegen()).grid(row=8, column=0, padx=0, pady=10)
        Button(tab1, text="Editieren", width=11, command=lambda: self.editieren()).grid(row=8, column=1)
        Button(tab1, text="Löschen", width=11, command=lambda: self.loeschen()).grid(row=9, column=0, pady=0)
        Button(tab1, text="Liste", width=11, command=lambda: self.liste()).grid(row=9, column=1)

    def hinzufuegen(self):

        self.versicherung = int(versicherungFeld.get())
        versicherungFeld.delete(0, tk.END)
        self.vorname1 = vornameFeld.get()
        vornameFeld.delete(0, tk.END)
        self.nachname = nachnameFeld.get()
        nachnameFeld.delete(0, tk.END)
        self.versicherungstyp = versicherungstypFeld.get()
        versicherungstypFeld.delete(0, tk.END)
        self.adresse = adresseFeld.get()
        adresseFeld.delete(0, tk.END)
        self.geburtsdatum = geburtsdatumFeld.get()
        geburtsdatumFeld.delete(0, tk.END)
        self.geschlecht = geschlechtFeld.get()
        geschlechtFeld.delete(0, tk.END)

        connection.execute(
            "INSERT INTO " + THD + " ( " + Versicherungsnummer + ", " + Versicherungstyp + ", " + vorName + ", "
            + Nachname + ", " + Adresse + ", " + Geburtsdatum + ", " + Geschlecht + ") VALUES (" + str(
                self.versicherung) + ", '" + self.versicherungstyp + "', '"
            + self.vorname1 + "', '" + self.nachname + "', '" + self.adresse + "', '" + self.geburtsdatum + "', '" + self.geschlecht + "'); ")
        connection.commit()
        messagebox.showinfo("Erfolgreich", "Patient wurde Hinzugefügt.")

    def loeschen(self):

        self.miniwindow = tk.Tk()
        self.miniwindow.title('Löschen')
        self.miniwindow.geometry('{}x{}'.format(500, 200))

        self.tk = tk.Label(self.miniwindow, text='Versicherungsnummer eingeben', font=("System", 12)).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=50,
                                                                                                           pady=50)
        self.platzhalter1 = tk.Entry(self.miniwindow)
        self.platzhalter1.grid(row=0, column=1)
        self.buttonentfernen = tk.Button(self.miniwindow, text='Löschen', command=self.entfernen).grid(row=1, column=1,
                                                                                                       pady=0)

        self.miniwindow.mainloop()

    def entfernen(self):
        self.platzhalter2 = int(self.platzhalter1.get())
        self.warten2 = connection.execute(
            "SELECT * FROM " + THD + " WHERE " + Versicherungsnummer + " = {}".format(self.platzhalter2))
        if self.warten2:
            connection.execute(
                "DELETE FROM " + THD + " WHERE " + Versicherungsnummer + " =  {}".format(self.platzhalter2))
            connection.commit()
            self.miniwindow.destroy()
            messagebox.showinfo('Fertig', "Daten wurden gelöscht")
        else:
            messagebox.showerror("Fehler", "Es gibt diese Versicherungsnummer nicht.")

    def editieren(self):
        self.versicherung = int(versicherungFeld.get())
        versicherungFeld.delete(0, tk.END)
        self.vorname1 = vornameFeld.get()
        vornameFeld.delete(0, tk.END)
        self.nachname = nachnameFeld.get()
        nachnameFeld.delete(0, tk.END)
        self.versicherungstyp = versicherungstypFeld.get()
        versicherungstypFeld.delete(0, tk.END)
        self.adresse = adresseFeld.get()
        adresseFeld.delete(0, tk.END)
        self.geburtsdatum = geburtsdatumFeld.get()
        geburtsdatumFeld.delete(0, tk.END)
        self.geschlecht = geschlechtFeld.get()
        geschlechtFeld.delete(0, tk.END)

        connection.execute(
            "UPDATE " + THD + " SET " + Versicherungstyp + " = " + "'" + self.versicherungstyp + "', " + vorName + " =" + "'" + self.vorname1 + "', " + Adresse + " = '"
            + self.adresse + "', " + Nachname + " = '" + self.nachname + "', " + Geschlecht + " ='" + self.geschlecht + "', " + Geburtsdatum + " = '"
            + self.geburtsdatum + "' WHERE " + Versicherungsnummer + " =  {}".format(self.versicherung))
        connection.commit()
        messagebox.showinfo('Aktualisiert', 'Daten wurden aktualisiert')

    def liste(self):
        self.secondWindow = tk.Tk()
        self.secondWindow.title("Informationen")
        self.secondWindow.resizable(width=False, height=False)
        self.secondWindow.geometry('{}x{}'.format(950, 300))
        # secondWindow.iconbitmap('C:/Users/Erwin/Desktop/logo.ico')
        self.alabel = tk.Label(self.secondWindow, text='Patienten Informationen', width=52, bg='gray35')
        self.alabel.config(font=("System", 30))
        self.alabel.pack()

        # -------------------Raster-------------------#

        self.tree = ttk.Treeview(self.secondWindow)
        self.tree['columns'] = (
        "Versicherungsnummer", "Versicherungstyp", "Vorame", "Nachname", "Adresse", "Geburtsdatum", "Geschlecht",)
        self.tree.column("#0", width=85)
        self.tree.column("Versicherungsnummer", width=150)
        self.tree.column("Versicherungstyp", width=150)
        self.tree.column("Vorame", width=100)
        self.tree.column("Nachname", width=100)
        self.tree.column("Adresse", width=150)
        self.tree.column("Geburtsdatum", width=100)
        self.tree.column("Geschlecht", width=80)
        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Versicherungsnummer", text="Versicherungsnummer")
        self.tree.heading("Versicherungstyp", text="Versicherungstyp")
        self.tree.heading("Vorame", text="Vorame")
        self.tree.heading("Nachname", text="Nachname")
        self.tree.heading("Adresse", text="Adresse")
        self.tree.heading("Geburtsdatum", text="Geburtsdatum")
        self.tree.heading("Geschlecht", text="Geschlecht")

        #########################################################################################################################################################################
        # --------------------------Patienten Aufzählung-------------------------------------------------#
        self.cursor = connection.execute("SELECT * FROM " + THD + " ;")
        i = 0

        for row in self.cursor:
            self.tree.insert('', i, text="Patient " + str(i + 1),
                             values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i = i + 1

        self.tree.pack()
        self.secondWindow.mainloop()


#########################################################################################TAB2###########################################################################################
class windowtab2():
    def __init__(self, tab2):
        global leistungsnummerFeld, leistungFeld, privatFeld, kassenFeld, loeschenFeld
        global list
        global THD_LEISTUNGEN, Leistungsnummer, Leistungsname, Privat, Kassen

        # --------------------------Datenbank-------------------------------------------------#

        connection.execute(
            " CREATE TABLE IF NOT EXISTS " + THD_LEISTUNGEN + " ( " + Leistungsnummer + " INTEGER PRIMARY KEY AUTOINCREMENT, " + Leistungsname +
            " TEXT, " + Privat + " TEXT, " + Kassen + " TEXT);")

        # --------------------------Text vor dem Eingabefeld-------------------------------------------------#
        alabel = tk.Label(tab2, text='Patientenverwaltung', width=20, bg='gray35')
        alabel.config(font=("System", 20))
        alabel.grid(row=0, columnspan=4, padx=20, pady=5)
        LeistungsnummerLabel = tk.Label(tab2, text="Leistungsnummer:", width=20, anchor='e', font=("System", 11)).grid(
            column=0,
            row=1)
        LeistungsnameLabel = tk.Label(tab2, text="Leistung:", width=20, anchor='e', font=("System", 11)).grid(column=0,
                                                                                                              row=2)
        PrivatLabel = tk.Label(tab2, text="Preis für Privat in €:", width=20, anchor='e', font=("System", 11)).grid(
            column=0, row=3)
        KassenLabel = tk.Label(tab2, text="Preis für Kassen in €:", width=20, anchor='e', font=("System", 11)).grid(
            column=0, row=4)
        LöschenLabel = tk.Label(tab2, text="Leistungsnummer Löschen:", width=25, anchor='center',
                                font=("System", 11)).grid(column=0, row=7)

        # ----------------------------------------Eingabe Felder----------------------------------------------------------------------
        leistungsnummerFeld = tk.Entry(tab2, width=20)
        leistungFeld = tk.Entry(tab2, width=20)
        privatFeld = tk.Entry(tab2, width=20)
        kassenFeld = tk.Entry(tab2, width=20)
        loeschenFeld = tk.Entry(tab2, width=20)

        # Positionierung
        leistungsnummerFeld.grid(row=1, column=1, padx=0, pady=0)
        leistungFeld.grid(row=2, column=1, padx=0, pady=0)
        privatFeld.grid(row=3, column=1, padx=0, pady=0)
        kassenFeld.grid(row=4, column=1, padx=0, pady=0)
        loeschenFeld.grid(row=7, column=1, padx=0, pady=0)

        tree1 = ttk.Treeview(tab2)
        tree1.grid(row=9, columnspan=100, padx=10)
        tree1['columns'] = ("Leistungsnummer", "Leistung", "Privat", "Kasse")
        tree1.column("#0", width=0, stretch=NO)
        tree1.column("Leistungsnummer", width=120)
        tree1.column("Leistung", width=80)
        tree1.column("Privat", width=80)
        tree1.column("Kasse", width=100)
        tree1.heading("#0", text="", anchor=W)
        tree1.heading("Leistungsnummer", text="Leistungsnummer")
        tree1.heading("Leistung", text="Leistung")
        tree1.heading("Privat", text="Privat in €")
        tree1.heading("Kasse", text="Kasse in €")
        cursor = connection.execute("SELECT * FROM " + THD_LEISTUNGEN + " ;")
        z = 0

        for row in cursor:
            tree1.insert('', z, text="" + str(z + 1), values=(row[0], row[1], row[2], row[3]))
            z = z + 1


class Tab2():
    def __init__(self, tab2):

        windowtab2(tab2)

        # Buttons

        Button(tab2, text="Hinzufügen", width=11, command=lambda: self.hinzufuegen_tab2()).grid(row=5, column=0, padx=0,
                                                                                                pady=10)
        Button(tab2, text="Editieren", width=11, command=lambda: self.editieren_tab2()).grid(row=5, column=1, padx=0,
                                                                                             pady=10)
        Button(tab2, text="Löschen", width=11, command=lambda: self.loeschen_tab2()).grid(row=8, column=0,
                                                                                          columnspan=100, padx=0,
                                                                                          pady=10)

    def hinzufuegen_tab2(self):
        self.leistungsnummer = int(leistungsnummerFeld.get())
        leistungsnummerFeld.delete(0, tk.END)
        self.leistung = leistungFeld.get()
        leistungFeld.delete(0, tk.END)
        self.privat = privatFeld.get()
        privatFeld.delete(0, tk.END)
        self.kassen = kassenFeld.get()
        kassenFeld.delete(0, tk.END)
        connection.execute(
            "INSERT OR REPLACE INTO " + THD_LEISTUNGEN + " ( " + Leistungsnummer + ", " + Leistungsname + ", " + Privat + ", " + Kassen + ") VALUES (" + str(
                self.leistungsnummer) + ", '" + self.leistung + "', '" + self.privat + "', '" + self.kassen + "'); ")
        connection.commit()
        messagebox.showinfo("Erfolgreich", "Leistung wurde Hinzugefügt. Bitte Programm neu starten")

    def loeschen_tab2(self):
        self.y = int(loeschenFeld.get())
        self.warten = connection.execute(
            "SELECT * FROM " + THD_LEISTUNGEN + " WHERE " + Leistungsnummer + " = {}".format(self.y))
        if self.warten:
            connection.execute(
                "DELETE FROM " + THD_LEISTUNGEN + " WHERE " + Leistungsnummer + " =  {}".format(self.y))
            connection.commit()
            messagebox.showinfo('Fertig', "Daten wurden gelöscht. Bitte Programm neu starten")
        else:
            messagebox.showerror("Fehler", "Leistungsnummer nicht vorhanden.")

    def editieren_tab2(self):
        self.leistungsnummer1 = int(leistungsnummerFeld.get())
        leistungsnummerFeld.delete(0, tk.END)
        self.leistung = leistungFeld.get()
        leistungFeld.delete(0, tk.END)
        self.privat = privatFeld.get()
        privatFeld.delete(0, tk.END)
        self.kasse = kassenFeld.get()
        kassenFeld.delete(0, tk.END)
        connection.execute(
            "UPDATE " + THD_LEISTUNGEN + " SET " + Leistungsname + " =" + "'" + self.leistung + "', " + Privat + " = '"
            + self.privat + "', " + Kassen + " = '" + self.kasse + "' WHERE " + Leistungsnummer + " =  {}".format(
                self.leistungsnummer1))
        connection.commit()
        messagebox.showinfo('Aktualisiert', 'Daten wurden aktualisiert. Bitte Programm neu starten')


###################################################################################################START Funktion ;(#################################################################################

def start():
    main(mainwindow)

    mainwindow.mainloop()


#############################################################################MAIN###########################################################################################


mainwindow = tk.Tk()

start()
