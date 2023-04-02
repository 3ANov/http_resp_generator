from typing import List, Dict


class HttpPackage:
    def __init__(
            self,
            start_line: List,
            headers: Dict,
            body: str
    ) -> None:
        self.start_line = start_line
        self.headers = headers
        self.body = body

    def __repr__(self):
        headers_str = ''.join(list(map(lambda z: f'{z[0]}: {z[1]}\n', self.headers.items())))
        return f"{' '.join(self.start_line)}\n" \
               f"{headers_str}\n" \
               f"{self.body}"

