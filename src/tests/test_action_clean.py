import pytest
from backend.action_clean import action_clean


def test_action_clean_marks_pig_as_clean():
    """Das Schwein wird korrekt als 'clean' markiert."""
    data = {"pig1": "dirty", "pig2": "dirty"}
    result = action_clean(data, "pig1")
    assert result["pig1"] == "clean"


def test_action_clean_overwrites_existing_state():
    """Auch wenn ein Schwein schon einen anderen Zustand hat, wird es überschrieben."""
    data = {"pig3": "muddy"}
    result = action_clean(data, "pig3")
    assert result["pig3"] == "clean"


def test_action_clean_key_is_string():
    """Der Key wird als String benutzt – auch wenn eine Zahl übergeben wird."""
    data = {}
    result = action_clean(data, 3)  # Übergabe als int
    assert result["3"] == "clean"
