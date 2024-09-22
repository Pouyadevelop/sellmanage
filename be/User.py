from sqlalchemy import create_engine,Column,String,Integer,NVARCHAR
from sqlalchemy.orm import declarative_base
from be.setting import setting
import pyodbc
conn=setting().connection()
engin=create_engine(str(conn))
Base=declarative_base()


class User(Base):
    __tablename__="User"
    id=Column(Integer,primary_key=True,autoincrement=True)
    Name=Column(NVARCHAR)
    Family=Column(NVARCHAR)


    def __init__(self,Name="",Family=""):
        self.Name=Name
        self.Family=Family

class Factor(Base):
    __tablename__ = "Factor"
    Id=Column(Integer,primary_key=True,autoincrement=True)
    Number=Column(NVARCHAR)
    Date=Column(NVARCHAR)
    Price=Column(NVARCHAR)
    State=Column(NVARCHAR)
    Namecustomer=Column(NVARCHAR)
    Kala=Column(NVARCHAR)

    def __init__(self,Date,Price,State,Namecustomer,Kala,Number):
        self.Date=Date
        self.State=State
        self.Namecustomer=Namecustomer
        self.Kala=Kala
        self.Price=Price
        self.Number=Number

class Mojudi(Base):
    __tablename__ = "Mojudi"
    Id=Column(Integer,primary_key=True,autoincrement=True)
    Namekala=Column(NVARCHAR)
    Color=Column(NVARCHAR)
    Nubmers=Column(NVARCHAR)
    Pricekala=Column(NVARCHAR)
    Shenasekala=Column(NVARCHAR)
    Explain=Column(NVARCHAR)

    def __init__(self,Namekala,Color,Nubmers,Pricekala,Shenasekala,Explain):
        self.Pricekala=Pricekala
        self.Namekala=Namekala
        self.Color=Color
        self.Shenasekala=Shenasekala
        self.Nubmers=Nubmers
        self.Explain=Explain

class Cost(Base):
    __tablename__ = "Cost"
    Id=Column(Integer,primary_key=True,autoincrement=True)
    PriceCost=Column(NVARCHAR)
    StatCost=Column(NVARCHAR)
    TypeCost=Column(NVARCHAR)
    DateCost=Column(NVARCHAR)
    ExplainCost=Column(NVARCHAR)

    def __init__(self,PriceCost,StatCost,TypeCost,DateCost,ExplainCost):
        self.PriceCost=PriceCost
        self.StatCost=StatCost
        self.TypeCost=TypeCost
        self.DateCost=DateCost
        self.ExplainCost=ExplainCost





Base.metadata.create_all(engin)