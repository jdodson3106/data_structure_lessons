from typing import Optional, Any


class Node:

    def __init__(self):
        pass


class LinkedList:

    def __init__(self):
        pass

    def append(self, node: Node) -> Any:
        pass

    def prepend(self, node: Node) -> Any:
        pass

    def get(self, data: Any) -> tuple[Optional[Any], Optional[int]]:
        pass

    def get_at(self, idx: int) -> Any | None:
        pass

    def delete(self, data: Any) -> tuple[Optional[Any], Optional[int]]:
        pass
    def delete_at(self, idx: int) -> Any | None:
        pass

    def is_empty(self) -> bool:
        pass

    def __len__(self) -> int:
        pass
