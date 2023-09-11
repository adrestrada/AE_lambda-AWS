import boto3

def lambda_handler(event, context):
    # Obtenemos el nombre del archivo que se cargó en el evento
    archivo = event['Records'][0]['s3']['object']['key']

    # Configuramos el cliente de S3
    s3_client = boto3.client('s3')

    # Definimos los nombres de los buckets
    bucket_origen = 'bucket-origen'
    bucket_destino = 'bucket-destino'

    # Copiamos el archivo del bucket de origen al bucket de destino
    s3_client.copy_object(
        CopySource={'Bucket': bucket_origen, 'Key': archivo},
        Bucket=bucket_destino,
        Key=archivo
    )

    return {
        'statusCode': 200,
        'body': 'Archivo copiado con éxito'
    }
