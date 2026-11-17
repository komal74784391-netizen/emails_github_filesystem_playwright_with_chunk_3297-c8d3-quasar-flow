from src.stream import Stream
from src.window import tumbling


def test_emit_and_drain():
    stream = Stream("orders")
    stream.emit({"id": 1})
    assert stream.drain(limit=1)[0]["id"] == 1


def test_tumbling_groups_events():
    stream = Stream("orders")
    for index in range(4):
        stream.emit({"id": index})
    windows = tumbling(stream, seconds=2)
    assert len(windows) == 2
