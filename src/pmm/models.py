from dataclasses import dataclass


@dataclass
class PackageUpdate:
    name: str
    oldv: str
    newv: str
