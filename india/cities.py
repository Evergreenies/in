""" This enables easy access to indian districts in the respective states """
# @coding: utf-8
# @author: Rishabh Batra
# @email: ribhu.1996@gmail.com
# TODO:
# Write the function for loading states
# get weather for every city

# python imports

# module imports
from . import states

CITIES = []


class City(object):
    """
    Defines a city
    """
    def __init__(self, abbr: str, name: str, state: str, population: int=None, area: int=None, url: str=None):
        self.name = name
        self.state = states.lookup(state)
        self.abbr = '%s_%s' %(self.state.abbr, abbr)
        self.population = population
        self.area = area
        self.density = self.population // self.area
        self.url = url

    def __repr__(self):
        return "<City: %s>" % self.name

    def __str__(self):
        return self.name

    def is_capital(self):
        """
        :return: boolean whether the city is capital or not
        """
        if self.name == self.state.capital:
            return True
        else:
            return False

def lookup():
    return


