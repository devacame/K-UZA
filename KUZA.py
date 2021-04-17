from PyQt5.QtWidgets import QApplication
from GUI import KUZA
import sys
app = QApplication(sys.argv)
a = KUZA()
sys.exit(app.exec_())