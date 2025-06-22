
def treat_input(text: str) -> str:
    """
    Treats the input text by removing leading and trailing whitespace,
    replacing multiple spaces into a single underscore, and ensuring lowercase.
    
    Args:
        text (str): The input text to be treated.
        
    Returns:
        str: The treated text.
    """

    return '_'.join(text.strip().split()).lower()