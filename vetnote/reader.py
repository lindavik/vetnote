import os


class FileReader:
    """
    A class to read files and return their contents.
    """

    def read_file(self, file_path: str) -> str:
        """
        Reads the content of a specific file.

        Args:
            file_path (str): The full path to the file to read.

        Returns:
            str: The content of the file as a string.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
