import sys

from vetnote.reader import FileReader


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file_path>")
        print("Please provide a file path")
        sys.exit(1)

    file_path = sys.argv[1]
    file_reader = FileReader()

    try:
        file_content = file_reader.read_file(file_path)
        print(f"Contents of the file:\n{file_content}")
    except FileNotFoundError as e:
        print(f"An exception occured while reading the input files: {e}")

    # 2. process the data ie translate it into an LLM prompt
    # 3. call the LLM
    # 4. process the LLM output, including error handling
    # 5. include fallback, if first LLM call fails,
    # depending on error retry and then pivot to second LLM
    # 6. write the output to a file in the solution folder


if __name__ == "__main__":
    main()
