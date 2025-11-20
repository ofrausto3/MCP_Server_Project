from typing import Dict, Any, List

# Simple in-memory job store so we can simulate job state
_JOBS: Dict[str, Dict[str, Any]] = {}


def submit_spark_job(script: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """
    Week 1: Submit a simple Spark job (stub).
    For now we just fake a job id and store it in memory.
    """
    job_id = f"job-{len(_JOBS) + 1}"
    _JOBS[job_id] = {
        "status": "running",
        "script": script,
        "params": params or {},
    }
    return {
        "status": "submitted",
        "job_id": job_id,
        "script": script,
    }


def get_job_status(job_id: str) -> Dict[str, Any]:
    """
    Week 1: Get status of a job (stub).
    """
    job = _JOBS.get(job_id)
    if not job:
        return {"job_id": job_id, "status": "unknown"}
    return {"job_id": job_id, "status": job["status"]}


def list_spark_jobs() -> Dict[str, Any]:
    """
    Week 1: List recent jobs (stub).
    """
    jobs: List[Dict[str, Any]] = [
        {"job_id": jid, "status": data.get("status", "unknown")}
        for jid, data in _JOBS.items()
    ]
    return {"jobs": jobs}


# ---------------------------
# Week 2: Advanced Spark tools
# ---------------------------

def cancel_job(job_id: str) -> Dict[str, Any]:
    """
    Week 2: Cancel a running job (stub).
    We just flip its status to 'cancelled'.
    """
    job = _JOBS.get(job_id)
    if not job:
        return {"job_id": job_id, "status": "not_found"}
    job["status"] = "cancelled"
    return {"job_id": job_id, "status": "cancelled"}


def execute_spark_sql(sql: str, output_format: str = "json") -> Dict[str, Any]:
    """
    Week 2: Execute Spark SQL (stub).
    To avoid depending on real tables, we just echo back the SQL and return an empty row set.
    """
    return {
        "sql": sql,
        "output_format": output_format,
        "rows": [],
    }


def get_job_logs(job_id: str) -> Dict[str, Any]:
    """
    Week 2: Retrieve job logs (stub).
    """
    if job_id not in _JOBS:
        return {"job_id": job_id, "logs": [], "status": "not_found"}

    logs = [
        f"[INFO] Job {job_id} started.",
        f"[INFO] Job {job_id} is currently in status: {_JOBS[job_id]['status']}.",
        "[INFO] This is a stub log entry for demo purposes.",
    ]
    return {"job_id": job_id, "logs": logs}
