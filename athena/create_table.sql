CREATE EXTERNAL TABLE IF NOT EXISTS fhv_data (
    field1 STRING,
    field2 STRING,
    ...
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
) LOCATION 's3://your-s3-bucket-name/';
