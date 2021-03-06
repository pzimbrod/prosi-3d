"""
Abstract Base Class for every class analyzing the measured data
"""

from abc import ABC, ABCMeta, abstractmethod

class DataModel(ABC):
    """
    Top-level (abstract) methods that have to be inherited and re-defined by the sub-classes
    """
    @abstractmethod
    def get_features(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def analyze(self):
        pass
