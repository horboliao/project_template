def output_text_to_console(text):
    """
    A function for outputting text to the console.

    Parameters:
    text (str): The text to output to the console.
    """
    print(text)


def write_text_to_file(text, file_path):
    """
    Function for writing text to a file.

    Parameters:
    text (str): The text to write to the file.
    file_path (str): The path to the file to write the text to.
    """
    with open(file_path, 'w') as file:
        file.write(text)
