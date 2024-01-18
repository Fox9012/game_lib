from PyQt5.QtWidgets import QApplication , QWidget , QPushButton , QLabel , QVBoxLayout 
from PyQt5.QtCore import Qt
from Space_Shooter.shooter_game import start_shooter
#from Maze.maze import start_maze
def start():
    start_shooter(True)
app = QApplication([])
mw = QWidget()
mw.resize(300,100)
mw.setWindowTitle('Библиотека игр')
label = QLabel('Выберите игру')
btn_shoot = QPushButton('Space Shooter')
btn_maze = QPushButton('Tropical Maze')
line = QVBoxLayout()

line.addWidget(label, alignment=Qt.AlignCenter) 
line.addWidget(btn_shoot, alignment=Qt.AlignCenter)
line.addWidget(btn_maze, alignment=Qt.AlignCenter)

mw.setLayout(line)
btn_shoot.clicked.connect(start)
#btn_maze.clicked.connect(start_maze)
mw.show()
app.exec_()