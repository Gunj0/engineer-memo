# AWS アカウント

- AWSアカウント: AWSのサービスを利用するための基本単位
  - 企業ではプロジェクトごと、環境ごとにアカウントを分けることが一般的
  - アカウント作成時にroot ユーザーが自動的に作成される
  - IAM (Identity and Access Management) を使用して、追加のユーザーやグループを作成・管理可能

## IAM ユーザーの作成

- IAM ロールを付与した IAM ユーザーを作成することで、権限を絞ったアクセスが可能になる
  - IAM > ユーザーの作成
  - ポリシーを直接アタッチする > AdministratorAccess
  - 基本的にはこの IAM ユーザーでマネジメントコンソールにアクセスすることが推奨される
  - IAM グループにユーザーを追加し、一括でロール管理も可能
  - IAM 作成は無料

## 料金

- [AWS無料利用枠](https://aws.amazon.com/jp/free/)
- [見積もりツール](https://calculator.aws/#/)
  - Create Estimate > サービスを選択して見積もりを作成
