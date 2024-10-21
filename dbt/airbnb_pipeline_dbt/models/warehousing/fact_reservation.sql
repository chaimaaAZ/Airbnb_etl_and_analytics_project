select 
dl.listing_key,
dt.date_key,
available,
TO_NUMBER(NULLIF(REPLACE(REPLACE(c.price, '$', ''), ',', ''), 'N/A')) AS price,
minimum_nights,
maximum_nights
from {{source('airbnb_pipeline','calendar')}} c 
inner join {{ ref('dim_datetime')}} dt on dt.datetime_id = c.date
inner join {{ ref('dim_listings')}} dl on dl.listing_id = c.listing_id