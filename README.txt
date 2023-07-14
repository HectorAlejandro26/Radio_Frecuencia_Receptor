Guardado:
    Se recomienda no cambiar el nombre de los archivos creados

    Los archivos originalmente se guardan en un directorio llamado ".temp", durante la
    ejecucion del programa se copiaran a la carpeta "Registro" donde el usuario ya 
    puede manipularlos.

    Los archivos creados por el programa que esten en la carpeta ".temp" se eliminaran
    cuando tengan mas de 2 dias de diferencia.

Cambiar microcontrolador:
    La configuracion actual esta hecha para que trabaje con Arduino.
    Si se desea usar otro se debera agregar el nombre del fabricante del controlado,
    La manera recomendada para encontrar este nombre, es ejecutar "scan_ports.py" en
    una sistema con python 3.9.5 instalado, y de esta manera ejecutar el programa con 
    el comando "py -u scan_ports.py" en una terminal con la ruta de este directorio.

    Finalmente el nombre del desarrollador se debera agregrar a la tupla "desarrolladores"
    en "constantes.py".

    Lea la seccion "Compilacion" para la continuacion de esta seccion.

Compilacion:
    Si se realizo algun cambio en la programacion y se desea obtener el executable.
    En una terminal ubicada en este directiorio, se ejecutaran los siguientes comandos:
    
    ".\.venv\Scripts\activate.ps1" -> Para entrar el entorno virtual del proyecto.
    "auto-py-to-exe" -> Para abrir la interfaz grafica del compilador.

    En la interfaz del compilador, en el apartado "Settings", seleccionar la opcion
    "import config from JSON file" y proporcionar el archivo json de este directorio,
    despues seleccionar "Convert .py to .exe" y esperar a que termine de compilar.

    Finalmente el archivo "main.exe" que estara dentro de la carpeta "output",
    moverlo a la carpeta principal del programa "Radio_Frecuencia_Receptor", despues puede
    eleminar la carpeta "output" ya que no es necesaria.