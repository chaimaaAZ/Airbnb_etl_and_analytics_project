import dlt 
from mongodb import mongodb
from prefect import flow, task
from prefect_dbt.cli.commands import DbtCoreOperation

@task
def mongodb_to_snowflake():
    airbnb = mongodb(
    database='Airbnb_db'
    ).with_resources(
        "neighborhood",
        "listings",
        "reviews",
        "calendar"
    )
    dlt_source=airbnb,
    dlt_pipeline=dlt.pipeline(
        pipeline_name="local_mongo_to_snowflake",
        destination='snowflake',
        dataset_name="Airbnb",
    )
    load_info= dlt_pipeline.run(dlt_source,write_disposition="merge")
    print(load_info)

@task
def transform_to_warehouse():
   result = DbtCoreOperation(
        commands=["dbt run --profiles-dir C:\\Users\\Chaimaa\\.dbt --project-dir \"C:\\Users\\Chaimaa\\Documents\\data\\Datacamp\\Snowflake\\Airbnb ETL pipeline\\dbt\\airbnb_pipeline_dbt\""],
    ).run()
   return result


@flow
def etl_pipeline():
    mongodb_to_snowflake()
    transform_to_warehouse()

if __name__ == "__main__":
    etl_pipeline.serve("etl_pipeline")