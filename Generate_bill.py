import datetime
def generate_bill(customer_name,boughtlist,customer=True):
    success = False
    total, bulkdiscount, domesticdiscount, discountAmount,finalPrice = bulkdiscountcheck(boughtlist)
    randomid = random_id()
    file_name = customer_name+"_"+randomid+".txt"
    try:
        with open("Bills/"+file_name,"w") as file:
            file.write("="*85+"\n")
            file.write("{:^85}\n".format("SPEEDZWEAR WHOLESALE"))
            file.write("{:^85}\n".format("KAPAN, KTM, NEPAL"))
            if customer:
                file.write("\n{:^85}\n".format("CUSTOMER INVOICE"))
            else:
                file.write("\n{:^85}\n".format("RESTOCK INVOICE"))
            file.write("-"*85+"\n")
            file.write("Bill   ID       : "+randomid+"\n")
            file.write("Transaction Date: "+ str(datetime.date.today())+"\n")
            if customer:
                file.write("Billed to       : "+customer_name+"\n")
            else:
                file.write("Supplier        : "+customer_name+"\n")
            file.write("-"*85+"\n")
            file.write("{:<5}  {:<15}  {:<15}  {:<10}  {:<15}  {:<15}\n".format("Sn", "Item", "Brand", "Qty", "Rate", "Amount"))
            file.write("-"*85+"\n")
            n=1
            for row in boughtlist:
                file.write("{:<5}  {:<15}  {:<15}  {:<10}  {:<15.2f}  {:<15.2f}\n".format(n, row[1], row[2],row[3],row[4],(row[3]*row[4])))
                n+=1
            if customer :
                file.write("{:50}{:35}\n".format(" ","-"*35))
                file.write("{:50}{:35}\n".format(" ","Discount Applied"))
                file.write("{:50}{:20}{:<15.2f}\n".format(" ","Bulk Discount     : ",bulkdiscount))
                file.write("{:50}{:20}{:<15.2f}\n".format(" ","Domestic Discount : ",domesticdiscount))
                file.write("{:50}{:35}\n".format(" ","-"*35))
                file.write("{:50}{:20}{:<15.2f}\n".format(" ","Gross amount      : ",total))
                file.write("{:50}{:20}{:<15.2f}\n".format(" ","Discount amount   : ",discountAmount))
                file.write("{:50}{:20}{:<15.2f}\n".format(" ","Net amount        : ",finalPrice))
                file.write("-"*85+"\n")
                file.write("{:^85}\n".format("EXCHANGE IN 7 DAYS WITH INVOICE BETWEEN 10-8PM"))
            else:
                file.write("{:50}{:35}\n".format(" ","-"*35))
                file.write("{:50}{:20}{:<15.2f}\n".format(" ","Net amount      : ",total))
                file.write("-"*85+"\n")
                file.write("{:^85}\n".format("Restocks are to be made by staff only"))
            file.write("{:^85}\n".format("**CONDITIONS APPLY**"))
            file.write("="*85+"\n")
        print("\nInvoice saved in Bills as {}\n".format(file_name))
        success = True
    except FileNotFoundError:
        print("Could not access Bills folder.")
    except Exception as e:
        print("Failed to generate Invoice {}".format(e))
    return success


def random_id():
    now = datetime.datetime.now()
    month = str(now.month)
    minute = str(now.minute)
    second = str(now.second)
    microsecond = str(now.microsecond)
    random = month + minute + second + microsecond
    return random

def bulkdiscountcheck(list1):
    product_total = 0
    bulk_total = 0
    domestic_product_total = 0
    for row in list1:
            amount = row[4]*row[3]
            product_total += amount
            if row[3] > 10:
                bulk_total += amount
                if row[5]=="Domestic":
                    domestic_product_total += amount
    discountbulk = bulk_total*0.05
    discountbulkdomestic = domestic_product_total*0.07
    discountAmount = discountbulk+discountbulkdomestic
    finalPrice = product_total - discountAmount
    return product_total,discountbulk,discountbulkdomestic, discountAmount,finalPrice
