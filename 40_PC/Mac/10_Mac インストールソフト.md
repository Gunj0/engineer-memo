# Mac インストールソフト

- 基本
  - [Homebrew](https://brew.sh/ja/)
    - パス通す(インストールメッセージ参照)
- Utility
  - brew install karabiner-elements
    - Karabiner。キーボードカスタム。
      - Simple Modifications
        - left_control→left_command
        - left_command→left_control
        - caps_lock→right_control
      - Complex Modifications
        - right_control + ijkl→arrow keys
        - left_control + tab→left_command + tab
        - left_command + tab→left_control + tab
        - right_control+left_option+j→right_control+left_option+左
        - right_control+left_option+l→right_control+left_option+右
        - right_control+left_option+i→right_control+left_option+上
  - brew install raycast
    - Raycast。ランチャー/ウィンドウスナップ/クリップボード。
      - Left Half→control+option+左
      - Right Half→control+option+右
      - Maximize→control+option+上
  - brew install google-japanese-ime
    - Google 日本語入力。再起動して追加する。
    - 変換エンジン起動失敗時は GoogleLLC とログイン時の設定チェック
      - ひらがな（Google）＋ ABC（デフォ）
      - ConfigDialog
        - キー設定の選択：MS-IME
          - 英数でカタカナ変換はできないっぽい？
      - DisctionaryTool
        - {名字 2 文字} → {フルネーム}
        - {名字ひらがな} → {名字漢字}
        - {名前ひらがな} → {名前漢字}
        - めあど → {メールアドレス}
  - brew install alt-tab
    - alttab
- ブラウザ
  - brew install google-chrome
    - Chrome。ログイン。
    - マウスジェスチャは OFF(二本指タップがきかなくなるため)
  - brew install firefox
    - Firefox。ログイン。
- 開発
  - brew install visual-studio-code
    - VSCode。ログインする。
  - brew install --cask docker
    - Docker。ログインする。cask つけないと CLI になる。
  - brew install unity-hub
    - Unity。ログインする。
  - brew install iterm2
    - iTerm2。多機能ターミナル。
      - Proofiles
        - Windows
          - Transparency: 30
          - Style: Full-Height Left of Screen
        - Keys
          - Configure Hotkey window
            - command + space
            - Pin hotkey window〜: ON
  - brew install stripe/stripe-cli/stripe
    - Stripe CLI
- ストレージ
  - brew install google-drive
    - GoogleDrive。ログインする。ミラーリング設定。
- ソフト
  - brew install discord
    - Discord。
  - brew install teamviewer
    - TeamViewer。
  - brew install bitwarden
    - Bitwarden。パスワードマネージャ。
  - brew install zoom
    - Zoom。ログインする。
  - brew install mas
    - AppStore から CLI インストールするツール。
    - mas searcħ LINE（LINE の ID 検索）
    - mas install 539883307
- フォント
  - brew install font-hackgen
    - 白源。プログラミング用。
- 言語
  - brew install mise
    - 色々バージョン管理ツール
    - https://mise.jdx.dev/getting-started.html#shells
    - パスを通す
  - mise use --global node@（LTS のバージョン）
    - Node.js

mysql
ruby
python
.net 8
node.js

・App Store から
bettersnapTool（購入済）
XCode

・保留
動画ビューワ IINA
画像ビューワ Toy viewer
Postman
スクショ skitch
クリーンツール
figma
CompareMerge 比較ツール
fiddler
tunnelbear
kindle
steam
logi options+

## 不要

- Visual Studio for Mac (廃止)
- BetterSnapTool (有料)
- BetterTouchTool (有料)
- HyperSwitch (ウィンドウ毎の切り替えは使わない)
- Amphetamine (スリープ防止)
- Mos (マウス使う用)
- Alfred (RayCast で代替)
