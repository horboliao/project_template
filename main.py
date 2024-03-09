from app.io.input import input_text_from_console, read_text_from_file, read_text_from_file_with_pandas
from app.io.output import output_text_to_console, write_text_to_file


def main():
    text_console = input_text_from_console()

    file_path = "data/example.txt"
    text_file = read_text_from_file(file_path)

    file_path_pandas = "data/example.csv"
    text_pandas = read_text_from_file_with_pandas(file_path_pandas)

    output_text_to_console(text_console)
    output_text_to_console(text_file)
    output_text_to_console(text_pandas)

    write_text_to_file(text_console, "data/output_console.txt")
    write_text_to_file(text_file, "data/output_file.txt")
    write_text_to_file(text_pandas, "data/output_pandas.txt")


if __name__ == "__main__":
    main()
