#Comandos Basicos
========================

###direccion de mi python 3.5.2
´
C:\Users\Malu\AppData\Local\Programs\Python\Python35-32\python.exe
´

###crear entorno virtual 
´
python -m virtualenv nombre
´

###activar entorno virtual
´
C:\env\proyecto\Scripts\activate.bat
´
###instalar virtual env

C:\env>C:\Users\Malu\AppData\Local\Programs\Python\Python35-32\python.exe -m pip install virtualenv


En el entorno virtual tendremos nuestro proyecto hay que activarlo cada vez que lo vayamos usar.

### para crear priveligios para mi usuario malu entramos a la consola de postgress

grant all privileges on database ganttbd to malu;

### con pip install instalamos django y psycopg2
esto ya es dentro del entorno virtual encendido.

pip install django
pip install psycopg2

### crear proyecto de django, una vez que ya esta instalado ponemos


###para levantar un servidor muy basico de django usamos, es como una libreria que tiene funciones utiles de django, levanta server, recolecta estaticos, entras al shell de django etc.

python manage.py 

