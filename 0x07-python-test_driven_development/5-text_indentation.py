def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    - text (str): The input text.

    Raises:
    - TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty line
    current_line = ""

    # Iterate through each character in the text
    for char in text:
        # Append the character to the current line
        current_line += char

        # Check if the character is one of ., ? or :
        if char in ['.', '?', ':']:
            # Print the current line without leading/trailing spaces
            print(current_line.strip())
            # Print two new lines
            print("\n" * 2)
            # Reset the current line
            current_line = ""

    # Print the remaining content in the current line (if any)
    if current_line:
        print(current_line.strip())


