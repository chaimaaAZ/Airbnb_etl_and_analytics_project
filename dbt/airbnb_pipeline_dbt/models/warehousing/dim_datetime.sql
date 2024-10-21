WITH temp_datetime AS (  
  SELECT DISTINCT
    c.date AS datetime_id
  FROM {{ source('airbnb_pipeline', 'calendar') }} c
  WHERE c.date IS NOT NULL
),

temp_datetime2 AS (  
  SELECT DISTINCT
    r.date AS datetime_id,
  FROM {{ source('airbnb_pipeline', 'reviews') }} r
  WHERE r.date IS NOT NULL
),

tem_date AS (
  SELECT * FROM temp_datetime
  UNION 
  SELECT * FROM temp_datetime2
)

SELECT DISTINCT 
   {{dbt_utils.generate_surrogate_key(['datetime_id'])}} as date_key,
  datetime_id,
  EXTRACT(YEAR FROM datetime_id) AS year,
  EXTRACT(MONTH FROM datetime_id) AS month,
  EXTRACT(DAY FROM datetime_id) AS day,
  EXTRACT(HOUR FROM datetime_id) AS hour,
  EXTRACT(MINUTE FROM datetime_id) AS minute,
  EXTRACT(DAYOFWEEK FROM datetime_id) AS weekday
FROM tem_date
