from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QVBoxLayout, QLineEdit, QProgressBar
from PyQt5.QtCore import Qt
from dataloader import FileSelector
from Analysis_tool.rare_earth_element import Normalization
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Main_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Geochemistry Analysis: Major and Trace')
        self.setGeometry(100, 100, 800, 600)
        self.path = ''
        self.normalization_method = ''
        self.txts = []
        self.file_selector = FileSelector()  # 创建FileSelector对象
        self.path_label = QLabel()
        self.createWidget()

    def createWidget(self):
        # 创建布局
        layout = QVBoxLayout()

        # 选择文件的按钮
        self.select_file_button = QPushButton('选择文件', self)
        self.select_file_button.setGeometry(10, 10, 100, 30)
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)
        
        self.help_button = QPushButton('帮助', self)
        self.help_button.setGeometry(690, 10, 100, 30)
        layout.addWidget(self.help_button)

        self.file_path_show = QLabel('文件路径:', self)
        self.file_path_show.setGeometry(10, 60, 100, 30)
        layout.addWidget(self.file_path_show)

        self.normalized_methods_select_button = QLabel('归一化方法:', self)
        self.normalized_methods_select_button.setGeometry(10, 110, 100, 30)
        layout.addWidget(self.normalized_methods_select_button)

        self.normalization_combobox = QComboBox(self)
        self.normalization_combobox.addItems(['PAAS', '球粒陨石', 'Sea water'])
        self.normalization_combobox.setGeometry(120, 110, 200, 30)
        layout.addWidget(self.normalization_combobox)

        self.start_analysis_button = QPushButton('开始分析', self)
        self.start_analysis_button.clicked.connect(self.data_analysis)
        self.start_analysis_button.setGeometry(350, 610, 100, 30)
        layout.addWidget(self.start_analysis_button)

        # self.label42 = QLabel('样本名称:', self)
        # self.label42.setGeometry(10, 160, 100, 30)
        # self.wenjianming_name = QLineEdit(self)
        # self.wenjianming_name.setGeometry(120, 160, 200, 30)

        # self.pb = QProgressBar(self)
        # self.pb.setGeometry(120, 210, 200, 30)
        # self.pb.setRange(0, 100)
        # self.pb.setValue(0)
        # self.pb.setOrientation(Qt.Horizontal)
        # self.pb.setFormat('%p%')

        self.author_show = QLabel('Author: Keran Li', self)
        self.author_show.setGeometry(self.width() - 210, self.height() - 40, 200, 30)
        self.author_show.setStyleSheet('font-size: 10pt; font-weight: bold; border: 2px solid black;')
        layout.addWidget(self.author_show)

        self.figure = plt.figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(10, 310, 780, 280)
        layout.addWidget(self.canvas)

        # 设置布局到主窗口
        self.setLayout(layout)

    def select_file(self):
        # 调用FileSelector对象的selectTxts方法选择文件
        self.file_selector.selectTxts()
        self.txts = self.file_selector.txts
        self.path = self.file_selector.path_name
        self.path_label.setText(self.path)

    def data_analysis(self):
        self.data_analysis = Normalization.data_analysis(self)