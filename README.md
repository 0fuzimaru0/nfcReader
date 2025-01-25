# README

## プロジェクト概要
このプロジェクトは、Pythonを使用して非接触ICカードのIDmを読み取るアプリケーションです。SonyのPaSoRi（RC-S380）リーダーを使用し、交通系ICカードやモバイルSuicaなどの情報を取得できます。

---

## 必要環境

- Python 3.x
- PaSoRi（RC-S380）
- 対応ICカード（交通系ICカード、モバイルSuicaなど）

---

## セットアップ手順

1. **リポジトリをクローンする**

   ```bash
   git clone <リポジトリURL>
   cd <リポジトリフォルダ>
   ```

2. **仮想環境を作成してアクティベートする**

   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **必要なライブラリをインストールする**

   ```bash
   pip install -r requirements.txt
   ```

4. **Zadigのセットアップ（Windows環境のみ必要）**

   1. **Zadigのダウンロードとインストール**:
      - Zadig公式サイトからZadigをダウンロードして起動します。

   2. **PaSoRiのデバイスを選択**:
      - PaSoRi（RC-S380）をUSBポートに接続。
      - Zadigの「Options」→「List All Devices」を選択。
      - ドロップダウンリストからPaSoRi（例: "Sony FeliCa Port/PaSoRi"）を選択。

   3. **libusb-win32ドライバをインストール**:
      - 下部の「Driver」セクションでlibusb-win32を選択。
      - 「Install Driver」をクリックしてインストール。

   4. **再起動**:
      - インストール後、念のためPCを再起動します。

5. **アプリケーションを実行する**

   ```bash
   python sample.py
   ```

---

## 使用方法

1. 必要なセットアップが完了したら、`python sample.py`を実行します。
2. リーダーがICカードを待機している状態で、カードをかざしてください。
3. 読み取られたIDmやUID情報がターミナルに表示されます。

---

## 注意事項

- `requirements.txt`に記載されているライブラリを正確にインストールしてください。
- Sony公式サイトからPaSoRi（RC-S380）のドライバをインストールしてください。
- 対応カード以外を使用した場合、エラーが発生する可能性があります。

---

## ファイル構成

```plaintext
<プロジェクトフォルダ>
├── sample.py          # メインのスクリプト
├── requirements.txt   # 必要なライブラリ一覧
├── README.md          # このファイル
```

---

