"""Quasar Flow stream runtime."""

from __future__ import annotations

from collections import deque


class Stream:
    def __init__(self, name: str, parallelism: int = 1):
        self.name = name
        self.parallelism = parallelism
        self.buffer = deque()

    def emit(self, event: dict) -> None:
        if not isinstance(event, dict):
            raise TypeError("events must be mapping objects")
        event.setdefault("stream", self.name)
        self.buffer.append(event)

    def drain(self, limit: int = 100) -> list:
        out = []
        while self.buffer and len(out) < limit:
            out.append(self.buffer.popleft())
        return out
