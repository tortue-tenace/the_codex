"""Dark validator module."""
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valids = {v.lower() for v in dark_spell_allowed_ingredients()}
    list_ing = {ing.strip().lower() for ing in ingredients.split(",")}
    keyword = "VALID" if list_ing & valids else "INVALID"
    return f"{ingredients} - {keyword}"
