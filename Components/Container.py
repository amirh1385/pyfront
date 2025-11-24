from ..pyfront import *

class HorizontalContainer(Element):
    def __init__(self, childs=None, spacing=0, align="start", justify="start", wrap=False, **kwargs):
        super().__init__("div", childs=childs, **kwargs)
        self.css.update({
            "display": "flex",
            "flex-direction": "row",
            "gap": f"{spacing}px",
            "align-items": self._map_align(align),
            "justify-content": self._map_justify(justify),
            "flex-wrap": "wrap" if wrap else "nowrap"
        })

    def _map_align(self, align):
        mapping = {
            "start": "flex-start",
            "center": "center",
            "end": "flex-end",
            "stretch": "stretch",
        }
        return mapping.get(align, "flex-start")

    def _map_justify(self, justify):
        mapping = {
            "start": "flex-start",
            "center": "center",
            "end": "flex-end",
            "space-between": "space-between",
            "space-around": "space-around",
            "space-evenly": "space-evenly",
        }
        return mapping.get(justify, "flex-start")


class VerticalContainer(Element):
    def __init__(self, childs=None, spacing=0, align="start", justify="start", wrap=False, **kwargs):
        super().__init__("div", childs=childs, **kwargs)
        self.css.update({
            "display": "flex",
            "flex-direction": "column",
            "gap": f"{spacing}px",
            "align-items": self._map_align(align),
            "justify-content": self._map_justify(justify),
            "flex-wrap": "wrap" if wrap else "nowrap"
        })

    def _map_align(self, align):
        mapping = {
            "start": "flex-start",
            "center": "center",
            "end": "flex-end",
            "stretch": "stretch",
        }
        return mapping.get(align, "flex-start")

    def _map_justify(self, justify):
        mapping = {
            "start": "flex-start",
            "center": "center",
            "end": "flex-end",
            "space-between": "space-between",
            "space-around": "space-around",
            "space-evenly": "space-evenly",
        }
        return mapping.get(justify, "flex-start")