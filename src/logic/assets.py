from abc import abstractmethod


class Asset:

    def __init__(self, ID, assetType, name, quantity, buyPrice, buyDate):
        self._ID = ID
        self._assetType = assetType
        self.name = name
        self.quantity = quantity
        self.buyPrice = buyPrice
        self.buyDate = buyDate

        self.currentValue = None
        self.percentageValue = None
        self.profitValue = None
        self.currentExchangeRate = None

    @abstractmethod
    def updateCurrentValue(self):
        pass

    @abstractmethod
    def updatePercentageValue(self):
        pass

    def getProfitValue(self):
        currentValue = self.updateCurrentValue()
        return currentValue - self.buyPrice


class CryptoAsset(Asset):

    def __init__(self, ID, assetType, name, quantity, buyPrice, buyDate='00-00-0000'):
        super(CryptoAsset, self).__init__(ID, assetType, name, quantity, buyPrice, buyDate)

    def updateCurrentValue(self):
        pass  # TODO Implement

    def updatePercentageValue(self):
        pass  # TODO Implement
