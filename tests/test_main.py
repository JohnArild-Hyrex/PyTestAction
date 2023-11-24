#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import main

def test_always_pass():
    assert True

def test_add_pass():
     assert (main.MainProgram().add(2, 2) == 4)
     assert (main.MainProgram().add(6, 99.1) == 105.1)

def test_add_fail():
     # Only pass if TypeError is raised
     with pytest.raises(TypeError):
        main.MainProgram().add(2, "test")

def test_addToVar_pass():
    myMain = main.MainProgram()
    assert myMain.addToVar(2) == 2
    assert myMain.addToVar(4) == 6

def test_addToVar_fail():
     # Only pass if TypeError is raised
     with pytest.raises(TypeError):
        myMain = main.MainProgram()
        assert myMain.addToVar(2) == 2
        assert myMain.addToVar("2") == 4

def test_logVar(monkeypatch):
    captured_print = ""
    def mockprint(text):
        nonlocal captured_print
        captured_print = text
    monkeypatch.setattr("logging.info", mockprint)
    myMain = main.MainProgram()
    assert myMain.addToVar(2) == 2
    assert myMain.addToVar(4) == 6
    myMain.logVar()
    assert captured_print == "Member variable var1 = 6"
