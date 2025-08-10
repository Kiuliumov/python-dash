from dataclasses import dataclass
import os

@dataclass
class Config:
    game_version: int = int(os.getenv("GAME_VERSION", 21))
    binary_version: int = int(os.getenv("BINARY_VERSION", 35))
    gdw: int = int(os.getenv("GDW", 0))
    secret: str = os.getenv("SECRET", "Wmfd2893gb7")
