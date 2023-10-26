from pyscript import window
import json

_colors = [
    [255, 89, 149],  [182, 227, 84],  [254, 237, 108], [140, 237, 255],
    [158, 111, 254], [137, 156, 161], [248, 248, 242], [191, 70, 70],
    [81, 96, 131],   [249, 38, 114],  [130, 180, 20],  [253, 151, 31],
    [86, 194, 214],  [128, 131, 132], [140, 84, 254],  [70, 84, 87]
]

class _Chart:
    def __init__(self, type, _plot_options={}):
        self.title = ""
        self.x_labels = ""
        self._data = []
        self._type = type
        self._plot_options = _plot_options

    def add(self, name, data):
        self._data.append({
            "name": name,
            "color": f"rgba({','.join(map(str, _colors[len(self._data)%len(_colors)]))}, 0.75)",
            "data": data
        })

    def render(self):
        options = {
            "chart": {
                "type": self._type,
                "height": 300,
                "width": 400
            },
            "credits": {
              "enabled": False  
            },
            "title": {
                "text": self.title
            },
            "xAxis": {
                "categories": list(self.x_labels)
            },
            "legend": {
                "layout": "vertical",
                "align": "left",
                "verticalAlign": "top",
                "y": 50,
                "borderWidth": 0
            },
            "yAxis": {
                
            },
            "series": self._data,
            "plotOptions": self._plot_options
        }

        window.renderChart(json.dumps(options))

class Line(_Chart):
    def __init__(self):
        super().__init__("line")
        
class StackedLine(_Chart):
    def __init__(self):
        super().__init__("line", {
            "area": {
                "stacking": "percent"
            },
            "series": {
                "stacking": "percent"
            }
        })
        
class Bar(_Chart):
    def __init__(self):
        super().__init__("column")
        
class StackedBar(_Chart):
    def __init__(self):
        super().__init__("column", {
            "column": {
                "stacking": "percent"
            }
        })

class HorizontalBar(_Chart):
    def __init__(self):
        super().__init__("bar")

class StackedHorizontalBar(_Chart):
    def __init__(self):
        super().__init__("bar", {
            "bar": {
                "stacking": "percent"
            }
        })

class XY(_Chart):
    def __init__(self):
        super().__init__("scatter")

class Pie(_Chart):
    def __init__(self):
        super().__init__("pie")