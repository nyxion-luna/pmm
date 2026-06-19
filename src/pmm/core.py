from pmm.managers.apt import AptManager
from pmm.utils.colors import cyan
from pmm.utils.headers import large

MANAGERS = {
    'apt': AptManager,
}


class Core:
    def __init__(self):
        self.results = {}

    def run(self, selected: list[str]):
        print()
        for name in selected:
            mgr_cls = MANAGERS.get(name)

            print(cyan(large(name)), '\n')

            if not mgr_cls:
                print(cyan(f'Unknown manager: {name}\n'))
                continue

            mgr = mgr_cls()
            self.results[name] = mgr.check()
            print()

    def has_updates(self) -> bool:
        return any(self.results.values())
