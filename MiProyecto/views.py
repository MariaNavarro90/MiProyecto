from django.http import HttpResponse
import datetime
from django.template import Template, Context

# Request: Para realizar peticiones.
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP.
"""El código proporciona algunas funciones básicas para manejar solicitudes HTTP en Django. 
Proporciona una función de bienvenida simple, una función para mostrar un mensaje de 
bienvenida con estilo en rojo, una función para determinar la categoría de edad y una 
función para mostrar la hora y fecha actuales."""

# Esto es una vista:
# Esta función devuelve una respuesta HTTP simple con el mensaje "Bienvenidos Hola Mundo."


def bienvenida(request):
    return HttpResponse("Bienvenidos Hola Mundo.")

# Esta función devuelve una respuesta HTTP con un mensaje en rojo "Bienvenidos Hola Mundo2."


def bienvenida2(request):
    return HttpResponse("<p style='color: red;'>Bienvenidos Hola Mundo2.</p>")

# Esta función determina la categoría de edad basada en el parámetro de edad recibido.
# Luego, devuelve una respuesta HTTP con la categoría de edad.


def categoriaEdad(resquest, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera Edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolecencia"
    resultado = "<h1>Categoria de la edad: %s</h1>" % categoria
    return HttpResponse(resultado)

# Esta función devuelve una respuesta HTTP con la hora y fecha actuales formateadas con .strftime("%A %d %m %Y %H:%M:%S").


def obtenerMomentoActual(request):
    respuesta = "<h1>Momento actual: {0}</h1>"
    ahora = datetime.datetime.now()
    respuestaFormateada = respuesta.format(
        ahora.strftime("%A %d %m %Y %H:%M:%S"))
    return HttpResponse(respuestaFormateada)


def contenidoHTML(request, nombre, edad):
    contenido = """ 
    <html>
    <body>
    <p>Nombre: %s / edad: %s</p> 
    </body>
    </html>
    """ % (nombre, edad)
    return HttpResponse(contenido)

from django.http import HttpResponse
from django.template import Template, Context

def miPrimerPlantilla(request):
    # Abres el archivo "miPrimerPlantilla.html" ubicado en la ruta especificada.
    plantillaExterna = open("C:/Users/Navar/OneDrive/CAPACITACIONES 2024/DJANGO_TRABAJO/MiProyecto/MiProyecto/plantillas/miPrimerPlantilla.html")
    
    # Lees el contenido del archivo y lo asignas a una variable `template`.
    template = Template(plantillaExterna.read())
    
    # Cierras el archivo después de leerlo.
    plantillaExterna.close()
    
    # Creas un contexto vacío.
    contexto = Context()
    
    # Renderizas la plantilla con el contexto creado.
    documento = template.render(contexto)
    
    # Devuelves una respuesta HTTP con el contenido renderizado de la plantilla.
    return HttpResponse(documento)
