import pickle



lista_vacia = []
pckl_file = open("personajes.pckl","wb")
pickle.dump(lista_vacia,pckl_file)
pckl_file.flush()
print("Archivo creado")

pckl_file.close()



with open("personajes.pckl","rb") as pckl_file: 

    lista_pj_dict = pickle.load(pckl_file)

    print(type(lista_pj_dict))
    print ("mostrando lista_pj dict: ",lista_pj_dict)