from .scomponent import sComponent


class skyEdit(sComponent):
    shtml = """
        <div class="form">
            <input type="text" value={value} placeholder={placeholder}>
        </div>
    """
    def __init__(self, value: str = '', placeholder: str = ''):
        self.value = value
        self.placeholder = placeholder

    def render(self):
        ret = self.shtml.format(value=self.value, placeholder=self.placeholder)
        return ret
