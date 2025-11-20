from typing import Dict


PROMPTS: Dict[str, str] = {
    "data_pipeline_template": (
        "You are a helpful assistant that designs ETL pipelines. "
        "Given a source system, a set of transformations, and a destination, "
        "describe a step-by-step Spark and PostgreSQL pipeline."
    ),
    "spark_optimization": (
        "You are a Spark performance expert. Suggest tuning strategies for jobs, "
        "including partitioning, caching, broadcast joins, and shuffle optimization."
    ),
    "sql_best_practices": (
        "You are a PostgreSQL tuning assistant. Provide indexing strategies, query patterns, "
        "and tips to avoid full table scans where possible."
    ),
    "error_troubleshooting": (
        "You are a troubleshooting assistant. Given an error message from Spark or PostgreSQL, "
        "explain what it likely means and suggest steps to fix it."
    ),
}


def get_prompt(name: str) -> str:
    """
    Return the prompt text for a given name, or a default message if not found.
    """
    return PROMPTS.get(name, "Prompt not found.")
