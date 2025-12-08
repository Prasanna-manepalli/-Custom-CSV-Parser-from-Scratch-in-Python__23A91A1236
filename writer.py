class CustomCSVWriter:
    def __init__(self, file_path):
        self.file = open(file_path, "w", encoding="utf-8")

    def _needs_quotes(self, field: str) -> bool:
        return (',' in field) or ('"' in field) or ('\n' in field) or ('\r' in field)

    def _escape_quotes(self, field: str) -> str:
        return field.replace('"', '""')

    def _format_field(self, field: str) -> str:
        if self._needs_quotes(field):
            field = self._escape_quotes(field)
            return f'"{field}"'
        return field

    def writerow(self, row: list[str]):
        formatted_fields = [self._format_field(f) for f in row]
        line = ",".join(formatted_fields)
        self.file.write(line + "\n")

    def writerows(self, rows: list[list[str]]):
        for row in rows:
            self.writerow(row)

    def close(self):
        self.file.close()
