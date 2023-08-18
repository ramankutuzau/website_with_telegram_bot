from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *

scheduler = None

def start():
    global scheduler
    if not scheduler:
        scheduler = BackgroundScheduler()
        scheduler.add_job(parse_instagram, 'interval', seconds=7200)
        scheduler.start()
    elif scheduler.running:
        pass
    else:
        scheduler.start()
