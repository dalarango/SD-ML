"""
Python model "Bass_dif.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    'TIME': 'time',
    'Time': 'time',
    'Customer': 'customer',
    'Adoption fraction': 'adoption_fraction',
    'Adoption from advertisement': 'adoption_from_advertisement',
    'Adoption from word of mouth': 'adoption_from_word_of_mouth',
    'Adoption rate': 'adoption_rate',
    'Advertising effectiveness': 'advertising_effectiveness',
    'Contact rate': 'contact_rate',
    'Potential adopters': 'potential_adopters',
    'Total population': 'total_population',
    'FINAL TIME': 'final_time',
    'INITIAL TIME': 'initial_time',
    'SAVEPER': 'saveper',
    'TIME STEP': 'time_step'
}

__pysd_version__ = "0.9.0"


@cache('step')
def customer():
    """
    Real Name: Customer
    Original Eqn: INTEG ( Adoption rate, Total population*0.1)
    Units: People
    Limits: (None, None)
    Type: component


    """
    return integ_customer()


@cache('run')
def adoption_fraction():
    """
    Real Name: Adoption fraction
    Original Eqn: 0.015
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.015


@cache('step')
def adoption_from_advertisement():
    """
    Real Name: Adoption from advertisement
    Original Eqn: Advertising effectiveness*Potential adopters
    Units: People/year
    Limits: (None, None)
    Type: component


    """
    return advertising_effectiveness() * potential_adopters()


@cache('step')
def adoption_from_word_of_mouth():
    """
    Real Name: Adoption from word of mouth
    Original Eqn: (Potential adopters/Total population)*Contact rate*Adoption fraction
    Units: People/year
    Limits: (None, None)
    Type: component


    """
    return (potential_adopters() / total_population()) * contact_rate() * adoption_fraction()


@cache('step')
def adoption_rate():
    """
    Real Name: Adoption rate
    Original Eqn: Adoption from advertisement+Adoption from word of mouth
    Units: People/year
    Limits: (None, None)
    Type: component


    """
    return adoption_from_advertisement() + adoption_from_word_of_mouth()


@cache('run')
def advertising_effectiveness():
    """
    Real Name: Advertising effectiveness
    Original Eqn: 0.011
    Units: 1/year
    Limits: (None, None)
    Type: constant


    """
    return 0.011


@cache('run')
def contact_rate():
    """
    Real Name: Contact rate
    Original Eqn: 100
    Units: People/year
    Limits: (None, None)
    Type: constant


    """
    return 100


@cache('step')
def potential_adopters():
    """
    Real Name: Potential adopters
    Original Eqn: INTEG ( -Adoption rate, Total population*0.9)
    Units: People
    Limits: (None, None)
    Type: component


    """
    return integ_potential_adopters()


@cache('run')
def total_population():
    """
    Real Name: Total population
    Original Eqn: 5e+06
    Units: People
    Limits: (None, None)
    Type: constant


    """
    return 5e+06


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 100
    Units: year
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 100


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: year
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 0


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: year
    Limits: (0.0, None)
    Type: component

    The frequency with which output is stored.
    """
    return time_step()


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 1
    Units: year
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 1


integ_customer = functions.Integ(lambda: adoption_rate(), lambda: total_population() * 0.1)

integ_potential_adopters = functions.Integ(lambda: -adoption_rate(),
                                           lambda: total_population() * 0.9)
