# Manual para correr los códigos

## avocadoProductionAnalysis
Este código no utiliza interacción con el usuario, utilice su IDE preferido, el resultado son varios print que describen los datos de producción de aguacate de Nueva York, California y Charlotte

## twitterLikesRetweetsAnalysis

Este código puede ser interpretado utilizando herramientas como google Colab o en tu IDE favorito. Asegurate de incluir las librerías pandas, matplotlib y seaborn con el instalador pip/pip3 de python en caso de correr el código de manera local.

## patronesConKmeans
1. Clona el repositorio de GitHub: Primero, necesitas clonar el repositorio que contiene el código. Puedes hacer esto utilizando el comando git clone seguido de la URL del repositorio.
2. Instala las dependencias: Este código requiere las bibliotecas matplotlib, pandas y sklearn. Puedes instalar estas bibliotecas utilizando pip, el administrador de paquetes de Python. Abre tu terminal y ejecuta los siguientes comandos:
```bash
pip install -U matplotlib pandas scikit-learn
```
3. Descarga el conjunto de datos: El código requiere un archivo llamado twitter_dataset.csv en la carpeta arteDeLaAnalitica. Asegúrate de tener este archivo en la ubicación correcta.
4. Ejecuta el código: Ahora puedes ejecutar el código. Si el archivo se llama patronesConKmeans.py, puedes ejecutarlo con el siguiente comando en tu terminal:
```bash
python patronesConKmeans.py
```
5. Interpreta los resultados: El script imprimirá las primeras filas del conjunto de datos, mostrará un gráfico del método del codo para determinar el número óptimo de clusters, imprimirá los centros de los clusters y finalmente mostrará un gráfico de los clusters de retweets y likes.
