from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.NameOfTablet = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NoOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.BloodPressure = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lblTitle = Label(self.root, text="HOSPITAL MANAGEMENT SYSTEM", bd=20, relief=RIDGE, bg="white", fg="red", font=("times new roman", 50, "bold"))
        lblTitle.pack(side=TOP, fill=X)

        # ------------ Data Frame -----------
        dataFrame = Frame(self.root, bd=15, relief=RIDGE)
        dataFrame.place(x=0, y=115, width=1367, height=400)

        dataFrameLeft = LabelFrame(dataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"),
                                   text="Patient Information")
        dataFrameLeft.place(x=0, y=5, width=895, height=350)

        dataFrameRight = LabelFrame(dataFrame, bd=10, padx=20, relief=RIDGE, font=("arial", 12, "bold"),
                                   text="Prescription")
        dataFrameRight.place(x=900, y=5, width=435, height=350)

        # ---------- Buttons Frame ------------

        buttonsFrame = Frame(self.root, bd=5, relief=RIDGE)
        buttonsFrame.place(x=0, y=517, width=1367, height=40)

        # ---------- Details Frame ------------

        detailsFrame = Frame(self.root, bd=5, relief=RIDGE)
        detailsFrame.place(x=0, y=557, width=1367, height=150)

        # ----------- Data Frame Left -------------

        lblTabletName = Label(dataFrameLeft, text="Names of Tablets", font=("arial", 12, "bold"), padx=2, pady=3)
        lblTabletName.grid(row=0, column=0, sticky=W)

            # dropbox == combobox
        tabletName = ttk.Combobox(dataFrameLeft, textvariable=self.NameOfTablet, font=("times new roman", 12, "bold"), width=30)
        tabletName["values"]= ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        tabletName.current(0)
        tabletName.grid(row=0, column=1)

        lblReference = Label(dataFrameLeft, text="Reference No.", font=("arial", 12, "bold"), padx=2, pady=6)
        lblReference.grid(row=1, column=0, sticky=W)
        txtReference = Entry(dataFrameLeft, textvariable=self.Ref, font=("arial", 13, "bold"), width= 29)
        txtReference.grid(row=1, column=1)

        lblDose = Label(dataFrameLeft, text="Dose", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(dataFrameLeft, textvariable=self.Dose, font=("arial", 13, "bold"), width=29)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(dataFrameLeft, text="No of Tablets", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(dataFrameLeft, textvariable=self.NoOfTablets, font=("arial", 13, "bold"), width=29)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(dataFrameLeft, text="Lot", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(dataFrameLeft, textvariable=self.Lot, font=("arial", 13, "bold"), width=29)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(dataFrameLeft, text="Issue Date", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(dataFrameLeft, textvariable=self.IssueDate, font=("arial", 13, "bold"), width=29)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(dataFrameLeft, text="Exp Date", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(dataFrameLeft,textvariable=self.ExpDate, font=("arial", 13, "bold"), width=29)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(dataFrameLeft, text="Daily Dose", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(dataFrameLeft, textvariable=self.DailyDose, font=("arial", 13, "bold"), width=29)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(dataFrameLeft, text="Side Effect", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(dataFrameLeft, textvariable=self.SideEffect, font=("arial", 13, "bold"), width=29)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(dataFrameLeft, text="Further Info", font=("arial", 12, "bold"), padx=10, pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(dataFrameLeft, textvariable=self.FurtherInformation, font=("arial", 13, "bold"), width=29)
        txtFurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(dataFrameLeft, text="Blood Pressure", font=("arial", 12, "bold"), padx=10, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(dataFrameLeft, textvariable=self.BloodPressure, font=("arial", 13, "bold"), width=29)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(dataFrameLeft, text="Storage Advice", font=("arial", 12, "bold"), padx=10, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(dataFrameLeft, textvariable=self.StorageAdvice, font=("arial", 13, "bold"), width=29)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(dataFrameLeft, text="Medication", font=("arial", 12, "bold"), padx=10, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(dataFrameLeft, textvariable=self.HowToUseMedication, font=("arial", 13, "bold"), width=29)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(dataFrameLeft, text="Patient Id", font=("arial", 12, "bold"), padx=10, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(dataFrameLeft, textvariable=self.PatientId, font=("arial", 13, "bold"), width=29)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(dataFrameLeft, text="NhsNumber", font=("arial", 12, "bold"), padx=10, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(dataFrameLeft, textvariable=self.NhsNumber, font=("arial", 13, "bold"), width=29)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(dataFrameLeft, text="Patient Name", font=("arial", 12, "bold"), padx=10, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(dataFrameLeft, textvariable=self.PatientName, font=("arial", 13, "bold"), width=29)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(dataFrameLeft, text="Date Of Birth", font=("arial", 12, "bold"), padx=10, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(dataFrameLeft, textvariable=self.DateOfBirth, font=("arial", 13, "bold"), width=29)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(dataFrameLeft, text="Patient Address", font=("arial", 12, "bold"), padx=10, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(dataFrameLeft, textvariable=self.PatientAddress, font=("arial", 13, "bold"), width=29)
        txtPatientAddress.grid(row=8, column=3)

        # ---------- Data Frame Right ------------

        self.txtPrescription = Text(dataFrameRight, font=("arial", 12, "bold"), width=42, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ----------- Buttons --------------------

        btnPrescription = Button(buttonsFrame, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, command=self.iPrescription, padx=2, pady=6)
        btnPrescription.grid(row=0, column=1)

        btnPrescriptionData = Button(buttonsFrame, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, command=self.iPrescriptionData, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=2)

        btnUpdate = Button(buttonsFrame, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, command=self.update_data, padx=2, pady=6)
        btnUpdate.grid(row=0, column=3)

        btnDelete = Button(buttonsFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, command=self.idelete, padx=2, pady=6)
        btnDelete.grid(row=0, column=4)

        btnClear = Button(buttonsFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, command=self.clear, padx=2, pady=6)
        btnClear.grid(row=0, column=5)

        btnExit = Button(buttonsFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),
                          width=21, command=self.iExit, padx=2, pady=6)
        btnExit.grid(row=0, column=6)

        # ----- Details Frame ----------
        #     ----- Scrollbar -------
        scroll_x = ttk.Scrollbar(detailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(detailsFrame, columns=("NameOfTable", "Ref", "Dose", "NoOfTablets",
                                            "Lot", "IssueDate", "ExpDate", "DailyDose", "Storage", "NhsNumber",
                                            "PName", "DoB", "Address"), xscrollcommand=scroll_x.set,
                                            yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview())
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview())

        self.hospital_table.heading("NameOfTable", text="Name Of Table")
        self.hospital_table.heading("Ref", text="Reference No.")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NoOfTablets", text="No Of Tablets")
        self.hospital_table.heading("Lot", text="Lot")
        self.hospital_table.heading("IssueDate", text="Issue Date")
        self.hospital_table.heading("ExpDate", text="Exp Date")
        self.hospital_table.heading("DailyDose", text="Daily Dose")
        self.hospital_table.heading("Storage", text="Storage")
        self.hospital_table.heading("NhsNumber", text="Nhs Number")
        self.hospital_table.heading("PName", text="Patient Name")
        self.hospital_table.heading("DoB", text="DoB")
        self.hospital_table.heading("Address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("NameOfTable", width=100)
        self.hospital_table.column("Ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("NoOfTablets", width=100)
        self.hospital_table.column("Lot", width=100)
        self.hospital_table.column("IssueDate", width=100)
        self.hospital_table.column("ExpDate", width=100)
        self.hospital_table.column("DailyDose", width=100)
        self.hospital_table.column("Storage", width=100)
        self.hospital_table.column("NhsNumber", width=100)
        self.hospital_table.column("PName", width=100)
        self.hospital_table.column("DoB", width=100)
        self.hospital_table.column("Address", width=100)


        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

        # ------------ Functionality Declaration ---------------

    def iPrescriptionData(self):
        if self.NameOfTablet.get()=="" or self.Ref.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost", user="abhishek", passwd="mitra1234", database="mydb1")
            myCursor = con.cursor()
            query = "insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (
                self.NameOfTablet.get(),
                self.Ref.get(),
                self.Dose.get(),
                self.NoOfTablets.get(),
                self.Lot.get(),
                self.IssueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.NhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            )
            myCursor.execute(query, data)
            con.commit()
            con.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="abhishek", passwd="mitra1234", database="mydb1")
        myCursor = con.cursor()
        myCursor.execute("update hospital set NameOfTablets=%s, Dose=%s, NumberOfTablets=%s, Lot=%s, IssueDate=%s, ExpDate=%s, DailyDose=%s, Storage=%s, NhsNumber=%s, PatientName=%s, DoB=%s, PatientAddress=%s where ReferenceNo=%s", (
            self.NameOfTablet.get(),
            self.Dose.get(),
            self.NoOfTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.NhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.Ref.get(),
        ))
        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been updated")

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="abhishek", passwd="mitra1234", database="mydb1")
        myCursor = con.cursor()
        myCursor.execute("select * from hospital")
        rows = myCursor.fetchall()
        if len(rows) != 0:
            # self.hospital_table.delete(self.hospital_table.get_children())
            for x in self.hospital_table.selection():
                self.hospital_table.delete(x)
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            con.commit()
        con.close()


    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.NameOfTablet.set(row[0])
        self.Ref.set(row[1])
        self.Dose.set(row[2])
        self.NoOfTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.NhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablet:\t\t\t" + self.NameOfTablet.get() + "\n")
        self.txtPrescription.insert(END, "Reference Number:\t\t\t" + self.Ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + self.NoOfTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END, "Expiry Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.SideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "Patient ID:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "NhsNumber:\t\t\t" + self.NhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date Of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        con = mysql.connector.connect(host="localhost", user="abhishek", passwd="mitra1234", database="mydb1")
        myCursor = con.cursor()
        query = "delete from hospital where ReferenceNo=%s"
        data = (self.Ref.get(),)

        myCursor.execute(query, data)
        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient data deleted successfully")


    def clear(self):
        self.NameOfTablet.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NoOfTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.NhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.BloodPressure.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm Exit..")
        if iExit > 0:
            root.destroy()
            return

root = Tk()
rims = Hospital(root)

root.mainloop()