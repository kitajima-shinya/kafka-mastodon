# kafka-mastodon

指定したkafkaのtopicをconsumeし，その内容をMattermostに投稿する

## pytooter_clientcred.secretの生成

```
# python
>>> from mastodon import Mastodon
>>> Mastodon.create_app("****", api_base_url = "http://mstdn.****", to_file = "pytooter_clientcred.secret")
```

## .gitlab-ci.yml セッティング

事前に以下の変数をSetting->CI / CD->Environment variablesに定義すること

- CI_REGISTRY
- CI_REGISTRY_PASSWORD
- CI_REGISTRY_USER
- http_proxy
- https_proxy

また，GitLabとHarbor上にあらかじめユーザ名/パスワードがCI_REGISTRY_USER/CI_REGISTRY_PASSWORDとなるユーザを作成しておくこと

## dockerコンテナ実行方法

```
# docker run --name kafka-mastodon -e ID=**** -e PASSWORD=**** -e MASTODON_URL=http://mstdn.**** -e KAFKA_URL=kafka.neko.flab.fujitsu.co.jp:9092 -e KAFKA_TOPIC=mastodon -d harbor.neko.flab.fujitsu.co.jp:9000/kitajima/kafka-mastodon
```
