from typing import Dict, Any


def make_resource(uri: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simple helper to wrap resource data with its URI.
    """
    return {"uri": uri, "data": data}
