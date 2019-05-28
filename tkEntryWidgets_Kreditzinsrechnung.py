#!/usr/bin/python
#  tkEntryWidgets_Kreditzinsrechnung
# -*- coding: iso-8859-15 -*-
from sys import version_info
if version_info.major == 3:
    from tkinter import *   # python 3.2
elif version_info.major == 2:
    from Tkinter import *   # python 2.7
else:
    print ("what the hell you are running?  :D")
fields = ('Annual Rate (Jahreszins %)', 'Nr / Payments (Ratenanzahl)', 'Loan Principle (Kreditsumme)', 'Payment/Month (Monatsrate)', 'Remaining Loan (Restschuld)')

def monthly_payment(entries):
   # period rate:
   r = (float(entries['Annual Rate (Jahreszins %)'].get()) / 100) / 12
# avoid division by zero -- added J.Klotzner
   if r==0:
      r=0.0000000001
   print("r", r)
   # principal loan:
   loan = float(entries['Loan Principle (Kreditsumme)'].get())
   n =  float(entries['Nr / Payments (Ratenanzahl)'].get())
   remaining_loan = float(entries['Remaining Loan (Restschuld)'].get())
   q = (1 + r)** n
   monthly = r * ( (q * loan - remaining_loan) / ( q - 1 ))
   monthly = ("%8.2f" % monthly).strip()
   entries['Payment/Month (Monatsrate)'].delete(0,END)
   entries['Payment/Month (Monatsrate)'].insert(0, monthly )
   print("Payment/Month (Monatsrate): %s" % monthly)

def final_balance(entries):
   # period rate:
   r = (float(entries['Annual Rate (Jahreszins %)'].get()) / 100) / 12
# avoid division by zero -- added J.Klotzner
   if r==0:
      r=0.0000000001
   print("r", r)
   # principal loan:
   loan = float(entries['Loan Principle (Kreditsumme)'].get())
   n =  float(entries['Nr / Payments (Ratenanzahl)'].get())
   q = (1 + r)** n
   monthly = float(entries['Payment/Month (Monatsrate)'].get())
   q = (1 + r)** n
   remaining = q * loan  - ( (q - 1) / r) * monthly
   remaining = ("%8.2f" % remaining).strip()
   entries['Remaining Loan (Restschuld)'].delete(0,END)
   entries['Remaining Loan (Restschuld)'].insert(0, remaining )
   print("Remaining Loan (Restschuld): %s" % remaining)

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=25, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)

   ents['Annual Rate (Jahreszins %)'].delete(0,END )
   ents['Annual Rate (Jahreszins %)'].insert(0,5 )
   ents['Nr / Payments (Ratenanzahl)'].delete(0,END )
   ents['Nr / Payments (Ratenanzahl)'].insert(0,120 )
   ents['Loan Principle (Kreditsumme)'].delete(0,END )
   ents['Loan Principle (Kreditsumme)'].insert(0,100000 )

   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Final Balance\nBerechne Restzahlung',
          command=(lambda e=ents: final_balance(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Monthly Payment\nBerechne Monatsrate',
          command=(lambda e=ents: monthly_payment(e)))
   b2.pack(side=LEFT, padx=5, pady=5)
   b3 = Button(root, text='Quit', command=root.quit)
   b3.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
