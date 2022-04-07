import pytest
import os
from todo_app.app import create_app
from threading import Thread
from selenium import webdriver


# @pytest.fixture(scope='module')
# def app_with_temp_board():
    # Create the new board & update the board id environment variable
#     board_id,todo_id,doing_id = create_trello_board()
#     #os.environ['BOARDID'] = board_id
#     #os.environ['DOING'] = doing_id
#     #os.environ['TODOID'] = todo_id
    
#     # construct the new application
#     ##application = create_app()
#     # start the app in its own thread.
#     thread = Thread(target=lambda:
#     application.run(use_reloader=False))
#     thread.daemon = True
#     thread.start()
#     yield application
#     # Tear Down
#     thread.join(1)
#     ##delete_trello_board(board_id)

# @pytest.fixture(scope='module')
# def driver():
#     opts = webdriver.ChromeOptions()
#     opts.add_argument('--headless')
#     opts.add_argument('--no-sandbox')
#     opts.add_argument('--disable-dev-shm-usage')
#     with webdriver.Chrome(options=opts) as driver:
#         yield driver

# def test_task_journey(driver, app_with_temp_board):
#     driver.get('http://localhost:5000/')
#     assert driver.title == 'To-Do App'
#     card_title = driver.find_element_by_name('additem')
#     card_title.send_keys('test')
#     card_submit=driver.find_element_by_name('submitnewitem')
#     card_submit.click()
#     assert driver.page_source.find('test')>0