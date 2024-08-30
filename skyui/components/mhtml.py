from .scomponent import sComponent


mg_html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Skalaplan</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="http://localhost:8081/ui/asserts/stylesheet"></link>
    <script src="https://unpkg.com/htmx.org@2.0.2" integrity="sha384-Y7hw+L/jvKeWIRRkqWYfPcvVxHzVzn5REgzbawhxAuQGwX1XWe70vji+VSeHOThJ" crossorigin="anonymous"></script>
    {scripts}
  </head>
  <body>
    {content}
  </body>
</html>
"""


class skyHtml(sComponent):
    def __init__(self, title: str, content: sComponent = None):
        self.title = title
        self.content = sComponent() if content is None else content

    def render(self) -> str:
        title = self.title.title()
        scripts = ''
        content = self.content.render()
        temp = mg_html.replace('\n', '').format(title=title, scripts=scripts, content=content)
        return temp
