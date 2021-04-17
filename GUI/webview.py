from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QGroupBox, QGridLayout


class WebView():

    def __init__(self, youtube_url):
        self.webview = QWebEngineView()
        youtube_id_idx = youtube_url.find('watch?v=')+len('watch?v=')
        youtube_id = youtube_url[youtube_id_idx:]
        self.webview.load(
            QUrl('https://www.youtube.com/embed/' + youtube_id))
        self.webview_groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(self.webview)
        self.webview_groupbox.setLayout(grid)
        self.webview.show()
