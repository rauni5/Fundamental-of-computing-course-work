def read_inventory():
    """
    description: Function that reads the data stored in file and modifies them into useable format into a list
    parameter  : none as file name and path is fixed
    return type: list that contains the file data
    """
    result_list=[]
    try:    
        with open("Catalogue.txt","r") as file: 
            lines = file.readlines() 
        for line in lines:
            parts = line.replace("\n","").split(",")
            parts[3]=int(parts[3])
            parts[4]=float(parts[4])
            result_list.append(parts)
        return result_list
    except FileNotFoundError:
        print("FIle not found")
    except Exception as e:
        print("Failed Operation : " + str(e))
