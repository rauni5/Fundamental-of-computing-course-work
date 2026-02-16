
def customer_sell(inventory):
    """
    description: Function that searches for product that the customer wants and updates inventory table stock if that item is added to the cart
                 also check for invalid input and stock available
    parameter  : list that has inventory data
    return type: list that contains product the the customer added to cart,
    """
    try:
        print("=="*24)
        while True:
            nameid = input("Enter Product name or id (or type EXIT to cancel): ")
            if nameid.upper() == "EXIT":
                return None
            row = find_product(inventory,nameid)
            if not row:
                print("Product not found")
                continue
            break
        print("Product found")
        print_row(row)
        
        while True:
            units_purchased = int_input("\nUnits purchased (or type EXIT to cancel): ")
            if units_purchased == "EXIT":
                return None
            if(units_purchased > row[3]):
                print("Not enough stock")
            else:
                break
        row[3] -= units_purchased
        purchased_item = row.copy()
        purchased_item[3] = units_purchased
        print("\n**Added prodcut to cart**\n")
        return purchased_item
    except Exception as e:
        print("Failed Operation {}".format(e))


def restock_product(inventory):
    """
    description: Function that searches for product that the shop wants to restock and updates inventory table stock if that item is restocked
                 also check for invalid input and can change selling price of already available product
    parameter  : list that has inventory data
    return type: list that contains details of restock
    """
    try:
        boughtlist = []
        print("=="*24)
        supplier_name = input("Enter Supplier name:")
        while True:
            nameid = input("Enter Product name or id  (or type EXIT to cancel): ")
            if nameid.upper() == "EXIT":
                return None,None
            row = find_product(inventory,nameid)
            if not row:
                    print("Product not found")
                    continue
            print("Product found")
            print_row(row)
            units_purchased = int_input("\nUnits purchased  (or type EXIT to cancel): ")
            if units_purchased == "EXIT":
                return None,None
            purchased_price = float_input("\nPurchase Price  :")
            while True:
                x = input("Update Selling price? (y / n)")
                x = x.lower()
                if(x == "n"):
                    break
                elif(x == "y"):
                    print("Old Price per-Unit   :",row[4])
                    new_price = int_input("ENter New selling price :")
                    row[4] = new_price
                    break
                else:
                    print("\nInvalid Entry\n")
            row[3] += units_purchased
            purchased_item = row.copy()
            purchased_item[3] = units_purchased
            purchased_item[4] = purchased_price
            boughtlist.append(purchased_item)
            x = input("Add another product? (y / n)")
            x = x.lower()
            if(x == "n"):
                break
            elif(x == "y"):
                continue
            else:
                print("\nInvalid Entry\n")
        return supplier_name,boughtlist
    except Exception as e:
        print("Failed Operation {}".format(e))

def add_product(inventory):
    """
    description: Function that adds product to the inventory and checks if the product already exists
                 also check for invalid input and has different inputs for purchase price and selling price
    parameter  : list that has inventory data
    return type: list that contains details of new product
    """
    try:
        boughtlist = []
        print("=="*24)
        supplier_name = input("Enter Supplier name :")
        while True:
            id = input("Enter product ID  (or type EXIT to cancel): ")
            if id.upper() == "EXIT":
                return None,None
            if find_product(inventory,id):
                print("Product ID already exists")
                continue
            name = input("Enter product name:")
            brand = input("Enter brand name:")
            stock = int_input("Enter Bought stock (or type EXIT to cancel):")
            if stock =="EXIT":
                return None,None
            boughtprice = float_input("Enter unit buying price  :")
            sellprice = float_input("Enter unit Selling price :")
            while True:
                source = input("Enter Source of manufacture (Domestic/International) :")
                source = source.title()
                if(source != "Domestic" and source != "International"):
                    print("Wrong source")
                    continue
                break
            boughtlist.append([id,name.title(),brand,stock,boughtprice,source])
            inventory.append([id,name.title(),brand,stock,sellprice,source])
            x = input("Add another product? (y / n)")
            x = x.lower()
            if(x == "n"):
                break
            elif(x == "y"):
                continue
            else:
                print("\nInvalid Entry\n")
        return supplier_name,boughtlist
    except Exception as e:
        print("Failed Operation {}".format(e))

def canceled_restock(inventory,boughtlist):
    try:
        for item in boughtlist:
            product = find_product(inventory, item[0])
            if product:
                product[3] += item[3] 
    except Exception as e:
        print("Failed to restock canceled product {}".format(e))

def find_product(inventory, nameid):
    """
    description: Helper function for product check
    parameter  : list that has inventory data, product id
    return type: list of required product
    """
    try:
        for row in inventory:
            if row[0].lower() == nameid.lower() or row[1].lower() == nameid.lower():
                return row
        return None
    except Exception as e:
        print("Failed Operation {}".format(e))

def int_input(string):
    """
    description: Helper function for invalid and exception check
    parameter  : String prompt for input
    return type: int for valid input
    """
    while True:
        value = input(string)
        if(value.upper()=="EXIT"):
            return "EXIT"
        try:
            value = int(value)
            if(value<=0):
                print("Enter valid value")
            else:
                return value
        except ValueError:
            print("Please enter an valid value.")
        except Exception as e:
            print("Failed Operation {}".format(e))

def float_input(string):
    """
    description: Helper function for invalid and exception check
    parameter  : String prompt for input
    return type: float for valid input
    """
    while True:
        value = input(string)
        try:
            value = float(value)
            if(value<=0):
                print("Enter valid value")
            else:
                return value
        except ValueError:
            print("Please enter an valid value")
        except Exception as e:
            print("Failed Operation {}".format(e))
def print_row(row):
    print("="*85)
    print("{:<5} | {:<15} | {:<12} | {:<10} | {:<14} | {:<14}".format("ID", "Shoe", "Brand", "Available", "Price", "Source"))
    print("-"*85)
    print("{:<5} | {:<15} | {:<12} | {:<10} | {:<14} | {:<14}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
