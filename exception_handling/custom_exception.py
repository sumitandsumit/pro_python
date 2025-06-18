import os


class InvalidFileError(Exception):
    """Exception raised when a file does not meet the required criteria."""

    def __init__(self, message):
        self.message = message


class FileUploadManager:
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
    ALLOWED_FILE_TYPES = ["pdf", "doc", "docx", "txt"]

    def upload_file(self, file_path):
        """
        Uploads a file to the server.

        Args:
            file_path (str): The path to the file to be uploaded.

        Raises:
            InvalidFileError: If the file does not meet the required criteria.
        """
        file_size = self.get_file_size(file_path)
        file_type = self.get_file_type(file_path)

        if file_size > self.MAX_FILE_SIZE:
            raise InvalidFileError(
                f"File size exceeds the limit of {self.MAX_FILE_SIZE / (1024 * 1024):.2f} MB."
            )

        if file_type not in self.ALLOWED_FILE_TYPES:
            raise InvalidFileError(
                f"File type '{file_type}' is not allowed. Allowed file types are: {', '.join(self.ALLOWED_FILE_TYPES)}."
            )

        # Code to actually upload the file to the server
        print(f"Uploading file: {file_path}")

    def get_file_size(self, file_path):
        """
        Retrieves the size of a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            int: The size of the file in bytes.
        """
        import os

        return os.path.getsize(file_path)

    def get_file_type(self, file_path):
        """
        Retrieves the type of a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The file type (extension).
        """
        _, file_extension = os.path.splitext(file_path)
        return file_extension[1:].lower()


try:
    file_manager = FileUploadManager()
    file_manager.upload_file("example.pdf")
    file_manager.upload_file("large_file.txt")
    file_manager.upload_file("image.jpg")
except InvalidFileError as e:
    print(f"Error: {e.message}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
