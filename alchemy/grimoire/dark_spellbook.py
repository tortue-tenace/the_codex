"""Dark spellbook module."""
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    keyword = result.rsplit(" - ", 1)[-1]
    if keyword == "VALID":
        return f"Spell '{spell_name}' recorded."
    return f"Spell '{spell_name}' rejected."
