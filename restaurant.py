import tkinter as tk
from tkinter import*
from tkinter import ttk
import sqlite3

root=tk.Tk()
root.title("Management system")
#initialising database**************************************************************

connection=sqlite3.connect("resturant.db")

#initialising new variables for database****************************************************

TABLE_NAME="management_table"
TABLE_ID="table_id"
CHICKEN_ID="chicken_id"
CHAPPATI_ID="chappati_id"
DAAL_ID="daal_id"
VEGETABLE_ID="vegetable_id"
DRINKS_ID="drinks_id"
DESERT_ID="desert_id"
SNACK_ID="snack_id"
COST_ID="cost_id"
SERVICE_ID="service_id"
GST_ID="gst_id"
TOTAL_ID="total_id"
# sqlite variables********************************************************************************************************************************************************************************************************************************************************************************************************************************************

connection.execute("CREATE TABLE IF NOT EXISTS "+TABLE_NAME+" ( "+TABLE_ID+" INTEGER PRIMARY KEY AUTOINCREMENT , "
                   +CHICKEN_ID+" INTEGER, "+CHAPPATI_ID+" INTEGER, "+DAAL_ID+" INTEGER, "+VEGETABLE_ID+" INTEGER,"
                   +DRINKS_ID+" INTEGER, "+DESERT_ID+" INTEGER, "+SNACK_ID+" INTEGER, "+COST_ID+" INTEGER, "+
                   SERVICE_ID+" INTEGER, "+GST_ID+" INTEGER, "+TOTAL_ID+" INTEGER );")

#heading presentation****************************************************************
appLabel=tk.Label(root,text="RESTURANT MANAGEMENT SYSTEM",width=90,bg="orange",fg="#ffff00")
appLabel.config(font=("sylfaen",30))
appLabel.grid(row=0,columnspan=5,padx=(30,30),pady=(30,0))
#implementing class************************************************************************
class Resturant:
    chicken=""
    chappati=""
    daal=""
    vegetable=""
    drinks=""
    desert=""
    snack=""
    cost=""
    service=""
    gst=""
    total=""

#defining a constructor function***************************************************************************

    def __init__(self,chicken,chappati,daal,vegetable,drinks,desert,snack,cost,service,gst,total):
        self.chicken =chicken
        self.chappati =chappati
        self.daal = daal
        self.vegetable =vegetable
        self.drinks = drinks
        self.desert = desert
        self.snack = snack
        self.cost = cost
        self.service =service
        self.gst = gst
        self.total =total

#defining variables that is used to print labels**************************************************

varChicken=tk.Label(root,text="CHICKEN_MEAL",fg="#adff2f",anchor='w')
varChicken.grid(row=1,column=0,padx=(30,0),pady=(10,0))
varChicken.config(font=("sylfaen",20))
varChappati=tk.Label(root,text="CHAPPATI_MEAL",fg="#adff2f",anchor='w')
varChappati.grid(row=2,column=0,padx=(30,0),pady=(10,0))
varChappati.config(font=("sylfaen",20))
varDaal=tk.Label(root,text="DAAL_MEAL",fg="#adff2f",anchor='w')
varDaal.grid(row=3,column=0,padx=(30,0),pady=(10,0))
varDaal.config(font=("sylfaen",20))
varVegetable=tk.Label(root,text="VEGETABLE_MEAL",fg="#adff2f",anchor='w')
varVegetable.grid(row=4,column=0,padx=(30,0),pady=(10,0))
varVegetable.config(font=("sylfaen",20))
varDrink=tk.Label(root,text="DRINK_MEAL",fg="#adff2f",anchor='w')
varDrink.grid(row=5,column=0,padx=(30,0),pady=(10,0))
varDrink.config(font=("sylfaen",20))
varDesert=tk.Label(root,text="DESERT_MEAL",fg="#adff2f",anchor='w')
varDesert.grid(row=1,column=2,padx=(30,0),pady=(10,0))
varDesert.config(font=("sylfaen",20))
varSnack=tk.Label(root,text="SNACK_MEAL",fg="#adff2f",anchor='w')
varSnack.grid(row=2,column=2,padx=(30,0),pady=(10,0))
varSnack.config(font=("sylfaen",20))
varCost=tk.Label(root,text="COST_MEAL",fg="#adff2f",anchor='w')
varCost.grid(row=3,column=2,padx=(30,0),pady=(10,0))
varCost.config(font=("sylfaen",20))
varService=tk.Label(root,text="SERVICE_MEAL",fg="#adff2f",anchor='w')
varService.grid(row=4,column=2,padx=(30,0),pady=(10,0))
varService.config(font=("sylfaen",20))
varGst=tk.Label(root,text="GST_MEAL",fg="#adff2f",anchor='w')
varGst.grid(row=5,column=2,padx=(30,0),pady=(10,0))
varGst.config(font=("sylfaen",20))
varTotal=tk.Label(root,text="TOTAL_MEAL",fg="#adff2f",anchor='w')
varTotal.grid(row=7,column=1,padx=(30,0),pady=(10,0))
varTotal.config(font=("sylfaen",20))

#some important variables**********************************************which is kept blank for further use***********

chickenItem=""
chappatiItem=""
daalItem=""
vegetableItem=""
drinkItem=""
desertItem=""
snackItem=""
costItem=""
serviceItem=""
gstItem=""
totalItem=""
list=[]

#now some entry space to be created***************************************************************************************
chickenEntry=Entry()
chappatiEntry=Entry()
daalEntry=Entry()
vegetableEntry=Entry()
drinkEntry=Entry()
desertEntry=Entry()
snackEntry=Entry()
costEntry=Entry()
serviceEntry=Entry()
gstEntry=Entry()
totalEntry=Entry()

#now defining the entry section*****************************************************************

