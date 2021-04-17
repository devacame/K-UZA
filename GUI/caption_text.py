from PyQt5.QtWidgets import QTextEdit, QGroupBox, QGridLayout


class CaptionText():

    def __init__(self, caption):
        self.caption = caption
        self.caption_text_groupbox = QGroupBox()
        self.caption_text_groupbox.setMaximumSize(700, 900)
        grid = QGridLayout()
        self.caption_text_display = QTextEdit()
        self.caption_text_display.setMaximumSize(650, 850)
        self.caption_text_display.setText(self.caption)
        grid.addWidget(self.caption_text_display)
        self.caption_text_groupbox.setLayout(grid)
