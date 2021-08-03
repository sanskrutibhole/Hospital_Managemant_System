from tkinter import *
from tkinter import ttk

import random
import time
import datetime

import tkinter.messagebox
import os
import tempfile
import pymysql


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        Nameoftablets = StringVar()
        ref = StringVar()
        Dose = StringVar()
        NumberofTablets = StringVar()
        Lot = StringVar()
        Issuedate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        #sideEffect = StringVar()
        #FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        #DrivingUsingMachine = StringVar()
        #HowToUseMedication = StringVar()
        #PatientId = StringVar()
        nhsNumber = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        PatientAddress = StringVar()

        #=======================Functinally Declaration=====================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("MySQL Connection","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Clear():
            Nameoftablets.set("")
            self.txtref.delete(0,END)
            self.txtDose.delete(0,END)
            self.txtNoOftablets.delete(0,END)
            self.txtLot.delete(0,END)
            self.txtissueDate.delete(0,END)
            self.txtExpDate.delete(0,END)
            self.txtDailyDose.delete(0,END)
            self.txtStorage.delete(0,END)
            self.txtNhsNumber.delete(0,END)
            self.txtPatientname.delete(0,END)
            self.txtDateOfBirth.delete(0,END)
            self.txtPatientAddress.delete(0,END)
            self.textPrescription.delete('1.0',END)
            


        
        def iPrescriptionData():
            if Nameoftablets.get()=="" or ref.get()=="":
                tkinter.messagebox.showerror("Error", "All Fields are required")
            else:

                sqlCon=pymysql.connect(host="localhost",user="root",password="<your_password>",database="mydata")

                cur=sqlCon.cursor()
                cur.execute("insert into mydata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Nameoftablets.get(),ref.get(),Dose.get(),NumberofTablets.get(),Lot.get(),Issuedate.get(),ExpDate.get(),DailyDose.get(),StorageAdvice.get(),nhsNumber.get(),PatientName.get(),DateOfBirth.get(),PatientAddress.get()))
             
                sqlCon.commit()
                fatch_data()
                sqlCon.close()
                tkinter.messagebox.showinfo("success","record has been inserted")
            
        def fatch_data():
            sqlCon=pymysql.connect(host="localhost",user="root",password="<your_password>",database="mydata")

            cur=sqlCon.cursor()
            cur.execute("select * from mydata")
            
            rows=cur.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("",END,values=row)
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connection","Record Displayed Succesfully")

        def patientInfo(ev):
            viewInfo=self.hospital_table.focus()
            learnerData=self.hospital_table.item(viewInfo)
            row=learnerData['values']
            Nameoftablets.set(row[0]) 
            ref.set(row[1]) 
            Dose.set(row[2])
            NumberofTablets.set(row[3])
            Lot.set(row[4])
            Issuedate.set(row[5])
            ExpDate.set(row[6])
            DailyDose.set(row[7])
            StorageAdvice.set(row[8])
            nhsNumber.set(row[9])
            PatientName.set(row[10])
            DateOfBirth.set(row[11])
            PatientAddress.set(row[12])

        def update():
            sqlCon=pymysql.connect(host="localhost",user="root",password='<your_password>',database="mydata")

            cur=sqlCon.cursor()
            cur.execute("update  mydata set Nameoftablets=%s,Dose=%s,NumbersofTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,StorageAdvice=%s,nhsNumber=%s,PatientName=%s,DateOfBirth=%s,PatientAddress=%s where ref=%s",(Nameoftablets.get(),Dose.get(),NumberofTablets.get(),Lot.get(),Issuedate.get(),ExpDate.get(),DailyDose.get(),StorageAdvice.get(),nhsNumber.get(),PatientName.get(),DateOfBirth.get(),PatientAddress.get(),ref.get()))
            sqlCon.commit()
            fatch_data()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connection","Record Updated Succesfully")
            

        def delete():
            sqlCon=pymysql.connect(host="localhost",user="root",password="<your_password>",database="mydata")

            cur=sqlCon.cursor()
            cur.execute("delete from  mydata where  ref=%s",ref.get())
            
            sqlCon.commit()
            fatch_data()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySQL Connection","Record Deleted Succesfully")
            Clear()

        
        def iPrescription():
            self.textPrescription.insert(END,"name of tablets:\t\t\t" +  Nameoftablets.get() + "\n")
            self.textPrescription.insert(END,"Reference No.:\t\t\t" +  ref.get() + "\n")
            self.textPrescription.insert(END,"Dose:\t\t\t" +  Dose.get() + "\n")
            self.textPrescription.insert(END,"NumberofTablets:\t\t\t" +  NumberofTablets.get() + "\n")
            self.textPrescription.insert(END,"Lot:\t\t\t" +  Lot.get() + "\n")
            self.textPrescription.insert(END,"Issue Date:\t\t\t" +  Issuedate.get() + "\n")
            self.textPrescription.insert(END,"Exp Date:\t\t\t" +  ExpDate.get() + "\n")
            self.textPrescription.insert(END,"Daily Dose:\t\t\t" +  DailyDose.get() + "\n")
            self.textPrescription.insert(END,"Storage Advice:\t\t\t" +  StorageAdvice.get() + "\n")
            self.textPrescription.insert(END,"nhs Number:\t\t\t" +  nhsNumber.get() + "\n")
            self.textPrescription.insert(END,"Patient Name:\t\t\t" +  PatientName.get() + "\n")
            self.textPrescription.insert(END,"Date of Birth:\t\t\t" +  DateOfBirth.get() + "\n")
            self.textPrescription.insert(END,"Patient Address:\t\t\t" +  PatientAddress.get() + "\n")


        def print_area(txt):
            
            temp_file=tempfile.mktemp('.txt')
            open(temp_file,'w').write(txt)
            os.startfile(temp_file,'print')





        #=======================Heading=====================================



        lbltitle = Label(self.root, bd=20, relief=RIDGE, text=" + HOSPITAL MANAGEMENT SYSTEM",
                         fg="#800020", bg="white", font=('arial', 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        #=======================DataFrame=====================================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe,  padx=10, relief=RIDGE, font=(
            "times new roman", 12, "bold"), text="Patient Informarion")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe,  padx=10, relief=RIDGE, font=(
            "times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        #=======================ButtonFrame=====================================
  
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        #=======================DetailsFrame=====================================
  
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600 ,width=1530, height=190)
 
        #=======================DataFrameLeft=====================================
        
        self.lblNameTablet = Label(DataframeLeft, text="Names of Tablet", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        self.lblNameTablet.grid(row=0, column=0)
        
        self.comNameTablet = ttk.Combobox(DataframeLeft,textvariable=Nameoftablets ,state="readonly", font=(
            "arial", 12, "bold"), width=33)
        self.comNameTablet["values"] = (" ","Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        self.comNameTablet.current(0)
        self.comNameTablet.grid(row=0, column=1)

        self.lblref= Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        self.lblref.grid(row=1,column=0,sticky=W)
        self.txtref=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=ref, width=35)
        self.txtref.grid(row=1,column=1)

        self.lblDose= Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.txtDose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=Dose,width=35)
        self.txtDose.grid(row=2,column=1)

        self.lblNoOftablets= Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablets:",padx=2,pady=6)
        self.lblNoOftablets.grid(row=3,column=0,sticky=W)
        self.txtNoOftablets=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=NumberofTablets,width=35)
        self.txtNoOftablets.grid(row=3,column=1)


        self.lblLot= Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        self.lblLot.grid(row=4,column=0,sticky=W)
        self.txtLot=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=Lot,width=35)
        self.txtLot.grid(row=4,column=1)

        self.lblissueDate= Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        self.lblissueDate.grid(row=5,column=0,sticky=W)
        self.txtissueDate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=Issuedate,width=35)
        self.txtissueDate.grid(row=5,column=1)

        self.lblExpDate= Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        self.lblExpDate.grid(row=6,column=0,sticky=W)
        self.txtExpDate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=ExpDate,width=35)
        self.txtExpDate.grid(row=6,column=1)
        
        self.lblDailyDose= Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        self.lblDailyDose.grid(row=7,column=0,sticky=W)
        self.txtDailyDose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=DailyDose,width=35)
        self.txtDailyDose.grid(row=7,column=1)

        #self.lblSideEffect= Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        #self.lblSideEffect.grid(row=8,column=0,sticky=W)
        #self.txtSideEffect=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=sideEffect,width=35)
        #self.txtSideEffect.grid(row=8,column=1)
 
        #self.lblFurtherinfo= Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=6)
        #self.lblFurtherinfo.grid(row=0,column=2,sticky=W)
        #self.txtFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=FurtherInformation,width=35)
        #self.txtFurtherinfo.grid(row=0,column=3)

        #self.lblDrivingMachine= Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        #self.lblDrivingMachine.grid(row=1,column=2,sticky=W)
        #self.txtDrivingMachine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=DrivingUsingMachine,width=35)
        #self.txtDrivingMachine.grid(row=1,column=3)

        self.lblStorage= Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        self.lblStorage.grid(row=8,column=0,sticky=W)
        self.txtStorage=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=StorageAdvice,width=35)
        self.txtStorage.grid(row=8,column=1)

        #self.lblMedicine= Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        #self.lblMedicine.grid(row=3,column=2,sticky=W)
        #self.txtMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=HowToUseMedication,width=35)
        #self.txtMedicine.grid(row=3,column=3)

        #self.lblPatientId= Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        #self.lblPatientId.grid(row=4,column=2,sticky=W)
        #self.txtPatientId=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=PatientId,width=35)
        #self.txtPatientId.grid(row=4,column=3)

        self.lblNhsNumber= Label(DataframeLeft,font=("arial",12,"bold"),text="Nhs Number:",padx=2,pady=6)
        self.lblNhsNumber.grid(row=0,column=2,sticky=W)
        self.txtNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=nhsNumber,width=35)
        self.txtNhsNumber.grid(row=0,column=3)

        self.lblPatientname= Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        self.lblPatientname.grid(row=1,column=2,sticky=W)
        self.txtPatientname=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=PatientName,width=35)
        self.txtPatientname.grid(row=1,column=3)

        self.lblDateOfBirth= Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        self.lblDateOfBirth.grid(row=2,column=2,sticky=W)
        self.txtDateOfBirth=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=DateOfBirth,width=35)
        self.txtDateOfBirth.grid(row=2,column=3)

        self.lblPatientAddress= Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        self.lblPatientAddress.grid(row=3,column=2,sticky=W)
        self.txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=PatientAddress,width=35)
        self.txtPatientAddress.grid(row=3,column=3)


        #=======================DataFrameRight=====================================
        self.textPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.textPrescription.grid(row=0, column=0)

        #=======================Buttons=====================================
        self.btnPrescription = Button(Buttonframe, text="Prescription",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnPrescriptionData = Button(Buttonframe, text="Prescription Data",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnUpdate = Button(Buttonframe, text="Update",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=update)
        self.btnUpdate.grid(row=0, column=2)

        self.btnDelete = Button(Buttonframe, text="Delete",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=delete)
        self.btnDelete.grid(row=0, column=3)

        self.btnClear = Button(Buttonframe, text="Clear",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=Clear)
        self.btnClear.grid(row=0, column=4)

        self.btnExit = Button(Buttonframe, text="Exit",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=iExit)
        self.btnExit.grid(row=0, column=5)

        self.btnPrintPresciption = Button(Buttonframe, text="Print Presciption",bg="green", fg="white", font=("arial", 12, "bold"), width=20, padx=2, pady=6,command=lambda:print_area(self.textPrescription.get('1.0',END)))
        self.btnPrintPresciption.grid(row=0, column=6)

        #=======================Table=====================================
        #=======================Scrollbar=====================================
        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,columns=("nameoftablets","ref","dose","nooftables","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftables",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="Nhs Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftables",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",patientInfo)
        fatch_data()

        
        





        







if __name__ == "__main__":
   root = Tk()

   application = Hospital(root)
   root.mainloop()

