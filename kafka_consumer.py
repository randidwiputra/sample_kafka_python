from kafka import KafkaConsumer
import sys

consumer = KafkaConsumer('testong', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

try:
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))

except KeyboardInterrupt:
    sys.exit()