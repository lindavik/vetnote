import os

from vetnote.reader import read_data_files


def main():
    print("Welcome to VetNote")

    # Todo steps:
    # 1. read the input/data files
    data_folder_path = os.path.join(os.path.dirname(__file__), "../data")
    parsed_data = read_data_files(data_folder_path)

    for i, entry in enumerate(parsed_data, start=1):
        print(f"Consultation data from file {i}: {entry}")
    
    # 2. process the data ie translate it into an LLM prompt
    # 3. call the LLM
    # 4. process the LLM output, including error handling
    # 6. write the output to a file in the solution folder


if __name__ == "__main__":
    main()
