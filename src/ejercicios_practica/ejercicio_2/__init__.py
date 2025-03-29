def search_rules(rules, word):
    """Busca la palabra ingresada en las reglas y devuelve una lista con las que la contienen."""
    return [rule for rule in rules.split("\n") if word in rule]