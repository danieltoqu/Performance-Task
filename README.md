# my_data_pipeline/

|-- lambda_function/
|   |-- Dockerfile
|   |-- lambda_function.py
|   |-- requirements.txt
|-- athena/
|   |-- create_table.sql
|-- eventbridge/
|   |-- eventbridge_rule.json
|-- serverless.yml
|-- README.md


# My Data Pipeline

## Overview
This project is a simple data pipeline that ingests data incrementally from the NYC "For Hire Vehicles (FHV) – Active" dataset and stores it in an S3 bucket. The data can then be queried using AWS Athena.

## Deployment Steps
1. Build the Docker image for the Lambda function.
2. Deploy using the Serverless Framework.

## AWS Services Used
- AWS Lambda
- Amazon S3
- AWS Athena
- AWS EventBridge
- AWS CloudWatch
