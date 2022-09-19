'''class telefons():
  def __init__(self, modelis,krasa):
    self.modelis=modelis
    self.krasa=krasa
  def zvanīt(self):
    print("Zvana")
  def SutitSMS(self):
    print("Nosūtīt")

modelis=input(" ievadi modeli")
t1=telefons(modelis,"pelēka")
t1.zvanīt()
t1.SutitSMS()

class suns():
  def __init__(self,skirne,vecums,krasa):
    self.skirne=skirne
    self.vecums=vecums
    self.krasa=krasa
  def riet():
    print("reju")
  def ed():
    print("Ņam ņam")
  def sedet():
    print("sēžu")

skirne=input("skirne=")
vecums=int(input("vecums="))
krasa=input(" krāsa=")
s1=suns(skirne,vecums, krasa)
print(s1.skirne,s1.vecums,s1.krasa)
s1.riet()
s1.ed()
s1.sedet()
'''
class skolens:
  def set(self,vards,vecums,klase, skola): # metodes definēšana
    self.__vards = vards # šeit tiek izveidots slēptais lauks vards
    self.__vecums = vecums # šeit tiek izveidots slēptais lauks vecums
    self.klase=klase # šeit tiek izveidots publiskais lauks klase
    self.skola=skola # šeit tiek izveidots publiskais lauks klase

  def info(self): # metodes IZVADE definēšana
    print(self.__name,self.__age)

sk1 = skolens() # objekta izveidošana
sk1.set("Maija",12,"6d","KG")
print(sk1.__name) # nevar piekļūt slēptajam laukam, izmet kļūdu
sk1.info()