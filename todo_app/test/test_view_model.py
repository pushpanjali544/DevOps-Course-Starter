import pytest
from todo_app.view_model import ViewModel
from todo_app.Item import Item

def test_todo_items():
    items=[Item(1,'test','TODO'),Item(2,'failstatus','DOING')]
    item_view_model=ViewModel(items)
    result=item_view_model.todo_items
    assert len(result) ==1
    assert result[0].id==1

def test_doing_items():
    items=[Item(1,'test','DOING')]
    item_view_model=ViewModel(items)
    item_view_model.doing_items
    assert len(item_view_model.doing_items) ==1  

def test_done_items():
    items=[Item(1,'test','DONE')]
    item_view_model=ViewModel(items)
    item_view_model.done_items
    assert len(item_view_model.done_items) ==1  