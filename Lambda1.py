import boto3
import csv
from io import StringIO

def lambda_handler(event, context):
    # Obtener el nombre del archivo que se cargó en el evento
    archivo = event['Records'][0]['s3']['object']['key']

    # Configurar el cliente de S3
    s3_client = boto3.client('s3')

    # Definir el nombre del bucket de S3 y la ruta al archivo
    bucket = 'tu-bucket-de-s3'
    ruta_archivo = f's3://{bucket}/{archivo}'

    # Descargar el archivo CSV desde S3
    response = s3_client.get_object(Bucket=bucket, Key=archivo)
    contenido_csv = response['Body'].read().decode('utf-8')

    # Realizar la transformación de datos (por ejemplo, cambiar mayúsculas a minúsculas)
    datos_transformados = []
    reader = csv.DictReader(StringIO(contenido_csv))
    for row in reader:
        row['nombre_columna'] = row['nombre_columna'].lower()
        datos_transformados.append(row)

    # Configurar el cliente de DynamoDB
    dynamodb_client = boto3.client('dynamodb')

    # Cargar los datos transformados en una tabla de DynamoDB
    for item in datos_transformados:
        dynamodb_client.put_item(
            TableName='nombre_de_la_tabla_dynamodb',
            Item=item
        )

    return {
        'statusCode': 200,
        'body': 'Datos transformados cargados en DynamoDB'
    }
