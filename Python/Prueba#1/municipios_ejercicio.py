def menu_principal():
    input("Presione ENTER para continuar: ")
    print("\n==========================")
    print("==== MENÚ DE OPCIONES ====")
    print("==========================\n")
    print('A. Registro de datos')
    print('B. Municipio que mas toneladas/día genera')
    print('C. Municipio que menos toneladas/día genera')
    print('D. Promedio de toneladas de basura/día')
    print('E. Promedio de toneladas de basura/mes')
    print('F. Mayor problema ambiental.')
    print('G. Menor problema ambiental.')
    print('H. Promedio de olores ofensivos')
    print('I. Promedio de creación asentamientos ilegales')
    print('J. Promedio de contaminación de Corrientes hídricas')
    print('K. Terminar')
    
# def municipios_llenos():
#     return [{"nombre":'Bello','toneladas':15, 'Porcentaje': {'Olores':59,'asentamientos': 21, 'hidricas': 20}}
#             {'nombre':'Medellin','toneladas':35, 'Porcentaje': {'Olores':45,'asentamientos': 10, 'hidricas': 45}}
#             {'nombre':'Envigado','toneladas':19, 'Porcentaje': {'Olores':30,'asentamientos': 15, 'hidricas': 55}}]
    
def registro_de_datos(municipios):
    
    nombre = input('Ingrese el nombre del municipio: ')
    toneladas = int(input('Ingrese la cantidad de toneladas que genera el municipia a diario: '))
    olores = int(input('Ingrese el porcentaje de afectacion respecto a olores: '))
    asentamientos = int(input('Ingrese el porcentaje de afectacion respecto a asentamientos ilegales: '))
    hidricas = int(input('Ingrese el porcentaje de afectacion respecto a contaminacion de corrientes hidricas: '))
    
    municipio={'nombre':nombre, 'toneladas': toneladas, 'porcentajes':{'olores':olores,'asentamientos':asentamientos,'hidricas':hidricas}}
    #agregar un diccionario al una lista
    municipios.append(municipio)
    print('El municipio fue ingresado con exito!')

def municipios(municipios):
    municipio_max=''
    contaminacion_mayor=''
    
    if municipios:
        for i in municipios:
            for j in 
    
    
        '
    
    if municipios.
    
    

def main():
    while True:
        #municipios=municipios_llenos()
        municipios1=[]

        menu_principal()

        opcion=input('Ingrese una opcion: ').upper()
        opcion.upper()
        if opcion=='A':
            registro_de_datos(municipios1)
        elif opcion=='B':
            toneladas(municipios1)




        elif opcion=='K':
            print('Bye')
            break
    
main()
    
    