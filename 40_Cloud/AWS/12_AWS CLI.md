# AWS CLI

- AWS CLI で出来ること
  - AWS の各種サービスをコマンドラインから操作できる
  - スクリプトを使って自動化できる
  - 複数の AWS アカウントやリージョンを簡単に切り替えられる

## インストール

- [Install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## 初期設定

- [Login](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)

```bash
% aws login
No AWS region has been configured. The AWS region is the geographic location of your AWS resources.

If you have used AWS before and already have resources in your account, specify which region they were created in. If you have not created resources in your account before, you can pick the region closest to you: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html.

You are able to change the region in the CLI at any time with the command "aws configure set region NEW_REGION".
AWS Region [us-east-1]: ap-northeast-1 # 東京リージョンを入力
```

ブラウザが開き、ログイン済みのセッションで認証が完了する
`% aws sts get-caller-identity` で認証情報が取得できることを確認する

## EC2 操作

- EC2 インスタンス一覧表示
  - `aws ec2 describe-instances`
- 既にある EC2 インスタンスの起動
  - `aws ec2 start-instances --instance-ids {インスタンスID}`
    - https://docs.aws.amazon.com/cli/latest/reference/ec2/start-instances.html
- AMI から EC2 を作成してインスタンス起動
  - `aws ec2 run-instances --image-id {AMI ID}`
    - https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html

## S3 操作

- S3 バケット一覧表示
  - `aws s3 ls`
- S3 バケット作成
  - `aws s3 mb s3://{バケット名}`
