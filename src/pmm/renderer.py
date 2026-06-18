from pmm.models import PackageUpdate
from pmm.utils.headers import small
from pmm.utils.colors import cyan, bold, cyan_bold


def render(manager: str, packages: list[PackageUpdate]) -> None:
    print(f'\n{cyan_bold(small(manager.upper()))}\n')

    if not packages:
        print(cyan(' No updates available.\n'))
        return

    name_pad = max(len(p.name) for p in packages) + 1
    oldv_pad = max(len(p.oldv) for p in packages) + 1

    print(bold(str('', 'Package'.ljust(name_pad), 'Old'.ljust(oldv_pad), 'New\n')))

    for item in packages:
        print(
            '',
            item['name'].ljust(name_pad),
            item['oldv'].ljust(oldv_pad),
            item['newv'],
            '\n',
        )
