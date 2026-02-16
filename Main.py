import Read
import Display
import Operations
import Write
from Generate_bill import generate_bill

def customer_operation(inventory):
    """
    description: Function thst displays options for customer operations to add product to cart, show cart and generate bill
                 each options calls for specific function related to its operation
    parameter  : list that holds the inventory data
    return type: none, return without value to the main menu
    """
    try:
        boughtlist=[]
        customername = input("Enter Customer Name : ")
        while True:
            print("\n"+"**"*25)
            print("*{:^48}*".format("Customer OPERATIONS"))
            print("*"+" "*48+"*")
            print("*  {:<44}  *".format("Customer Name : "+customername))
            print("*"+" "*48+"*")
            print("*  {:<25} {:<20}*".format("1.Show Cart ","2.Add product"))
            print("*"+" "*48+"*")
            print("*  {:<25} {:<20}*".format("3.Buy and Generate Bill","4.Cancel purchase"))
            print("*"+" "*48+"*")
            print("**"*25+"\n")
            selected = input("\nSelect Operation : ")
            if(selected == "1" ):
                if boughtlist:                  
                    Display.display_buylist(boughtlist,customername)
                else:
                    print("\n**Empty Cart**\n")
            elif (selected == "2"):
                Display.display_available(inventory)
                purchased_item = Operations.customer_sell(inventory)
                if purchased_item:  
                    boughtlist.append(purchased_item)
            elif (selected == "3"):
                if boughtlist:
                    success = generate_bill(customername,boughtlist)
                    if success:
                        Write.write_inventory(inventory)
                    else:
                        print("Purchase Cancelled")
                    break
                else:
                    print("\nEmpty Cart\n")
            elif(selected == "4"):
                if boughtlist:
                    Operations.canceled_restock(inventory,boughtlist)
                print("\n**Purchase Cancelled**\n")
                break
            else:
                print("\nInvalid Entry\n")
    except Exception as e:
        print("Failed Operation {}".format(e))

def stock_operation(inventory):
    """
    description: Function thst displays options for inevntory stock operations to add product to inventory, restock product
                 each options calls for specific function related to its operation
    parameter  : list that holds the inventory data
    return type: none, return without value to the main menu
    """
    try:
        while True:
            print("\n"+"**"*23)
            print("*{:^44}*".format("STOCK OPERATIONS"))
            print("*"+" "*44+"*")
            print("*  {:<21} {:<20}*".format("1. ADD new Product","2. Restock product"))
            print("*"+" "*44+"*")
            print("*  {:<21} {:<20}*".format("3. BACK",""))
            print("*"+" "*44+"*")
            print("**"*23+"\n")
            selected = input("\nSelect Operation : ")
            if(selected == "1" ):                  
                suppliername,boughtlist = Operations.add_product(inventory)
                if boughtlist:
                    success = generate_bill(suppliername,boughtlist,False)
                    if success:
                        Write.write_inventory(inventory)
            elif (selected == "2"):
                Display.display_inventory(inventory)
                suppliername,boughtlist = Operations.restock_product(inventory)
                if boughtlist:
                    success = generate_bill(suppliername,boughtlist,False)
                    if success:
                        Write.write_inventory(inventory)
            elif (selected == "3"):
                print("\n**Back to main menu**\n")
                break
            else:
                print("\nInvalid Entry\n")
    except Exception as e:
        print("Failed Operation {}".format(e))



"""
    description: main code that runs right after program execution and keeps looping until the program ends
                 is the main menu of the program
"""
inventory_data = Read.read_inventory()

while True:
    try:
        print("\n"+"**"*23)
        print("*{:^44}*".format("OPERATIONS"))
        print("*"+" "*44+"*")
        print("*  {:<21} {:<20}*".format("1. Display Inventory","2. Stock product"))
        print("*"+" "*44+"*")
        print("*  {:<21} {:<20}*".format("3. Sell Product","4. EXIT"))
        print("*"+" "*44+"*")
        print("**"*23+"\n")
        selected = input("\nSelect Operation : ")
        if(selected == "1"):                      
            Display.display_inventory(inventory_data)
        elif (selected == "3"):
            customer_operation(inventory_data)
        elif (selected == "2"):
            stock_operation(inventory_data)
        elif (selected == "4"):
            print("\n**EXIT PROGRAM**\n")
            break
        else:
            print("\nInvalid Entry\n")
    except Exception as e:
        print("Failed Operation {}".format(e))


