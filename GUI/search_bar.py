import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QComboBox, QPushButton, QFileDialog, QGroupBox, QGridLayout, QLabel


class SearchBar(QWidget):

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
        self.target_lang.setPlaceholderText('영상의 언어를 선택하세요.')

        self.manual_lang = QLineEdit()
        self.manual_lang.setPlaceholderText('영상 언어를 GCP의 STT에 맞게 입력(선택)')

        self.submit_btn = QPushButton()
        self.submit_btn.setText('시작')
        self.submit_btn.clicked.connect(self.submit)
        self.submit_btn.resize(100, 20)

        self.json_upload_btn = QPushButton("JSON 파일 열기")
        self.json_upload_btn.clicked.connect(self.upload_GCP_key)

        self.search_bar_groupbox = QGroupBox()
        grid = QGridLayout()
        grid.addWidget(self.video_url_input, 0, 0)
        grid.addWidget(self.target_lang, 0, 1)
        grid.addWidget(self.manual_lang, 0, 2)
        grid.addWidget(self.submit_btn, 0, 3)
        self.search_bar_groupbox.setLayout(grid)

    def submit(self):
        url = self.video_url_input.text()
        man_lang = self.manual_lang.text()
        if man_lang:
            return (url, man_lang)
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
            return (url, lang_GCP[lang])

    def upload_GCP_key(self):
        json_path = QFileDialog.getOpenFileName(self, 'Open File', './')
        if not json_path[0]:
            return
        with open(json_path[0], 'r') as json:
            GCP_KEY = json.read()
        with open('./GCP-API-KEY.json', 'w') as key_file:
            key_file.write(GCP_KEY)
