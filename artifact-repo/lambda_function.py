import json
import requests
import boto3
from datetime import datetime
from sqlalchemy import create_engine
import logging

# Initialize logger for CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Function to run SQL query
def run_sql_query():
    try:
        # Create a database connection
        engine = create_engine('postgresql://username:password@host:port/database')

        # Execute SQL query
        result = engine.execute("SELECT COUNT(*) FROM your_table WHERE some_condition")

        # Fetch result
        count = result.fetchone()[0]

        # Log result to CloudWatch
        logger.info(f"SQL query executed successfully. Count: {count}")

    except Exception as e:
        # Log the exception to CloudWatch
        logger.error(f"SQL query failed: {str(e)}")

# Lambda function handler
def lambda_handler(event, context):
    try:
        # Fetch data from NYC API
        url = "https://data.cityofnewyork.us/resource/8wbx-tsch.json"
        response = requests.get(url)
        data = response.json()

        # Initialize S3 client
        s3 = boto3.client('s3')
        bucket_name = 'your-s3-bucket-name'
        
        # Generate a timestamp for incremental data
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # Upload data to S3 with a timestamp for incremental ingestion
        s3.put_object(
            Bucket=bucket_name,
            Key=f'fhv_data_{timestamp}.json',
            Body=json.dumps(data)
        )

        # Run SQL query
        run_sql_query()

        # Log success message to CloudWatch
        logger.info(f'Data ingested successfully at {timestamp}!')

        return {
            'statusCode': 200,
            'body': json.dumps(f'Data ingested successfully at {timestamp}!')
        }

    except Exception as e:
        # Log the exception to CloudWatch
        logger.error(f"An error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('An error occurred.')
        }
