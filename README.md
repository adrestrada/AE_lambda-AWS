# Lambda-AWS

Automatizar tareas utilizando AWS Lambda junto con otros servicios de AWS. 
Automatizaremos la copia de archivos desde un bucket de Amazon S3 a otro bucket.
la función Lambda se ejecutará automáticamente y copiará ese archivo al bucket-destino. Esto automatiza la tarea de copiar archivos entre buckets de S3 cuando se producen cambios en el bucket-origen.

Arquitectura:
1) Amazon S3 Buckets: Tendremos dos buckets de S3, uno llamado bucket-origen desde donde copiaremos archivos y otro llamado bucket-destino donde copiaremos los archivos.
2) AWS Lambda: Crearemos una función Lambda que se ejecutará cada vez que se cargue un archivo en el bucket-origen. Esta función copiará automáticamente el archivo al bucket-destino.

Pasos para configurar la automatización:
1) Crea dos buckets de S3: bucket-origen y bucket-destino.
2) Crea una función Lambda en la consola de AWS Lambda.
3) Configura el disparador de la función Lambda para que esté vinculado al bucket-origen y se ejecute cuando se cargue un archivo en ese bucket.
4) Copia y pega el código Python de la función Lambda en el editor de código de la consola de Lambda.
5) Asegúrate de que la función Lambda tenga permisos para acceder a los buckets de S3. Puedes configurar los permisos en la pestaña "Permissions" (Permisos) de la consola de Lambda.
6) Guarda y despliega la función Lambda.


Pasos para configurar la automatización:
1) Crea un bucket de Amazon S3 que contenga el archivo CSV que deseas procesar.
2) Crea una tabla en Amazon DynamoDB donde deseas cargar los datos transformados.
3) Crea una función Lambda en la consola de AWS Lambda.
4) Configura el disparador de la función Lambda para que esté vinculado al bucket de S3 y se ejecute cuando se cargue un archivo CSV en ese bucket.
5) Copia y pega el código Python de la función Lambda en el editor de código de la consola de Lambda.
6) Asegúrate de que la función Lambda tenga permisos para acceder a los buckets de S3 y a la tabla de DynamoDB. Puedes configurar los permisos en la pestaña "Permissions" (Permisos) de la consola de Lambda.
7) Guarda y despliega la función Lambda.

Ahora, cada vez que se cargue un archivo CSV en el bucket de S3, la función Lambda se ejecutará automáticamente, realizará la transformación de datos y cargará los datos transformados en la tabla de DynamoDB. 
Esto automatiza parte del proceso ETL en AWS. 
Asegúrate de ajustar los nombres de los buckets y la tabla, así como de definir la transformación de datos adecuada para tu caso específico
