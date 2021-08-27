"""
- Filther methods

Características:

    * No usa algoritmos de Machine Learning.
    * Agnóstico al modelo.
    * Es menos costoso es términos computacionales.
    * Son adecuados para eliminar rápidamente características irrelevantes.

Pasos:

    * Clasifique las características de acuerdo con cierto criterio.
        * Cada característica se clasifica independientemente del espacio de características.
    * Seleccione las características de mayor rango.

Estos métodos pueden seleccionar variables redundantes porque no consideran las relaciones entre características.

Criterios:

    * Chi-Cuadrado - Fisher Score.
    * Pruebas univariadas parametricas.
    * Información mutua.
    * Varianza (características constantes o cuasi-constantes)

- Wrapper methods

Características:

    * Utiliza modelos predictivos para puntuar un subconjunto de características.
    * Entrena un nuevo modelo en cada subconjunto de características.
    * Son costosos computacionalmente.
    * Por lo general, proporciona el subconjunto de características de mejor rendimiento para un algoritmo determinado.
    * Posiblemente no produzca la mejor combinación de características para un modelo ML diferente.

Estos métodos detectan relaciones entre las variables. Adicional encuentran el mejor subconjunto de características para el clasificador deseado.

Pasos:

    * Busca un subconjunto de características.
    * Construye un modelo usando un algoritmo de Machine Learning en el subconjunto de características seleccionado.
    * Evalúa el desempeño del modelo.
    * Repite.

Búsqueda:

1. Forward selection, agrega una característica a la vez.
2. Backward selection, elimina una característica a la vez.
3. Exhaustive search, busca entre todas las combinaciones posibles de características.

Stoping:

    * Aumenta el rendimiento del modelo(Forward).
    * Disminuye el rendimiento del modelo (Backward).
    * Alcanza el número de características definido (Exhaustive).

Los criterios de stoping suelen ser muy arbitrarios. Deben ser definidos por cada usuario.

- Embedded methods

Características:

    * Realiza la selección de características como parte del proceso de construcción del modelo.
    * Considera la interacción entre características y modelos.
    * Son menos costosos computacionalmente que los métodos wrapper, porque se ajustan al modelo ML solo una vez.

Pasos:

    * Entrenar un modelo usando un algoritmo de Machine Learning.
    * Derivar la importancia de las características.
    * Eliminar las características no importantes.
"""