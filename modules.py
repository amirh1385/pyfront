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
        self.parent = self
        self.root = self
        self.childs: list[Element] = [] if childs == None else childs

    def __add__(self, element: Element):
        if(not isinstance(element, Element)):
            raise TypeError("type error! just Element type")

        self.parent.childs.append(element)
        return self
    
    def append(self, element: Element):
        self.parent.childs.append(element)
    
    def appendRoot(self, element: Element):
        self.root.childs.append(element)
    
    def generate(self):
        if("style" in self.properties):
            self.properties["style"] += " ".join([name+": "+(value if isinstance(value, (int, float)) else "'"+value+"'")+";" for name, value in self.css.items()])
        else:
            self.properties["style"] = " ".join([name+": "+value+";" for name, value in self.css.items()])
        
        html = "<"+self.tag+" "+(" ".join([name+"="+(value if isinstance(value, (int, float)) else '"'+value+'"') for name, value in self.properties.items()]))+">"+self.default_value
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
        self.parent = body

root = RootHtml(childs=[
    Element("p", style_background_color="red", text="Hello World")
], global_styles={
    "margin": 0,
    "padding": 0,
    "box-sizing": "border-box"
})

result = root.generate()
print(result)

open("output.html", "w", encoding="utf-8").write(result)