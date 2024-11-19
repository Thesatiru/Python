quantidade_sim = 0
quantidade_nao = 0
mulher_sim = 0
homem_nao = 0
N = int(input("Quantas pessoas serão entrevistadas? |"))
for i in range(N):
    pesquisa = int(input("Por favor nos de sua opnião!\nLançamos a nova coca-cola de óreo em nosso mercado.\nVocê gostou deste produto?\n1.SIM 2.NÃO "))
    if pesquisa != 1 and pesquisa != 2:
        print("só vai de 1 a 2")
        break
    elif pesquisa == 1:
        quantidade_sim += 1
        sexos = (input("Qual seu gênero?\n(M)Masculino (F)Feminino | ")).upper()
        if pesquisa == 1 and sexos == "F":
            mulher_sim += 1
    elif pesquisa == 2:
        quantidade_nao +=1
        sexos = input("Qual seu gênero?\n(M)Masculino (F)Feminino | ").upper()
        if pesquisa == 2 and sexos == "M":
            homem_nao += 1
print(f"Número de entrevistados que responderam 'sim': {quantidade_sim}")
print(f"Número de entrevistados que responderam 'não': {quantidade_nao}")
if quantidade_sim > 1:
  resultado_1 = print(f"Porcentagem de mulheres que gostaram: {(mulher_sim * 100)/quantidade_sim:.2f}%")
else:
    print("Porcentagem de mulheres que gostaram: 0.00%")

if quantidade_nao > 1:
  resultado_2 = print(f"Porcentagem de homens que não gostaram: {(homem_nao * 100)/quantidade_nao:.2f}%")
else:
    print("Porcentagem de homens que não gostaram: 0.00%")

