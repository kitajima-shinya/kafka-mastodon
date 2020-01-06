# kafka-mastodon

指定したkafkaのtopicをconsumeし，その内容をMastodonに投稿する

Subscribeするtopicはコンマ区切りで複数指定できる

MASTODON_URLを変更する際は，以下のpytooter_clientcred.secretも再度生成する必要がある

## pytooter_clientcred.secretの生成

```
# python
>>> from mastodon import Mastodon
>>> Mastodon.create_app("アプリ名", api_base_url = "http://mstdn.****", to_file = "pytooter_clientcred.secret")
```

起動時に作成したpytooter_clientcred.secretを/usr/src/app/pytooter_clientcred.secretにマウントする必要がある

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
# docker run --name kafka-mastodon -e ID=**** -e PASSWORD=**** -e MASTODON_URL=http://mstdn.**** -e KAFKA_URL=kafka.****:9092 -e KAFKA_TOPICS=test,topic -d harbor.neko.flab.fujitsu.co.jp:9000/kitajima/kafka-mastodon -v ./pytooter_clientcred.secret:/usr/src/app/pytooter_clientcred.secret
```
