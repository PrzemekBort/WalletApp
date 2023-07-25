from PyQt6.QtWidgets import QWidget
from src.gui.interfaces.assetWidgetInterface import Ui_Form


class AssetWidget(QWidget):

    def __init__(self, assetObject):
        super(AssetWidget, self).__init__()
        self.assetObject = assetObject
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.nameLabel.setText(str(self.assetObject.name))
        self.ui.quantityLabel.setText(str(self.assetObject.quantity))
        self.ui.pricelabel.setText(str(self.assetObject.currentValue))
        self.ui.profitLabel.setText(str(self.assetObject.profitValue))

