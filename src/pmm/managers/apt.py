import shlex
import subprocess
from pmm.managers.base import BaseManager
from pmm.models import PackageUpdate


class AptManager(BaseManager):
    def __init__(self):
        super().__init__(name='apt', requires_sudo=True)

    def check(self) -> list[PackageUpdate]:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)

        raw = subprocess.run(
            [
                'apt-get',
                '--quiet',
                '--quiet',
                '--simulate',
                'upgrade',
            ],
            capture_output=True,
            text=True,
            check=True,
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
        subprocess.run(['sudo', 'apt-get', 'upgrade', '--yes'], check=True)
