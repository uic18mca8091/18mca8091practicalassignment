from tkinter import *
from tkinter import ttk
import smtplib


gmail_user = 'uic.18mca8091@gmail.com'
gmail_password = '8988491681a'

def sendmail():
    try:
        var2=password.get()
        cc=[receiver.get()]
        bcc=[bcc1.get()]
        var5=subject.get()
        sent_from=gmail_user
        msg = msgbody.get('1.0','end')
        msgtosend = "From: %s\r\n" % gmail_user + "To: %s\r\n" % var2 + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % var5 + "\r\n" + msg
        
        toaddrs = [var2] + cc + bcc
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, toaddrs, msgtosend)
        server.close()
    
        print ('Email sent!')
        ttk.Label(mainframe, text=str('Email sent!')).grid(column=4,row=9,sticky=W)
    except Exception as e:
        print ('Something went wrong...')
        ttk.Label(mainframe, text=str(e)).grid(column=4,row=9,sticky=W) 

root = Tk()
root.title("Compose Email")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()
bcc1 = StringVar()



ttk.Label(mainframe, text="From ").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text=str(gmail_user)).grid(column=4, row=1, sticky=(W, E))

ttk.Label(mainframe, text="To ").grid(column=3, row=2, sticky=E)
password_entry = ttk.Entry(mainframe, width=30, textvariable=password)
password_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Cc ").grid(column=3, row=3, sticky=E)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
receiver_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Bcc ").grid(column=3, row=4, sticky=E)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=bcc1)
receiver_entry.grid(column=4, row=4, sticky=(W, E))

ttk.Label(mainframe, text="Subject ").grid(column=3, row=5, sticky=E)
subject_entry = ttk.Entry(mainframe, width=30, textvariable=subject)
subject_entry.grid(column=4, row=5, sticky=(W, E))

ttk.Label(mainframe, text="Attachments ").grid(column=3, row=6, sticky=E)

msgbody = Text(mainframe, width=60, height=10)
msgbody.grid(column=4, row=7, sticky=(W, E))

ttk.Button(mainframe, text="Send", command=sendmail).grid(column=4,row=8,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

password_entry.focus()

root.mainloop()

