# Car Evaluation Streaming

Este proyecto implementa un flujo de procesamiento en tiempo real con **Apache Spark Streaming** y **Apache Kafka**, basado en el dataset **Car Evaluation**.  
El objetivo es simular la llegada continua de datos de evaluación de automóviles y analizarlos dinámicamente para determinar la clasificación más frecuente.

## Tecnologías utilizadas
- Apache Spark 3.5.3
- Apache Kafka
- Python 3
- Pandas

## Archivos principales
- `download_dataset.py` → Descarga automática del dataset desde UCI.
- `producer_car_eval.py` → Envía los datos al topic de Kafka.
- `spark_stream_car_eval.py` → Procesa los datos en tiempo real desde Kafka.

## Ejecución
1. Descargar el dataset:
   ```bash
   python3 download_dataset.py
