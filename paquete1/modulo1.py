

def usuarios(nombre, contraseña):
  crear_usuario= {}
  crear_usuario["NOMBRE"] = nombre
  crear_usuario["CONTRASEÑA"] = contraseña

  return crear_usuario

def mostrarUsuarios(usuario):
  print("------------------------------------\n")
  print(f"Nombre: {usuario['NOMBRE']}")
  print(f"Contraseña: {usuario['CONTRASEÑA']}")
  print("\n------------------------------------\n")

def comprobarUsuario(nombre, contraseña, baseDeDatos):
    for usuario in baseDeDatos:
      if usuario["NOMBRE"]==nombre and usuario["CONTRASEÑA"]==contraseña:
        return True
      

def guardarDatos(baseDeDatos, nombreArchivo, ruta):

 with open(ruta + nombreArchivo, "a") as f:
 
  for usuario in baseDeDatos:
   f.write (usuario["NOMBRE"] + "," + usuario["CONTRASEÑA"]+ "\n")


baseDeDatos = []
nombre = input("Ingrese su nombre:")
contraseña = input("Ingrese su contraseña:")

nombre = input("Ingrese su nombre:")
contraseña = input("Ingrese su contraseña:")

baseDeDatos.append(usuarios(nombre, contraseña))
nombre = input("Ingrese su nombre:")
contraseña = input("Ingrese su contraseña:")

baseDeDatos.append(usuarios(nombre, contraseña))

mostrarUsuarios(baseDeDatos[0])

ruta = "C:\cursos\python\paquete1"

guardarDatos (baseDeDatos, "usuario.txt", ruta)

if comprobarUsuario("maxi", "123", baseDeDatos):
  print("Usuario correcto!")