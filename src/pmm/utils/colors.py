def cyan(text: str) -> str:
    return f'\033[36m{text}\033[39m'


def bold(text: str) -> str:
    return f'\033[1m{text}\033[22m'


def cyan_bold(text: str) -> str:
    return f'\033[1;36m{text}\033[0m'
