

 # AFTERNOON EXERCISE 

fruits = {"mango": 1,"orange": 2,"apple":3,"ovacoda":4}
print(fruits)
print(fruits.keys())
print(fruits.values())
  
if "orange" in fruits:
    print("Key exists")
else:
    print("NO such key exists")

# changing items
names = {"Samuel": 1,"Odongo": 2,"Mark":3,"Mary":4}
names["Samuel"] = 5 
print(names)
#updating itemss
names.update({"Mark" :8}) 
print(names)
# adding items
phones ={"iphone":1 , "Samsung":2 ,"Techno":3}
phones["Infinix"] = 4
print(phones)
# removing items from above
phones.pop("Techno")
print(phones)
#looping through the dictionary
for x in phones:
   print(x)
   # nesting dictionaries
   cars1 = {"BMW":1,"Rover":2,"Toyota":3 }
   cars2 = {"Volvo":3, "Hammer":4}
   total ={
    "cars1" :cars1,
    "cars2" :cars2
   }
   print(total)
   # condition to show how to use boolean
a = 5
b = 7
    
if a > b:
   print(True)
else:
    print(False)
    # Exercise 1, how to use the len() fucntion
    str1 = "I love programming"
    print(len(str1))
    # Exercise 2, using for loop in string
#for x in "Akoldou":
   # print(x)
    # Exercise on slicing a string
    string = "food"
    s1 = slice(3)
    s2 = slice(1, 2)
    print(string[s1])
    #print(string[s2])



    # MORNING EXERCISE

    # Exception handling

Emotions = {
 1: "you are angry.",
 2:  "you are unhappy.",
 3: "you are sad.",
 4: "you are fair.",
 5: "you are doing well.",
 6: "you are good.",
 7: "you are great.",
 8:"you are are fine.",
 9: "you are very fine.",
 10: "you are excellent." ,
}
 
User_Emotion = (input("please rate your current Emotions in a scale of 1 - 10 ?"))
#print("User_Emotion is:" + User_Emotion)
try:
   User_Emotion = int(User_Emotion)
except ValueError as error:
      print("ivalid input ")
      print("please enter a value between 1- 10")
      exit()
if User_Emotion in Emotions:
         print(Emotions[User_Emotion])
else: 
        print("please enter a number between 1 - 10")


 