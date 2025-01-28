# Database

## 言語

- SQL

## Relational Database(RDB): 安定向け

- 特徴
  - 強み: SQL で複雑なクエリが可能, トランザクションによる一貫性
  - 弱み: 可用性の確保が難しい, スケーラビリティの確保が難しい
- ランキング
  - [PostgreSQL](https://www.postgresql.org/)
    - OSS
  - [MySQL](https://www.mysql.com/jp/)
    - OSS, Oracle 製
  - [SQLite](https://www.sqlite.org/)
    - OSS
  - [Microsoft SQL Server](https://www.microsoft.com/ja-jp/sql-server/sql-server-downloads)
    - Microsoft 製
  - [MariaDB](https://mariadb.org/)
    - OSS, MySQL 派生
  - [Oracle Database](https://www.oracle.com/jp/database/)
    - Oracle 製
  - [Supabase](https://supabase.com/)
    - OSS, PostgreSQL 基盤, Firebase 代替

## Not Only SQL(NoSQL): 大規模データ向け

- 特徴
  - 強み: 可用性が高い, スケーラビリティが高い
  - 弱み: 複雑なクエリ/関係が難しい, 一貫性が弱い
- ランキング
  - [MongoDB](https://www.mongodb.com/ja-jp)
    - OSS, ドキュメント型
  - [Redis](https://redis.io/)
    - OSS, キーバリューストア型
  - [DynamoDB](https://aws.amazon.com/jp/dynamodb/)
    - Amazon 製
  - [Firebase Realtime Database](https://firebase.google.com/docs/database?hl=ja)
    - Google 製
  - [Cloud Firestore](https://firebase.google.com/docs/firestore?hl=ja)
    - Google 製, Google 推奨はこちら
  - [Azure Cosmos DB](https://azure.microsoft.com/ja-jp/products/cosmos-db)
    - Microsoft 製

## NewSQL: 大規模データもできる分散 SQL

- 特徴
  - 強み: 可用性が高い, スケーラビリティが高い, SQL あり, 一貫性あり
  - 弱み: 構成が複雑, 高価
- ランキング
  - [CockroachDB](https://www.cockroachlabs.com/)
    - OSS

## その他

- [Elasticsearch](https://www.elastic.co/jp/elasticsearch)
  - OSS, 分散型 RESTful 検索・分析エンジン
- [BigQuery](https://cloud.google.com/bigquery?hl=ja)
  - Google 製, AI 用分析プラットフォーム
- [Microsoft Access](https://www.microsoft.com/ja-jp/microsoft-365/access)
  - Microsoft 製, SQL Server に似ている

## 参考

- [Stack OverFlow Survey 2024](https://survey.stackoverflow.co/2024/technology)
