n_rot = input("Geef cesearrotatie")
code_zin = input("Geef code zin")

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

try:
    n_rot  = int(n_rot)
except ValueError:
        print("Error converting ceasar rotatie")
        exit(-1)

list_word = code_zin.split()

dic = {}
for i in range (0,len(alphabet)):
    dic[alphabet[i]]=alphabet[(i-n_rot)% len(alphabet)]
for i in range (0,len(dic)):
    print ("converted alphabet is {} ". format(dic))

decodetext= ""
for x in code_zin.lower():
    if x in dic:
        x=dic[x]
    decodetext += x

print ("Decode text is {}".format(decodetext))
