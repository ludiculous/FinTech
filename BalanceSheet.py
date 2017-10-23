

class Debt:

class FinObligations:

class SHequity:
  def __init__(self,invested):
    self.invested = invested

class BalanceSheet:
  def __init__(self, liabilities, equity):
    self.liabilities = liabilities
    self.equity = equity
  
  def getAsset(self):
    self.assets = self.liabilities + self.equity
    return self.assets

  def getNetWorth(self):