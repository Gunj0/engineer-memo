# Database

- 主要なデータベース一覧
  - Stack Overflow Survey の人気順

## RDB: Relational Database

- Features
  - (+) ACID特性, 安定向け, 複雑なクエリ実行が可能, トランザクションによる一貫性
  - (-) 可用性の確保が難しい, スケーラビリティの確保が難しい
- [PostgreSQL](https://www.postgresql.org/)
  - OSS
- [MySQL](https://www.mysql.com/jp/)
  - OSS, Oracle 製
- [SQLite](https://www.sqlite.org/)
  - OSS
- [Microsoft SQL Server](https://www.microsoft.com/ja-jp/sql-server/)
  - Microsoft 製
- [MariaDB](https://mariadb.org/)
  - OSS, MySQL 派生
- [Oracle Database](https://www.oracle.com/jp/database/)
  - Oracle 製
- [Supabase](https://supabase.com/)
  - OSS, PostgreSQL 基盤, Firebase 代替
- [H2](https://www.h2database.com/html/main.html)
  - OSS, Java ベース, テスト用
- [Microsoft Access](https://www.microsoft.com/ja-jp/microsoft-365/access)
  - Microsoft 製, 業務アプリ向け

## NoSQL: Not Only SQL

- Features
  - (+) 大規模データ向け, 可用性が高い, スケーラビリティが高い
  - (-) 複雑なクエリ/関係が難しい, 一貫性が弱い
- [Redis](https://redis.io/)
  - OSS, キーバリューストア型
- [MongoDB](https://www.mongodb.com/ja-jp)
  - OSS, ドキュメント型
- [DynamoDB](https://aws.amazon.com/jp/dynamodb/)
  - Amazon 製, キーバリューストア型, サーバレス
- [Cloud Firestore](https://firebase.google.com/docs/firestore?hl=ja)
  - Google 製, ドキュメント型
- [Firebase Realtime Database](https://firebase.google.com/docs/database?hl=ja)
  - Google 製, リアルタイムデータベース
- [Azure Cosmos DB](https://azure.microsoft.com/ja-jp/products/cosmos-db)
  - Microsoft 製, マルチモデルデータベース

## NewSQL

- Features
  - (+) 大規模データでも安定, 可用性, スケーラビリティ, SQL あり, 一貫性あり
  - (-) 構成が複雑, 高価
- [CockroachDB](https://www.cockroachlabs.com/)
  - OSS

## Analytics

- [Elasticsearch](https://www.elastic.co/jp/elasticsearch)
  - OSS, 分散型検索・分析エンジン
- [BigQuery](https://cloud.google.com/bigquery?hl=ja)
  - Google 製, AI 用分析プラットフォーム
- [Snowflake](https://www.snowflake.com/)
  - Snowflake 製, クラウドデータウェアハウス

## 参考

- [Stack OverFlow Survey 2024](https://survey.stackoverflow.co/2024/technology)
- [Stack OverFlow Survey 2025](https://survey.stackoverflow.co/2025/technology)
