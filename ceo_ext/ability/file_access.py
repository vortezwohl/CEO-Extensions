from ceo import ability


@ability
def read_local_file(filename: str, encoding: str = 'utf-8') -> str:
    content = str()
    with open(filename, 'r', encoding=encoding) as f:
        content = f.read()
    return f'Content read from "{filename}": "{content}".'


@ability
def write_file(filename: str, content: str, encoding: str = 'utf-8') -> str:
    with open(filename, 'w', encoding=encoding) as f:
        f.write(content)
    return f'"{content}" written to "{filename}".'
