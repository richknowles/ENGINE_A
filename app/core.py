# Core logic to drive ENGINE A

from app.browser import login_and_send
from app.queue import get_next_batch
from app.flags import is_flagged, cooldown
import time

def run_campaign():
    print("Starting ENGINE A...")
    while True:
        batch = get_next_batch()
        for number, message in batch:
            if is_flagged():
                cooldown()
            try:
                login_and_send(number, message)
                time.sleep(5)
            except Exception as e:
                print(f"Failed to send message to {number}: {e}")
