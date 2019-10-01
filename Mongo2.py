import pymongo


class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        print(self.client)

    def listDBS(self):
        k = 0
        print("Following Databases are Present")
        for i in self.client.database_names():
            k += 1
            print(k, ".", i)

    def createDB(self):
        self.dbname = input("Enter Database Name: ")
        re = self.client[self.dbname]
        self.client[self.dbname].create_collection("dummy_collection")  # Creating Blank Collection
        print(re)

    def choseDB(self):
        self.listDBS()
        self.dbch = int(input("Chose Database\n"))
        self.rr = self.client.database_names()
        self.mydb = self.rr[self.dbch - 1]
        print("Chosen Database is: ", self.mydb)

    def deleteDB(self):
        self.choseDB()
        cnfm = int(input("Press 1 to Delete 0 to Cancel:\n"))
        if cnfm == 1:
            print("Deleting.. " + self.mydb)
            self.client.drop_database(self.mydb)
            print(self.mydb)
            if self.mydb not in self.client.database_names():
                print("Deleted Successfully")
            else:
                print("Delete Error")
        else:
            pass

    def listCollections(self):
        self.choseDB()
        k = 0
        print("Following Collections are present.")
        for i in self.client[self.mydb].collection_names():
            k += 1
            print(k, '.', i)

    def createCollection(self):
        self.choseDB()
        cname = input("Enter Collection Name:\n")
        r1 = self.client[self.mydb].create_collection(cname)
        print(r1)
        if cname in self.client[self.mydb].collection_names():
            print("Collection " + cname + " Created Successfully")
        else:
            print("Collection creation failed.")

    def deleteCollection(self):
        self.listCollections()
        ch = int(input("\nChoose collection No to Delete: \n"))
        ch -= 1
        self.clist = self.client[self.mydb].collection_names()
        cname = self.clist[ch]
        self.client[self.mydb].drop_collection(cname)
        if cname not in self.client[self.mydb].collection_names():
            print("Collection " + cname + " Deleted Successfully")
        else:
            print("Deletion Error")

    def showData(self, datbase_name, collection_name):
        record = self.client[datbase_name][collection_name].find({}, {'_id': False})  # Filtering
        final_record = list(record)  # Its a cursor and need to translate to list
        print(final_record)
        for i in final_record:
            for k, v in i.items():
                print(k, v)

    def showDocument(self):
        self.listCollections()
        chCol = int(input("Choose Collection:\n"))
        chCol -= 1
        self.clist = self.client[self.mydb].collection_names()
        self.cname = self.clist[chCol]
        print("Chosen Collection is: ", self.cname)
        print("-" * 20, "Cureent Data", "-" * 20)
        self.showData(self.mydb, self.cname)
        print("-" * 55)

    def test(self):
        client = pymongo.MongoClient('mongodb://localhost:27017/')

        db = client.testdb
        rr = client.cars.find()
        cars = db.cars.find()

        for car in cars:
            print('{0} {1}'.format(car['name'],
                                   car['price']))

    def insertDocumentSingle(self):
        self.listCollections()
        chCol = int(input("Choose Collection:\n"))
        chCol -= 1
        self.clist = self.client[self.mydb].collection_names()
        self.cname = self.clist[chCol]
        print("Chosen Collection is: ", self.cname)
        print('1. {"Key1":"Value1}"')
        print('2. {"Key1":"Value1}"')
        new_document = int(input("Chose any Document to Insert:"))
        if new_document == 1:
            new_data = {"Key1": "Value1"}
        else:
            new_data = {"Key2": "Value2"}
        re=self.client[self.mydb][self.cname].insert_one(new_data)
        print(re)

    def insertDocumentMany(self):
        self.listCollections()
        chCol = int(input("Choose Collection:\n"))
        chCol -= 1
        self.clist = self.client[self.mydb].collection_names()
        self.cname = self.clist[chCol]
        print("Chosen Collection is: ", self.cname)
        new_data = [{"name": "Amy", "address": "Apple st 652"}, {"name": "Hannah", "address": "Mountain 21"}]
        re=self.client[self.mydb][self.cname].insert_many(new_data)
        print(re)

    def deleteDocument(self):
        self.listCollections()
        chCol = int(input("Choose Collection:\n"))
        chCol -= 1
        self.clist = self.client[self.mydb].collection_names()
        self.cname = self.clist[chCol]
        print("Chosen Collection is: ", self.cname)
        print("-" * 40)
        record = self.client[self.mydb][self.cname].find({}, {'_id': False})  # Filtering
        final_record = list(record)  # Its a cursor and need to translate to list
        k = 1
        if len(final_record)==0:
            print("No Document Present to Delete.Continuing")
            pass
        else:
            for i in final_record:
                print(k, ".", i)
                k += 1
            ch = int(input("Chose Document to Delete"))
            ch -= 1
            query = final_record[ch]
            re = self.client[self.mydb][self.cname].delete_one(query)
            print("Delete Status", re)


if __name__ == "__main__":
    ob = Mongo()
    while True:
        print("------------------------------")
        print("0  to Exit:")
        print("1  to List Databases:")
        print("2  to Create Database:")
        print("3  to Delete Database:")
        print("4  to List Collection:")
        print("5  to Create Collection:")
        print("6  to Delete Collection")
        print("7  to Show Document")
        print("8  to Insert Document:Single")
        print("9  to Insert Document:Many")
        print("10 to Delete Document")
        print("-------------------------------\n")
        ch = int(input())
        if ch == 0:
            exit()
        elif ch == 1:
            ob.listDBS()
        elif ch == 2:
            ob.createDB()
        elif ch == 3:
            ob.deleteDB()
        elif ch == 4:
            ob.listCollections()
        elif ch == 5:
            ob.createCollection()
        elif ch == 6:
            ob.deleteCollection()
        elif ch == 7:
            ob.showDocument()
        elif ch == 8:
            ob.insertDocumentSingle()
        elif ch == 9:
            ob.insertDocumentMany()
        elif ch == 10:
            ob.deleteDocument()
        else:
            print("Error!")
