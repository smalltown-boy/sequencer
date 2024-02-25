# -*- coding: utf-8 -*-
import sys
from PyQt6 import QtWidgets

from source.WindowLogin import WindowLogin


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
