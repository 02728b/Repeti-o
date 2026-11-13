#condicional multipla 
lanche = 0 
combo = 0
qtde = 0
valor = 0
acom = 0
bebi = 0
print('programa lanchonete')
print("")
combo = int(input("digite o número do combo: "))    
match combo:
   case 1:
      print("X-salada - R$ 24.99")
      qtde = int (input("quantas unidades deseja? "))
      valor =float (qtde * 24.99 )
   case 2:
      print("X-Egg - R$ 120")
      qtde = int(input("quantas unidades deseja"))
      valor =float (qtde * 19.99)
   case 3:
      print("X-Picanha - R$ 1300 ")
      qtde = int(input("quantas unidades deseja"))
      valor = float (qtde * 27.99) 
   case _:
      print("Opção invalida! Tente novamente")

sim_Nao = print (input(" quer escolher alguma bebida ?"))
if sim_Nao == 'Sim':
 bebi = int (input('digite o numero do seu combo'))
 match bebi: 
    case 1:
        print("Coca cola - R$ 8.99")
        qtde = int (input("quantas unidades deseja? "))
        valor = float (qtde * 8.99)
    case 2 :
      print("Pepsi - R$ 8.99")
      qtde
else:
 print('inv')

sim = str (input("vai querer acompanhamento ?"))
if (sim == sim):
  acom = int(input("Digite qual acompanhamento vai querer:"))
  match acom :
      case 1:
        print("Bata palha pequena - R$ 5")
        qtde =int(input("qual a quantidade de batatas"))
        valor = float (qtde * 5 )








