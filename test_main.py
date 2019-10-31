import unittest

from pip._internal.utils.misc import captured_stdout
import os
import main as m

class TestGetTopicList(unittest.TestCase):
    # KAFKA_TOPICSが環境変数に存在しない場合はNoneが返る
    def test_kafka_topics_none(self):
        # KAFKA_TOPICSという環境変数があれば削除する
        os.environ.pop('KAFKA_TOPICS', None)
        self.assertEqual(m.get_topic_list(), None)

    def test_kafka_topics_single(self):
        os.environ['KAFKA_TOPICS'] = 'test_topic'
        self.assertEqual(m.get_topic_list(), ['test_topic'])

    def test_kafka_topics_double(self):
        os.environ['KAFKA_TOPICS'] = 'test_topic, mastodon'
        self.assertEqual(m.get_topic_list(), ['test_topic', 'mastodon'])

class TestKafkaToot(unittest.TestCase):
    # idがNoneの場合はエラー表示
    def test_id_none(self):
        with captured_stdout() as stdout:
            id = None
            password = 'hogepiyo*$#'
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = 'kafka.test.com:9092'
            kafka_topics = "test_topic, mastodon"
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topics)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: ID env is not defined.')

    # passwordがNoneの場合はエラー表示
    def test_password_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = None
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = 'kafka.test.com:9092'
            kafka_topics = "test_topic, mastodon"
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topics)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: PASSWORD env is not defined.')

    # mastodon_urlがNoneの場合はエラー表示
    def test_mastodon_url_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = 'hogepiyo*$#'
            mastodon_url = None
            kafka_url = 'kafka.test.com:9092'
            kafka_topics = "test_topic, mastodon"
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topics)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: MASTODON_URL env is not defined.')

    # kafka_urlがNoneの場合はエラー表示
    def test_kafka_url_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = 'hogepiyo*$#'
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = None
            kafka_topics = "test_topic, mastodon"
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topics)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: KAFKA_URL env is not defined.')

    # kafka_topicがNoneの場合はエラー表示
    def test_kafka_topic_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = 'hogepiyo*$#'
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = 'kafka.test.com:9092'
            kafka_topics = None
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topics)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: KAFKA_TOPICS env is not defined.')

if __name__ == '__main__':
    unittest.main()
