import ctypes

#arquivo em hexadecimal a ser ocultado
atributo_ocultar = 0x02

#DLL que permite que esse arquivo seja manipulado no SO e vire oculto 
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')

else:
    print('Arquivo não foi ocultado')
    