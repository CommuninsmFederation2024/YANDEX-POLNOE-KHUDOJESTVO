# приуэт началника ми усе делали кака ты сказати. тоби ми уси ради
# пасиба начальника. храни тебе господь
import sys
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
import requests

class MainWindow(QMainWindow):
  g_map: QLabel
  def __init__(self):
    super().__init__()
    uic.loadUi('untitled.ui', self)
    self.spn = 0.00001
    self.zoom = 5
    self.ll = [37.977751, 55.757718]
    self.typemap = 'map'
    self.key = ''
    
  def show_map(self):
    map_params = {
      'll': ','.join(map(str, self.ll)),
      'l': self.typemap,
      'z': self.zoom
    }
    response = requests.get('http://static-maps.yandex.ru/1.x/',
                  params=map_params)
    with open('tmp.png', mode='wb') as tmp:
      tmp.write(response.content)
    pixmap = QPixmap()
    pixmap.load('tmp.png')
    self.g_map.setPixmap(pixmap)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
