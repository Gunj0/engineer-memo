# OSI参照モデル

- OSI (Open Systems Interconnection) 参照モデル: ネットワーク通信を7つの階層に分けたモデル
  - 各階層は特定の機能を担当し、通信プロセスを標準化する
  - 7階層:
    1. 物理層 (Physical Layer)
       - ビットの伝送、物理的な接続 (例: ケーブル、ハブ)
    2. データリンク層 (Data Link Layer)
       - フレームの転送、エラーチェック (例: スイッチ、MACアドレス)
    3. ネットワーク層 (Network Layer)
       - パケットのルーティング、論理アドレス (例: ルーター、IPアドレス)
    4. トランスポート層 (Transport Layer)
       - データの信頼性、フロー制御 (例: TCP、UDP)
    5. セッション層 (Session Layer)
       - セッションの確立、管理、終了 (例: セッションID)
    6. プレゼンテーション層 (Presentation Layer)
       - データの表現形式、暗号化 (例: JPEG、SSL/TLS)
    7. アプリケーション層 (Application Layer)
       - ユーザーインターフェース、アプリケーションサービス (例: HTTP、FTP、SMTP)
  - 各階層は独立しており、上位層は下位層のサービスを利用する
