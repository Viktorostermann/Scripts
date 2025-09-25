# --- Pedir contraseña al usuario
password = input("Introduce su copntraseña : ")
print("")

# --- Comprobar si contraseña del usuario es segura

# Si cumple los requisitos seguros (Cumple requisitos seguros)
# Si no cumple los requisitos (No cumple requisitos seguros)
# Debe tener una vocal (a,e,o)
# Debe tener simbolo especail (& , *, #, _ )
print("\n")
if ("a" in password or "e" in password or "o" in password) and ( "*") or ("&") or ("#") or ("_"):
    print(" La contraseña es segura! ")
    print("\n")
else:
    print("La contraseña no es segura! ")
    print("\n")