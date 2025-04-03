Requisitos para el proyecto: 
 - Python 3.12.9
 - Jupyter Notebook (incluido en requirements.txt)

Para instalar las dependencias (en este caso sólo jupyter notebook) es necesario tener instalado previamente el gestor de paquetes de Python PIP. Para verificar si lo tenes instalado, ejecuta el comando: 
  - pip --version

Si no está instalado, podes hacerlo con:
  - python -m ensurepip --default-pip

Finalmente, para instalar las dependencias del proyecto desde el archivo requirements.txt, usa el comando:
  - pip install -r requirements.txt

Una vez que se instaló, acceder al directorio notebooks y abrir el archivo con extensión .ipynb. 
**Importante**: para que los notebooks puedan importar las funciones definidas en archivos `.py`, debes ejecutar la primera celda del notebook antes de ejecutar el resto.  
Esa celda se encarga de conectar los archivos y asegurarse de que todo funcione correctamente.

Estructura del proyecto:
    act2
    |-- notebooks   
                |-- ejercicio10.ipynb     # ejercicio entregable
                |-- ejercicios.ipynb      # ejercicios adicionales
    |-- src
            |-- ejercicio_10              # directorio con funciones para ejercicio10.ipynb
            |-- ejercicios_practica       # directorio con funciones para ejercicios.ipynb
    |-- requirements.txt                  # Dependencias
    |-- README.md