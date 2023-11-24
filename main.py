#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

class MainProgram():
    def __init__(self):
        self.var1 = 0
    
    def addToVar(self, number1):
        self.var1 += number1
        return self.var1

    def logVar(self):
        logging.info(f"Member variable var1 = {self.var1}")

    @staticmethod
    def add(number1: float, number2: float) -> float:
        return number1 + number2    


if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    print(f"MainProgram().add(2, 3) = {MainProgram().add(2, 3)}")
    main = MainProgram()
    print(f"main.addToVar(2) = {main.addToVar(2)}")
    print(f"main.addToVar(3) = {main.addToVar(2)}")
    main.logVar()
