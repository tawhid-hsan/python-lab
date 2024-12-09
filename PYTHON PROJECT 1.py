print("Thanks For Choosing Our Sportswear Shop")
item_dict={}
f = open("F:/hello/data.txt","r")
while True:
    item = f.readline()
    if item =="":
        break 
    quantity = f.readline()
    price = f.readline()
    item = item[:len(item)-1]
    quantity = int(quantity[:len(quantity)-1])
    price = float(price[:len(price)-1])
    item_dict[item]= [quantity,price]
    
f.close()
ml = 40
iml = 30
def show_dict():
    print(ml*"=")
    print("Available Sports Equipments and Quantity")
    print(ml*"=")
    for x in item_dict:
        print(x,(iml-len(x))*" ",
              (6-len(str(item_dict[x][0])))*" ",
                     item_dict[x][0])
    print(ml*"-")
#show_dict()  
def dec_quant(key,val):
    item_dict[key][0]-=val
def inc_quant(key,val):
    item_dict[key][0]+=val
def process_order():
    print("Input Order Details:")
    while True:
        item = input("Items(Enter x to stop):")
        if item =="x":
            break
        value =int (input("Quantity:"))
        if item not in item_dict:
            print("New Item Found!")
            uprice = float (input("Unit Price:"))
            item_dict[item]=[value,uprice]
            continue
        inc_quant(item,value)

    #show_dict()
def sell_order():
    print("Output Sell:")
    order_list =[]

    while True:
        item = input("Items(x to stop):")
        if item =="x":
            break
        if item not in item_dict:
            print(f"the item '{item}' is not available")
            continue
        value =int (input("Quantity:"))
        if value>item_dict[item][0]:
            print(f"Total of {item_dict[item][0]} quantity are available")
            continue
        dec_quant(item,value)
        order_list+=[item,value,
                      item_dict[item][1],
                      value*item_dict[item][1]],
#printing the payment receipt

    print(40*"=")
    
    print ("**Payment Receipt**".center(40))
    print (40*"=")
    print ("item",7*" ","quant."," ","u.price",2*" ","s.total")
    tprice=0
    for x in demand_list:
          tprice+=x[3]
          print (x[0].title(),(11-len(x[0]))*" ",
                 (5-len(str(x[1])))*" ",x[1],
                 (8-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
                 (9-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print (40*"-")
    print ("Total Price:"," ",tprice)
    print (order_list)
    #show_dict()
    
#show_dict()
while True:
    show_dict()
    print ("Choose An Option:")
    print ("Type '1':To Process Order")
    print ("type '2':To Sell Order")
    print ("Type '3':To Exit The Program")
    choice = input ("Choice:")
    if choice =='1':
        process_order()
    elif choice=='2':
        sell_order()
    elif choice=='3':
        break
    else:
        continue
