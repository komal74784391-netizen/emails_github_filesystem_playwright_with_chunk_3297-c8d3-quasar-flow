"""Event-time windowing for Quasar Flow."""

from src.stream import Stream


def tumbling(stream: Stream, seconds: int) -> list:
    if seconds <= 0:
        raise ValueError("window size must be positive")
    events = stream.drain(limit=seconds * 10)
    return [
        {"window_start": index * seconds, "events": batch}
        for index, batch in enumerate(
            events[i:i + seconds] for i in range(0, len(events), seconds)
        )
    ]
