import shelve
db=shelve.open('persondb')

for key in sorted(db):
    print(key,'\t=>',db[key])

fei=db['fei m']  # Index by key to fetch
fei.giveRaise(.10)   # Update in memory using class's method
db['fei m']= fei # Assign to key to update in shelve
db.close()           # Close after making changes