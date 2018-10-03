import pika

#Establishes a connection with the RabbitMQ server and defines a broker(localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#Create a queue
channel.queue_declare(queue='hello')

#Exchange
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
#Message
print(" [x] Sent 'Hello World!'")
connection.close()
