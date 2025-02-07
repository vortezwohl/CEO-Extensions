import os.path

from ceo import ability


@ability
def read_local_file(filename: str, encoding: str = 'utf-8', *args, **kwargs) -> str:
    # the `read_local_file` ability can read text content from a local file,
    # and can also verify whether the file exists.
    if os.path.exists(filename):
        content = str()
        with open(filename, 'r', encoding=encoding) as f:
            content = f.read()
        return f'Content read from "{filename}": "{content}".'
    return f'File "{filename}" not exist.'


@ability
def write_local_file(filename: str, write_mode: str, content: str, encoding: str = 'utf-8', *args, **kwargs) -> str:
    # value range for `write_mode` ∈ ['append', 'a', 'overwrite', 'w', 'create_and_write'].
    # if the file doesn't exist, select 'create_and_write' mode to create file and write the initial content into it.
    __append = 'a'
    __create_or_overwrite = 'w'
    _write_mode = __append
    _chosen_write_mode = write_mode.lower().strip()
    if _chosen_write_mode in ['append', 'a']:
        _write_mode = __append
    elif _chosen_write_mode in ['overwrite', 'w', 'create_and_write']:
        _write_mode = __create_or_overwrite
    if not os.path.exists(filename):
        _write_mode = __create_or_overwrite
    with open(filename, _write_mode, encoding=encoding) as f:
        f.write(content)
    return f'"{content}" written to "{filename}".'
