from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from be.setting import setting
from sqlalchemy import *

conn=setting().connection()
engine=create_engine(conn)
Sessions=sessionmaker(bind=engine)
session=Sessions()

#CRUD
class Repository():


    def Add(self,obj):
        session.add(obj)
        session.commit()
        return True

    def Read(self,TableName):
        return session.query(TableName).all()
        #output->List


    def ReadById(self,TableName,id):
        return session.query(TableName).filter(TableName.Id==id).first()
        #output->Object


    def Delete(self,obj):
        session.delete(obj)
        session.commit()
        return True


    def UpdatePersonal(self,objold,objnew):
        objold.prs_name=objnew.prs_name
        objold.prs_family=objnew.prs_family
        objold.prs_age=objnew.prs_age
        objold.prs_date=objnew.prs_date
        objold.prs_ghodrati=objnew.prs_ghodrati
        objold.prs_havazi=objnew.prs_havazi
        session.commit()
        return True


    def Search(self,Tablename,search):
        result=session.query(Tablename).filter((Tablename.Namekala.like(f"%{search}%"))|
                                               (Tablename.Nubmers.like(f"%{search}%")) |
                                               (Tablename.Shenasekala.like(f"%{search}%"))|
                                                (Tablename.Explain.like(f"%{search}%"))|
                                                 (Tablename.Pricekala.like(f"%{search}%")))
        return result


    def Searchf(self,Tablename,search):
        result=session.query(Tablename).filter((Tablename.Kala.like(f"%{search}%"))|
                                               (Tablename.Namecustomer.like(f"%{search}%")) |
                                               (Tablename.State.like(f"%{search}%"))|
                                                (Tablename.Price.like(f"%{search}%"))|
                                                 (Tablename.Date.like(f"%{search}%"))|
                                               (Tablename.Number.like(f"%{search}%")))
        return result

    def Searchc(self,Tablename,search):
            result=session.query(Tablename).filter((Tablename.ExplainCost.like(f"%{search}%"))|
                                                   (Tablename.DateCost.like(f"%{search}%")) |
                                                   (Tablename.TypeCost.like(f"%{search}%"))|
                                                    (Tablename.StatCost.like(f"%{search}%"))|
                                                     (Tablename.PriceCost.like(f"%{search}%"))
                                                   )
            return result



    def Update_mojudi(self,objold,objnew):
        objold.Explain=objnew.Explain
        objold.Shenasekala=objnew.Shenasekala
        objold.Pricekala=objnew.Pricekala
        objold.Nubmers=objnew.Nubmers
        objold.Color=objnew.Color
        objold.Namekala=objnew.Namekala
        session.commit()
        return True


    def Update_factor(self,objold,objnew):
        objold.Kala=objnew.Kala
        objold.Namecustomer=objnew.Namecustomer
        objold.State=objnew.State
        objold.Price=objnew.Price
        objold.Date=objnew.Date
        objold.Number=objnew.Number
        session.commit()
        return True


    def Update_cost(self,objold,objnew):
        objold.ExplainCost=objnew.ExplainCost
        objold.DateCost=objnew.DateCost
        objold.TypeCost=objnew.TypeCost
        objold.StatCost=objnew.StatCost
        objold.PriceCost=objnew.PriceCost

        session.commit()
        return True

    def ReadLimit(self, TableName, limit=5):
        return session.query(TableName).order_by(desc(TableName.Id)).limit(limit).all()

    def Readlimit1(self, TableName, limit=None):
        query = session.query(TableName).order_by(asc(TableName.Id))

        if limit:
            query = query.limit(limit)

        return query.all()

    def combocount(self):
        counter=[]
        for item in range(1,51):
            counter.append(item)
        return counter

class  DataAccess():
    def __init__(self):
            self.data = []  # در اینجا داده‌ها را ذخیره می‌کنیم

    def add_data(self, item):
            self.data.append(item)  # داده جدید را به لیست اضافه می‌کند

    def get_all_data(self):
            return self.data  # تمامی داده‌ها را برمی‌گرداند