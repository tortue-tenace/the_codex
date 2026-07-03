def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    valids = {v.lower() for v in light_spell_allowed_ingredients()}
    list_ing = {ing.strip().lower() for ing in ingredients.split(",")}
    keyword = "VALID" if list_ing & valids else "INVALID"
    return f"{ingredients} - {keyword}"
