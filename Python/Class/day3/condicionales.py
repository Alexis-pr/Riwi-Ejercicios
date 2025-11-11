#pagina se llama  --- Contraseña
contraseñaUsuario = "123."

#python tutory

for i in range(3):
       
    contra  = ""
    contra  = input(" ingrese contraseña: ")
    
    if contraseñaUsuario != contra:
        print("contraseña incorrecta ingresela nuevamente")     
    else:
        print("contraseña correcta")
        break


