from abc import ABC, abstractmethod
from pmm.models import PackageUpdate


class BaseManager(ABC):
    def __init__(self, name: str, requires_sudo: bool = False):
        self.name = name
        self.requires_sudo = requires_sudo

    @abstractmethod
    def check(self) -> list[PackageUpdate]:
        pass

    @abstractmethod
    def update(self) -> None:
        pass
