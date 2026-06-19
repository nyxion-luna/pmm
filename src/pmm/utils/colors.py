def cyan(text: str) -> str:
    return f'\033[36m{text}\033[39m'


def bold(text: str) -> str:
    return f'\033[1m{text}\033[22m'


def red(text: str) -> str:
    return f'\033[31m{text}\033[39m'
