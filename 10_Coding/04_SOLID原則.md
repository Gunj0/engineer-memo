# SOLID 原則

- オブジェクト指向の 5 大原則
  - ドメイン駆動開発の基礎となっている

## 単一責任の原則: Single Responsibility Principle

- クラスの責務は 1 つにする
  - ：クラスを変更する理由(=責務)は 1 つ以上存在してはならない
  - ：最小カプセル（これ以上分割すると制御できなくなる）にする
    - 例：タイマーインスタンス+スタートメソッド+ストップメソッド+存在チェック
  - 修正箇所が最小になる, 修正箇所が明確になる

## オープン・クローズドの原則: Open-Closed Principle

- 既存機能に影響がないように機能拡張ができるようにする

## リスコフの置換原則: Liskov Substitution Principle

- 継承関係の使い所の原則
- 親クラスインスタンスを子クラスインスタンスに置き換えても意味が通るようにする

## インタフェース分離の原則: Interface Segregation Principle

## 依存関係逆転の原則: Dependency Inversion Principle
