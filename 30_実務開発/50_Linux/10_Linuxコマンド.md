# Linux コマンド

- Linux システムを操作するための命令
- ターミナルやシェルで実行される
- | (パイプ) を使用して複数のコマンドを組み合わせることができる
  - 例: `ls -l | grep sample`

## ディレクトリ・ファイル操作

- `ls`: ファイル一覧表示, -l: 詳細表示, -a: 隠しファイルを含める
  - `ll`: `ls -l` のエイリアス, 詳細表示
  - `la`: `ls -a` のエイリアス, 隠しファイルを含めて表示
- `cd`: ディレクトリ移動
- `pwd`: 現在のディレクトリ表示
- `mkdir`: ディレクトリ作成
- `rmdir`: ディレクトリ削除
- `touch`: ファイル作成
- `rm {ファイル名}`: ファイル削除
- `cp {コピー元} {コピー先}`: ファイルコピー
- `mv {移動元} {移動先}`: ファイル移動, 名前変更
- `cat {ファイル名}`: ファイル内容表示
- `grep {検索文字列} {ファイル名}`: ファイル検索
- `chmod {権限} {ファイル名}`: ファイル権限変更
  - 例: `chmod 400 sample.pem` : 読み取り専用に設定

## 通信

- `ping {ホスト名}`: ネットワーク接続確認
- `curl {URL}`: HTTPリクエスト送信, レスポンス表示
- `wget {URL}`: ファイルダウンロード
- `scp {localファイル} {ユーザー名}@{ホスト名}:{リモートパス}`: ファイル送信
  - 例: `scp -i sample.pem sample.pem ec2-user@10.XX.XX.XX:/home/ec2-user/`
    - sample.pem で ssh ログインして sample.pem をリモートの /home/ec2-user/ にコピー

## 設定

- `source {ファイル名}`
  - シェルスクリプト実行
  - 例: `source ~/.bashrc` : .bashrc を再読み込み

## システムリソース管理

- `systemctl`
  - サービス管理コマンド
  - `sudo systemctl start httpd` で httpd サービスを起動
  - `sudo systemctl stop httpd` で httpd サービスを停止
  - `sudo systemctl status httpd` で httpd サービスの状態を確認
- `top`
  - CPU 利用率等のシステムリソース一覧表示
- `free`
  - メモリ使用率, mac にはない
- `ps`
  - 起動中のプロセス表示
- `yes | {コマンド}`
  - "y"を無限に出力してコマンドに入力する
    - 例: `yes | sudo apt-get install -y {パッケージ名}` で確認プロンプトを自動で "y" と答える
  - `yes > /dev/null &` で CPU に負荷をかけることもできる
    - `> /dev/null` は出力を捨てるための特殊ファイル, `&` はバックグラウンド実行するための記号
    - `jobs` でバックグラウンドジョブの一覧表示, `kill %1` でジョブを停止

## OS設定

- `hostnamectl`
  - ホスト名設定
  - 例: `sudo hostnamectl set-hostname sample-server` でホスト名を sample-server に変更
- `timedatectl`
  - タイムゾーン設定
  - 例: `sudo timedatectl set-timezone Asia/Tokyo` でタイムゾーンを東京に変更
- `localectl`
  - ロケール設定
  - 例: `sudo localectl set-locale LANG=ja_JP.UTF-8` でロケールを日本語に変更
  - 例: `sudo localectl status` で現在のロケール設定を確認

## リモート接続

- `ssh -i {秘密鍵ファイル.pem} {ユーザー名}@{ホスト名}`
  - リモートサーバに接続
  - 例: `ssh -i sample.pem ec2-user@ec2-xx-xx-xx-xx.compute-1.amazonaws.com`

## 履歴

- `history`
  - コマンド履歴表示
  - `!{番号}` で履歴の特定のコマンドを再実行
    - 例: `!42` で履歴の42番目のコマンドを再実行
  - `history -c` で履歴をクリア
