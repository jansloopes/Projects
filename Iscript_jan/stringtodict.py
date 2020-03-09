persoon = "geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True"
print (type(persoon))
persoon.replace("man", "vrouw")
print (persoon)
type(persoon)
#Splitting the string based on , we get key value pairs
list = persoon.split(",")

persoon_dict={}
for i in list:
    #Get Key Value pairs separately to store in dictionary
    keyvalue = i.split('=')

    #Replacing the single quotes in the leading.
    m= keyvalue[0].strip('\'')
  #  m = m.replace("\"", "")
    persoon_dict[m] = keyvalue[1].strip('"\'')

print ("persoon in functie is {} ".format (persoon_dict ['geslacht'] ))

str ="aap noot"
print (str)
str2 = str.replace("noot", "mies")
print (str2)
