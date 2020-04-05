from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    print("\n\nType \"quit\" to exit")
    print("Enter message to be sent:")
    message = input()

    if message == "quit":
        print("Exiting...")
        break
    producer.send('testong', message.encode('utf-8'))
    print("Sending message \"{}\"".format(message))
    print("Message sent!")
