
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from logic import calculate_primes

class PrimeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("prime.ui", self)
        self.runButton.clicked.connect(self.run_button_clicked)

    def run_button_clicked(self):
        try:
            number = int(self.inputLine.text())
            primes = calculate_primes(number)

            if self.actionCombo.currentText() == "Print the text box":
                self.outputBox.setPlainText(", ".join(map(str, primes)))
                self.statusLabel.setText("Printed in textbox")
            else:
                with open("primes.txt", "w") as f:
                    f.write(", ".join(map(str, primes)))
                self.statusLabel.setText("Written to file")

        except ValueError:
            self.statusLabel.setText("Enter a valid number!")
