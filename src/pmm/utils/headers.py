def large(text: str) -> str:
    return f'---------------< {text} >'.ljust(75, '-')


def small(text: str) -> str:
    return f"\033[1m {f' {text} '.center(20, '-')}\033[22m"
