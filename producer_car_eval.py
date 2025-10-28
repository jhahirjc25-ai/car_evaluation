from kafka import KafkaProducer
import pandas as pd
import time
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv("car_evaluation.csv")

for _, row in df.iterrows():
    record = row.to_dict()
    producer.send("car-evaluations", value=record)
    print(f"🚗 Enviado: {record}")
    time.sleep(0.5)

producer.flush()
print("✅ Envío completo al topic car-evaluations")
