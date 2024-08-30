from .scomponent import sComponent


class skyLeftMenu(sComponent):
    shtml = """
        <div style="display: flex; flex-direction: row; background-color: #1e293b; position: absolute; top: 0; bottom: 0; left: 0; right: 0;">
            <div style="min-width: 50px; max-width: 500px;background-color: #1e293b; padding: 0.5em; margin-top: 1em; margin-bottom: 1em; margin-right: 1em;">{menu}</div>
            <div style="flex: 1; background-color: #e2e8f0; padding: 0.5em; border-radius: 7px; margin-top: 1em; margin-bottom: 1em; margin-right: 1em; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);">{body}</div>
        </div>
    """

    def __init__(self, menu: sComponent = None, body: sComponent = None):
        self.menu = menu if menu else sComponent()
        self.body = body if body else sComponent()

    def render(self):
        body = self.shtml.format(
            # menu_proportion=self.proportions[0],
            # body_proportion=self.proportions[1],
            menu=self.menu.render(), 
            body=self.body.render(),
        )
        return body