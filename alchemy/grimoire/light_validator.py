import light_spellbook

def validate_ingredients(ingredients: str)->str:
    valids = light_spellbook.light_spell_allowed_ingredients()
    for ing in ingredients:
        for _ in valids:
            if ing == _:
                flag += 1
    if flag != 0:
        return ("VALID")
    else:
        return("INVALID")


validate_ingredients("")