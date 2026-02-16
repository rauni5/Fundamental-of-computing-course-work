def display_inventory(inventory):
    try: 
        print("{:^85}".format("Inventory"))
        print("="*85)
        print("{:<5} | {:<15} | {:<12} | {:<10} | {:<14} | {:<14}".format("ID", "Shoe", "Brand", "Available", "Price", "Source"))#string format forrow of column titles
        print("-"*85)
        for row in inventory:
            print("{:<5} | {:<15} | {:<12} | {:<10} | Rs. {:<10} | {:<14}".format(row[0], row[1], row[2], row[3], row[4], row[5]))#string format to add row, taking data from single list using index
        print("="*85)
    except Exception as e:
        print("Failed to display Data:", e)

def display_available(inventory):
    try: 
        print("{:^85}".format("Inventory"))
        print("="*85)
        print("{:<5} | {:<15} | {:<12} | {:<10} | {:<14} | {:<14}".format("ID", "Shoe", "Brand", "Available", "Price", "Source"))#string format forrow of column titles
        print("-"*85)
        for row in inventory:
            if(row[3]>0):
                print("{:<5} | {:<15} | {:<12} | {:<10} | Rs. {:<10} | {:<14}".format(row[0], row[1], row[2], row[3], row[4], row[5]))#string format to add row, taking data from single list using index
        print("="*85)
    except Exception as e:
        print("Failed to display Data:", e)

def display_buylist(boughtlist,customername):
    try: 
        print("{:^85}".format("CART FOR "+customername))
        print("="*85)
        print("{:<5} | {:<15} | {:<12} | {:<10} | {:<14} | {:<14}".format("ID", "Shoe", "Brand", "  QTY", "Price", "Source"))#string format forrow of column titles
        print("-"*85)
        for row in boughtlist:
                print("{:<5} | {:<15} | {:<12} | {:<10} | Rs. {:<10} | {:<14}".format(row[0], row[1], row[2], row[3], row[4], row[5]))#string format to add row, taking data from single list using index
        print("="*85)
    except Exception as e:
        print("Failed to display Data:", e)