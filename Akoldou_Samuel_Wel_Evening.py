# Day3 individual Assignment

 # EXERCISE 5( DICTIONARIES)

shoes = {"brand":"Nick",
            "color": "black",
            " size": 40
          }
shoes["brand"] = "Adidas"
print(shoes)
shoes["type"] = "sneakers"
print(shoes)
r = shoes.keys()
print(r)
h = shoes.values()
print(h)
if shoes.get("size") == None:
    print("size exists")
else:
        print("does not exist")
for w in shoes:
   print(w)
shoes.pop("color")
print(shoes)
#del shoes
#print(shoes)

marks = {"maths": 90, "English": 98,"chemistry": 100 }
mark2 = marks.copy() 
print(mark2)
fruit1 = {"Mango": 1,
        "Orange" :2 ,
        "Apple": 3 
        }
fruit2 = {"Banana": 4,
          "pineaaple": 5
          }
total = {
"fruit1" : fruit1 ,
"fruit2" : fruit2
        }
print(total)
  

   # EXERCISE 4(STRINGS)
a = 20
b = "marks"
d = f"{a} {b}"
print(d)
txt = " Hello,   Uganda!  "
txt.strip()
replaced = txt.replace(" " , "")
print(replaced)
print(txt.upper())
print(txt.replace("U","V"))
y = "Iam proudly Ugandan"
print(y[1:5])
# x = "All "Data Scientists" are cool!"
U = "All \"Data Scientists\" are cool"
print(U)


 # EXERCISE 3(SETS)

beverages = set(("milk","juice","coffee"))
print(beverages)
beverages2 = {"water","wine","cofee"}
beverages3 = {"softdrink","porridge"}
beverages2.update(beverages3)
print(beverages2)
myset = {"oven","kettle","microwave","refrigerator"}
print("microwave" in myset)
myset.remove("kettle")
print(myset)
for k in myset:
    print(k)
    set1 = {1,2,3,4}
    list1 = [20,30,]
    set1.update(list1)
    print(set1)
    ages = { 10,16,18}
    firstname = {"Akoldo","Samuel","Wel"}
    set3 =ages.union(firstname)
    print(set3)

    # EXERCISE 2(TUPLES)
    ]
x = ("samsung","iphone","techno","redmi")
print(x[1])
print(x[-2])
y = list(x)
y[1] = "ite1"
x =tuple(y)
print(x)
m = list(x)
m.append("Huawei")
x = tuple(m)
print(x)
for p in x:
   print(p)
d = list(x)
d.remove("samsung")
x = tuple(d)
print(x)
cities = tuple(("kampala","Gulu","Arua","Mbarara","Lira"))
print(cities)
(kampala,Gulu,Arua,Mbarara,Lira) = cities
print(kampala)
print(Gulu)
print(Arua)
print(Mbarara)
print(Lira)
print(cities[2:6])
myname1 = ("Akoldou","Samuel")
myname2 = ( "Wel","Machiek")
myname = myname1 + myname2
print(myname)
colors = ("red","blue","black")
mytuple = colors * 3
print(mytuple)
thistuple = (1,3,7,8,7,5,4,6,8,5)
k = thistuple.count(8)
print(k)


# EXERCISE 1(LISTS)

names = ["Mary","John","Sam","Wel","Mark"]
print(names[1])
#2
names[0] = "Akoldou"
print(names)
names.append("Martha")
print(names)
names[2] = "Bathel"
print(names)
names.pop(3)
print(names)
print(names[-1])

numbers = [1,2,3,4,5,6,7]
print(names[2:6])
countries1= ["Uganda","Kenya","Tazania","South Sudan"]
countries2 = countries1.copy()
print(countries2)
for x in countries1:
    print(x)
animalnames = ["lion","zebra","girrafe","cow"]
# sorting in assending order
animalnames.sort()
print(animalnames)
# sorting in descending order
animalnames.sort(reverse = True)
print(animalnames)
#def myFunc(e):
 #return e (animalnames("a"))
#animalnames = ["lion","zebra","girrafe","cow"]
#animalnames.sort(key=myFunc)
#print(animalnames)

list5 = ["AKOLDOU","SAMUEL"]
list6 = ["WEL","MACHIEK"]
total8 = list5 + list6
print(total8)





