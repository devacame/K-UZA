import sys
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPushButton, QFileDialog


class SearchBar():

    def set_video_url_input(self):
        self.video_url_input = QLineEdit(self)
        self.video_url_input.setPlaceholderText(
            'eg. https://www.youtube.com/watch?v=5NTvXKUXEX4')
        self.video_url_input.setToolTip('유튜브 URL을 입력하세요.')

    def set_target_lang(self):
        self.target_lang = QComboBox(self)
        self.target_lang.addItem('영어')
        self.target_lang.addItem('중국어')
        self.target_lang.addItem('일본어')
        self.target_lang.addItem('이탈리아어')
        self.target_lang.addItem('독일어')
        self.target_lang.addItem('러시아어')
        self.target_lang.addItem('스페인어')
        self.target_lang.addItem('프랑스어')
        self.target_lang.setPlaceholderText('영상의 언어를 선택하세요.')

    def set_manual_lang(self):
        self.manual_lang = QLineEdit(self)
        self.manual_lang.setPlaceholderText('영상 언어를 GCP의 STT에 맞게 입력(선택)')

    def set_submit_btn(self):
        self.submit_btn = QPushButton(self)
        self.submit_btn.setText('시작')
        self.submit_btn.clicked.connect(self.submit)

    def set_json_upload_btn(self):
        self.json_upload_btn = QPushButton("JSON 파일 열기")
        self.json_upload_btn.clicked.connect(self.upload_GCP_key)

    def submit(self):
        url = self.video_url_input.text()
        lang = self.target_lang.currentText() or self.manual_lang.text()
        return (url, lang)

    def upload_GCP_key(self):
        json_path = QFileDialog.getOpenFileName(self)
        with open(json_path[0], 'r') as json:
            GCP_KEY = json.read()
        with open('./GCP-API-KEY.json', 'w') as key_file:
            key_file.write(GCP_KEY)
