import unittest
from unittest import mock

from pip._internal.utils.misc import captured_stdout
from requests.exceptions import HTTPError
import os
import main as m

class TestGetId(unittest.TestCase):
    # IDが環境変数に存在しない場合はNoneが返る
    def test_none(self):
        # IDという環境変数があれば削除する
        os.environ.pop('ID', None)
        self.assertEqual(m.get_id(), None)

    # IDが存在する場合はそのまま返す
    def test_id(self):
        os.environ['ID'] = 'testid'
        self.assertEqual(m.get_id(), 'testid')

class TestGetPassword(unittest.TestCase):
    # PASSWORDが環境変数に存在しない場合はNoneが返る
    def test_none(self):
        # PASSWORDという環境変数があれば削除する
        os.environ.pop('PASSWORD', None)
        self.assertEqual(m.get_password(), None)

    # PASSWORDが存在する場合はそのまま返す
    def test_password(self):
        os.environ['PASSWORD'] = 'hogepiyo*$#'
        self.assertEqual(m.get_password(), 'hogepiyo*$#')

class TestGetMastodonUrl(unittest.TestCase):
    # MASTODON_URLが環境変数に存在しない場合はNoneが返る
    def test_none(self):
        # MASTODON_URLという環境変数があれば削除する
        os.environ.pop('MASTODON_URL', None)
        self.assertEqual(m.get_mastodon_url(), None)

    # MASTODON_URLが存在する場合はそのまま返す
    def test_password(self):
        os.environ['MASTODON_URL'] = 'http://test.mastodon.com'
        self.assertEqual(m.get_mastodon_url(), 'http://test.mastodon.com')

class TestGetKafkaUrl(unittest.TestCase):
    # KAFKA_URLが環境変数に存在しない場合はNoneが返る
    def test_none(self):
        # KAFKA_URLという環境変数があれば削除する
        os.environ.pop('KAFKA_URL', None)
        self.assertEqual(m.get_kafka_url(), None)

    # KAFKA_URLが存在する場合はそのまま返す
    def test_password(self):
        os.environ['KAFKA_URL'] = 'kafka.test.com:9092'
        self.assertEqual(m.get_kafka_url(), 'kafka.test.com:9092')

class TestGetKafkaTopic(unittest.TestCase):
    # KAFKA_TOPICが環境変数に存在しない場合はNoneが返る
    def test_none(self):
        # KAFKA_TOPICという環境変数があれば削除する
        os.environ.pop('KAFKA_TOPIC', None)
        self.assertEqual(m.get_kafka_topic(), None)

    # KAFKA_TOPICが存在する場合はそのまま返す
    def test_password(self):
        os.environ['KAFKA_TOPIC'] = 'test_topic'
        self.assertEqual(m.get_kafka_topic(), 'test_topic')

class TestKafkaToot(unittest.TestCase):
    # idがNoneの場合はエラー表示
    def test_id_none(self):
        with captured_stdout() as stdout:
            id = None
            password = 'hogepiyo*$#'
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = 'kafka.test.com:9092'
            kafka_topic = 'test_topic'
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: ID env is not defined.')

    # passwordがNoneの場合はエラー表示
    def test_password_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = None
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = 'kafka.test.com:9092'
            kafka_topic = 'test_topic'
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: PASSWORD env is not defined.')

    # mastodon_urlがNoneの場合はエラー表示
    def test_mastodon_url_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = 'hogepiyo*$#'
            mastodon_url = None
            kafka_url = 'kafka.test.com:9092'
            kafka_topic = 'test_topic'
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: MASTODON_URL env is not defined.')

    # kafka_urlがNoneの場合はエラー表示
    def test_kafka_url_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = 'hogepiyo*$#'
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = None
            kafka_topic = 'test_topic'
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: KAFKA_URL env is not defined.')

    # kafka_topicがNoneの場合はエラー表示
    def test_kafka_topic_none(self):
        with captured_stdout() as stdout:
            id = 'testid'
            password = 'hogepiyo*$#'
            mastodon_url = 'http://test.mastodon.com'
            kafka_url = 'kafka.test.com:9092'
            kafka_topic = None
            m.kafka_toot(id, password, mastodon_url, kafka_url, kafka_topic)
            lines = stdout.getvalue().splitlines()
            self.assertEqual(lines[0], 'ERROR: KAFKA_TOPIC env is not defined.')

if __name__ == '__main__':
    unittest.main()
