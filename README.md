# FSI Second Practice
- **Universidad**: Universidad de Las Palmas de Gran Canaria
- **Edificio**: Escuela de Ingeniería Informática
- **Grado**: Grado en Ciencia e Ingeniería de Datos
- **Curso**: 2º año, grupo 18.43
- **Asignatura**: Fundamentos de los Sistemas Inteligentes
- **Autores**: Daniel López Correas and Nicole Ortega Ojeda

## Funcionalidad
Esta práctica implica programar en Python utilizando OpenCV, que es una librería de computación visual para el procesamiento de imágenes en Python. Esta biblioteca proporciona herramientas para realizar operaciones de procesamiento de imágenes, como el filtrado, la detección de bordes, el reconocimiento de características, el seguimiento de objetos, etc.

En este caso, se pide desarrollar un algoritmo capaz de hacer un seguimiento de personas en una calle concurrida. Para ello hemos combinado dos técnicas diferentes, haciendo primero un barrido de detección con los Clasificadores en Cascada Basados en Características Haar para buscar personas y tratar de seguirlas en el vídeo. Para comprobar que la persona ha abandonado la escena o ha sido un fallo de los clasificadores en cascada empleamos la Comparación de Plantillas o Template Matching, que es una técnica en el procesamiento de imágenes digitales para encontrar pequeñas partes de una imagen que coincidan con una imagen de plantilla.

## Recursos utilizados
- Hemos empleado el entorno de desarrollo de Visual Studio Code.
- Hemos hecho uso de una plantilla de cuerpo entero proporcionada previamente en los apuntes de OpenCV.
- Se utilizará como vídeo base el archivo “people_walking2.mp4”, pero también será probado el funcionamiento del código con el video llamado “people_walking.mp4”.

## Diseño
### Person.py
Este código define una clase Person que representa a una persona en un entorno de detección de objetos. La clase tiene métodos para la creación de personas, la identificación de personas cercanas y la actualización de sus propiedades.

### Main.py
Contiene el código principal responsable de coordinar y ejecutar las pruebas. Está diseñado para ser configurable dependiendo de las pruebas que queramos realizar. Cuenta con la carga del clasificador en cascada, el archivo que queremos probar, el contador de escenas o cuadros de dicho frame junto con un bucle para recorrerlas hasta su fin, pues se analiza cada escena individualmente a pesar de ser un video; y muestra los cuadros procesados con los rectángulos añadidos incrementando a su vez el contador del cuadro actual.
