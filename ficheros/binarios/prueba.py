with open("personajes.pckl", "wb") as pckl_file:
    
    completo = pckl_file.readlines()
    print(type(completo))