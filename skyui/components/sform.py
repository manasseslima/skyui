from pydantic import BaseModel
from .scomponent import sComponent
from .sedit import skyEdit


class skyForm(sComponent):
    shtml = """
        <div class="form">
            {rows}
        </div>
    """
    def __init__(self, model: BaseModel, layout: list = None, data: dict = None):
        if data is None:
            data = {}
        if layout is None:
            layout = []
        self.layout = layout
        self.data = data

    def render(self):
        rows = ''
        for line in self.layout:
            row = f'<div class="row">'
            for item in line:
                row += skyEdit()
            row += '</div>'

        ret = self.shtml.format(rows=rows)
        return ret