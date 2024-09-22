from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from dal.repository import Repository,DataAccess
from bll.blpersonal import blPersonal,BusinessLogic
from be.User import Mojudi,Factor,Cost




class App(ttk.Frame):

    def __init__(self,screen):
        super().__init__(screen)
        self.master=screen

        self.is_mojudi_opened = False
        self.is_factor_opened = False
        self.is_cost_opened = False
        self.Creatwieget()
        self.Name1.focus_set()
        self.Color1 = StringVar()
        self.Namekala = StringVar()
        self.Shenase = IntVar()
        self.Number = IntVar()
        self.Price = IntVar()
        self.Ex=StringVar()
        self.Id1 = StringVar()
        self.Search=StringVar()

        self.Id2=StringVar()
        self.Id3=StringVar()
        self.Costtp = StringVar()
        self.Costd = StringVar()
        self.Costex = StringVar()
        self.Costst = StringVar()
        self.Costpr = IntVar()
        self.name_ctr = StringVar()
        self.date_fcr = StringVar()
        self.price_fcr = IntVar()
        self.number_fcr = IntVar()
        self.kala_fcr = StringVar()
        self.condition_fcr = StringVar()






    def Creatwieget(self):
        style = ttk.Style()
        style.theme_use("vista")




        self.name=StringVar()
        self.password=StringVar()

        #lables
        self.Name=ttk.Label(self.master,text="Username",font="nazanin 9 ").pack(pady=5)
        self.Name1 =ttk.Entry(self.master,textvariable=self.name)
        self.Name1 .pack()
        self.Password=ttk.Label(self.master,text="Password",font="nazanin 9 ").pack(pady=10)
        self.Password1 =ttk.Entry(self.master,textvariable=self.password)
        #self.Password1.bind("<FocusIn>", self.focus_in())
        self.Password1 .pack()
        #Button
        self.login=ttk.Button(self.master,text="ورود",command=self.chake)
        self.login.pack(pady=20,ipady=2,ipadx=10)








    def chake(self):








        self.master.destroy()
        self.open_new_window()




        #Entry







    def open_new_window(self):



            self.Load()
            self.Load_Factor()
            self.Load_Factor_Mini()
            self.Clean_Mini()
            self.screen = Tk()
            self.screen.title("مدیریت فروش")
            self.screen.config(bg="#d4d7dc")
            self.screen.iconbitmap("img/work.ico")
            self.screen.geometry("%dx%d+%d+%d" % (1100, 748, 200, 20))




              # سپس داده‌ها را به جدول اضافه کنید

            self.imagebtn=PhotoImage(file="img/menulines.png")
            self.imagemoney =PhotoImage(file="img/money2.png")
            self.imageplus = PhotoImage(file="img/plus2.png")
            self.imagehome = PhotoImage(file="img/home1.png")
            self.imagewarehouse =PhotoImage(file="img/warehouse1.png")
            self.imageerror= PhotoImage(file="img/error1.png")


            self.framadd = Frame(self.screen, bg="pink")
            self.framadd.pack_forget()


            self.moneyfram = Label(self.screen, bg="#c9c9c9")


            self.tblcost_mini = ttk.Treeview(self.screen, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                                          show="headings",
                                          )
            self.tblcost_mini.heading("#1", text="نوع هزینه")
            self.tblcost_mini.column("#1", width=60, anchor=S)
            self.tblcost_mini.heading("#4", text="قیمت")
            self.tblcost_mini.column("#4", width=100, anchor=S)
            self.tblcost_mini.heading("#2", text="تاریخ")
            self.tblcost_mini.column("#2", width=60, anchor=S)
            self.tblcost_mini.heading("#3", text="کالا")
            self.tblcost_mini.column("#3", width=60, anchor=S)
            self.tblcost_mini.heading("#5", text="وضعیت")
            self.tblcost_mini.column("#5", width=50, anchor=S)
            self.tblcost_mini.heading("#6", text="شماره")
            self.tblcost_mini.column("#6", width=50, anchor=S)

            self.tblcost_mini.place_configure(x=600, y=70,width=380,height=300)

            self.Load_Cost_Mini()

            self.tblmojudi_mini = ttk.Treeview(self.screen, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                                          show="headings",
                                          )
            self.tblmojudi_mini.heading("#4", text="توضیحات")
            self.tblmojudi_mini.column("#4", width=120, anchor=S)
            self.tblmojudi_mini.heading("#1", text="قیمت")
            self.tblmojudi_mini.column("#1", width=100, anchor=S)
            self.tblmojudi_mini.heading("#6", text="نام کالا")
            self.tblmojudi_mini.column("#6", width=60, anchor=S)
            self.tblmojudi_mini.heading("#5", text="شناسه کالا")
            self.tblmojudi_mini.column("#5", width=100, anchor=S)
            self.tblmojudi_mini.heading("#3", text="تعداد")
            self.tblmojudi_mini.column("#3", width=30, anchor=S)
            self.tblmojudi_mini.heading("#2", text="رنگ")
            self.tblmojudi_mini.column("#2", width=40, anchor=S)
            self.tblmojudi_mini.heading("#7", text="شماره")
            self.tblmojudi_mini.column("#7", width=30, anchor=S)

            self.tblmojudi_mini.place_configure(x=10, y=70,width=533,height=300)
            self.Load_Mojudi_Mini()


            self.moneyfram.pack_forget()

            self.anbar = Label(self.screen, bg="#c1c3c8")
            self.anbar.pack_forget()

        #Image



        #Frams
        #self.fram=Label(screen,bg="#e74343").pack(fill=BOTH,side=BOTTOM,ipady=22)
        #Menus
            self.frammenu=Frame(self.screen,bg="#f0f0f0",height=2,width=5)
            self.frammenumoney=Frame(self.moneyfram,bg="#f0f0f0",height=200,width=200)
            self.frammenuanbar=Frame(self.anbar,bg="#f0f0f0",height=200,width=200)
            self.frammenu.pack_forget()
            self.frammenumoney.place_forget()
            self.frammenuanbar.place_forget()
            self.fram=Label(self.screen,bg="#e74343").pack(fill=BOTH,side=TOP,ipady=17)
            self.fram1=Label(self.screen,bg="#e74343").pack(fill=BOTH,side=BOTTOM,ipady=22)
            #SubMenu






            #SubMenuMoney
            self.Factor=Label(self.frammenumoney, text="لیست فاکتورها", bg="#09cb68", fg="white"
                                 , pady=(8), padx=(45), font=("Yekan 15 bold"))
            self.Factor.bind("<Button-1>",self.open_factor)

            self.Factor.place_configure(x=5, y=10,)
            self.Costs=Label(self.frammenumoney, text="لیست هزینه ها", bg="#e4c603", fg="white",
                                pady=(8), padx=(45), font=("Yekan 15 bold"),)
            self.Costs.bind("<Button-1>",self.open_Costs)
            self.Costs.place(x=5, y=70)


        #listfactor








            self.menu=Label(self.screen,text="q",image=self.imagebtn,bg="#e74343")

            self.menu.bind("<Button-1>", self.close_menubar)

            #self.menu.bind("<Leave>", self.ResetShape)
            self.menu.bind("<Enter>", self.open_menubar)
            self.menu.place(x=0,y=10)

            self.money=Label(self.fram1,text="امور مالی",image=self.imagemoney,bg="#e74343")
            self.money.bind("<Button-1>", self.new_win)
            self.money.place(x=70, y=690)
            self.moneyname=Label(self.fram1,text="امور مالی",bg="#e74343",font=("nazanin 13"))

            self.moneyname.place(x=60, y=718)

            self.fhome = Label(self.fram1, text="d", bg="#e74343",image=self.imagehome)
            self.fhome.bind("<Button-1>",self.new_home)
            self.fhome.place(x=1000, y=690)
            self.home=Label(self.fram1,text="خانه",bg="#e74343",font=("nazanin 15"))
            self.home.place(x=1000, y=718)

            self.fstore = Label(self.fram1, text="d", bg="#e74343",image=self.imagewarehouse)
            self.fstore.place(x=555, y=690)
            self.fstore.bind("<Button-1>",self.new_anbar)
            self.stone=Label(self.fram1,text="انبار ",bg="#e74343",font=("nazanin 13"))
            self.stone.place(x=558, y=718)




            self.add=Label(self.fram,text="s",image=self.imageplus,bg="#e74343")
            #self.add.bind("<Button-1>",self.Add)
            self.add.place(x=1440,y=3)

            #انبار
            self.new_kala=Label(self.frammenuanbar,text="ثبت کالای جدید",font=("Yekan 13 bold"),bg="#36962a",fg="white",pady=8, padx=50)
            self.new_kala.bind("<Button-1>",self.open_kala)
            self.new_kala.place(x=5,y=10)

            self.mojudi = Label(self.frammenuanbar, text="موجودی", font=("Yekan 13 bold"), bg="#aab017", fg="white", pady=9, padx=68)
            self.mojudi.bind("<Button-1>", self.open_mojudi)

            self.mojudi.place(x=5,y=60)

            self.setting = Label(self.frammenuanbar, text="تنظیمات", font=("Yekan 13 bold"),bg="#666a65",fg="white",pady=8, padx=70)
            self.setting.bind("<Button-1>")
            self.setting.place(x=5,y=110)

            #امورمالی
            self.factor=Frame(self.frammenumoney,bg="pink")
            self.factor.place(x=300, y=300)

            self.tblfactor_mini = ttk.Treeview(self.screen, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                                               show="headings")

            self.tblfactor_mini.heading("#6", text="شماره فاکتور")
            self.tblfactor_mini.column("#6", width=70, anchor=S)
            self.tblfactor_mini.heading("#2", text="قیمت")
            self.tblfactor_mini.column("#2", width=100, anchor=S)
            self.tblfactor_mini.heading("#4", text="نام مشتری")
            self.tblfactor_mini.column("#4", width=60, anchor=S)
            self.tblfactor_mini.heading("#5", text="تاریخ")
            self.tblfactor_mini.column("#5", width=60, anchor=S)
            self.tblfactor_mini.heading("#3", text="کالا")
            self.tblfactor_mini.column("#3", width=60, anchor=S)
            self.tblfactor_mini.heading("#1", text="وضعیت")
            self.tblfactor_mini.column("#1", width=50, anchor=S)
            self.tblfactor_mini.heading("#7", text="شماره")
            self.tblfactor_mini.column("#7", width=30, anchor=S)

            self.tblfactor_mini.place_configure(x=10, y=380, width=533, height=250)

            # بارگذاری اطلاعات به‌صورت خودکار هنگام باز شدن برنامه
            self.Load_Factor_Mini()

    def Load_Factor_Mini(self):
        if hasattr(self, 'tblfactor_mini'):
            self.tblfactor_mini.delete(*self.tblfactor_mini.get_children())  # پاک کردن جدول قبل از بارگذاری جدید

        objbl = blPersonal()

        # دریافت 10 فاکتور آخر
        lstFactorMini = objbl.blReadLimit(Factor, 10)
        for item in lstFactorMini:
            # Check if tblfactor_mini exists before accessing it
            if hasattr(self, 'tblfactor_mini'):
                self.tblfactor_mini.insert('', "end", values=[item.State, item.Price, item.Kala, item.Namecustomer,
                                                              item.Date, item.Number, item.Id])

    def Clean_Mini(self):
        if hasattr(self, 'tblfactor_mini'):
            for item in self.tblfactor_mini.get_children():
                self.tblfactor_mini.delete(item)

    def Load_Cost_Mini(self):
        if hasattr(self, 'tblcost_mini'):
            self.tblcost_mini.delete(*self.tblcost_mini.get_children())  # پاک کردن جدول قبل از بارگذاری جدید

        objbl = blPersonal()

        # دریافت 10 فاکتور آخر
        lstFactorMini = objbl.blReadLimit(Cost, 10)
        for item in lstFactorMini:
            # Check if tblfactor_mini exists before accessing it
            if hasattr(self, 'tblcost_mini'):
                self.tblcost_mini.insert('', "end",  values=[item.TypeCost, item.DateCost, item.ExplainCost, item.PriceCost,
                                          item.StatCost,item.Id])

    def Clean_Mini_cost(self):
        if hasattr(self, 'tblcost_mini'):
            for item in self.tblcost_mini.get_children():
                self.tblcost_mini.delete(item)



    def Load_Mojudi_Mini(self):
        if hasattr(self, 'tblmojudi_mini'):
            self.tblmojudi_mini.delete(*self.tblmojudi_mini.get_children())  # پاک کردن جدول قبل از بارگذاری جدید

        objbl = blPersonal()

        # دریافت 10 فاکتور آخر
        lstMojudiMini = objbl.blReadLimit(Mojudi, 10)
        for item in lstMojudiMini:
            # Check if tblfactor_mini exists before accessing it
            if hasattr(self, 'tblmojudi_mini'):
                self.tblmojudi_mini.insert('', "end",   values=[item.Shenasekala, item.Nubmers, item.Namekala, item.Explain,
                                                         item.Pricekala,item.Color,item.Id])

    def Clean_Mini_mojudi(self):
        if hasattr(self, 'tblmojudi_mini'):
            for item in self.tblmojudi_mini.get_children():
                self.tblmojudi_mini.delete(item)





    def open_settings(self, event=None):
        new_screenset = Toplevel()
        new_screenset.config(background="#ff7676")
        new_screenset.geometry("1500x670+8+86")
        new_screenset.overrideredirect(True)
        cancelset = Button(new_screenset, text="برگشت", font="Yekan 11 bold", background="#fe4545",
                         command=new_screenset.destroy)
        cancelset.place(x=730, y=450)

    def open_Costs(self,e):


        if hasattr(self,'framfactor_screen'):

            self.framfactor_screen.place_forget()
        self.framcost=Frame(bg="#e43838",)

        self.framcost.place_configure( width=560, height=600,x=300, y=70)

        self.cancelcost = Button(self.framcost, text="برگشت")
        self.cancelcost.configure( background="#fe4545")
        self.cancelcost.bind("<Button-1>", self.Cancelcost)

        self.cancelcost.place(x=400, y=558)
        self.frammenumoney.place_forget()

        self.Id = StringVar()

        self.tblcosts = ttk.Treeview(self.framcost, columns=("c1", "c2", "c3", "c4", "c5","c6"), show="headings",
                               )
        self.tblcosts.heading("#3", text="توضیحات")
        self.tblcosts.column("#3", width=130, anchor=S)
        self.tblcosts.heading("#4", text="قیمت")
        self.tblcosts.column("#4", width=120, anchor=S)
        self.tblcosts.heading("#5", text="وضعیت")
        self.tblcosts.column("#5", width=60, anchor=S)
        self.tblcosts.heading("#2", text="تاریخ")
        self.tblcosts.column("#2", width=60, anchor=S)
        self.tblcosts.heading("#1", text="نوع هزینه")
        self.tblcosts.column("#1", width=60, anchor=S)
        self.tblcosts.heading("#6", text="شماره")
        self.tblcosts.column("#6", width=20, anchor=S)
        self.tblcosts.place_configure(x=15, y=38, height=517,width=530)
        self.tblcosts.bind("<Button-1>", self.GetSelection)

        self.Search_cost=StringVar()






        self.txtsearchcost = Button(self.framcost, text="جستجو",command=self.searchboxc,pady=-2 ,bg="#0fc0e1")
        self.txtsearchcost.place(x=160, y=10)

        self.boxsearchcost = Entry(self.framcost,textvariable=self.Search_cost,bg="#07d8ff")
        self.boxsearchcost.place(x=30, y=10)

        self.btnaddcost = Button(self.framcost, text="ثبت هزینه", fg="black", bg='#e9cb04',font="Yekan 11 ",padx=10,command=self.new_cost)
        self.btnaddcost.place(x=458, y=7)

        self.btnedit=Button(self.framcost,text="ویرایش",command=self.OnClickEdit,bg='#e9cb04')
        self.btnedit.place(x=450, y=560)

        self.btndelete_cost=Button(self.framcost,text="حذف",bg="red",command=self.delete_cost)

        self.btndelete_cost.place(x=500, y=560)
        self.Load_Cost()
        self.is_cost_opened=True

    def GetSelection(self, e):


        if hasattr(self, 'tblcosts'):
            objbl = blPersonal()
            SelectRow = self.tblcosts.selection()

            if SelectRow != ():
                row_values = self.tblcosts.item(SelectRow)["values"]


            # استفاده از ستون 5 برای شناسه (ID)
                idrow = row_values[5]  # شناسه در ستون 5 است

                if str(idrow).isdigit():
                    self.Id.set(int(idrow))
                else:
                    messagebox.showerror("خطا", "شناسه انتخابی معتبر نیست")
                    return

            # دریافت شیء بر اساس شناسه
                obj = objbl.blReadById(Cost, self.Id.get())

                if obj is not None:
                    self.Costtp.set(obj.TypeCost)
                    self.Costd.set(obj.DateCost)
                    self.Costex.set(obj.ExplainCost)
                    self.Costst.set(obj.StatCost)
                    self.Costpr.set(obj.PriceCost)

                else:
                    messagebox.showerror("خطا", "هیچ داده‌ای برای این شناسه یافت نشد")

    def OnClickEdit(self):
        Id3=self.Id3.get()

        #NewObject
        objp=Cost(self.Costpr.get(), self.Costst.get(), self.Costtp.get(),self.Costd.get(),self.Costex.get())
        objbl=blPersonal()
        result=objbl.blUpdatecost(Cost,Id3,objp)
        if result==True:
            self.Load_Cost()
            messagebox.showinfo("عملیات موفق", "عملیات ویرایش با موفقیت انجام شد")
        else:
            messagebox.showinfo("عملیات ناموفق", "عملیات ویرایش انجام نشد")


    def searchboxc(self):
        stch=self.Search_cost.get()
        if stch=="":
            self.Load_Cost()
        else:
            obj=blPersonal()
            resullt=obj.searchbox3(Cost,stch)
            if resullt!=[]:
                self.Clean_cost()

                for item in resullt:
                        self.tblcosts.insert("","end",  values=[item.TypeCost, item.DateCost, item.ExplainCost, item.PriceCost,
                                          item.StatCost])
    def delete_cost(self):
        select_rows = self.tblcosts.selection()
        if select_rows:
            deletobj1 = blPersonal()
            for row in select_rows:
                prc_id1 = self.tblcosts.item(row)["values"][5]  # مطمئن شوید که index صحیح است
                obj = deletobj1.blReadById(Cost, prc_id1)

                if obj is None:
                    messagebox.showerror("خطا", f"آیتمی با شناسه {prc_id1} پیدا نشد")
                    continue

                result = deletobj1.blDelete(Cost, prc_id1)
                if not result:
                    messagebox.showerror("خطا", f"خطا در حذف اطلاعات با شناسه {prc_id1}")
                    return

            self.Load_Cost()  # پس از حذف موفق، جدول را بارگذاری کنید
            messagebox.showinfo("حذف", "اطلاعات با موفقیت حذف گردید")






    def new_cost(self):

        self.fram_add_cost = Frame(bg="#939191", height=350, width=400)
        self.fram_add_cost.place_configure(x=900, y=150, height=350, width=400)

        self.Costtp=StringVar()
        self.Costd=StringVar()
        self.Costex=StringVar()
        self.Costst=StringVar()
        self.Costpr=IntVar()





        self.lblcost=Label(self.fram_add_cost,text="نوع هزینه")
        self.lblcost.place(x=340,y=30)
        self.entcost=Entry(self.fram_add_cost,textvariable=self.Costtp)
        self.entcost.place(x=215,y=30)

        self.lblcostst = Label(self.fram_add_cost, text="وضعیت")
        self.lblcostst.place(x=345, y=180)
        self.entcostst = Entry(self.fram_add_cost, textvariable=self.Costst)
        self.entcostst.place(x=220, y=180)

        self.lblcostda = Label(self.fram_add_cost, text="تاریخ")
        self.lblcostda.place(x=150, y=30)
        self.entcostda = Entry(self.fram_add_cost, textvariable=self.Costd)
        self.entcostda.place(x=25, y=30)

        self.lblcostpr = Label(self.fram_add_cost, text="قیمت")
        self.lblcostpr.place(x=150, y=110)
        self.entcostpr = Entry(self.fram_add_cost, textvariable=self.Costpr)
        self.entcostpr.place(x=25, y=110)

        self.lblcostex = Label(self.fram_add_cost, text="توضیخات")
        self.lblcostex.place(x=340, y=110)
        self.entcostex=Entry(self.fram_add_cost,textvariable=self.Costex)
        self.entcostex.place(x=215,y=110)


        self.btnSave_cost=Button(self.fram_add_cost,text="ثبت",bg="green",padx=8, font="Yekan 11 ",command=self.oncklick_Savedata_Cost)
        self.btnSave_cost.place(x=265,y=312)

        self.btncansel_cost=Button(self.fram_add_cost,text="انصراف",bg="red",padx=8, font="Yekan 11 ",command=self.Cansel_framcost)
        self.btncansel_cost.place(x=320,y=312)

        if self.is_cost_opened:
            self.fram_add_cost.place_configure(x=250, y=480, height=200, width=748)
            self.framcost.place_configure(width=750, height=413, x=250, y=60)
            self.tblcosts.place_configure(x=10, y=36, height=342, width=733)
            self.lblcost.place(x=680, y=50)
            self.entcost.place(x=550, y=50)
            self.lblcostst.place(x=430, y=110)
            self.entcostst.place(x=300, y=110)
            self.lblcostda.place(x=440, y=50)
            self.entcostda.place(x=310, y=50)
            self.lblcostpr.place(x=690, y=110)
            self.entcostpr.place(x=555, y=110)
            self.lblcostex.place(x=185, y=50)
            self.entcostex.place(x=50, y=50)
            self.btnSave_cost.place(x=20, y=165)
            self.btncansel_cost.place(x=75, y=165)

            self.txtsearchcost.place(x=160, y=10)
            self.boxsearchcost.place(x=30, y=10)
            self.btnaddcost.place(x=655, y=5)
            self.btnedit.place(x=645, y=380)
            self.btndelete_cost.place(x=700, y=380)


    def Cansel_framcost(self):
        self.fram_add_cost.place_forget()
        self.framcost.place_configure(width=560, height=600, x=300, y=70)
        self.cancelcost.place(x=100, y=558)
        self.tblcosts.place_configure(x=15, y=38, height=517, width=530)
        self.txtsearchcost.place(x=160, y=10)
        self.boxsearchcost.place(x=30, y=10)
        self.btnaddcost.place(x=458, y=7)
        self.btnedit.place(x=450, y=568)
        self.btndelete_cost.place(x=500, y=568)


    def oncklick_Savedata_Cost(self):
        objp = Cost(self.Costpr.get(), self.Costst.get(), self.Costtp.get(),self.Costd.get(),self.Costex.get())
        objbl = blPersonal()
        result = objbl.blAdd(objp)
        if result == True:
            self.Load_Cost()
            messagebox.showinfo("ثبت نام", "اطلاعات فرد با موفقیت ثبت گردید")

    def Clean_cost(self):
        if hasattr(self, 'tblcosts'):
            for item in self.tblcosts.get_children():
                self.tblcosts.delete(item)

    def Load_Cost(self):
        self.Clean_cost()

        objbl = blPersonal()
        lstPersonal = objbl.blRead(Cost)
        for item in lstPersonal:
            # Check if tblfactor exists before accessing it
            if hasattr(self, 'tblcosts'):
                self.tblcosts.insert('', "end", values=[item.TypeCost, item.DateCost, item.ExplainCost, item.PriceCost,
                                          item.StatCost,item.Id])






    def open_factor(self,e):


        if hasattr(self,'framcost'):

            self.framcost.place_forget()

        self.framfactor_screen=Frame(bg="#e43838",height=550,width=650)
        self.framfactor_screen.place(x=240,y=90,height=550,width=650)

        self.cancelfact = Button(self.framfactor_screen, text="برگشت",)
        self.cancelfact.configure( bg="#fe4545")
        self.cancelfact.bind("<Button-1>", self.Cancel)
        self.Id1=StringVar()

        self.cancelfact.place_configure(x=483, y=515)
        # Table
        self.tblfactor = ttk.Treeview(self.framfactor_screen, columns=("c1", "c2", "c3", "c4", "c5", "c6","c7"), show="headings",
                               )
        self.tblfactor.heading("#6", text="شماره فاکتور")
        self.tblfactor.column("#6", width=90, anchor=S)
        self.tblfactor.heading("#2", text="قیمت")
        self.tblfactor.column("#2", width=100, anchor=S)
        self.tblfactor.heading("#4", text="نام مشتری")
        self.tblfactor.column("#4", width=130, anchor=S)
        self.tblfactor.heading("#5", text="تاریخ")
        self.tblfactor.column("#5", width=70, anchor=S)
        self.tblfactor.heading("#3", text="کالا")
        self.tblfactor.column("#3", width=70, anchor=S)
        self.tblfactor.heading("#1", text="وضعیت")
        self.tblfactor.column("#1", width=60, anchor=S)
        self.tblfactor.heading("#7", text="شماره")
        self.tblfactor.column("#7", width=30, anchor=S)

        self.tblfactor.place_configure(x=30, y=35,width=600, height=475)
        self.tblfactor.bind("<Button-1>", self.GetSelection_factor)

        self.txtsearch=Button(self.framfactor_screen,text="جستجو",command=self.searchboxf,bg="#0fc0e1")
        self.txtsearch.place(x=165,y=7)
        self.Search_factor = StringVar()

        self.boxsearch=Entry(self.framfactor_screen,textvariable=self.Search_factor,bg="#07d8ff")
        self.boxsearch.place(x=30,y=10)


        self.btnadd=Button(self.framfactor_screen,text="ایجاد فاکتور جدید",fg="black",font="Yekan 11 ",bg="#09cb68",command=self.new_factor)
        self.btnadd.place(x=530,y=2)

        self.btneditfact = Button(self.framfactor_screen, text="ویرایش",command=self.OnClickEdit_factor,bg='#e9cb04')
        self.btneditfact.place(x=537, y=515)

        self.btndelete_factor = Button(self.framfactor_screen, text="حذف",bg="red",command=self.delete_factor)

        self.btndelete_factor.place(x=590, y=515)


        self.Load_Factor()
        self.frammenumoney.place_forget()
        self.tblfactor_mini.place_forget()
        self.is_factor_opened = True

    def GetSelection_factor(self, e):


        if hasattr(self, 'tblfactor'):
            objbl = blPersonal()
            SelectRow = self.tblfactor.selection()

            if SelectRow != ():
                row_values = self.tblfactor.item(SelectRow)["values"]

            # چاپ مقادیر ردیف انتخابی برای بررسی
                print(f"Row Values: {row_values}")

            # استفاده از ستون 5 برای شناسه (ID)
                idrow = row_values[6]  # شناسه در ستون 5 است

            # چاپ مقدار idrow برای بررسی آن
                print(f"idrow: {idrow}")

                if str(idrow).isdigit():
                    self.Id1.set(int(idrow))
                else:
                    messagebox.showerror("خطا", "شناسه انتخابی معتبر نیست")
                    return

            # دریافت شیء بر اساس شناسه
                obj = objbl.blReadById(Factor, self.Id1.get())

                if obj is not None:
                    self.condition_fcr.set(obj.State)
                    self.kala_fcr.set(obj.Kala)
                    self.number_fcr.set(obj.Number)
                    self.name_ctr.set(obj.Namecustomer)
                    self.date_fcr.set(obj.Date)
                    self.price_fcr.set(obj.Price)
                else:
                    messagebox.showerror("خطا", "هیچ داده‌ای برای این شناسه یافت نشد")

    def OnClickEdit_factor(self):
        Id2=self.Id2.get()

        #NewObject
        objp=Factor(self.name_ctr.get(), self.date_fcr.get(), self.price_fcr.get(),self.condition_fcr.get(),self.kala_fcr.get(),self.number_fcr.get())
        objbl=blPersonal()
        result=objbl.blUpdatefact(Factor,Id2,objp)
        if result==True:
            self.Load_Factor()
            messagebox.showinfo("عملیات موفق", "عملیات ویرایش با موفقیت انجام شد")
        else:
            messagebox.showinfo("عملیات ناموفق", "عملیات ویرایش انجام نشد")



    def searchboxf(self):
        stch=self.Search_factor.get()
        if stch=="":
            self.Load_Factor()
        else:
            obj=blPersonal()
            resullt=obj.searchbox2(Factor,stch)
            if resullt!=[]:
                self.Clean()

                for item in resullt:
                        self.tblfactor.insert("","end", values=[item.Namecustomer, item.Price, item.Date, item.State,
                                          item.Kala,item.Number])

    def Clean(self):
        if hasattr(self, 'tblfactor'):
            for item in self.tblfactor.get_children():
                self.tblfactor.delete(item)

    def Load_Factor(self):
        self.Clean()
        objbl = blPersonal()

        lstPersonal = objbl.blRead(Factor)
        for item in lstPersonal:
            # Check if tblfactor exists before accessing it
            if hasattr(self, 'tblfactor'):
                self.tblfactor.insert('', "end", values=[item.Namecustomer, item.Price, item.Date, item.State,
                                          item.Kala,item.Number,item.Id])




    def delete_factor(self):
        select_rows = self.tblfactor.selection()
        if select_rows:
            deletobj1 = blPersonal()
            for row in select_rows:
                prc_id1 = self.tblfactor.item(row)["values"][6]  # مطمئن شوید که index صحیح است
                obj = deletobj1.blReadById(Factor, prc_id1)

                if obj is None:
                    messagebox.showerror("خطا", f"آیتمی با شناسه {prc_id1} پیدا نشد")
                    continue

                result = deletobj1.blDelete(Factor, prc_id1)
                if not result:
                    messagebox.showerror("خطا", f"خطا در حذف اطلاعات با شناسه {prc_id1}")
                    return

            self.Load_Factor()  # پس از حذف موفق، جدول را بارگذاری کنید
            messagebox.showinfo("حذف", "اطلاعات با موفقیت حذف گردید")


    def new_factor(self):


        self.framfactor=Frame(bg="#939191")
        self.framfactor.place_configure(x=550,y=180,width=450,height=300)

        self.name_ctr=StringVar()
        self.date_fcr=StringVar()
        self.price_fcr=IntVar()
        self.number_fcr=IntVar()
        self.kala_fcr=StringVar()
        self.condition_fcr=StringVar()

        self.lblctr=Label(self.framfactor,text="نام مشتری")
        self.lblctr.place(x=385,y=110)
        self.entctr=Entry(self.framfactor,textvariable=self.name_ctr,justify=CENTER)
        self.entctr.place(x=260,y=110)

        self.lbldate=Label(self.framfactor,text="تاریخ صدور")
        self.lbldate.place(x=170,y=20)
        self.entdate = Entry(self.framfactor,textvariable=self.date_fcr, justify=CENTER)
        self.entdate.place(x=45, y=20)

        self.lblprice=Label(self.framfactor,text="قیمت")
        self.lblprice.place(x=393,y=180)
        self.entprice = Entry(self.framfactor,textvariable=self.price_fcr, justify=LEFT)
        self.entprice.place(x=255, y=180)

        self.lblnumber=Label(self.framfactor,text="شماره فاکتور ")
        self.lblnumber.place(x=370,y=20)
        self.entnumber = Entry(self.framfactor,textvariable=self.number_fcr, justify=LEFT)
        self.entnumber.place(x=245, y=20)

        self.lblkala=Label(self.framfactor,text="کالا")
        self.lblkala.place(x=210,y=110)
        self.entkala=Entry(self.framfactor,textvariable=self.kala_fcr,justify=CENTER)
        self.entkala.place(x=85,y=110)

        self.lblex=Label(self.framfactor,text="وضعیت")
        self.lblex.place(x=190,y=180)
        self.lblentex=Entry(self.framfactor,textvariable=self.condition_fcr,justify=CENTER,)
        self.lblentex.place(x=65,y=180)

        self.btnsavef=Button(self.framfactor,text="ذخیره",bg="darkgreen",padx=5,command=self.oncklick_Savedata_Factor)
        self.btnsavef.place(x=340,y=258)
        self.btncanself=Button(self.framfactor,text="انصراف",bg="red",command=self.Cansel_factor)
        self.btncanself.place(x=390,y=258)

        if self.is_factor_opened:
            self.framfactor_screen.place(x=244, y=55, width=750, height=420)
            self.tblfactor.place_configure(x=10, y=35, width=730, height=350)
            self.framfactor.place_configure(x=242, y=482, width=748, height=200)
            self.lblctr.place(x=680, y=100)
            self.entctr.place(x=550, y=100)
            self.lbldate.place(x=410, y=30)
            self.entdate.place(x=280, y=30)
            self.lblprice.place(x=440, y=100)
            self.entprice.place(x=300, y=100)
            self.lblnumber.place(x=680, y=30)
            self.entnumber.place(x=550, y=30)
            self.lblkala.place(x=180, y=30)
            self.entkala.place(x=50, y=30)
            self.lblex.place(x=190, y=100)
            self.lblentex.place(x=65, y=100)
            self.btnsavef.place(x=20, y=170)
            self.btneditfact.place(x=650, y=390)
            self.btndelete_factor.place(x=700, y=390)
            self.btnadd.place(x=635,y=5)
            self.btncanself.place(x=80, y=170)

        else:


            self.is_factor_opened = False




    def oncklick_Savedata_Factor(self):
        objp = Factor(self.date_fcr.get(), self.price_fcr.get(), self.condition_fcr.get(),self.name_ctr.get(),self.kala_fcr.get(),self.number_fcr.get())
        objbl = blPersonal()
        result = objbl.blAdd(objp)
        if result == True:
            self.Load_Factor()
            messagebox.showinfo("ثبت نام", "اطلاعات فرد با موفقیت ثبت گردید")


    def Cansel_factor(self):
        if self.framfactor:
            self.framfactor.place_forget()
            self.framfactor_screen.place(x=240, y=90, height=550, width=650)
            self.tblfactor.place_configure(x=30, y=35, width=600, height=475)
            self.txtsearch.place(x=170, y=8)
            self.boxsearch.place(x=30, y=10)
            self.btnadd.place(x=550, y=2)
            self.btneditfact.place(x=530, y=515)
            self.btndelete_factor.place(x=590, y=515)
            self.cancelfact.place(x=480, y=515)








    def open_mojudi(self,e):
        self.tblfactor_mini.place_forget()



        # Initialize the frame and table
        self.Frame_moj = Frame(self.screen, bg="#e43838",)
        self.Frame_moj.place(x=210, y=60, width=750, height=600)
        self.canselmoj=Button(self.Frame_moj,text="برگشت",command=self.canselMoj,bg='#f35757')
        self.canselmoj.place_configure(x=20,y=558)

        self.Search=StringVar()

        self.Id=StringVar()


        self.txtsearchm = Button(self.Frame_moj, text="جستجو",command=self.searchbox,bg="#0fc0e1")
        self.txtsearchm.place(x=150, y=4)

        self.boxsearch = Entry(self.Frame_moj,textvariable=self.Search,bg='#07d8ff')
        self.boxsearch.place(x=10, y=5)

        # Ensure table is initialized here
        self.tblmojudi = ttk.Treeview(self.Frame_moj, columns=("c1", "c2", "c3", "c4", "c5", "c6","c7"),
                                      show="headings")
        self.tblmojudi.heading("#5", text="شناسه کالا")
        self.tblmojudi.column("#5", width=105, anchor=CENTER)
        self.tblmojudi.heading("#1", text="قیمت")
        self.tblmojudi.column("#1", width=80, anchor=CENTER)
        self.tblmojudi.heading("#3", text="تعداد")
        self.tblmojudi.column("#3", width=20, anchor=CENTER)
        self.tblmojudi.heading("#6", text="نام کالا")
        self.tblmojudi.column("#6", width=105, anchor=CENTER)
        self.tblmojudi.heading("#2", text="رنگ")
        self.tblmojudi.column("#2", width=30, anchor=CENTER)
        self.tblmojudi.heading("#4", text="توضیحات")
        self.tblmojudi.column("#4", width=120, anchor=CENTER)
        self.tblmojudi.heading("#7", text="شماره")
        self.tblmojudi.column("#7", width=20, anchor=CENTER)
        self.tblmojudi.place(x=15, y=50, width=730, height=500)
        self.tblmojudi.bind("<Button-1>", self.GetSelection_mojudi)

        self.btneditmoj = Button(self.Frame_moj, text="ویرایش",command=self.OnClickEdit_mojudi,font="Yekan 11 ",bg='#e9cb04')
        self.btneditmoj.place(x=648, y=558)

        self.btndelet=Button(self.Frame_moj,text="حذف",bg="red",font="Yekan 10 ",command=self.delete,padx=5)

        self.btndelet.place(x=700, y=558)
        self.frammenuanbar.place_forget()

        self.Load()
        self.is_mojudi_opened = True

        # Populate sample data
        # ...

    def searchbox(self):
        stch=self.Search.get()
        if stch=="":
            self.Load()
        else:
            obj=blPersonal()
            resullt=obj.searchbox1(Mojudi,stch)
            if resullt!=[]:
                self.Clean_mojudi()

                for item in resullt:
                        self.tblmojudi.insert("","end", values=[item.Shenasekala, item.Nubmers, item.Namekala, item.Explain,
                                                         item.Pricekala,item.Color,item.Id])


    def Clean_mojudi(self):
        if hasattr(self, 'tblmojudi'):
            for item in self.tblmojudi.get_children():
                self.tblmojudi.delete(item)

    def Load(self):
        self.Clean_mojudi()

        objbl = blPersonal()

        lstPersonal = objbl.blRead(Mojudi)
        for item in lstPersonal:
            # Check if tblmojudi exists before accessing it
            if hasattr(self, 'tblmojudi'):
                self.tblmojudi.insert('', "end", values=[item.Shenasekala, item.Color, item.Nubmers, item.Pricekala,
                                                         item.Explain,item.Namekala,item.Id])
        # پر کردن نمونه داده در جدول




    def open_kala(self,e):


        self.fram_open_moj=Frame(bg="#939191")
        self.fram_open_moj.place_configure(x=215,y=480,height=200,width=750)

        #Var
        self.Color1=StringVar()
        self.Namekala=StringVar()
        self.Shenase=IntVar()
        self.Number=IntVar()
        self.Price=IntVar()
        self.Ex=StringVar()




        self.namegoods = ttk.Entry(self.fram_open_moj,textvariable=self.Namekala)
        self.namegoods.place(x=300, y=100)
        self.namegoods1 = Label(self.fram_open_moj, text=" نام کالا  ",bg="#939191", font=("Yekan 11 bold"))
        self.namegoods1.place(x=420, y=100)

        self.shenase1 = Label(self.fram_open_moj, text=" شناسه کالا ", bg="#939191", font=("Yekan 11 bold"))
        self.shenase1.place(x=200, y=100)
        self.shenase2 = ttk.Entry(self.fram_open_moj,textvariable=self.Shenase)
        self.shenase2.place(x=70, y=100)

        self.number = Label(self.fram_open_moj, text=" تعداد", font=("Yekan 11 bold"), bg="#939191")
        self.number.place(x=420, y=200)
        self.Comboo = StringVar()
        self.combo = ttk.Combobox(self.fram_open_moj, textvariable=self.Number, state="readonly", )
        self.allcount = Repository()
        self.combo["values"] = self.allcount.combocount()
        #self.combo.grid(row=0, column=0, padx=280, pady=200)
        self.combo.place_configure(x=270,y=200)
        self.color = Label(self.fram_open_moj, text="رنگ", bg="#939191", font=("Yekan 11 bold"))
        self.color.place(x=200, y=200)
        self.color1 = ttk.Entry(self.fram_open_moj, justify="right",textvariable=self.Color1,)
        self.color1.place(x=70, y=200)

        self.explain1 = ttk.Entry(self.fram_open_moj,textvariable=self.Ex, font=("nazanin 11"),justify=RIGHT)
        self.explain1.place_configure(height=20,width=170)
        self.explain1.place(x=241, y=330)
        self.explain = Label(self.fram_open_moj, text="توضیحات", bg="#939191", font=("Yekan 11 bold"))

        self.explain.place(x=410, y=330)

        self.price = Label(self.fram_open_moj, text="قیمت", bg="#939191", font=("Yekan 11 bold"))
        self.price.place(x=200, y=330)
        self.price1 = ttk.Entry(self.fram_open_moj,textvariable=self.Price )
        self.price1.place(x=70, y=330)

        self.cancel1 = Button(self.fram_open_moj, text="انصراف")
        self.cancel1.configure(font="Yekan 11 bold  ",background="#fe4545")
        self.cancel1.bind("<Button-1>", self.Canceladd)

        self.cancel1.place(x=430, y=380)

        self.Save= Button(self.fram_open_moj, text="ذخیره")
        self.Save.configure(font="Yekan 11 bold  ", background="#11d400",command=self.oncklick_Savedata_Mojudi)
        self.Save.place(x=380, y=380)
        self.frammenuanbar.place_forget()

        if self.is_mojudi_opened:
            self.fram_open_moj.place_configure(x=211, y=480, height=200, width=748)
            self.tblmojudi.place(x=15, y=29, width=730, height=342)
            self.Frame_moj.place(x=210, y=60, width=750, height=413)
            self.btneditmoj.place(x=648, y=380)
            self.btndelet.place_configure(x=700, y=380)
            self.namegoods.place(x=560, y=30)
            self.namegoods1.place(x=690, y=30)
            self.shenase1.place(x=438, y=30)
            self.shenase2.place(x=310, y=30)
            self.number.place(x=190, y=30)
            self.combo.place_configure(x=50,y=30)
            self.color.place(x=700, y=100)
            self.color1.place_configure(x=565, y=100)
            self.explain1.place_configure(x=270, y=100,height=20,width=170)
            self.explain.place_configure(x=450, y=100)
            self.price.place_configure(x=190, y=100)
            self.price1.place_configure(x=50, y=100)
            self.cancel1.place_configure(x=20, y=160)
            self.Save.place_configure(x=80, y=160)
        else:
            # تنظیمات دیگر در صورت عدم دسترسی به موجودی

            self.fram_open_moj.place_configure(x=300, y=60, height=420, width=500)
            self.Frame_moj.place_forget()
            self.tblmojudi.place_forget()



        self.is_mojudi_opened = False





    def oncklick_Savedata_Mojudi(self):
        objp = Mojudi(self.Namekala.get(), self.Color1.get(), self.Number.get(),self.Ex.get(),self.Price.get(),self.Shenase.get())
        objbl = blPersonal()
        result = objbl.blAdd(objp)
        if result == True:
            self.Load()
            messagebox.showinfo("ثبت نام", "اطلاعات فرد با موفقیت ثبت گردید")

    def GetSelection_mojudi(self,e):


        objbl=blPersonal()
        SelectRow=self.tblmojudi.selection()
        if SelectRow!=():


            #namerow = self.tbl.item(SelectRow)["values"][5]
            #self.Name.set(namerow)

            row_values = self.tblmojudi.item(SelectRow)["values"]
            self.Id.set(row_values)
            self.Price.set(row_values[0])  # قیمت
            self.Color1.set(row_values[1])  # رنگ
            self.Number.set(row_values[2])  # تعداد
            self.Ex.set(row_values[3])  # توضیحات
            self.Shenase.set(row_values[4])  # شناسه کالا
            self.Namekala.set(row_values[5])  # نام کالا
            self.Id.set(row_values[6])  # شماره (ID)





    def OnClickEdit_mojudi(self):
        Id1=self.Id1.get()

        #NewObject
        objp=Mojudi(self.Namekala.get(), self.Color1.get(), self.Number.get(),self.Ex.get(),self.Price.get(),self.Shenase.get())
        objbl=blPersonal()
        result=objbl.blUpdatemoj(Mojudi,Id1,objp)
        if result==True:
            self.Load()
            messagebox.showinfo("عملیات موفق", "عملیات ویرایش با موفقیت انجام شد")
        else:
            messagebox.showinfo("عملیات ناموفق", "عملیات ویرایش انجام نشد")




    def delete(self):
        select_rows = self.tblmojudi.selection()
        if select_rows:
            deletobj = blPersonal()
            for row in select_rows:
                prc_id = self.tblmojudi.item(row)["values"][6]  # مطمئن شوید که index صحیح است
                obj = deletobj.blReadById(Mojudi, prc_id)

                if obj is None:
                    messagebox.showerror("خطا", f"آیتمی با شناسه {prc_id} پیدا نشد")
                    continue

                result = deletobj.blDelete(Mojudi, prc_id)
                if not result:
                    messagebox.showerror("خطا", f"خطا در حذف اطلاعات با شناسه {prc_id}")
                    return

            self.Load()  # پس از حذف موفق، جدول را بارگذاری کنید
            messagebox.showinfo("حذف", "اطلاعات با موفقیت حذف گردید")

    def Cancel(self,e):
        if self.framfactor_screen:
            self.framfactor_screen.place_forget()


    def Cancelcost(self,e):
        if self.framcost:
            self.framcost.place_forget()




    def new_screensell_dis(self):
        if self.new_screensell:
            self.new_screensell.destroy()


    def Canceladd(self,e):
        if self.fram_open_moj:
            self.fram_open_moj.place_forget()
            if hasattr(self,'tblmojudi'):
                self.tblmojudi.place(x=15, y=50, width=730, height=500)
                self.Frame_moj.place(x=210, y=60, width=750, height=600)
                self.btneditmoj.place(x=630, y=550)
                self.btndelet.place(x=700, y=550)



    def focus_in(self):
        self.Password1.config(show="*")


    def open_menubar(self,e):



        self.frammenumoney.place(x=0,y=0)

        self.frammenuanbar.place(x=0,y=0)

    def Hide_All(self):

        self.frammenuanbar.place_forget()
        self.frammenumoney.place_forget()

    def hide_anbar_menu(self):
        self.frammenuanbar.place_forget()
    def hide_money_menu(self):
        self.frammenumoney.place_forget()
    def hide_home_menu(self):
        pass


    def close_menubar(self,e):

        self.frammenumoney.place_forget()
        self.frammenuanbar.place_forget()

    def hide(self):
        self.moneyfram.pack_forget()
        self.anbar.pack_forget()
         # Close the menu if it is open

    def hide1(self):
        self.anbar.pack_forget()
        # Close the menu if it is o
    def hide3(self):
        self.moneyfram.pack_forget()
          # Close the menu if it is open

    #تابع های صفحه
    def new_home(self,e):
        self.Load_Factor_Mini()
        self.Load_Cost_Mini()
        self.Load_Mojudi_Mini()

        self.Hide_All()

        self.hide1()
        self.hide3()
        self.fhome.place(x=1000, y=690)
        self.tblfactor_mini.place_configure(x=10, y=380, width=533, height=300)
        self.tblcost_mini.place_configure(x=600, y=70, width=380, height=300)
        self.tblmojudi_mini.place_configure(x=10, y=70, width=533, height=300)


    def new_win(self, e):
        self.Hide_All()
        self.tblfactor_mini.place_forget()
        self.tblmojudi_mini.place_forget()
        self.tblcost_mini.place_forget()


        self.hide1()
        self.hide3()
        self.moneyfram.pack(fill=BOTH, side=TOP, ipady=500)

    def menu(self):
        self.menu = Label(self.moneyfram, text="q", image=self.imagebtn, bg="#e74343")
        self.menu.place(x=0, y=10)




    def new_anbar(self, e):
        self.Hide_All()
        self.tblfactor_mini.place_forget()
        self.tblmojudi_mini.place_forget()
        self.tblcost_mini.place_forget()

        self.hide1()
        self.hide3()
        self.anbar.pack(fill=BOTH, side=TOP, ipady=500)

    def canselMoj(self):
        if self.Frame_moj:
            self.Frame_moj.place_forget()