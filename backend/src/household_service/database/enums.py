from enum import Enum

class Role(Enum):
    user = "user"
    admin = "admin"

class Bill(Enum):
    rent = "rent"
    energy = "energy"
    water = "water"
    broadband = "broadband"
    council_tax = "council_tax"