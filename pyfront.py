class Element:
    def __init__(self, tag="div",text="", childs=None, **kwargs):
        self.css = {}
        self.tag = tag
        self.properties = {}
        for name, value in kwargs.items():
            if(name.startswith("style_")):
                self.css[name[6:].replace("_", "-")] = value
            else:
                self.properties[name] = value
        self.default_value = text
        self.container = self
        self.childs: list[Element] = childs or []

    def __add__(self, element: Element):
        if(not isinstance(element, Element)):
            raise TypeError("type error! just Element type")

        self.container.childs.append(element)
        return self
    
    def append(self, element: Element):
        self.container.childs.append(element)
    
    def appendRoot(self, element: Element):
        self.childs.append(element)
    
    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters"""
        return (
            text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#39;")
        )
    
    def generate(self):
        if "style" in self.properties:
            self.properties["style"] += " ".join(
                f"{name}: {self._escape_html(str(value))};" for name, value in self.css.items()
            )
        else:
            self.properties["style"] = " ".join(
                f"{name}: {self._escape_html(str(value))};" for name, value in self.css.items()
            )
        
        html = "<"+self.tag+" "+(" ".join([name+"="+(value if isinstance(value, (int, float)) else '"'+self._escape_html(value)+'"') for name, value in self.properties.items()]))+">"+self._escape_html(self.default_value)

        for i in self.childs:
            html += i.generate()

        return html+"</"+self.tag+">"

class RootHtml(Element):
    def __init__(self, global_styles=None, **kwargs):
        super().__init__("html", **kwargs)
        head = Element("head")
        if(global_styles != None):
            head += Element("style", text=("*{ " + (" ".join([str(name)+": "+str(value)+";" for name, value in global_styles.items()])) + " }"))
        self += head
        body = Element("body")
        self += body
        self.container = body
