from ..pyfront import *

class Label(Element):
    def __init__(self, text="", color=None, font_size=None, bold=False, italic=False, **kwargs):
        super().__init__("span", text=text, **kwargs)
        
        if color:
            self.css["color"] = color
        if font_size:
            self.css["font-size"] = f"{font_size}px"
        if bold:
            self.css["font-weight"] = "bold"
        if italic:
            self.css["font-style"] = "italic"