
n = 0
srow = 2
while n == 0:
    cell_obj1a = sheet_obja.cell(row=srow, column=1)
    cell_obj2a = sheet_obja.cell(row=srow, column=2)
    if cell_obj1a.value ==None or cell_obj1a.value =="":

        break

    if cell_obj2a.value.upper().strip() == text.upper().strip() :
        text=cell_obj1a.value
        strLen = len(text)
        range_obj = range(strLen)
        character = "."
        count = 0
        count1 = ""
        for index in range_obj:
            if text[index] == character:
                count = count + 1
                count1 = count1 + "<" + str(index)
        break

    else:
      srow=srow+1
print("========================================")
print("new file")
print(text)
a1a=""
b1=""
b3=""
str1c=""
str1a=""
a1b=""
b2=""
b4=""
str1d=""
str1b=""
print(text)
pos1=count1.find("<")
pos1=count1[pos1+1:pos1+2]
pos2=count1.rfind("<")
pos2=count1[pos2+1:len(count1)]
print(pos1)
print(pos2)
str1=text[0:int(pos1)]
str2=text[int(pos1)+1:int(pos2)]
str3=text[int(pos2)+1:len(text)]
str1=str1.strip()
str2=str2.strip()
str3=str3.strip()
print(str1)
print(str2)
print(str3)

str1a=str1[0:1]
str1b=str1[1:2]
str1c=str1[2:3]
str1d=str1[3:4]
if str1c!="0" and str1c!="1" and str1c!="2" and str1c!="3" and str1c!="4" and str1c!="5" and str1c!="6" and str1c!="7" and str1c!="8" and str1c!="9":
    str1c=""
if str1d!="0" and str1d!="1" and str1d!="2" and str1d!="3" and str1d!="4" and str1d!="5" and str1d!="6" and str1d!="7" and str1d!="8" and str1d!="9":
    str1d=""
if str1a!="A" and str1a!="B" and str1a!="C" and str1a!="D" and str1a!="E" and str1a!="F" and str1a!="G" and str1a!="H" and str1a!="I" and str1a!="J":
    str1a=""
if str1b!="A" and str1b!="B" and str1b!="C" and str1b!="D" and str1b!="E" and str1b!="F" and str1b!="G" and str1b!="H" and str1b!="I" and str1b!="J":
    str1a=""
print(str1a)
print(str1b)
print(str1c)
print(str1d)

if str3[0:1]=="0" or str3[0:1]=="1" or str3[0:1]=="2" or str3[0:1]=="3" or str3[0:1]=="4" or str3[0:1]=="5" or str3[0:1]=="6" or str3[0:1]=="7" or str3[0:1]=="8" or str3[0:1]=="9" :
 str3a=str3[0:2]
 next=2
else:
 str3a=str3[0:1]
 next=1

if str3[next:next+1]=="0" or str3[next:next+1]=="1" or str3[next:next+1]=="2" or str3[next:next+1]=="3" or str3[next:next+1]=="4" or str3[next:next+1]=="5" or str3[next:next+1]=="6" or str3[next:next+1]=="7" or str3[next:next+1]=="8" or str3[next:next+1]=="9" :
 str3b=str3[next:next+2]
 next=next+2
else:
 str3b=str3[next:next+1]
 next=next+1

if str3[next:next+1]=="0" or str3[next:next+1]=="1" or str3[next:next+1]=="2" or str3[next:next+1]=="3" or str3[next:next+1]=="4" or str3[next:next+1]=="5" or str3[next:next+1]=="6" or str3[next:next+1]=="7" or str3[next:next+1]=="8" or str3[next:next+1]=="9" :
 str3c=str3[next:next+2]
 next=next+2
else:
 str3c=str3[next:next+1]
 next=next+1
if str3[next:next+1]=="0" or str3[next:next+1]=="1" or str3[next:next+1]=="2" or str3[next:next+1]=="3" or str3[next:next+1]=="4" or str3[next:next+1]=="5" or str3[next:next+1]=="6" or str3[next:next+1]=="7" or str3[next:next+1]=="8" or str3[next:next+1]=="9" :
 str3d=str3[next:next+2]
 next=next+2
else:
 str3d=str3[next:next+1]
 next=next+1


print(str3a)
print(str3b)
print(str3c)
print(str3d)

print(text)
n=0
srow=2
while n==0:

    if str1a=="A":
        str1a = "0"

    if str1a=="B":
        str1a = "1"

    if str1a=="C":
        str1a = "2"
    if str1a=="D":
        str1a = "3"
    if str1a=="E":
        str1a = "4"
    if str1a=="F":
        str1a = "5"
    if str1a=="G":
        str1a = "6"
    if str1a=="H":
        str1a = "7"
    if str1a=="I":
        str1a = "8"
    if str1a=="J":
        str1a = "9"


    if str1b=="A":
        str1b = "0"

    if str1b=="B":
        str1b = "1"

    if str1b=="C":
        str1b = "2"
    if str1b=="D":
        str1b = "3"
    if str1b=="E":
        str1b = "4"
    if str1b=="F":
        str1b = "5"
    if str1b=="G":
        str1b = "6"
    if str1b=="H":
        str1b = "7"
    if str1b=="I":
        str1b = "8"
    if str1b=="J":
        str1b = "9"
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
    if cell_obj1.value == None or cell_obj1.value == "":
       break
    print(str2)

    #print("hello :"+cell_obj2.value.upper())
    if cell_obj2.value.strip().upper()==str2.strip():
       a1= cell_obj1.value.strip()
       if len(a1)==3:
        a1a=a1[0:1]
        a1b=a1[1:3]
       else:
           a1a = a1[0:2]
           a1b = a1[2:4]

    print("a1a: "+a1a)
    if cell_obj4.value==str3a:
       b1= cell_obj3.value
    if cell_obj4.value == str3b:
        b2 = cell_obj3.value
    if cell_obj4.value == str3c:
        b3 = cell_obj3.value
    if cell_obj4.value == str3d:
        b4 = cell_obj3.value




    srow=srow+1
print("------------------------------------------")
print(a1a)
print(a1b)
print(b1)
print(b2)
print(b3)
print(b4)
print(str1a)
print(str1b)
print(str1c)
print(str1d)

#print(a)
if a1a!="" and a1b!="" and b1!="" and b2!="" and b3!="" and b4!=""  and str1a!="" and str1b!="" and str1c!="" and str1d!="":
    lat = a1a+"."+b1+b3+str1c+str1a
    long=a1b+"."+b2+b4+str1d+str1b
    message = "https://www.google.com/maps/search/?api=1&query=" + lat + "," + long
else:
  message="?"



