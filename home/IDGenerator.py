import random
number = [1,2,3,4,5,6,7,8,9,0,"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
unique_ID = ""
def generate_id():
    global unique_ID
    for i in range(15):
        choice = random.choice(number)
        unique_ID = unique_ID + str(choice)
    return unique_ID
print(generate_id())