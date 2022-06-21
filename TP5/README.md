# Sistemas de inteligencia artificial

## TP5: Deep learning - Autoencoders

### Instituto Tecnológico de Buenos Aires (ITBA)

### Autores

- [Ana Cruz](https://github.com/anitacruz) - Legajo 60476
- [Agustín Spitzner](https://github.com/aspitzner) - Legajo 60142
- [Camila Borinsky](https://github.com/camilaborinsky) - Legajo 60083

### Ejecución

#### Dependencias

Para la ejecución se requiere de al menos Python 3 y de pip<br>

```
pip install -r requirements.txt
```

En `/resources/config.json` pueden elegirse las configuraciones para el autoencoder. <br>

- font_numbers: Se pueden utilizar hasta 3 fuentes para entrenar, 1 de símbolos y dígitos, 1 de letras mayúsculas y 1 de letras minúsculas.
- trainig_sample: Número entre 0 y 1 que representa la fracción de datos que se utilizan para entrenar a la red. Esta muestra es elegida aleatoriamente.
- architectures: lista de arquitecturas de capas ocultas a ser probadas por el comparador de arquitecturas. Notar que se trata de la arquitectura de la mitad de la red, que luego se duplica y revierte para que sea un autoencoder.
- momentum: vale `true` si quiere ejecutarse con momentum y `false` en caso contrario.
- update_learn_rate: vale `true` si quiere utilizarse una tasa de aprendizaje adaptativa y `false` en caso contrario.
- epoch_limit: límite de épocas para la red, y en caso de que se utilice un optimizador cantidad máxima de iteraciones.
- learning_rate: tasa de aprendizaje inicial
- optimizer: Nombre del optimizador a utilizar. Se siguió la convención de la librería scipy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize
- optimizers: vector de nombres de optimizadores a ser utilizados por el comparador de optimizadores.
- arquitecture: arquitectura de capas ocultas de la parte del encoder para cuando no se ejecuta el comparador de arquitecturas.
- denoising: configuración para cuando se quiere usar el DAE.
  - noise_prob: probabilidad de ruido para los caracteres
  - sample_size: Cantidad de muestras ruidosas a generar de la misma letra
  - multiple_noise_prob: vector con probabilidades de ruido a utilizar para entrenar y testear al DAE.

El TP consta de 5 notebooks que se encuentran en la raíz del proyecto

- `autoencoder.ipynb`: notebook para comparar las distintas arquitecturas.
- `optimizers.ipynb`: notebook para comparar los optimizadores.
- `denoising.ipynb`: notebook para ejecutar el DAE.
- `content_generation.ipynb`: notebook para entrenar a la red y generar nuevo contenido.
- `vae.ipynb`: notebook para utilizar un autoencoder variacional de una librería y analizar la generación de nuevo contenido y representación del espacio latente.
