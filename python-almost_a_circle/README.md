# Python - Almost a circle

A small shape library built step by step: a `Base` class that manages ids and JSON persistence, a validated `Rectangle`, and a `Square` that reuses it, all covered by unit tests.

## Files

| File | Description |
|------|-------------|
| `models/base.py` | `Base`: automatic ids, JSON string helpers, `save_to_file`, `create` and `load_from_file` |
| `models/rectangle.py` | `Rectangle`: validated `width`, `height`, `x`, `y`, plus `area`, `display`, `update` and `to_dictionary` |
| `models/square.py` | `Square`: a `Rectangle` with a `size` property |
| `tests/test_models/` | Unit tests for each module |

## Running the tests

```
python3 -m unittest discover tests
```
