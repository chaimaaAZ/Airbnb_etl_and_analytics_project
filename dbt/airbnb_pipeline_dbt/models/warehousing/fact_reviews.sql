
select 
  dl.listing_key,
  dt.date_key,
  reviewer_id,
  reviewer_name,
  comments
from {{source('airbnb_pipeline','reviews')}} r
inner join {{ ref('dim_listings')}} dl on dl.listing_id = r.listing_id
inner join {{ ref ('dim_datetime')}} dt on dt.datetime_id = r.date