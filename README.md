# network_automation
---

# 使用技術
<!--
 <img src="https://img.shields.io/badge/-{言語、フレームワーク名など}-{シールドのカラーコード}.svg?logo=next.js&style={バッチのスタイル}&logoColor={ロゴのカラーコード}">
  -->
<img src="https://img.shields.io/badge/-Python-0C0C0C.svg?logo=python&style=for-the-badge">
<img src="https://img.shields.io/badge/-FastAPI-0C0C0C.svg?logo=fastAPI&style=for-the-badge">

バッジ：https://shields.io/badges/static-badge</br>
アイコン：https://simpleicons.org/?q=react</br>
URL生成：https://t8csp.csb.app/</br>

---

# 環境変数
|変数名|役割|デフォルト値|環境差分|
|:----|:----|:---------|:-------|
|TEST|テスト|test|test|
|||||

---

# 基本ルール
モデルは<a link="https://openconfig.net/projects/models/schemadocs/">OpenConfig Data Model</a>に準拠するが、必要に応じて<a link="https://github.com/YangModels">Yang Models</a>を使用する。
使用するプロトコルは、取得可能な場合は、RESTCONFにてネットワーク機器の設定情報を取得する。
該当の情報が原則JSON形式で取得することが難しい場合、NETCONFを使用してXML形式で情報を取得する。
FastAPIにて差分を吸収し、必要な情報をJSON形式にして応答する。

---

# 機能予定
### 機能一覧
```
┌ 設定情報の取得
    ├ ホスト情報
        ├ バージョン
        └ 稼働時間
    ├ インターフェース情報
        ├ IPアドレス情報
            └ サブネット・セグメント情報
        └ インターフェースステータス
            ├ リンクステータス情報
            ├ Speed/Duplex
            └ I/O情報
    └ ルーティング情報
        ├ ルーティングテーブル情報
        ├ 各メトリックの表示
        └ RIB(Routing Information Base)
├ 設定変更
    ├ インターフェース設定変更
    ├ VLAN設定変更
    ├ 各BGP設定変更
    ├ 各OSPF設定変更
    ├ 各ACL設定変更
    ├ スタティックルート設定変更
    ├ NAT設定変更
    ├ VRRP設定変更
    ├ IPSec設定変更
    ├ 各STP設定変更
    ├ L2スイッチポート設定変更
    └ LAG設定変更
└ リアルタイム統計情報を取得
    ├ 必要な情報を整理後記載
```

---

## 機能詳細
### ・設定情報の取得
今後記載

---

### ・設定変更
今後記載

---

### ・リアルタイム統計情報を取得
今後記載

---