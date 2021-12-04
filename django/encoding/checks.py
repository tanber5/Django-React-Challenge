from django.core.checks import register
from mypy import api
import re
from django.core.checks import register
from django.core.checks.messages import CheckMessage, DEBUG, INFO, WARNING, ERROR

class MyPyErrorLocation:
    def __init__(self, location):
        self.location = location

    def __str__(self):
        return self.location

@register()
def mypy(app_configs, **kwargs):
    print("Performing mypy checks...\n")
    errors = []
    result = api.run(['.']) # stderr
    error_messages = result[0]
    if not error_messages:
        return []
    pattern = re.compile("^(.+\d+): (\w+): (.+)")

    errors = []
    for message in error_messages.rstrip().split("\n"):
        parsed = re.match(pattern, message)
        if not parsed:
            continue

        location = parsed.group(1)
        mypy_level = parsed.group(2)
        message = parsed.group(3)

        level = DEBUG
        if mypy_level == "note":
            level = INFO
        elif mypy_level == "warning":
            level = WARNING
        elif mypy_level == "error":
            level = ERROR
        else:
            print(f"Unrecognized mypy level: {mypy_level}")

        errors.append(CheckMessage(level, message, obj=MyPyErrorLocation(location)))
    return errors