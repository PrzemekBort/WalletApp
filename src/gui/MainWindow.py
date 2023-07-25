from PyQt6.QtWidgets import QMainWindow
from src.gui.interfaces.MainWindowInterface2 import Ui_MainWindow
from src.gui.assetWidget import AssetWidget
from src.logic.assets import *

# TODO Rozwiązać problem braku bold na czcionce


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setupButtons()

    def _setupButtons(self):
        """
        Connects buttons signales with right actions/slots
        """
        # Left menu buttons
        self.ui.portfolioPushButton.clicked.connect(lambda: self.changePage(0, 'Portfolio'))
        self.ui.raportsPushButton.clicked.connect(lambda: self.changePage(1, 'Raports'))
        self.ui.settingsPushButton.clicked.connect(lambda: self.changePage(2, 'Settings'))

        # Portfolio page buttons
        self.ui.goldButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.ui.cryptoButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.cashButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(2))
        self.ui.sharesButton.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(3))

    def changePage(self, index: int, text: (str, None)):
        """
        Changes contentStacketWidget current page and set new text in pageTitlelabel
        :param index: new page index
        :param text: new text, if None nothing changes
        """
        self.ui.contentStackedWidget.setCurrentIndex(index)
        if text is not None:
            self.ui.pageTitleLabel.setText(text)

    def addCryptoAsset(self, valuesList: list):

        # valuesList[0]: Asset_ID, valuesList[1]: assetType, valuesList[2]: name
        # valuesList[3]: quantity, valuesList[4]: buyPrice, valuesList[5]: buyDate
        newCryptoAsset = CryptoAsset(valuesList[0], valuesList[1], valuesList[2],
                                     valuesList[3], valuesList[4], valuesList[5])
        newCryptoAsset.updateCurrentValue()

        newCryptoWidget = AssetWidget(newCryptoAsset)
        self.ui.verticalLayout_6.addWidget(newCryptoWidget)  # TODO Sprawdzić czy to dobry layout