chickenEntry.grid(row=1,column=1)
chappatiEntry.grid(row=2,column=1)
daalEntry.grid(row=3,column=1)
vegetableEntry.grid(row=4,column=1)
drinkEntry.grid(row=5,column=1)
desertEntry.grid(row=1,column=3)
snackEntry.grid(row=2,column=3)
costEntry.grid(row=3,column=3)
serviceEntry.grid(row=4,column=3)
gstEntry.grid(row=5,column=3)
totalEntry.grid(row=7,column=3)

#now creating a function to take input whick is used for function of button*********************
def takeInput():
    global chickenItem,chappatiItem,daalItem,vegetableItem,drinkItem,desertItem,snackItem,costItem,serviceItem,gstItem,totalItem
    global chickenEntry,chappatiEntry,daalEntry,vegetableEntry,drinkEntry,desertEntry,snackEntry,costEntry,serviceEntry,gstEntry,totalEntry
    global list
    global TABLE_NAME,TABLE_ID,CHICKEN_ID,CHAPPATI_ID,DAAL_ID,VEGETABLE_ID,DRINKS_ID,DESERT_ID,SNACK_ID,COST_ID,SERVICE_ID,GST_ID,TOTAL_ID
    chickenItem=chickenEntry.get()
    chappatiItem=chappatiEntry.get()
    daalItem=daalEntry.get()
    vegetableItem=vegetableEntry.get()
    drinkItem=drinkEntry.get()
    desertItem=desertEntry.get()
    snackItem=snackEntry.get()
    costItem=costEntry.get()
    serviceItem=serviceEntry.get()
    gstItem=gstEntry.get()
    totalItem=totalEntry.get()

    connection.execute("INSERT INTO "+TABLE_NAME+ " ( "+CHICKEN_ID+","+CHAPPATI_ID+", "+DAAL_ID+", "+
                       VEGETABLE_ID+", "+DRINKS_ID+", "+DESERT_ID+", "+SNACK_ID+", "+COST_ID+", "+SERVICE_ID+", "+
                       GST_ID+", "+TOTAL_ID+" ) VALUES ( "+str(chickenItem)+ ","+str(chappatiItem)+","+
                       str(daalItem)+","+str(vegetableItem)+","+str(drinkItem)+","+str(desertItem)+","+
                       str(snackItem)+","+str(costItem)+","+str(serviceItem)+","+str(gstItem)+","+str(totalItem)+");")
    connection.commit()


#now another funciton for delete button*************************************************************

def deleteFunction():
    global chickenItem, chappatiItem, daalItem, vegetableItem, drinkItem, desertItem, snackItem, costItem, serviceItem, gstItem, totalItem
    global chickenEntry, chappatiEntry, daalEntry, vegetableEntry, drinkEntry, desertEntry, snackEntry, costEntry, serviceEntry, gstEntry, totalEntry
    global list
    chickenEntry.delete(0,END)
    chappatiEntry.delete(0,END)
    daalEntry.delete(0,END)
    vegetableEntry.delete(0,END)
    drinkEntry.delete(0,END)
    desertEntry.delete(0,END)
    snackEntry.delete(0,END)
    costEntry.delete(0,END)
    serviceEntry.delete(0,END)
    gstEntry.delete(0,END)
    totalEntry.delete(0,END)


#print fuction is now created to used in the print button*******************************************

def printFunction():
    for singleItem in list:
        print("the values are %f\n %f\n %f\n %f\n %f\n %f\n %f\n %f\n %f\n %f\n %f\n" % (singleItem.chicken,singleItem.chappati,singleItem.daal,singleItem.vegetable,singleItem.drinks,singleItem.desert,singleItem.snack,singleItem.cost,singleItem.service,singleItem.gst,singleItem.total))
        print("*********************************************************************************************************************")

def deleteWindow():
    root.destroy()


inputButton=tk.Button(root,text="TAKE INPUT",bg="silver",command=takeInput)
inputButton.grid(row=9,column=1)

deleteButton=tk.Button(root,text="DELETE",bg="silver",command=deleteFunction)
deleteButton.grid(row=9,column=2)

displayButton=tk.Button(root,text="PRINT",bg="silver",command=deleteWindow)
displayButton.grid(row=9,column=3)

root.mainloop()
#new window to be opened from here**********************************************************************

window=tk.Tk()
window.title("printed")

appLabel=tk.Label(window,text="RESTURANT MANAGEMENT SYSTEM",width=90,bg="orange",fg="#ffff00")
appLabel.config(font=("sylfaen",30))

tree=ttk.Treeview(window)
tree["column"]=("one","two","three","four","five","six","seven","eight","nine","ten","eleven")
tree.column("one",width=200)
tree.column("two",width=200)
tree.column("three",width=200)
tree.column("four",width=200)
tree.column("five",width=200)
tree.column("six",width=200)
tree.column("seven",width=200)
tree.column("eight",width=200)
tree.column("nine",width=200)
tree.column("ten",width=200)
tree.column("eleven",width=200)
tree.heading("one",text="chicken_price")
tree.heading("two",text="chappati_price")
tree.heading("three",text="daal-price")
tree.heading("four",text="vegetable_price")
tree.heading("five",text="DRINKS_PRICE")
tree.heading("six",text="DESERT_PRICE")
tree.heading("seven",text="SNACK_PRICE")
tree.heading("eight",text="cost")
tree.heading("nine",text="Service")
tree.heading("ten",text="GST")
tree.heading("eleven",text="TOTAL")

cursor=connection.execute("SELECT*FROM "+TABLE_NAME+";")
i=0
for row in cursor:
    tree.insert('',i,text="FOOD ITEM"+str(row[0]),values=\
        (row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
i=i+1
tree.pack()
connection.close()
window.mainloop()