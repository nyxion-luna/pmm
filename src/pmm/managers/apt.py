import shlex
from pmm.managers.base import BaseManager
from pmm.models import PackageUpdate
from pmm.utils.process import run


class AptManager(BaseManager):
    def __init__(self):
        super().__init__(name='apt', requires_sudo=True)

    def check(self) -> list[PackageUpdate]:
        run(['sudo', 'apt-get', 'update'])

        raw = run(
            [
                'apt-get',
                '--quiet',
                '--quiet',
                '--simulate',
                'upgrade',
            ],
            capture_output=True,
            text=True,
        ).stdout.splitlines()

        updates = []

        for line in raw:
            if not line.startswith('Inst '):
                continue

            parts = shlex.split(line)

            updates.append(
                PackageUpdate(
                    name=parts[1],
                    oldv=parts[2].strip('[]'),
                    newv=parts[3].lstrip('('),
                )
            )

        return updates

    def update(self) -> None:
        run(['sudo', 'apt-get', 'upgrade', '--yes'])
