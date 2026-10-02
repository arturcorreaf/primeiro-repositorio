# Conversor de Medidas EU-US

opcao=""

while opcao!=0:
  opcao = int(input(
    "=== CONVERSOR DE MEDIDAS EU-US ===\n\n"
    "1 - Metros para pés\n"
    "2 - Quilômetros para milhas\n"
    "3 - Quilo para Libra\n"
    "4 - Celsius para Fahrenheit\n"
    "0 - Sair\n\n"
    "Escolha uma opção: "
  ))
  if opcao == 1:
    n=float(input("\nQuantos metros? "))
    calc=n*3.28
    print(f"\n{calc} pés. \n")
  if opcao == 2:
    n=float(input("\nQuantos quilômetros? "))
    calc=n*0.62
    print(f"\n{calc} milhas. \n")
  if opcao == 3:
    n=float(input("\nQuantos quilos? "))
    calc=n*2.20
    print(f"\n{calc} libras. \n")
  if opcao == 4:
    n=float(input("\nQuantos graus celsius? "))
    calc=(n*9/5) + 32
    print(f"\n{calc} °F. \n")

print("Saindo...")
