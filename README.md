El Proyecto es una aplicación para Registro de materiales.

En la página principal se pueden ver los materiales registrados si existieran.

Cuenta con 3 formularios de ingreso:

- Formulario de ingreso de materiales
- Formulario de ingreso de dimensiones
- Formulario de ingreso de proveedores

Es necesario ejecutar los siguientes pasos una vez hecho el clone de GitHub:

Si no tienes el entorno virtual creado, puedes abrir el archivo `requirements.txt` con Visual Studio Code y hacer clic en **Crear ambiente**, luego elegir `Venv`, luego el intérprete Python (última versión), y finalmente pregunta por las dependencias: elegimos requirements.txt.

## Migraciones

`python manage.py makemigrations`
> Crea las migraciones, que son archivos Python encargados de la base de datos

`python manage.py migrate`
> Ejecuta las migraciones, para que se realicen los cambios en la base de datos

`python manage.py createsuperuser`
> Crea un usuario administrador para acceder a 127.0.0.1:8000/admin



