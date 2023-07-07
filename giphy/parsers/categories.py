from .gif import Gif

class Category:
    def __init__(self, data):
        self._data = data
        self.name = data.get("name")
        self.encoded_name = data.get("encoded_name", "")
        if self._data.get("subcategories"):
            self.sub_categories = [SubCategory(data) for data in self._data.get("subcategories")]
            self.gif = Gif(data.get("gif"))

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, encoded_name={self.encoded_name})"
        
class SubCategory(Category):
    is_sub = True
