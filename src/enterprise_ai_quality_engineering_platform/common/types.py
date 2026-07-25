"""
Shared type aliases.
"""

type JsonValue = (str | int | float | bool | None | JsonDict | JsonList)

type JsonDict = dict[str, JsonValue]

type JsonList = list[JsonValue]
