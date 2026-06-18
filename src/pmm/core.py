from pmm.managers.apt import AptManager

MANAGERS = {
    'apt': AptManager,
}


class Core:
    def __init__(self):
        self.results = {}

    def run(self, selected: list[str]):
        for name in selected:
            mgr_cls = MANAGERS.get(name)

            if not mgr_cls:
                print(f'Unknown manager: {name}')

            mgr = mgr_cls()
            self.results[name] = mgr.check()

    def has_updates(self) -> bool:
        return any(self.results.values())
