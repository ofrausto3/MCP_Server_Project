from typing import Dict, Any
from .base import make_resource


def spark_cluster_info() -> Dict[str, Any]:
    """
    Resource: spark://cluster/info (stub).
    """
    data = {
        "master_url": "spark://example-master:7077",
        "worker_count": 2,
        "total_cores": 8,
        "total_memory_gb": 32,
    }
    return make_resource("spark://cluster/info", data)


def spark_job_details(job_id: str) -> Dict[str, Any]:
    """
    Resource: spark://jobs/{job_id} (stub).
    """
    data = {
        "job_id": job_id,
        "status": "running",
        "stages": [],
        "metrics": {},
    }
    return make_resource(f"spark://jobs/{job_id}", data)
