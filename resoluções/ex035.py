retaA = float(input('Digite o valor da reta a: '))
retaB = float(input('Digite o valor da reta b: '))
retaC = float(input('Digite o valor da reta c: '))

if retaA < retaB + retaC and retaB < retaA + retaC and retaC < retaA + retaB:
    print('\033[32mAs retas A, B e C formam um triângulo')
else:
    print('\033[31mAs retas A, B e C não formam um triângulo')
