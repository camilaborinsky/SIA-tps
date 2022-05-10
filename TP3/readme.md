# TP3: grupo 3
Integrantes:
* Ana Cruz
* Agustin Spitzner
* Camila Borinsky

## Estructura del proyecto
El proyecto se divide en cuatro partes principales. Por cada ejercicio del enunciado a resolver tenemos una carpeta que incluye las resoluciones particulares de cada ejercicio y los subíndices correspondientes. Por otro lado, tenemos las implementaciones de las distintas clases de perceptrones, todo dentro de la carpeta "perceptrons". También tenemos la carpeta utils, que contiene únicamente al archivo file_utils que tiene funciones de parseo. Por último, en el root tenemos múltiples archivos de jupiter notebook, que sirven para hacer demostraciones de las resoluciones de los distintos ejercicios y sus resultados. 

## Notebooks
El proyecto contiene tres tipos de notebooks: final, results y setup. Los cuadernos de setup son bastante simples y los creamos con el objetivo de borrar el contenido de distintos archivos de texto que usamos para ir guardando información de varias corridas. Queremos poder hacer este reset para cuando queremos abrir un espacio de corridas nuevo. Los cuadernos de nombre final_x son los responsables de correr los fragmentos de código necesarios para ejecutar las corridas del ejercicio x. Para estos hay varios casos que requieren de varias corridas de un mismo algoritmo para luego calcular promedios. Estas corridas se guardan en archivos de texto dentro de la carpeta del ejercicio correspondiente. Por ultimo los cuadernos de results son para visualizar distintos graficos relevantes de cada ejercicio. 

## Ejercicio 1
Para correr el ejercicio 1, ya sea para probar el XOR o el AND, hay que correr desde el root del proyecto (léase, estar parado en TP3) lo siguiente:
```
    python -m ex_1.main
````
Para elegir que conjunto de entrenamiento usar (Si el AND o el XOR), podemos entrar a la carpeta ex_1/resources y en el archivo config.json cambiar los parámetros necesarios. 

## Ejercicio 2
Correr el ejercicio 2 es bastante análogo al ejercicio 1, donde simplemente hay que poblar el config.json que esta dentro de la carpeta ex_2/resources y luego correr:
```
python -m ex_2.main
```
En cuanto al archivo de configuración, tenemos una variable booleana que indica si se quiere usar el método de momentum o no, un entero llamado cross_validation que sería el k de validación cruzada. Es decir, la cantidad de subconjuntos que se van a armar a partir del conjunto de entrenamiento.


## Ejercicio 3
Para el ejercicio 3, la manera ideal de conseguir los resultados es mediante el cuaderno "results_3". Anteriormente se debe cambiar el config.json dentro de la carpeta de ex_3 para indicar si el subejercicio a correr es el 2 o el 3 y cualquier otro parámetro. 


