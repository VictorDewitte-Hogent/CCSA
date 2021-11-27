class BankRekening:
    
    def __init__(self,a,b,c) :
        self.Name= a
        self.RekeningNummer = b
        self.Amount = c
    def storten(self,bedrag):
        self.Amount+=bedrag
    def afhalen(self,bedrag):
        self.Amount-=bedrag
    def __repr__(self):
        pass
    def __str__(self):
        return (str(f"{self.Name}, {self.RekeningNummer}, bedrag : {self.Amount}"))   
