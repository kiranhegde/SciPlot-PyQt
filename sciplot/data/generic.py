# -*- coding: utf-8 -*-
"""
Generic data containers

Created on Thu Jul  7 10:31:43 2016

@author: chc
"""

class Data:
    """
    Contains the underlying data to be plotted
    """
    def __init__(self):
        self._setupData()

    def _setupData(self):
        self.x = None
        self.y = None
        self.label = None
        #self.units = {'x_units': None, 'y_units': None}
        self.style_dict = {}

    @property
    def model_style(self):
        out = {}
        out.update(self.style_dict)
        out['label'] = self.label
        return out

class DataGlobal:
    """
    Contains data that is pertinent across all plots
    """
    def __init__(self):
        self.labels = {'x_label': None, 'y_label': None, 'title': None}
