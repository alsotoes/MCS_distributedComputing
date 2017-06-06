# MCS_distributedComputing

* Python code using "stomp.py" Python client library for accessing messaging servers using the STOMP protocol.



Queue consumer and producer (queue called *springfield*)
=======

* Generates argv (5 in the example) messages using random values from 0 to 1000

	$ python3 queue_producer.py 5  
        [+] Sending message in springfield queue  
                --> sended message 61  
                --> sended message 29  
                --> sended message 48  
                --> sended message 42  
                --> sended message 97  
                  
                  
* Reads messages in springfield queue, acts as a server and reads any unread message in the queue before the script starts.

	$ python3 queue_consumer.py 
        [+] Receiving message from springfield queue  
                --> received a message 61  
                --> received a message 29  
                --> received a message 48  
                --> received a message 42  
                --> received a message 97  
                         
                
PubSub topic based consumer and producer
=======

* Generates 100 random values from 0 to 1000 and publish, also randomly, between 3 topis (homero, bart, lisa).

	$ python3 pubsub_producer.py 100  
         [+] Publishing message 162 in lisa topic  
         [+] Publishing message 199 in bart topic  
         [+] Publishing message 892 in bart topic  
         [+] Publishing message 121 in lisa topic  
         [+] Publishing message 40 in homero topic  
         [+] Publishing message 558 in homero topic  
         [+] Publishing message 31 in homero topic  
         [+] Publishing message 688 in homero topic  
         [+] Publishing message 768 in homero topic  
         ...  
         ...  

