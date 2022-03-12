switchbot-client-app v0.0.5
=====================

Windows/Mac向けのSwitchBotの非公式クライアントアプリ実装です。

不完全な部分が多いのですが、pre-alpha版という位置づけで公開しています。
PCから部屋の電気をつけたり消したりできればOKという程度の最低限の作り込みしかしていません。
個人として所有していないSwitchBot端末も操作できるように組んでいるので、
実際に正しく動くのか動作確認できていない部分もたくさんあります。この点理解の上ご利用ください。

何か不具合があれば、以下のGitHubリポジトリ宛にissueやPRを出していただければ確認します。
https://github.com/kzosabe/switchbot-client-app

SwitchBot API経由で情報を取得したり操作する処理のベースになっているのは以下のライブラリです。
PyPIに公開しているため、pip経由でインストールすることですぐに利用可能です。
Pythonのコード中から自由にSwitchBot端末の操作をすることができます。
https://github.com/kzosabe/switchbot-client


認証について
----------------------

以下のSwitchBot公式のリポジトリに書かれている手順に従ってSwitchBotのスマートフォンアプリを操作し、
認証用のトークンを取得する必要があります。

https://github.com/OpenWonderLabs/SwitchBotAPI#authentication

取得した値を同梱されているconfig.ymlの token: 以降に入力すると、そのトークンに紐付いた端末を操作できるようになります。
