from typing import Iterable

from flask import jsonify


def read_file(filename: str):
    with open(filename) as file:
        for line in file:
            yield line


def filter_query(value: str, data: Iterable[str]) -> list:
    """
    Return filtered data by value
    """
    return list(filter(lambda x: value in x, data))


def unique(data: Iterable[str], *args, **kwargs) -> set:
    """
    Return unique data
    """
    return set(data)


def map_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """
    Return data by column
    """
    return map(lambda x: x.split()[int(value)], data)


def limit_query(value: str, data: Iterable[str]) -> list:
    """
    Return limit list
    """
    return list(data)[:int(value)]


def sort_query(value: str, data: Iterable[str]) -> Iterable[str]:
    """
    Return sorted data
    """
    reverse: bool = value == "desc"
    return sorted(data, reverse=reverse)


CMDS = {
    "filter": filter_query,
    "unique": unique,
    "map": map_query,
    "limit": limit_query,
    "sort": sort_query
}


def execute(query: dict[str:str], filename: str):
    """
    Execute user commands
    """
    data = read_file(filename)
    cmd1 = query.get("cmd1")
    cmd2 = query.get("cmd2")
    data = CMDS[cmd1](value=query["value1"], data=data)
    if cmd2:
        data = CMDS[cmd2](value=query["value2"], data=data)
    return jsonify(list(data))
