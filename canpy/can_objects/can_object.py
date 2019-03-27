__author__ = "Stefan Holzl"
__all__ = ['CANObject', 'CANNone']

from CANpy.canpy.can_objects.can_attribute import CANAttributesContainer


class CANObject(object):
    """Provides basic functionality for CAN-Objects"""
    def __init__(self):
        self._parent = CANNone()
        self._attributes = CANAttributesContainer(self)
        self.description = ""

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def attributes(self):
        return self._attributes

    def add_child(self, child):
        child.parent = self

    # Protocol definitions
    def __eq__(self, other):
        return super().__eq__(other)


class CANNone(CANObject):
    def __init__(self):
        pass

    # Protoclol definitions
    def __bool__(self):
        return False

    def __eq__(self, other):
        if other is None:
            return True
        return super().__eq__(other)