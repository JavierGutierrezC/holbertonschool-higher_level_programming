#!/usr/bin/python3


class MyInt(int):

    def __init__(self, value):
        self.value = value

    def __eq__(self, number):
        return self.value != number

    def __ne__(self, number):
        return not self == number
