import requests #for http things
import json #for json dumps things
import pprint 
from tkinter import * #for gui things
apikey = 'dc3ec57ee666562a7ccf3d77f2e1eb85' #openweathermap api key
requrl=''

def menuclick(menuvalue): #destroy previous window and allow central menu location for expansion
    root.destroy()
    if(menuvalue==2):
        setzip()
    if(menuvalue==1):
        setcity()
        
def setcity(): #enter city and link to url joiner
    root = Tk()
    store=""
    entercity=Label(text="enter your city")
    entercity.grid(row=0)
    e = Entry(width=50)
    e.grid(row=1,column=0)
    enterbutton = Button(root, text="Enter",command=lambda:[setcityurl(e.get()),root.destroy()])
    enterbutton.grid(row=1,column=1)
    
def setcityurl(var1):#city url joiner
    city=var1
    global requrl
    requrlcity=''.join(['https://api.openweathermap.org/data/2.5/forecast?q=',city,'&appid=',apikey]) #joins var city and var apikey to url
    requrl=requrlcity
    
def setzip(): #enter zip and link to url joiner
    root = Tk()
    enterzip=Label(text="enter your zipcode")
    enterzip.grid(row=0)
    e = Entry(width=50,text="input your zipcode")
    e.grid(row=1,column=0)
    enterbutton = Button(text="Enter",command=lambda: [setzipurl(e.get()),root.destroy()])
    enterbutton.grid(row=1,column=1)
    
def setzipurl(var1): #zip url joiner
    zipcode=var1
    global requrl
    requrlzip =''.join(['https://api.openweathermap.org/data/2.5/forecast?zip=',zipcode,'&appid=',apikey])
    requrl=requrlzip
    
root = Tk()
citybutton = Button(root, text="city",padx=50,pady=50, command=lambda: menuclick(1))
citybutton.grid(row=0,column=0)

zipbutton = Button(root, text="zipcode",padx=50,pady=50, command=lambda: menuclick(2))
zipbutton.grid(row=0,column=1)
root.mainloop()

json_object = json.loads(requests.get(requrl).text)
json_formatted_str = json.dumps(json_object, indent=1)
print(json_formatted_str)

ziporcityout = Label(text=(json_formatted_str))
ziporcityout.pack()
root.mainloop()