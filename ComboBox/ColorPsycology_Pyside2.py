import sys


# Just for better understanding
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import (   QWidget,
                                QMainWindow
                            )
from PySide2.QtWidgets import (   QStatusBar,
                                QToolBar
                            )
from PySide2.QtWidgets import (   QHBoxLayout,
                                QVBoxLayout,
                                QGridLayout,
                                QFormLayout
                            )
from PySide2.QtWidgets import (   QPushButton,
                                QLineEdit,
                                QLabel,
                                QComboBox
                            )
from PySide2.QtWidgets import (   QDialog,
                                QDialogButtonBox
                            )


def comboTriggered(text):
    helloMsg.setText(colorInfo[text])

colorInfo = {
    'red': 'color of energy, passion, action, ambition and determination.'
            'It is also the color of anger',
    'orange': 'color of social communication and optimism. From a negative '
            'color meaning it is also a sign of pessimism and superficiality',
    'yellow': 'yellow is the color of the mind and the intellect. It is '
                'optimistic and cheerful. However it can also suggest impatience, '
                'criticism and cowardice',
    'green': 'color of balance and growth. It can mean both self-reliance as a '
                'positive and possessiveness as a negative, among many other '
                'meanings',
    'blue': 'color of trust and peace. It can suggest loyalty and integrity as well'
                ' as conservatism and frigidity'
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()

combo = QComboBox()
for color in colorInfo:
    combo.addItem(color)
combo.activated[str].connect(comboTriggered) 
helloMsg = QLabel('---')

layout.addWidget(combo, 0, 0)
layout.addWidget(helloMsg, 1, 0)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
