'''
Author: magictomagic
Date: 2020-11-19 23:40:37
LastEditors: magictomagic
LastEditTime: 2020-11-20 16:38:09
Description: file content
'''
# -*- coding: utf-8 -*-
import time
import webbrowser

from PyQt5.QtCore import QSize, QPoint, Qt
from PyQt5.QtGui import QMouseEvent, QMovie, QCursor
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMenu, qApp
from psutil import net_io_counters #net_io_counters 网络输入与输出 如果需要获取单个网卡的io信息，加上pernic=True参数。
from threading import Thread
import sys
from qtpy import QtWidgets, QtCore


class Main(QWidget):
  _startPos = None
  _endPos = None
  _isTracking = False
  all_bytes=0
  about = "监控电脑网络的上传跟下载网速。\n统计网络使用总流量！\n作者：旋凯凯旋"

  def __init__(self):
    super().__init__()
    self._initUI()
    # with open('流量使用情况.txt', 'r') as f:
    #   self.all_bytes = int(f.read())

  def _initUI(self):
    self.setFixedSize(QSize(259, 270))
    self.setWindowFlags(Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | Qt.Tool) 

    self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明

    self.label = QtWidgets.QLabel(self)
    self.label.setGeometry(QtCore.QRect(0, 0, 259, 111))
    self.label.setMinimumSize(QtCore.QSize(259, 111))
    self.label.setBaseSize(QtCore.QSize(259, 111))
    self.label.setStyleSheet("font: 75 20pt \"Adobe Arabic\";color:rgb(255,0,0)")
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    self.label.setObjectName("label")

    self.label2 = QtWidgets.QLabel(self)
    self.label2.setGeometry(QtCore.QRect(10, 110, 259, 161))
    self.label2.setMinimumSize(QtCore.QSize(259, 161))
    self.label2.setBaseSize(QtCore.QSize(259, 161))
    self.label2.setAlignment(QtCore.Qt.AlignCenter)
    self.gif = QMovie('1271.gif')
    self.label2.setMovie(self.gif)
    self.label2.setObjectName("label2")
    self.gif.start()

    self.timer = QtCore.QTimer(self)
    self.timer.start(1000)
    # self.timer.timeout.connect(self.start)

    self.setCursor(QCursor(Qt.PointingHandCursor))

    self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Main()
#   sys.exit(app.exec_())