from typing import Dict, Any

_PIPELINES: Dict[str, Dict[str, Any]] = {}
_EXECUTIONS: Dict[str, Dict[str, Any]] = {}


def create_etl_pipeline(source: str, transformations: list[str], destination: str) -> Dict[str, Any]:
    """
    Week 2: Define an ETL workflow (stub).
    """
    pipeline_id = f"pipeline-{len(_PIPELINES) + 1}"
    _PIPELINES[pipeline_id] = {
        "source": source,
        "transformations": transformations,
        "destination": destination,
    }
    return {
        "pipeline_id": pipeline_id,
        "status": "created",
    }


def execute_pipeline(pipeline_id: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Week 2: Execute a defined ETL pipeline (stub).
    """
    if pipeline_id not in _PIPELINES:
        return {
            "pipeline_id": pipeline_id,
            "status": "not_found",
        }

    execution_id = f"exec-{len(_EXECUTIONS) + 1}"
    _EXECUTIONS[execution_id] = {
        "pipeline_id": pipeline_id,
        "params": params or {},
        "status": "running",
    }
    return {
        "execution_id": execution_id,
        "pipeline_id": pipeline_id,
        "status": "started",
    }


def get_pipeline_status(execution_id: str) -> Dict[str, Any]:
    """
    Week 2: Monitor pipeline execution (stub).
    """
    exec_info = _EXECUTIONS.get(execution_id)
    if not exec_info:
        return {
            "execution_id": execution_id,
            "status": "not_found",
        }

    # For now, pretend everything finishes successfully
    exec_info["status"] = "finished"
    return {
        "execution_id": execution_id,
        "pipeline_id": exec_info["pipeline_id"],
        "status": exec_info["status"],
    }
