class Cachorro:
  def __init__(self, nome, idade):
    self.nome  = nome;
    self.idade = idade;
  
  def latir(self):
    print(f"{self.nome} está latindo!");
  
  def anos(self):
    print(f"{self.nome} está latindo e tem {self.idade} anos");
  
  def fome(self):
    print(f"{self.nome} está com fome");    


cachorro1 = Cachorro("Max", 3);
cachorro2 = Cachorro("Melissa", 9);

cachorro1.latir();

cachorro2.latir();
print("");

cachorro1.anos();

cachorro2.fome();