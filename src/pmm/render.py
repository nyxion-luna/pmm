from pmm.models import PackageUpdate
from pmm.utils.colors import bold, cyan
from pmm.utils.headers import small


def render(manager: str, packages: list[PackageUpdate]) -> None:
    print(f'{cyan(bold(small(manager.upper())))}\n')

    if not packages:
        print(cyan(' No updates available.\n'))
        return

    name_pad = max(len(p.name) for p in packages)
    oldv_pad = max(len(p.oldv) for p in packages)

    print(bold(f" {'Package'.ljust(name_pad)}  {'Old'.ljust(oldv_pad)}  New"))

    for item in packages:
        print(f' {item.name.ljust(name_pad)}  {item.oldv.ljust(oldv_pad)}  {item.newv}')

    print()
