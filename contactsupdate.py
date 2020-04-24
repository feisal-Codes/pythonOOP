from contacts import PhoneBook
import shelve
db=shelve.open('contactsdb')
for key in sorted(db):
    print(key,'\t=>',db[key])

fei=db['Feisal']
fei.updateContact('Feisal',716345234,'fem@gmail.com')
db['Feisal']=fei
db.close()

