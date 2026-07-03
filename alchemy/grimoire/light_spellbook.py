from . import light_validator


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = light_validator.validate_ingredients(ingredients)
    keyword = result.rsplit(" - ", 1)[-1]
    if keyword == "VALID":
        return f"Spell {spell_name} ({result}) recorded."
    return f"Spell '{spell_name}' rejected."
