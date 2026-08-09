# 生成に関するパターン

## Factory Method: サブクラスにインスタンスを生成させて共通ロジックを書く方法

### 公式説明

オブジェクトを生成するときのインターフェースだけを規定して、
実際にどのクラスをインスタンス化するかはサブクラスが決めるようにする。
FactoryMethod パターンは、インスタンス化をサブクラスに任せる。

### 解説

- 基本
  - オブジェクト生成のインターフェースだけを規定して、サブクラスが実際にどのクラスをインスタンス化するか決める
- 詳細
  - `ProductService`抽象クラスに`Create`メソッドと`FactoryMethod`メソッドを定義する, これを Creator クラスと呼ぶ
  - これを継承した`ProductServiceFactory`の中で`Kind`を引数に`IProduct`を返す`FactoryMethod`の処理を書く
  - Creator 側の`Create`メソッドでは`FactoryMethod`で生成した`IProduct`に対する共通ロジックで処理して`IProduct`を返す
  - クライアント側では`ProductServiceFactory`の`Create`を呼ぶことで共通ロジックを通してクラス生成ができる
- メリット
  - Factory に共通ロジックを持たせられる
