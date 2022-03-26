import os
bind = f"0.0.0.0:{os.getenv('PORT')}"
workers = 4
timeout = 30