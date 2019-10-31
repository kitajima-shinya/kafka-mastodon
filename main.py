import os
# pip install kafka-python
from kafka import KafkaConsumer
# pip install Mastodon.py
from mastodon import Mastodon

def get_topic_list():
    if 'KAFKA_TOPICS' in os.environ:
        kafka_topics = os.getenv('KAFKA_TOPICS')
        topic_list = [x.strip() for x in kafka_topics.split(',')]
        return topic_list
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

def kafka_toot(id, password, mastodon_url, kafka_url, topic_list):
    if id != None and password != None and mastodon_url != None and kafka_url != None and topic_list != None:
        consumer = KafkaConsumer(bootstrap_servers=kafka_url)
        consumer.subscribe(topic_list)

        login(id, password, mastodon_url)
        print('Login completed.')

        mastodon = Mastodon(
            access_token='pytooter_usercred.secret',
            api_base_url=mastodon_url
        )

        print('Start subscribing...')
        print('Subscribing topics: ')
        print(topic_list)

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
    if topic_list == None:
        print('ERROR: KAFKA_TOPICS env is not defined.')

def main():
    id = os.getenv('ID', None)
    password = os.getenv('PASSWORD', None)
    mastodon_url = os.getenv('MASTODON_URL', None)
    kafka_url = os.getenv('KAFKA_URL', None)
    topic_list = get_topic_list()

    kafka_toot(id, password, mastodon_url, kafka_url, topic_list)

if __name__ == '__main__':
    main()