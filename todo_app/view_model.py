from todo_app.Item import Item


class ViewModel:
    def __init__(self, items):
        self._items = items
        self.todo_items=items
        self.doing_items=items
        self.done_items=items
        
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self,items):
        self._items=items
    
    @property
    def todo_items(self):
        return self._todo_items

    @todo_items.setter
    def todo_items(self,todo_items):
        self._todo_items=[]
        for item in todo_items:
            if item.status=='TODO':
               self._todo_items.append(item)

    @property
    def doing_items(self):
        return self._doing_items

    @doing_items.setter
    def doing_items(self,doing_items):
        self._doing_items=[]
        for item in doing_items:
            if item.status=='DOING':
               self._doing_items.append(item)

    @property
    def done_items(self):
        return self._done_items

    @done_items.setter
    def done_items(self,done_items):
        self._done_items=[]
        for item in done_items:
            if item.status=='DONE':
               self._done_items.append(item)
            