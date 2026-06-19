import argparse
import sys
from pmm import __description__, __version__
from pmm.core import Core
from pmm.render import render
from pmm.utils.colors import cyan, red


def main():
    try:
        parser = argparse.ArgumentParser(
            prog='pmm',
            description='Update your packages without the hassle of juggling fifteen different managers.',
        )

        parser.add_argument(
            '-n',
            '--dry-run',
            help='run the script without actually upgrading the packages',
            action='store_true',
        )
        parser.add_argument(
            '-y',
            '--yes',
            help='automatically update without asking for verification, assuming yes',
            action='store_true',
        )
        parser.add_argument(
            '--no-sudo',
            help='skips all package managers that require sudo',
            action='store_true',
        )
        parser.add_argument(
            '-v',
            '--version',
            help='print the program version and exit',
            action='store_true',
        )
        parser.add_argument(
            'managers',
            nargs='*',
            help='package managers to update (apt, flatpak, etc.)',
        )

        args = parser.parse_args()

        if args.version:
            print(f'pmm, version {__version__}')
            sys.exit(0)

        core = Core()
        core.run(args.managers)

        for name, packages in core.results.items():
            render(name, packages)

        if not core.has_updates():
            return

        if not args.yes:
            choice = input(cyan('Update? [Y/n/s]: ')).lower()
            match choice:
                case 'y' | '':
                    for name in args.managers:
                        mgr_cls = core.results.get(name)
                case _:
                    return
    except KeyboardInterrupt:
        print(red('\nExiting due to Ctrl+C.'))
