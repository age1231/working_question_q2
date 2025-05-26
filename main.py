
import sys
from PyQt5.QtWidgets import QApplication
from app_logic import PrimeApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrimeApp()
    window.show()
    sys.exit(app.exec_())
