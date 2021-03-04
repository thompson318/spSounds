# coding=utf-8

"""spSounds tests"""

from spsounds.ui.spsounds_demo import run_demo
from spsounds.midi import sounds

# Pytest style
def test_using_pytest_spsounds():
    """First test"""
    #pylint:disable=invalid-name
    assert run_demo(args = "nothing")
