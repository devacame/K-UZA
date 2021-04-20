from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, QGroupBox, QFileDialog, QSplitter)
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
sys.path.append('./')
sys.path.append('./src/')

from src import run_backend

class KUZA(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.video_url_input = QLineEdit()
        self.video_url_input.setPlaceholderText('유튜브 URL을 입력하세요.')

        self.target_lang = QComboBox()
        self.target_lang.addItem('영어')
        self.target_lang.addItem('중국어(간체-중국)')
        self.target_lang.addItem('일본어')
        self.target_lang.addItem('이탈리아어')
        self.target_lang.addItem('독일어')
        self.target_lang.addItem('러시아어')
        self.target_lang.addItem('스페인어')
        self.target_lang.addItem('프랑스어')
        self.target_lang.setToolTip('영상의 언어를 선택하세요.')

        self.manual_lang = QLineEdit()
        self.manual_lang.setPlaceholderText('영상 언어를 GCP의 STT에 맞게 입력(선택)')

        self.submit_btn = QPushButton()
        self.submit_btn.setText('시작')
        self.submit_btn.clicked.connect(self.submit)

        self.json_upload_btn = QPushButton("JSON 파일 열기")
        self.json_upload_btn.clicked.connect(self.upload_GCP_key)

        self.search_bar_groupbox = QGroupBox()
        search_grid = QGridLayout()
        search_grid.addWidget(self.video_url_input, 0, 0)
        search_grid.addWidget(self.target_lang, 0, 1)
        search_grid.addWidget(self.manual_lang, 0, 2)
        search_grid.addWidget(self.submit_btn, 0, 3)
        search_grid.addWidget(self.json_upload_btn, 0, 4)
        self.search_bar_groupbox.setLayout(search_grid)
        self.search_bar_groupbox.setMaximumHeight(50)
        self.search_bar_groupbox.setMinimumWidth(850)

        self.webview = QWebEngineView()
        self.webview.load(QUrl('https://www.youtube.com'))
        self.webview_groupbox = QGroupBox()
        webview_grid = QGridLayout()
        webview_grid.addWidget(self.webview)
        self.webview_groupbox.setLayout(webview_grid)
        self.webview.show()

        self.caption = caption
        self.caption_text_groupbox = QGroupBox()
        caption_grid = QGridLayout()
        self.caption_text_display = QTextEdit()
        caption_grid.addWidget(self.caption_text_display)
        self.caption_text_groupbox.setLayout(caption_grid)

        self.split_video_caption = QSplitter(Qt.Horizontal)
        self.split_video_caption.addWidget(self.webview_groupbox)
        self.split_video_caption.addWidget(self.caption_text_groupbox)
        self.split_video_caption.setMinimumHeight(700)

        grid = QGridLayout()
        grid.addWidget(self.search_bar_groupbox, 0, 0)
        grid.addWidget(self.split_video_caption, 1, 0)

        self.setLayout(grid)

        self.setWindowTitle('K-UZA')
        self.setGeometry(0, 0, 1920, 1080)
        self.show()

    def submit(self):
        url = self.video_url_input.text().strip()
        if not 'watch?v=' in url:
            caption = '정상적인 URL을 입력해주세요.'
        else:
            youtube_id_idx = url.find('watch?v=')+len('watch?v=')
            youtube_id = url[youtube_id_idx:]
            self.webview.load(QUrl('https://www.youtube.com/embed/' + youtube_id))
            man_lang = self.manual_lang.text()
            if man_lang:
                caption = run_backend(url, man_lang)
            else:
                lang = self.target_lang.currentText()
                if lang:
                    lang_GCP = {
                        '영어': 'en-US',
                        '중국어(간체-중국)': 'zh',
                        '프랑스어': 'fr-FR',
                        '러시아어': 'ru-RU',
                        '이탈리아어': 'it-IT',
                        '스페인어': 'es-ES',
                        '일본어': 'ja-JP',
                        '독일어': 'de-DE'
                    }
                caption = run_backend(url, lang_GCP[lang])
        self.caption_text_display.setText(caption)

    def upload_GCP_key(self):
        json_path = QFileDialog.getOpenFileName(self, 'Open File', './')
        if not json_path[0]:
            return
        with open(json_path[0], 'r') as json:
            GCP_KEY = json.read()
        with open('./GCP-API-KEY.json', 'w') as key_file:
            key_file.write(GCP_KEY)