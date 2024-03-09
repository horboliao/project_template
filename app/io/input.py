def input_text_from_console():
    """
    A function for entering text from the console.

    Returns the text entered by the user.
    """
    text = input("Enter text: ")
    return text


def read_text_from_file(file_path):
    """
    Function for reading text from a file.

    Parameters:
    file_path (str): The path to the file from which to read the text.

    Returns the read text.
    """
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def read_text_from_file_with_pandas(file_path):
    """
    A function for reading text from a file using the Pandas library.

    Parameters:
    file_path (str): The path to the file from which to read the text.

    Returns the read text.
    """
    import pandas as pd
    data = pd.read_csv(file_path)
    if isinstance(data, pd.DataFrame):
        text = data.to_string(index=False, header=False)
        return text
    else:
        raise ValueError("Failed to read data from file as DataFrame.")
