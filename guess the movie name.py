db = firestore.client()

docs = db.collection("movies").stream()
for d in docs:
#print(d.to_dict())
database = d.to_dict()
d=database["Name"]
import random
movie = database["Name"]
player = input("Write your Name: ")
print("Guess the character: ")
print("You have 10 chance to get the movie name: ")
print("Best of luck!",player)


count = 10

geuss= ""

word = random.choice(movie) #war

while count>0:
    fail = 0
    for char in word:
        if char in geuss:
            print(char)
        else:
            print("_")
            fail+=1
            
            
    if fail==0:
        print("Congratulation you won!!!")
        print("Movie Name was:",word)
        break
        
    g = input("Enter your character: ")
    geuss = geuss+g
    
    if g not in word:
        count = count-1
        print("Wrong Answer:(")

        print("You have ",count,"more geusses")








