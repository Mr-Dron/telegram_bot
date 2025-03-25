def escape_markdow(text: str) -> str:
    """Проходит по всему переданному тексту, находит специальные символы и добавляет перед ним \\

    Args:
        text (str): Исходный текст

    Returns:
        str: Отредактированный текст
    """
    special_symbols = r"_|*[](){}~`>#+-=.!"
    for char in special_symbols:
        text = text.replace(char, f"\\{char}")
    return text