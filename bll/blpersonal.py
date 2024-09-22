from dal.repository import Repository
from tkinter import messagebox

class blPersonal():

    def blAdd(self,obj):
        repos=Repository()
        result=repos.Add(obj)
        return result

    def blRead(self,TableName):
        repos=Repository()
        result=repos.Read(TableName)
        return result

    def blReadById(self,TableName,id):
        repos=Repository()
        result=repos.ReadById(TableName,id)
        return result

    def blDelete(self,TableName,id):
        repos=Repository()
        obj=repos.ReadById(TableName,id)
        return repos.Delete(obj)

    def blUpdatePersonal(self,TableName,id,datanew):
        repos=Repository()
        obj=repos.ReadById(TableName,id)
        return repos.UpdatePersonal(obj,datanew)


    def Mojudi(self, Tablename):
        repos = Repository()
        data = repos.Read(Tablename)
        if len(data) < 20:
            messagebox.showwarning("هشدار", "موجودی فعلی شما کمتر از 20 است")
        return data

    def searchbox1(self,Tablename,search):

        repos=Repository()
        new=repos.Search(Tablename,search)
        return new

    def searchbox2(self,Tablename,search):

        repos=Repository()
        new=repos.Searchf(Tablename,search)
        return new

    def searchbox3(self,Tablename,search):

            repos=Repository()
            new=repos.Searchc(Tablename,search)
            return new

    def blUpdatemoj(self, TableName, id, datanew):

        repos = Repository()
        obj = repos.ReadById(TableName, id)
        return repos.Update_mojudi(obj, datanew)

    def blUpdatefact(self, TableName, id, datanew):

        repos = Repository()
        obj = repos.ReadById(TableName, id)
        return repos.Update_factor(obj, datanew)

    def blUpdatecost(self, TableName, id, datanew):

        repos = Repository()
        obj = repos.ReadById(TableName, id)
        return repos.Update_cost(obj, datanew)

    def blReadLimit(self, TableName, limit=5):
        repos = Repository()
        obj=repos.ReadLimit(TableName,limit)
        return obj




class BusinessLogic:
    def __init__(self, data_access):
        self.data_access = data_access

    def add_item(self, item):
        if all(item):  # بررسی وجود تمامی مقادیر
            self.data_access.add_data(item)
            return True
        return False

    def get_items(self):
        return self.data_access.get_all_data()

