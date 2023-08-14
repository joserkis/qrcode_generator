from editor import Editor
from creator import Creator
import sys
import PyQt4

if __name__ == '__main__':
    app = PyQt4.QtGui.QApplication(sys.argv)
    e = Editor()
    app.exit(app.exec_(creator))
