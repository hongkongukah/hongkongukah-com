# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

import datetime

from pyscript import document, window  # type: ignore
from pyscript.ffi import create_proxy  # type: ignore

def update_countdown():
    current = datetime.datetime.now(datetime.timezone.utc)
    target = datetime.datetime.fromtimestamp(1749873600, datetime.timezone.utc)
    delta = target - current
    if delta.days < -8:
        announcement = "See you next year!\n\U0001F62D"
    elif delta < datetime.timedelta():
        day_number = -int(delta.days)
        announcement = f"Day {day_number}!\n\U0001F389\U0001F3A4\U0001F37B"
    else:
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds // 60) % 60
        seconds = delta.seconds % 60
        announcement = f"Starting in {days} days, {hours} hours, {minutes} minutes, {seconds} seconds\n\U0001F440"
    countdown = document.querySelector("#countdown-header")
    countdown.innerText = str(announcement)
    window.setTimeout(create_proxy(update_countdown), 100)  # type: ignore

update_countdown()
