# webhooks.py
_callbacks = {}

def send(title, message, recipient):
    print(f"[WEBHOOK] {title} → {message} → {recipient}")

def add_callback(event, func):
    _callbacks[event] = func

def trigger(event, data):
    if event in _callbacks:
        _callbacks[event](data)
