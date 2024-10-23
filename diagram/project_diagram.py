from diagrams import Diagram, Cluster
from diagrams.onprem.analytics import Dbt
from diagrams.onprem.database import MongoDB,Mongodb
from diagrams.saas.analytics import Snowflake
from diagrams.programming.language import Python
from diagrams.onprem.analytics import PowerBI
from diagrams.custom import Custom

with Diagram("Airbnb ETL Pipeline"):
    with Cluster("Workflow"):
        nosql_db = Mongodb("Airbnb Data")
        dlt_etl = Custom("dlt_hub", "dlthub.png")
        snow1 = Snowflake("Staging Area")
        dbt = Dbt("Data transformation")
        snow2 = Snowflake("Data Warehouse")
    BI = PowerBI("Business insights")
    orchestration = Custom("Prefect","prefect.png")
    
    nosql_db >> dlt_etl >> snow1 >> dbt >> snow2 >> BI