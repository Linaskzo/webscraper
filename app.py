import csv

names = [

{'id': 2, 'first_name': 'Ahmed', 'last_name': 'Samir'},

{'id': 3, 'first_name': 'Waleed', 'last_name': 'Marzoog'},

{'id': 4, 'first_name': 'Hanaa', 'last_name': 'Sultan'},

{'id': 5, 'first_name': 'Tala', 'last_name': 'Naser'} ,

]

with open('names2.csv', 'w', newline='') as csvfile:
 fieldnmes = ['id','first_name','last_name']
 writer=csv.DictWriter(csvfile,fieldnames=fieldnmes)

 writer.writeheader()
 writer.writerow({'id':1,'first_name':'Mohammed','last_name':'Taher'})
 writer.writerows(names)
