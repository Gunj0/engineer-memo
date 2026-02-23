# RDS

- Relational Database Service
  - マネージドRDBサービス
  - 自動バックアップ、スケーリング、パッチ適用などの管理機能を提供
  - マルチAZ配置やリードレプリカなどの高可用性オプションも利用可能
  - VPCに配置する必要がある
- RDSとは別に、NoSQLのDynamoDBやElastiCacheなども提供されている

## 対応DBMS

- MySQL
- PostgreSQL
- MariaDB (MySQL互換のオープンソースRDBMS)
- Oracle Database
- Microsoft SQL Server
- Amazon Aurora (AWS独自のRDBMS, MySQL互換とPostgreSQL互換の2種類がある)
  - AWSに最適化されているためMySQLやPostgreSQLよりも高性能

## RDSクラス

- サイズ
  - micro 〜 16xlarge
- ファミリー例
  - db.m5: 汎用インスタンスタイプ
  - db.t3: バースト可能な汎用インスタンスタイプ
  - db.r5: メモリ最適化インスタンスタイプ

## 料金

- インスタンス料金(ライセンス込み)
- ストレージ料金
- データ転送量
  - VPC内のデータ転送量は無料
- オプション(バックアップストレージ、リードレプリカなど)
