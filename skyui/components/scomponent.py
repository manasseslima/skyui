

class sComponent:
    shtml = ''

    def __init__(self, body: str = ''):
        self.shtml = body

    def render(self) -> str:
        return self.shtml