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
            learning_logs/models.py で TOPIC というクラスを作成
            Topic クラスには 'text', 'date_added' の2つの属性を追加
        3. モデルを有効化
            learning_log/settings.py の INSTALLED APPS に learning_logs を追加
        4. 以下を実行し、マイグレーションしてデータベースに TOPIC 用のテーブルを作成する
            python3 manage.py makemigrations learning_logs
            python3 manage.py migrate

    # 管理サイトを利用する
        1. スーパーユーザーを設定
            python3 manage.py createsuperuser
        2. Topic モデルを管理サイトに登録
            admin.py に admin.site.register(Topic) を追加し、Topic モデルをインポートして管理サイトで使えるようにする

    # Entry モデルを定義する
        1. learning_logs/models.py で TOPIC というクラスを作成
            Entry クラスには 'topic', 'text', 'date_added' の3つの属性を追加
            __str__() メソッドで個々の記事を参照したときに表示する情報を指定
        2. 作成したモデルをマイグレーション
            python3 manage.py makemigrations learning_logs
            python3 manage.py migrate
        3. Entry モデルを管理サイトに登録
            admin.py に admin.site.register(Entry) を追加
    
    # ページを作成する
        1. learning_log/urls.py を編集
            path('', include('learning_logs.urls')), を追加し、learning_logs の urls モジュールを取り込む
            learning_logs/urls.py はまだないので、
        2. learning_logs/urls.py を新規作成して、
            urlpatterns = [path('', views.index, name='index'),] を追加し、views モジュールの index 関数を呼び出す
            index() 関数はまだ定義していないので、
        3. learning_logs/views.py で index() 関数を定義
            learning_logs/index.html を render (描写) するように定義した
            index.html はまだないので、
        4. テンプレートを作成する
            learning_logs フォルダーの下に templates フォルダーを作り、更にその下に learning_logs フォルダーを作る
            learning_logs/templates/learning_logs/index.html を作る。