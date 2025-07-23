# -*- coding: utf-8 -*-
import os
"""
Tách phần import Qt để tránh lỗi khi chạy trên Maya 2022 và các phiên bản mới hơn.
"""
try:

    import shiboken2 as shiboken
    import PySide2.QtUiTools as QtUiTools
    import PySide2.QtWidgets as QtWidgets
    import PySide2.QtGui as QtGui
    import PySide2.QtCore as QtCore

    from shiboken2 import wrapInstance
    from PySide2.QtWidgets import QAction
except ImportError:

    import shiboken6 as shiboken
    import PySide6.QtUiTools as QtUiTools
    import PySide6.QtWidgets as QtWidgets
    import PySide6.QtGui as QtGui
    import PySide6.QtCore as QtCore

    from shiboken6 import wrapInstance
    from PySide6.QtGui import QAction


__all__ = ["QtWidgets", "QtGui", "QtCore", "QtUiTools", "wrapInstance"]

