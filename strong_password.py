import random as ran


while True:
    ask = input("Do you want password ? (y/n)")
    if ask.lower() == "y":
        alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",
                    "W","X","Y","Z"]

        password = ["~","!","{}","#","$","%","^","&","*","(",")","_","+","=","-","?","/",">","<","{",",","|",";"]


        empty_list = []

        for alp in range(7):
            empty_list.insert(0,ran.choice(alphabet))
        for x in  range(25):
            empty_list.insert(0,ran.choice(password))

        print("".join(empty_list))
    else:
        break
