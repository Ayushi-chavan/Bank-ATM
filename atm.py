class ATM:
    def __init__(self,atm_card_number, pin_number,CashWithdrawl, BalanceEnquiry) :
        self.atm_card_number=atm_card_number
        self.pin_number=pin_number
        self.CashWithdrawl=CashWithdrawl
        self.BalanceEnquiry=BalanceEnquiry
        

    def display(self) :
           print('Atm card number',self.atm_card_number)
           print('Pin number',self.pin_number)
           print('Cash Withdrawl',self.CashWithdrawl)
           print('Balance Enquiry',self.BalanceEnquiry)
   
XYZ= ATM(124578,987,5000,451210)
XYZ.display() 