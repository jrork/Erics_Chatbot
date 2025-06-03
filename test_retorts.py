import sys
import types
import pytest

# Stub modules used by app that may not be installed in the test environment
sys.modules.setdefault('oci', types.ModuleType('oci'))

flask_stub = types.ModuleType('flask')
class FakeFlask:
    def __init__(self, *args, **kwargs):
        pass
    def route(self, *args, **kwargs):
        def decorator(func):
            return func
        return decorator
flask_stub.Flask = FakeFlask
flask_stub.render_template = lambda *a, **k: ""
flask_stub.request = object()
flask_stub.jsonify = lambda *a, **k: {}
sys.modules.setdefault('flask', flask_stub)

from app import get_schoolyard_retort

# Predefined retorts list from app.py
RETORTS = [
    "I know you are, but what am I?",
    "Your mom!",
    "No backsies!",
    "Takes one to know one!",
    "I'm rubber, you're glue, whatever you say bounces off me and sticks to you!",
    "Last one there is a rotten egg!",
    "Not uh!",
    "Yeah, well, double infinity no take-backs!",
    "Make me!",
    "Oh yeah? Prove it!",
    "Psych!",
    "Liar, liar, pants on fire!",
    "You and what army?",
    "Did too! Did not! Did too! Did not!",
    "Betcha can't catch me!",
]

def test_get_schoolyard_retort_multiple_calls():
    # Call the function multiple times to ensure randomness doesn't matter
    for _ in range(20):
        retort = get_schoolyard_retort()
        assert retort in RETORTS
