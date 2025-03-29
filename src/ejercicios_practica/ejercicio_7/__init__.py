import string
import random

def create_chars(total_char):
    chars = string.ascii_uppercase + string.digits
    random_str= ""
    # Itero hasta que se completen los caracteres faltantes
    for i in range(total_char):
        # Genero una posicion aleatoria de chars
        index = random.randrange(len(chars))
        random_str += chars[index]
    return random_str

def user_valid(user):
    """Verifico validez del usuario"""
    return len(user)<= 15

def generate_code(user, date):
    """ Genero el código de descuento con usuario, fecha y parte aleatoria"""
    #Elimino los guiones de la fecha
    date = date.replace("-", "")
    user_may = user.upper()

    # Calculo cuantos caracteres tengo y le sumo 2 porque sé que el codigo va a tener dos guiones
    cant_char = len(user_may) + len(date) + 2
    total_char = 30 - cant_char

    random_str = create_chars(total_char)    
    return (f'Codigo de descuento: {user_may}-{date}-{random_str}')