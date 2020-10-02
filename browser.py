import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

web = QWebEngineView()
web.setGeometry(0, 0, 1400, 950)
web.setWindowTitle('Medium Reader')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
url="https://google.com"
while True:
    web.load(QUrl(url))
    web.show()
    sys.exit(app.exec_())
    url=input("Paste the URL: ")
    if url=='Exit' or url=='exit' or url=='close' or url=='Close':break
sys.exit(app.exec_())
