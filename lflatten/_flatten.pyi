from typing import Any

from ._types import Flatten

def flatten(
    data: Any,
    sep: str = ".",
    *,
    prefix: str = "",
    ignore_none: bool = True,
) -> Flatten: 
    ...