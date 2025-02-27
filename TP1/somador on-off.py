#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python somador_on-off.py <texto>")
        sys.exit(1)
    
    # Junta todos os argumentos (exceto o nome do script) numa única string
    texto = " ".join(sys.argv[1:])
    
    total = 0         # Soma acumulada
    estado = True     # True significa "ligado" (on), False "desligado" (off)
    i = 0
    numero_atual = "" # Para acumular dígitos de uma sequência

    while i < len(texto):
        c = texto[i]
        
        # Se o carácter for dígito, acumula-o e imprime-o
        if c.isdigit():
            numero_atual += c
            sys.stdout.write(c)
            i += 1
            continue
        else:
            # Se terminou uma sequência numérica, converte-a em inteiro e soma (se estiver ligado)
            if numero_atual:
                if estado:
                    total += int(numero_atual)
                numero_atual = ""
            
            # Se encontrar o carácter '=', imprime-o e o total acumulado até então
            if c == "=":
                sys.stdout.write("=")
                i += 1
                sys.stdout.write("\n>> " + str(total))
                continue
            
            # Verifica se encontra "Off" (3 caracteres) em qualquer combinação de maiúsculas/minúsculas
            if i <= len(texto) - 3 and texto[i:i+3].lower() == "off":
                sys.stdout.write(texto[i:i+3])
                estado = False
                i += 3
                continue
            
            # Verifica se encontra "On" (2 caracteres) em qualquer combinação de maiúsculas/minúsculas
            if i <= len(texto) - 2 and texto[i:i+2].lower() == "on":
                sys.stdout.write(texto[i:i+2])
                estado = True
                i += 2
                continue
            
            # Caso contrário, apenas imprime o carácter atual
            sys.stdout.write(c)
            i += 1
    
    # Se houver uma sequência numérica pendente no final, processa-a
    if numero_atual:
        if estado:
            total += int(numero_atual)
    
    # Imprime o total final
    sys.stdout.write("\n>> " + str(total))

if __name__ == "__main__":
    main()
