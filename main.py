import os
# pip install kafka-python
from kafka import KafkaConsumer
# pip install Mastodon.py
from mastodon import Mastodon

def get_id():
    if 'ID' in os.environ:
        id = os.getenv('ID')
        return id
    else:
        return None

def get_password():
    if 'PASSWORD' in os.environ:
        password = os.getenv('PASSWORD')
        return password
    else:
        return None

def get_mastodon_url():
    if 'MASTODON_URL' in os.environ:
        mastodon_url = os.getenv('MASTODON_URL')
        return mastodon_url
    else:
        return None

def get_kafka_url():
    if 'KAFKA_URL' in os.environ:
        kafka_url = os.getenv('KAFKA_URL')
        return kafka_url
    else:
        return None

def get_kafka_topic():
    if 'KAFKA_TOPIC' in os.environ:
        kafka_topic = os.getenv('KAFKA_TOPIC')
        return kafka_topic
    else:
        return None

def login(id, password, mastodon_url):
    mastodon = Mastodon(
        client_id = 'pytooter_clientcred.secret',
        api_base_url = mastodon_url
    )
    mastodon.log_in(
        id,
        password,
        to_file='pytooter_usercred.secret'
    )
    return mastodon

def kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic):
    if id != None and password != None and mastodon_url != None and kafka_url != None and kafka_topic != None:
        consumer = KafkaConsumer(kafka_topic, bootstrap_servers=kafka_url)

        login(id, password, mastodon_url)
        mastodon = Mastodon(
            access_token='pytooter_usercred.secret',
            api_base_url=mastodon_url
        )

        for msg in consumer:
            print(msg.value)
            mastodon.toot(msg.value)

    if id == None:
        print('ERROR: ID env is not defined.')
    if password == None:
        print('ERROR: PASSWORD env is not defined.')
    if mastodon_url == None:
        print('ERROR: MASTODON_URL env is not defined.')
    if kafka_url == None:
        print('ERROR: KAFKA_URL env is not defined.')
    if kafka_topic == None:
        print('ERROR: KAFKA_TOPIC env is not defined.')

def main():
    id = get_id()
    password = get_password()
    mastodon_url = get_mastodon_url()
    kafka_url = get_kafka_url()
    kafka_topic = get_kafka_topic()

    kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic)

if __name__ == '__main__':
    main()