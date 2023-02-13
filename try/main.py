try: 
    valor = int(input('Informe um valor a ser dividido por 1: '))
    resultado = 1 / valor
    print(f'resultado: {resultado}')

except ZeroDivisionError:
    raise Exception('O valor informado não pode ser 0')

except TypeError:
    raise Exception('Informe um valor inteiro')

except ValueError:
    raise Exception('Informe um valor inteiro')

except Exception:
    raise Exception('Erro indefinido encontrado')

finally:
    print('Nome: Luiz Antônio Marques Junior')