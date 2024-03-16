# yuru-bot
discord用便利bot

## Cording rule
PEP: 8
> https://pep8-ja.readthedocs.io/ja/latest/

## Setting dev
1. VSCodeの拡張機能で Black Formatter をインストール
2. VSCodeの拡張機能で Flake8 をインストール

## 実行前に`.env`を設定
カレントディレクトリに`.env`ファイルを用意し、以下の値を設定する
```
TOKEN=botのtoken
ENTRY_EXIT_MONITOR_VOICE_CHANNEL_ID=監視するボイスチャンネルID
ENTRY_EXIT_MONITOR_NOTIFICATION_CHANNEL_ID=ボイスチャンネル入退室を通知するチャンネルID
WEATHER_NOTIFICATION_CHANNEL_ID=天気予報を通知するチャンネルID
```

## Launching the development environment
```
docker compose up
```
