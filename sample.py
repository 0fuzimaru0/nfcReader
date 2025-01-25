import nfc
import binascii

def on_connect(tag):
    """カードがリーダーに接続されたときの処理"""
    try:
        if tag.TYPE == "Type3Tag":
            # Type3Tag（主に交通系ICカード）のIDmを取得
            id_info = binascii.hexlify(tag.idm).decode()
            print(f"IDm (Type3Tag): {id_info}")
        elif tag.TYPE == "Type4Tag":
            # Type4Tag（スマホなど）のUIDを取得
            id_info = binascii.hexlify(tag.identifier).decode()
            print(f"UID (Type4Tag): {id_info}")
        else:
            print(f"その他のカードがスキャンされました: {tag.TYPE}")
    except AttributeError:
        print("カード情報の取得に失敗しました")
    return False  # 一度接続後に自動で切断する

def main():
    try:
        # データレートを指定して接続
        with nfc.ContactlessFrontend('usb') as clf:
            print("リーダーを待機中...")
            tag = clf.connect(rdwr={
                "targets": ["212F", "424F"],  # Type3Tag（交通系ICカード）のみに絞り込み
                "on-connect": on_connect
            })
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
