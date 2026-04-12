# Linux系ツール

## パッケージ管理

- DNF
  - RHEL系のパッケージ管理ツール
  - `sudo dnf update -y` でシステム全体を最新にする
  - `sudo dnf install {パッケージ名}` でインストール
  - `sudo dnf list installed` でインストール済みパッケージの一覧表示

## httpd

- Apache HTTP Server
- オープンソースのWebサーバソフトウェア
- HTTPプロトコルを使用してWebコンテンツを提供
- Linuxディストリビューションの多くで利用可能
  - 例:
  - `sudo dnf install httpd` でインストール
  - `sudo systemctl enable httpd` で自動起動設定
  - `sudo systemctl start httpd` で起動, `sudo systemctl stop httpd` で停止
  - `sudo systemctl status httpd` で状態確認, Active なら起動中
  - `sudo vim /etc/httpd/conf/httpd.conf` で設定ファイル編集
    - `DirectoryIndex` でトップページのファイル名指定
    - `ServerName` でサーバのホスト名指定
  - `httpd -t` で設定ファイルの文法チェック
  - `/var/www/html` がデフォルトのドキュメントルート

## PHP

- サーバサイドスクリプト言語
- Web開発に広く使用される
- Linuxディストリビューションの多くで利用可能
  - 例:
  - `sudo dnf install -y php8.4` でインストール
  - `sudo dnf install -y php-mysqlnd` で MySQL 連携モジュールもインストール
  - `php -v` でバージョン確認
  - `php -m` でインストールされているモジュールの一覧表示
  - `php -i` で PHP の設定情報を表示

## MariaDB

- MySQLのフォークでオープンソースのリレーショナルデータベース管理システム
- Linuxディストリビューションの多くで利用可能
  - 例:
  - `sudo dnf install -y mariadb mariadb-server` でインストール
  - `sudo systemctl start mariadb` で起動, `sudo systemctl enable mariadb` で自動起動設定
  - `sudo mysql`でMySQLシェルに接続, `exit` で終了
  - `sudo mysql -u root -p` でMySQLシェルに接続
  - `mysql -h {ホスト名} -u {ユーザー名} -p` でリモートの MySQL シェルに接続
