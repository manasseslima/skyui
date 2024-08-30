from .scomponent import sComponent


class skyTable(sComponent):
    shtml = """
        <table class="table">
            <thead>
                {thead}
            </thead>
            <tbody>
                {tbody}
            </tbody>
        </table>
    """

    def __init__(self, columns: list, rows: list = None):
        if not rows:
            rows = []
        self.rows = rows
        self.columns = columns

    def render(self):
        tbody = ''
        for row in self.rows:
            trow = '<tr>'
            for dt in row:
                trow += f'<td>{dt}</td>'
            trow += '</tr>'
            tbody += trow
        thead = '<tr>'
        for col in self.columns:
            thead += f'<th>{col}</th>'
        thead += '</tr>'
        return self.shtml.format(thead=thead, tbody=tbody)
