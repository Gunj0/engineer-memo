# 振る舞いに関するパターン

## Observer: 変化の通知

### 公式説明

あるオブジェクトが状態を変えたときに、それに依存するすべてのオブジェクトに自動的にそのことが知らされ、
また、それらが更新されるように、オブジェクト間に一対多の依存関係を定義する。

### 解説

- 基本
  - オブジェクトの状態変化が自動的に他のオブジェクトに通知されるようにする
- 詳細
  - GoF 本の方法
    - `Update(bool isWarning)` メソッドを持つ INotify インターフェース を作る
    - 通知する側は`List<INotify>`のリストを持つ
      - Add メソッドでリストの中に、受け取った INotify 型のオブジェクトを追加する
      - Remove メソッドでリストの中から、受け取った INotify 型のオブジェクトを削除する
      - 通知するときは、List の中身に対して Update を実行する
    - 通知される側は`INotify`を実装する
      - 通知する側の`Add(this)`で自身のインスタンスを登録する
      - `Update(bool isWarning)`メソッドを実装して通知されたときの処理を書く
  - C# の方法
    - `public static event Action<bool> WarningAction` のようにイベントを宣言する
      - `event`をつけておくとカプセル化され、上書きできなくなるので安全
    - 値が変わったときの処理に`WarningAction?.Invoke(value)`を書き、値の受け渡し設定をする
    - 起動処理に`WarningAction += WarningTimer_WarningAction`としてイベント処理を登録する
    - `private void WarningTimer_WarningAction(bool inWarning)`の中に、通知されたときの処理を書く
    - event は追加すると画面を閉じても残ってしまうので、Dispose 処理の中で`-=`で削除する
- メリット
  - 監視する側から監視される側を定期的に見に行く無駄な処理が不要になる
