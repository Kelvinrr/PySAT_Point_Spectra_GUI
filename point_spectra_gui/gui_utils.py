# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:40:30 2016

@author: rbanderson
"""

from PyQt5 import QtGui, QtWidgets


def make_combobox(choices):
    combo = QtWidgets.QComboBox()
    combo.setMinimumWidth(150)  # TODO: make comboboxes update their width when new data is added.
    font = QtGui.QFont()
    font.setPointSize(10)
    combo.setFont(font)
    for i, choice in enumerate(choices):
        combo.addItem("")
        combo.setItemText(i, str(choice))

    return combo


def make_listwidget(choices):
    listwidget = QtWidgets.QListWidget()
    for item in choices:
        list_item = QtWidgets.QListWidgetItem(item)
        listwidget.addItem(list_item)
    return listwidget


def change_combo_list_vars(obj, newchoices):
    obj.clear()
    for i in newchoices:
        if isinstance(i, tuple):
            obj.addItem(i[1])
        elif isinstance(i, str):
            obj.addItem(i)
