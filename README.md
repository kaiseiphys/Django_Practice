# 概要

    「最短距離でゼロからしっかり学ぶ Python入門 実践編」
        https://www.amazon.co.jp/%E6%9C%80%E7%9F%AD%E8%B7%9D%E9%9B%A2%E3%81%A7%E3%82%BC%E3%83%AD%E3%81%8B%E3%82%89%E3%81%97%E3%81%A3%E3%81%8B%E3%82%8A%E5%AD%A6%E3%81%B6-Python%E5%85%A5%E9%96%80-%E3%80%9C%E3%82%B2%E3%83%BC%E3%83%A0%E9%96%8B%E7%99%BA%E3%83%BB%E3%83%87%E3%83%BC%E3%82%BF%E5%8F%AF%E8%A6%96%E5%8C%96%E3%83%BBWeb%E9%96%8B%E7%99%BA-Eric-Matthes/dp/4297115727/?_encoding=UTF8&pd_rd_w=VgM5E&pf_rd_p=9b1525c2-a61e-4d68-ab17-d93f310e1f50&pf_rd_r=QSE22A8G8N80WCSSJX9B&pd_rd_r=97ce8aaa-6120-4258-b947-d0d4617ed007&pd_rd_wg=y9VxI&ref_=pd_gw_ci_mcx_mi

    のプロジェクト3「Webアプリケーション」(183 ~ 290 ページ) を練習し、Django の使い方を学習します。

# 環境
    ・個人で編集するだけなので、Docker で環境を用意する事はしていない。
    ・venv 仮想環境モジュールを実行して、ll_env という名前の仮想環境を作成。
        有効化: source ll_env/bin/activate
        無効化: deactivate

# 手順
    # 準備
        1. Django をインストール
            pip install django
        2. Django プロジェクト [leaning_log] を作成
            django-admin startproject learning_log .
        3. データベースを作成
            python3 manage.py migrate
        4. 開発サーバを起動
            python3 manage.py runserver

    # アプリケーションを開始
        1. アプリケーション [learning_logs] を開始
            python3 manage.py startapp learning_logs
        2. モデルを定義
            learning_logs/models.py を編集
        3. モデルを有効化
            learning_log/models.py を編集

