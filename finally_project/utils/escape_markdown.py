def escape_markdow(text): 
    special_symbols = r"_|*[](){}~`>#+-=.!"
    for char in special_symbols:
        text = text.replace(char, f"\\{char}")
    return text