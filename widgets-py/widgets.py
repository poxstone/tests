import unittest


class Widget:
    def __init__(self, word):
        self.size = (50,50)

    def size(self):
        return self.size

    def resize(self, x,y):
        self.size = (x,y)


class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.assertEqual((50,50), (50,50), 'incorrect default size')

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        self.assertEqual((100,150), (100,150), 'wrong size after resize')

