import tkinter
import requests
mainpage=tkinter.Tk()
mainpage.title="conect to api"
apikey=tkinter.Entry(master=mainpage)

apisecret=tkinter.Entry(master=mainpage)

def hello():
    session = requests.session()
    session.auth = (apikey.get(), apisecret.get())
    e = session.get("https://api.hitbtc.com/api/2/account/balance").json()
    g=[]
    for i in e:
        q=(i.pop("available"))
        w=(i.pop("currency"))
        if q != "0":
            d=(q+"        "+w)
            g.append(d )
    print(g)
    r=tkinter.Message(master=mainpage,text=g)

    r.grid(row=2,column=2)
e=tkinter.Button(master=mainpage,command=hello,text="click here")
apikey_label=tkinter.Label(mainpage, text = 'apikey', font=('calibre',10, 'bold'))
apisecret_label=tkinter.Label(mainpage, text = 'apisecret', font=('calibre',10, 'bold'))
apikey_label.grid(row=0,column=0)
apikey.grid(row=0,column=1)
apisecret_label.grid(row=1,column=0)
apisecret.grid(row=1,column=1)
e.grid(row=2,column=1)

mainpage.mainloop()