from typing import Any
from ._types import Flatten

def unflatten(
    data: Flatten, 
    sep: str = "."
) -> dict[str, Any]:
    ...