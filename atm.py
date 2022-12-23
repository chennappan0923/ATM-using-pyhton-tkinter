from tkinter import*
from tkinter import ttk
from tkinter import messagebox

class atm:

    def __init__(self,root):
        
        self.root = root
        blank_space =" "
        self.root.title(110*blank_space+"ATM system")
        self.root.geometry("790x760+280+0")
        self.root.configure(bg="gainsboro")
        #=====================================Frames=================================

        MainFrame = Frame(self.root, bd=20, width=784, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame1.grid(row=1,column=0,padx=12)
        TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
        TopFrame2.grid(row=0,column=0,padx=8)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0,column=0,padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0,column=1,padx=3)
  
        TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0,column=2,padx=3)
        #=====================================Functions=================================
        def enter_pin():
            pinNo = self.txtreceipt.get("1.0","end-1c")
            if ((pinNo == str("0923")) or (pinNo == str("8905")) or (pinNo == str("1105"))):
                self.txtreceipt.delete("1.0",END)

                self.txtreceipt.insert(END,'\t\t      ATM '+"\n\n")
                self.txtreceipt.insert(END,'Withdraw \t\t\t\t Loan' +"\n\n\n\n")
                self.txtreceipt.insert(END,'CAsh with Receipt\t\t\t\t Deposit' +"\n\n\n\n")
                self.txtreceipt.insert(END,'Balance\t\t\t Request New pin' +"\n\n\n\n")
                self.txtreceipt.insert(END,'Mini Statement cash\t\t\t print Statement' +"\n\n\n\n")

                self.btnArrowR1=Button(TopFrame2Right,width=160,height=60,state=ACTIVE,command=loan,
                image=self.imgarrow_Right).grid(row=0,column=0,padx=2,pady=2)

                self.btnArrowR2=Button(TopFrame2Right,width=160,height=60,state=ACTIVE,command=deposit,
                image=self.imgarrow_Right).grid(row=1,column=0,padx=2,pady=2)

                self.btnArrowR3=Button(TopFrame2Right,width=160,height=60,state=ACTIVE,command=request_new_pin,
                image=self.imgarrow_Right).grid(row=2,column=0,padx=2,pady=2)

                self.btnArrowR4=Button(TopFrame2Right,width=160,height=60,state=ACTIVE,command=request_new_pin,
                image=self.imgarrow_Right).grid(row=3,column=0,padx=2,pady=2)
                #=================================================PIN NUMBER BUTTONS======================================
                self.btnArrowL1=Button(TopFrame2Left,width=160,height=60,state=ACTIVE,command=withdraw,
                image=self.imgarrow_Left).grid(row=0,column=0,padx=2,pady=2)

                self.btnArrowL2=Button(TopFrame2Left,width=160,height=60,state=ACTIVE,command=withdraw,
                image=self.imgarrow_Left).grid(row=1,column=0,padx=2,pady=2)

                self.btnArrowL3=Button(TopFrame2Left,width=160,height=60,state=ACTIVE,command=balance,
                image=self.imgarrow_Left).grid(row=2,column=0,padx=2,pady=2)

                self.btnArrowL4=Button(TopFrame2Left,width=160,height=60,state=ACTIVE,command=statement,
                image=self.imgarrow_Left).grid(row=3,column=0,padx=2,pady=2)

            else:
                self.txtreceipt.delete("1.0",END)

                self.txtreceipt.insert(END,'invalid pin number'+"\n\n")
                
            #======================================CLEAR BUTTON========================
        def clear():
            self.txtreceipt.delete("1.0",END)
            self.imgarrow_Left=PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/lArrow.png")

            self.btnArrowL1=Button(TopFrame2Left,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Left).grid(row=0,column=0,padx=2,pady=2)

            self.btnArrowL2=Button(TopFrame2Left,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Left).grid(row=1,column=0,padx=2,pady=2)

            self.btnArrowL3=Button(TopFrame2Left,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Left).grid(row=2,column=0,padx=2,pady=2)

            self.btnArrowL4=Button(TopFrame2Left,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Left).grid(row=3,column=0,padx=2,pady=2)
            #=======================================================================================
            self.imgarrow_Right=PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/rArrow.png")

            self.btnArrowR1=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Right).grid(row=0,column=0,padx=2,pady=2)

            self.btnArrowR2=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Right).grid(row=1,column=0,padx=2,pady=2)

            self.btnArrowR3=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Right).grid(row=2,column=0,padx=2,pady=2)

            self.btnArrowR4=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
            image=self.imgarrow_Right).grid(row=3,column=0,padx=2,pady=2)
            
        def insert0():
            value0 = 0
            self.txtreceipt.insert(END,value0)
        def insert1():
            value1 = 1
            self.txtreceipt.insert(END,value1)
        def insert2():
            value2 = 2
            self.txtreceipt.insert(END,value2)
        def insert3():
            value3 = 3
            self.txtreceipt.insert(END,value3)
        def insert4():
            value4 = 4
            self.txtreceipt.insert(END,value4)                   
        def insert5():
            value5 = 5
            self.txtreceipt.insert(END,value5)
        def insert6():
            value6 = 6
            self.txtreceipt.insert(END,value6)
        def insert7():
            value7 = 7
            self.txtreceipt.insert(END,value7)
        def insert8():
            value8 = 8
            self.txtreceipt.insert(END,value8)
        def insert9():
            value9 = 9
            self.txtreceipt.insert(END,value9)
        def cancel():
            Cancel = messagebox.askyesno("ATM","Confirm if you want to cancel")
            if Cancel > 0:
                self.root.destroy()
                return
        def withdraw():
            enter_pin()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.focus_set()

        def loan():
            enter_pin()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END, 'Loan  $ ') 
            self.txtreceipt.focus_set()
        def deposit():
            enter_pin()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.focus_set()

        def request_new_pin():
            enter_pin()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END,'\t\tWelcome to iBank\n')
            self.txtreceipt.insert(END, 'New Pin will be send to your phone number \n')
            self.txtreceipt.insert(END,'\t\t      ATM '+"\n\n")
            self.txtreceipt.insert(END,'Withdraw \t\t\t\t Loan' +"\n\n\n\n")
            self.txtreceipt.insert(END,'Cash with Receipt\t\t\t\t Deposit' +"\n\n\n\n")
            self.txtreceipt.insert(END,'Balance\t\t\t Request New pin' +"\n\n\n\n")
            self.txtreceipt.insert(END,'Mini Statement cash\t\t\t print Statement' +"\n\n\n\n")
            self.txtreceipt.insert(END,'\t\t Thanks for using iBank\n')
        def balance():
            enter_pin()
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END,'\t\tWelcome to iBank\n')
            self.txtreceipt.insert(END,'Rs 100000 '+ "\n")
            
            self.txtreceipt.insert(END,'\t\t      ATM '+"\n\n")
            self.txtreceipt.insert(END,'Withdraw \t\t\t\t Loan' +"\n\n\n\n")
            self.txtreceipt.insert(END,'CAsh with Receipt\t\t\t\t Deposit' +"\n\n\n\n")
            self.txtreceipt.insert(END,'Balance\t\t\t Request New pin' +"\n\n\n\n")
            self.txtreceipt.insert(END,'Mini Statement cash\t\t\t print Statement' +"\n\n\n\n")
            self.txtreceipt.insert(END,'\t\t Thanks for using iBank\n')

        def statement():
            pinNo1 = str(self.txtreceipt.get("1.0","end-1c"))
            pinNo2 = str(pinNo1)
            pinNo3 = float(pinNo2)
            pinNo4 = float(100000,(pinNo3))
            self.txtreceipt.delete("1.0",END)
            self.txtreceipt.insert(END,'\n\t' + str(pinNo4) + '\n')
            self.txtreceipt.insert(END,'Rs 100000 '+ "\n")
            self.txtreceipt.insert(END,'\t\t\n\n  Account Balance Rs' + + str(pinNo4) + '\t\t\n\n')
            self.txtreceipt.insert(END,'Withdraw \t\t\t\t Loan' +"\n\n\n\n")
           

        

        #=====================================Widgets=================================

        self.txtreceipt=Text(TopFrame2Mid, height = 17,width=42,bd=12, font=('arial',9,'bold'))
        self.txtreceipt.grid(row=0,column=0)

        self.imgarrow_Left=PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/lArrow.png")

        self.btnArrowL1=Button(TopFrame2Left,width=160,height=60,state=DISABLED,command=withdraw,
        image=self.imgarrow_Left).grid(row=0,column=0,padx=2,pady=2)

        self.btnArrowL2=Button(TopFrame2Left,width=160,height=60,state=DISABLED,command=withdraw,
        image=self.imgarrow_Left).grid(row=1,column=0,padx=2,pady=2)

        self.btnArrowL3=Button(TopFrame2Left,width=160,height=60,state=DISABLED,
        image=self.imgarrow_Left).grid(row=2,column=0,padx=2,pady=2)

        self.btnArrowL4=Button(TopFrame2Left,width=160,height=60,state=DISABLED,
        image=self.imgarrow_Left).grid(row=3,column=0,padx=2,pady=2)
        #=======================================================================================
        self.imgarrow_Right=PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/rArrow.png")

        self.btnArrowR1=Button(TopFrame2Right,width=160,height=60,state=DISABLED,command=loan,
        image=self.imgarrow_Right).grid(row=0,column=0,padx=2,pady=2)

        self.btnArrowR2=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
        image=self.imgarrow_Right).grid(row=1,column=0,padx=2,pady=2)

        self.btnArrowR3=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
        image=self.imgarrow_Right).grid(row=2,column=0,padx=2,pady=2)

        self.btnArrowR4=Button(TopFrame2Right,width=160,height=60,state=DISABLED,
        image=self.imgarrow_Right).grid(row=3,column=0,padx=2,pady=2)
        #=================================================PIN NUMBER BUTTONS======================================
        self.img1 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/one.png")
        self.btn1=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert1,
        image=self.img1).grid(row=2,column=0,padx=6,pady=4)

        self.img2 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/two.png")
        self.btn2=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert2,
        image=self.img2).grid(row=2,column=1,padx=6,pady=4)

        self.img3 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/three.png")
        self.btn3=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert3,
        image=self.img3).grid(row=2,column=2,padx=6,pady=4)

        self.imgCE =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/cancel.png")
        self.btnCE=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=cancel,
        image=self.imgCE).grid(row=2,column=3,padx=6,pady=4)
        #================================================================================================
        self.img4 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/four.png")
        self.btn4=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert4,
        image=self.img4).grid(row=3,column=0,padx=6,pady=4)

        self.img5 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/five.png")
        self.btn5=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert5,
        image=self.img5).grid(row=3,column=1,padx=6,pady=4)

        self.img6 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/six.png")
        self.btn6=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert6,
        image=self.img6).grid(row=3,column=2,padx=6,pady=4)

        self.imgCL =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/clear.png")
        self.btn3=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=clear,
        image=self.imgCL).grid(row=3,column=3,padx=6,pady=4)
        #================================================================================================
        self.img7 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/seven.png")
        self.btn7=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert7,
        image=self.img7).grid(row=4,column=0,padx=6,pady=4)

        self.img8 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/eight.png")
        self.btn8=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert8,
        image=self.img8).grid(row=4,column=1,padx=6,pady=4)

        self.img9 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/nine.png")
        self.btn9=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert9,
        image=self.img9).grid(row=4,column=2,padx=6,pady=4)

        self.imgEN =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/enter.png")
        self.btnEN=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=enter_pin,
        image=self.imgEN).grid(row=4,column=3,padx=6,pady=4)
        #================================================================================================
        self.imgsp1 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/empty.png")
        self.btnsp1=Button(TopFrame1,width=160,height=60,state=ACTIVE,
        image=self.imgsp1).grid(row=5,column=0,padx=6,pady=4)

        self.img0 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/zero.png")
        self.btn0=Button(TopFrame1,width=160,height=60,state=ACTIVE,command=insert0,
        image=self.img0).grid(row=5,column=1,padx=6,pady=4)

        self.imgsp2 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/empty.png")
        self.btn9=Button(TopFrame1,width=160,height=60,state=ACTIVE,
        image=self.imgsp2).grid(row=5,column=2,padx=6,pady=4)

        self.imgsp3 =PhotoImage(file ="C:/Users/LENOVO/Downloads/ATM_Icon/ATM_Icon/empty.png")
        self.btnsp3=Button(TopFrame1,width=160,height=60,state=ACTIVE,
        image=self.imgsp3).grid(row=5,column=3,padx=6,pady=4)

         
        

        
 




if __name__=='__main__':
    root=Tk()
    application = atm(root)
    root.mainloop()
    
    
        
                        
