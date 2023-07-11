srow=2
n=0
a=""
b=""
c=""
d=""
e=""
lat=latid
long=longid
while n==0:

    finddotlat=lat.find(".")
    beforedotlat=lat[0:finddotlat]
    afterdotlat=lat[finddotlat+1:len(lat)]

    if len(afterdotlat)<2:
        afterdotlat=afterdotlat+"00000"
    if len(afterdotlat) < 3:
        afterdotlat = afterdotlat + "0000"
    if len(afterdotlat) < 4:
        afterdotlat = afterdotlat + "000"
    if len(afterdotlat) < 5:
        afterdotlat = afterdotlat + "00"
    if len(afterdotlat) < 6:
        afterdotlat = afterdotlat + "0"

    #print(beforedotlat)
    #print(afterdotlat)
    finddotlong = long.find(".")
    beforedotlong = long[0:finddotlong]
    afterdotlong= long[finddotlong + 1:len(long)]

    if len(afterdotlong) < 2:
        afterdotlong = afterdotlong + "00000"
    if len(afterdotlong) < 3:
        afterdotllong = afterdotlong + "0000"
    if len(afterdotlong) < 4:
        afterdotlong = afterdotlong + "000"
    if len(afterdotlong) < 5:
        afterdotlong = afterdotlong + "00"
    if len(afterdotlong) < 6:
        afterdotlong = afterdotlong + "0"

    #print(beforedotlong)
    #print(afterdotlong)

    str1=beforedotlat+beforedotlong
    print(str1)
    str2=afterdotlat[0:2]
    str3=afterdotlat[2:4]
    str4a=afterdotlat[4:5]
    str4b = afterdotlat[5:6]
    if str4b=="0":
        str4b = "A"

    if str4b=="1":
        str4b = "B"

    if str4b=="2":
        str4b = "C"
    if str4b=="3":
        str4b = "D"
    if str4b=="4":
        str4b = "E"
    if str4b=="5":
        str4b = "F"
    if str4b=="6":
        str4b = "G"
    if str4b=="7":
        str4b = "H"
    if str4b=="8":
        str4b = "I"
    if str4b=="9":
        str4b = "J"



    str5 = afterdotlong[0:2]
    str6 = afterdotlong[2:4]
    str7a = afterdotlong[4:5]
    str7b = afterdotlong[5:6]
    if str7b == "0":
        str7b = "A"

    if str7b == "1":
        str7b = "B"

    if str7b == "2":
        str7b = "C"
    if str7b == "3":
        str7b = "D"
    if str7b == "4":
        str7b = "E"
    if str7b == "5":
        str7b = "F"
    if str7b == "6":
        str7b = "G"
    if str7b == "7":
        str7b = "H"
    if str7b == "8":
        str7b = "I"
    if str7b == "9":
        str7b = "J"
    lat=beforedotlat+"."+afterdotlat
    long = beforedotlong + "." + afterdotlong
    latn = float(lat)
    longn = float(long)
    if (int(latn)<8 and int(latn)>38)  or (int(longn)<68 and int(longn)>98):
        print("You are not Inside Bounadaries of India")
        continue
    cell_obj1 = sheet_obj.cell(row=srow, column=1)
    cell_obj2 = sheet_obj.cell(row=srow, column=2)
    cell_obj3 = sheet_obj.cell(row=srow, column=3)
    cell_obj4 = sheet_obj.cell(row=srow, column=4)
    cell_obj5 = sheet_obj.cell(row=srow, column=5)
    cell_obj6 = sheet_obj.cell(row=srow, column=6)
    cell_obj7 = sheet_obj.cell(row=srow, column=7)
    cell_obj8 = sheet_obj.cell(row=srow, column=8)
    cell_obj9 = sheet_obj.cell(row=srow, column=9)
    cell_obj10 = sheet_obj.cell(row=srow, column=10)
    #print(str1)
    #print(str2)
    #print(str3)
    #print(str4a)
    #print(str4b)
    #print(str5)
    #print(str6)
    #print(str7a)
    #print(str7b)
    if cell_obj1.value==str1:
       a= cell_obj2.value

    if cell_obj3.value==str2:
       b= cell_obj4.value
    if cell_obj3.value==str5:
       c= cell_obj4.value
    if cell_obj3.value==str3:
       d= cell_obj4.value
    if cell_obj3.value==str6:
       e= cell_obj4.value


    if cell_obj1.value == None or cell_obj1.value == "":
       break

    srow=srow+1

#print(a)
if a!="":
    address = str4b+str7b+str4a+str7a + "." +"<b>"+(a.strip().upper()+"</b>"+ "." + b.strip() +  c.strip() + d.strip() + e.strip())
else:
 address=""

print(address)



