def write_inventory(inventory):
    """
    description: Function that writes data into the file, this data is the updated inventory data
    parameter  : list that contains the updated data for file
    return type: none, return without value to the main menu
    """
    try:
        with open("Catalogue.txt", "w") as file:
            for row in inventory:
                line = "{},{},{},{},{},{}\n".format(row[0],row[1],row[2],row[3],row[4],row[5])
                file.write(line)
    except Exception as e:
        print("Failed to update inventory" + str(e))