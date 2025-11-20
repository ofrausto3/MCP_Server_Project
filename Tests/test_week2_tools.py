from tools.spark_tools import (
    submit_spark_job,
    get_job_status,
    list_spark_jobs,
    cancel_job,
    execute_spark_sql,
    get_job_logs,
)
from tools.postgres_tools import (
    execute_query,
    get_table_schema,
    list_tables,
    execute_dml,
    create_table,
    bulk_load_from_spark,
)
from tools.pipeline_tools import (
    create_etl_pipeline,
    execute_pipeline,
    get_pipeline_status,
)
from resources.spark_resources import spark_cluster_info, spark_job_details
from resources.postgres_resources import postgres_schema_info, postgres_table_data
from resources.pipeline_and_metrics_resources import active_pipelines, system_metrics
from prompts.templates import get_prompt


if __name__ == "__main__":
    print("=== Spark tools (Week 2) ===")
    res = submit_spark_job("print('hello')", {})
    print("submit_spark_job:", res)
    job_id = res["job_id"]
    print("get_job_status:", get_job_status(job_id))
    print("list_spark_jobs:", list_spark_jobs())
    print("cancel_job:", cancel_job(job_id))
    print("get_job_logs:", get_job_logs(job_id))
    print("execute_spark_sql (stub):", execute_spark_sql("SELECT 1"))

    print("\n=== Postgres tools (Week 2) ===")
    print("execute_query:", execute_query("SELECT * FROM users"))
    print("get_table_schema:", get_table_schema("users"))
    print("list_tables:", list_tables())
    print("execute_dml:", execute_dml("UPDATE users SET name = 'test' WHERE id = 1"))
    print("create_table:", create_table("demo", {"id": "integer", "name": "text"}))
    print("bulk_load_from_spark:", bulk_load_from_spark("df_users", "users"))

    print("\n=== Pipeline tools ===")
    p = create_etl_pipeline("spark:source", ["clean", "aggregate"], "postgres:dest")
    print("create_etl_pipeline:", p)
    exec_res = execute_pipeline(p["pipeline_id"], {"run_mode": "full"})
    print("execute_pipeline:", exec_res)
    print("get_pipeline_status:", get_pipeline_status(exec_res["execution_id"]))

    print("\n=== Resources ===")
    print("spark_cluster_info:", spark_cluster_info())
    print("spark_job_details:", spark_job_details(job_id))
    print("postgres_schema_info:", postgres_schema_info("public"))
    print("postgres_table_data:", postgres_table_data("users"))
    print("active_pipelines:", active_pipelines())
    print("system_metrics:", system_metrics())

    print("\n=== Prompts ===")
    for name in ["data_pipeline_template", "spark_optimization", "sql_best_practices", "error_troubleshooting"]:
        print(f"{name}:", get_prompt(name))
