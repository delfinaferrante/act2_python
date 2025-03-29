def numbers(name):
    """Verifica que el nombre tenga al menos un numero"""
    for char in name:
        if char.isdigit():
            return True
    return False

def caract(name):
    """Verifica que el nombre tenga al menos 5 caracteres"""
    return len(name) >= 5 

def validation(name):
    """ Verifica que todos los requisitos se cumplan """
    return caract(name) and numbers(name) 

def check_name(name):
    """Devuelve un mensaje según si el nombre de usuario es válido o no"""
    valid = validation(name)
    return "El nombre de usuario es válido" if valid else "El nombre de usuario no cumple con los requisitos"