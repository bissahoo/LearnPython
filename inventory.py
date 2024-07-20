def displayInventory(inventory):
    totalInv=0    
    print("Inventory:")
    for k,v in inventory.items():
        print(v," ",k)
        totalInv+=v
    print("Total number of items: ",totalInv)


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)