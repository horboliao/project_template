def input_text_from_console():
    text = input("Enter text: ")
    return text


def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


def read_text_from_file_with_pandas(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    text = data.to_string(index=False, header=False)
    return text
