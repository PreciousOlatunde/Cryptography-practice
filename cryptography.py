#cryptography.py

#substitution cypher and preset key
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
key =   "XPMGTDHLYONZBWEARKJUFSCIQV "

#user menu
def menu():
    print("""
    SECRET DECODER MENU

    0) Quit
    1) Encode
    2) Decode

    """)
    output = input("What is your choice: ")
    return output


#message to encrypted code funtion
def encode(plain):
    coded = ""
    plain = plain.upper()
    for i in range(0, len(plain)):
        ind = alpha.find(plain[i])
        if ind == -1:
            coded = coded
        else:
            letter = key[ind]
            coded = coded + letter
    return coded

#encrypted code to original message function
def decode(coded):
    plain = ""
    coded = coded.upper()
    for i in range(0, len(coded)):
        ind = key.find(coded[i])
        if ind == -1:
            plain = plain
        else:
            letter = alpha[ind]
            plain = plain + letter
    return plain

#main function
def main():
    keepGoing = True
    while keepGoing:
        response = menu()
        if response == "1":
            plain = input("Text to be encoded: ")
            print("CODE: " + encode(plain))
        elif response == "2":
            coded = input("Code to be decyphered: ")
            print ("MESSAGE: " + decode(coded))
        elif response == "0":
            print ("Thanks for doing secret spy stuff with me.")
            keepGoing = False
        else:
            print ("I don't know what you want to do...")

main()