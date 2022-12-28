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
        tabletName = ttk.Combobox(dataFrameLeft, font=("times new roman", 12, "bold"), width=30)
        tabletName["values"]= ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        tabletName.current(0)
        tabletName.grid(row=0, column=1)

        lblReference = Label(dataFrameLeft, text="Reference No.", font=("arial", 12, "bold"), padx=2, pady=6)
        lblReference.grid(row=1, column=0, sticky=W)
        txtReference = Entry(dataFrameLeft, font=("arial", 13, "bold"), width= 29)
        txtReference.grid(row=1, column=1)

        lblDose = Label(dataFrameLeft, text="Dose", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(dataFrameLeft, text="No of Tablets", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(dataFrameLeft, text="Lot", font=("arial", 12, "bold"), padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(dataFrameLeft, text="Issue Date", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(dataFrameLeft, text="Exp Date", font=("arial", 12, "bold"), padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(dataFrameLeft, text="Daily Dose", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(dataFrameLeft, text="Side Effect", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(dataFrameLeft, text="Further Info", font=("arial", 12, "bold"), padx=10, pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtFurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(dataFrameLeft, text="Blood Pressure", font=("arial", 12, "bold"), padx=10, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(dataFrameLeft, text="Storage Advice", font=("arial", 12, "bold"), padx=10, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(dataFrameLeft, text="Medication", font=("arial", 12, "bold"), padx=10, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(dataFrameLeft, text="Patient Id", font=("arial", 12, "bold"), padx=10, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(dataFrameLeft, text="NhsNumber", font=("arial", 12, "bold"), padx=10, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(dataFrameLeft, text="Patient Name", font=("arial", 12, "bold"), padx=10, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPatientName.grid(row=6, column=3)

        lblDateOfBirth = Label(dataFrameLeft, text="Date Of Birth", font=("arial", 12, "bold"), padx=10, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(dataFrameLeft, text="Patient Address", font=("arial", 12, "bold"), padx=10, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(dataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPatientAddress.grid(row=8, column=3)

        # ---------- Data Frame Right ------------

        self.txtPrescription = Text(dataFrameRight, font=("arial", 12, "bold"), width=42, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ----------- Buttons --------------------

        btnPrescription = Button(buttonsFrame, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, padx=2, pady=6)
        btnPrescription.grid(row=0, column=1)

        btnPrescriptionData = Button(buttonsFrame, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=2)

        btnUpdate = Button(buttonsFrame, text="Update", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, padx=2, pady=6)
        btnUpdate.grid(row=0, column=3)

        btnDelete = Button(buttonsFrame, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, padx=2, pady=6)
        btnDelete.grid(row=0, column=4)

        btnClear = Button(buttonsFrame, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=21, padx=2, pady=6)
        btnClear.grid(row=0, column=5)

        btnExit = Button(buttonsFrame, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"),
                          width=21, padx=2, pady=6)
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


root = Tk()
rims = Hospital(root)

root.mainloop()