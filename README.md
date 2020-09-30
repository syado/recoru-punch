# RecoRu Punch

- RecoRuの出勤/退勤を行うプログラム
- class RecoRuを使用してお好みのプログラムを作成するのもよし
- そのまま認証情報を入力して使うのもよし

#### 以降はそのまま使う場合の説明

## 設定

### 実行環境
- Python3
- [requests](https://github.com/psf/requests)

### プログラム内に認証情報を入力
```python
contractId="0000000" #契約ID
authId="id or mail" #IDまたはメールアドレス
password="xxxxxxxxx" #パスワード
```

## 使用方法

### 出勤
```shell
python3 recoru-punch.py in
```

### 退勤
```shell
python3 recoru-punch.py out
```

### メモをつける場合
```shell
python3 recoru-punch.py in メモ
```
