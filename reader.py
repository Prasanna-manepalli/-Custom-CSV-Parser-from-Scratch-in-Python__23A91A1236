class CustomCSVReader:
    def __init__(self, file_path):
        self.file = open(file_path, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self):
        row = self._parse_next_row()
        if row is None:
            self.file.close()
            raise StopIteration
        return row

    def _parse_next_row(self):
        current_row = []
        current_field = []
        inside_quotes = False

        while True:
            char = self.file.read(1)

            if not char:  # End of file
                if current_field or current_row:
                    current_row.append("".join(current_field))
                    return current_row
                return None

            if char == '"':  # Handle quotes
                if inside_quotes:
                    next_char = self.file.read(1)

                    if next_char == '"':  # Escaped quote
                        current_field.append('"')
                    else:
                        inside_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    inside_quotes = True

            elif char == ',' and not inside_quotes:  # Column break
                current_row.append("".join(current_field))
                current_field = []

            elif char in ("\n", "\r") and not inside_quotes:  # Row break
                current_row.append("".join(current_field))
                return current_row

            else:
                current_field.append(char)
