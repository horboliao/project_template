def output_text_to_console(text):
    print(text)


def write_text_to_file(text, file_path):
    with open(file_path, 'w') as file:
        file.write(text)
