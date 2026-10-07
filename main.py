print("grocery checkout line")
totalrice=totalmilk=totalbread=totaleggs=totalsugar=totaltea=totaloil=totalsoap=0
customerserved=0
totalbilled=0
customers=int(input("how many customers are waiting in line: "))
c=1
while c<=customers:
    name=input("enter customer name: ")
    print(f"hello {name} enter quantity of each item in your cart (0 if none)")
    bill=0
    i=1
    while i<=8:
        if i==1:
            item,price="rice",200
        elif i==2:
            item,price="milk",150
        elif i==3:
            item,price="bread",100
        elif i==4:
            item,price="eggs",50
        elif i==5:
            item,price="sugar",120
        elif i==6:
            item,price="tea",300
        elif i==7:
            item,price="oil",500
        elif i==8:
            item,price="soap",80
        count=int(input(f"{item} ({price} each): "))
        if count<0:
            print("invalid quantity, please enter again")
            continue
        if count>0:
            print(f"{count}x{item} unit price {price}={count*price}")
            bill+=count*price
            if price==200:
                totalrice+=count
            elif price==150:
                totalmilk+=count
            elif price==100:
                totalbread+=count
            elif price==50:
                totaleggs+=count
            elif price==120:
                totalsugar+=count
            elif price==300:
                totaltea+=count
            elif price==500:
                totaloil+=count
            elif price==80:
                totalsoap+=count
        i+=1
    if bill==0:
        print(f"empty cart {name}, next customer")
        c+=1
        continue
    customerserved+=1
    totalbilled+=bill
    print(f"total bill for {name}: {bill}")
    print(f"transaction complete {name}")
    c+=1
print("daily item report")
for i in range(1,9):
    if i==1:
        item,total="rice",totalrice
    elif i==2:
        item,total="milk",totalmilk
    elif i==3:
        item,total="bread",totalbread
    elif i==4:
        item,total="eggs",totaleggs
    elif i==5:
        item,total="sugar",totalsugar
    elif i==6:
        item,total="tea",totaltea
    elif i==7:
        item,total="oil",totaloil
    elif i==8:
        item,total="soap",totalsoap
    if total>0:
        print(f"{item} sold:{total}", end="")
        for note in range(total):
            print("=", end="")
        print()
print(f"customer served{customerserved} ")
print(f"total billed{totalbilled}")
print("store session closed")