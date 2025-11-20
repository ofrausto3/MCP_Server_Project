from typing import Dict, Any, List
from .base import make_resource


def active_pipelines() -> Dict[str, Any]:
    """
    Resource: pipelines://active (stub).
    """
    data = {
        "active": [],  # list of running pipelines would go here
    }
    return make_resource("pipelines://active", data)


def system_metrics() -> Dict[str, Any]:
    """
    Resource: metrics://system (stub).
    """
    data = {
        "cpu_percent": 0.0,
        "memory_percent": 0.0,
        "open_connections": 0,
    }
    return make_resource("metrics://system", data)
