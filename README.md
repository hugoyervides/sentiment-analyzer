# Proyecto Integrador #1
##### Esta actividad contiene un analizador de sentimientos utilizando el api de [twitter](https://developer.twitter.com), en base a un término de busqueda ingresado por el usuario. Reconoce los twits positivos o negativos; además de clasificarlos por ubicación geográfica.

Utilizando la librera nltk en conjunto con las librerías, el programa recibe un stream utilizando el api de twitter, realizando las busqueda de twitts por cordenada, y tokenizando el stream de salida. Despues de ello, el analizador de sentimientos clasifica el numero de comentarios positivos y negativos de cada continente. (El stream de twits varia de información por ser busqueda en tiempo real, y la cantidad varía por ubicación, se tiene un limite duro de 6,000 twits).

El código en el jupyter notebook, muestra los URLs minados, así como aquellos que son descargados. 

Consideramos en base al programa y su presentación que presentaría un buen punto de partida para aquellos interesados en desarrollar un analizador de sentimientos de twits, u bases de datos de terceras personas.

##### Representación y fuente de datos. 
Los twits utilizados son extraidos de un query desde el api de twitter con la libreria [tweepy](https://www.tweepy.org/),  y analizados por la herramienta [nltk](https://www.nltk.org/).

##### Dependencias 
1. nltk
2. tweepy

##### Algoritmo
1. Busqueda de streams de twitts por ubcación geogŕafica.

```
# Search of African twiits
twitterStream = Stream(auth, listener())
twitterStream.filter(locations=[-15.258424824,-33.8737847792,37.7103108709,36.3118596404])
```
2. Almacenar el contenido.

```

```
3. 

```

```
4. 

```

```
5. 

```

```
##### Las imagenes son graficas de humor de twitter por ubicación geográfica.
![](Numero_total.png)
![](Porcentaje.png) 
 
##### Contribuidores
* [GustavoDLRA](https://github.com/GustavoDLRA)
* [hugoyervides](https://github.com/hugoyervides)
* Astrid
* [olefran](https://github.com/olefran)
* [Felipe Villaseñor](https://github.com/Felipev201)

En caso de estar interesado en una introducción al procesamiento de lenguaje, o analizador de sentimientos:
- [NLTK Tutorial by sentdex](https://www.youtube.com/playlist?list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL)
- [Natural Language Processing Standford University Course](https://www.youtube.com/watch?v=mOAXEQevCAE&ab_channel=AutomationStepbyStep-RaghavPal)

Para aprovechar al máximo este repositorio y poder editarlo al momento de descargarlo se recomienda el uso de Jupyter Notebook mediante Anaconda: 
1. Instalar [Anaconda](https://www.anaconda.com/products/individual)
2. Instalar [nltk](https://www.nltk.org/).
3. Instalar [tweepy](https://www.tweepy.org/)
4. Remplazar la key, comsumer secret, access token y access secret en los archivos bot_\*.py (obtenido de una cuenta developer de twitter)
```
#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""
```
5. Abrir Jupyter Notebook
