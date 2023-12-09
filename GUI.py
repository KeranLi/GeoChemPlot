from PyQt5.QtWidgets import *
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
        self.createWidget()

    def createWidget(self):
        self.btn11 = QPushButton('选择文件', self)
        self.btn11.clicked.connect(self.select_file)
        self.btn11.setGeometry(10, 10, 100, 30)
        self.btn12 = QPushButton('帮助', self)
        self.btn12.setGeometry(690, 10, 100, 30)

        self.label31 = QLabel('选择的文件路径:', self)
        self.label31.setGeometry(10, 60, 100, 30)
        self.label32 = QLabel(self.path, self)
        self.label32.setGeometry(120, 60, 500, 30)

        self.label41 = QLabel('归一化方法:', self)
        self.label41.setGeometry(10, 110, 100, 30)
        self.normalization_combobox = QComboBox(self)
        self.normalization_combobox.addItems(['Method 1', 'Method 2', 'Method 3'])
        self.normalization_combobox.setGeometry(120, 110, 200, 30)

        self.label42 = QLabel('样本名称:', self)
        self.label42.setGeometry(10, 160, 100, 30)
        self.wenjianming_name = QLineEdit(self)
        self.wenjianming_name.setGeometry(120, 160, 200, 30)

        self.pb = QProgressBar(self)
        self.pb.setGeometry(120, 210, 200, 30)
        self.pb.setRange(0, 100)
        self.pb.setValue(0)
        self.pb.setOrientation(Qt.Horizontal)
        self.pb.setFormat('%p%')

        self.label91 = QLabel('Author: Keran Li', self)
        self.label91.setGeometry(300, 260, 200, 30)
        self.label91.setStyleSheet('font-size: 15pt; font-weight: bold; border: 2px solid black;')

        self.figure = plt.figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(10, 310, 780, 280)

        self.btn51 = QPushButton('开始分析', self)
        self.btn51.clicked.connect(self.data_analysis)
        self.btn51.setGeometry(350, 610, 100, 30)

    def select_file(self):
        self.selectTxts = FileSelector.selectTxts(self)

    def data_analysis(self):
        self.data_analysis = Normalization.data_analysis(self)