#ページ構成
学期タブで変更(全てもあり)→
デフォルトのメインページ:科目一覧ページor時間割ページタブで変更可能→個別の科目ページからその成績とそのタスク、科目設定(曜日など)
タスク一覧(全体のタスク、並び替え機能)
カレンダーページ
gpaページ(全体の目標と個々の成績表示)
ノート、リンク集ページ
設定ページ
#python
import sqlite3
import time
import os
#データベースに接続
con = sqlite3.connect('data.db')
cursor = con.cursor()
#sqlを実行
cursor.execute(

CREATE TABLE term (
    id_term INT PRIMARY KEY,
    term_name VARCHAR(255) NOT NULL,
    term_start INT NOT NULL,
    term_finish INT NOT NULL,
    term_remove INT
);

CREATE TABLE sub (
    id_sub INT PRIMARY KEY,
    sub_name VARCHAR(255) NOT NULL,
    sub_day INT,
    sub_time INT,
    credit INT NOT NULL,
    note TEXT,
    link TEXT,
    target_score INT,
    FOREIGN KEY (task_id) REFERENCES task(id_task),
    FOREIGN KEY (score_id) REFERENCES score(id_score)
);

CREATE TABLE enroll (
    id_e INT PRIMARY KEY,
    term_name VARCHAR(255) NOT NULL,
    term_id INT NOT NULL,
    sub_id INT NOT NULL,
    target_gpa INT NOT NULL,
    FOREIGN KEY (term_id) REFERENCES term(id_term),
    FOREIGN KEY (sub_id) REFERENCES sub(id_sub)
);
CREATE TABLE score (
    id_score INT PRIMARY KEY,
    score_name VARCHAR(255) NOT NULL,
    score_value INT NOT NULL,
    score_rate INT NOT NULL
    FOREIGN KEY(sub_id) REFERENCES sub(id_sub)
);
CREATE TABLE task (
    id_task INT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    task_desc TEXT,
    task_start INT NOT NULL,
    task_finish INT NOT NULL,
    task_repeat INT,
    task_done INT NOT NULL,
    FOREIGN KEY(sub_id) REFERENCES sub(id_sub)      
);
)


#関数リスト

#汎用関数
def add_data(key, value):
    cursor.execute(f"INSERT INTO term ({key}) VALUES (?)", (value,))
    con.commit()

def edit_data(key, value):
    cursor.execute(f"UPDATE term SET {key} = ? WHERE id_term = (SELECT id_term FROM term ORDER BY id_term DESC LIMIT 1)", (value,))
    con.commit()

def delete_data(key, value):
    cursor.execute(f"DELETE FROM term WHERE {key} = ?", (value,))
    con.commit()

def read_json():
    pass

def write_json():
    pass
関数_辞書show
特定の辞書を出力


#学期
学期名でjsonを作る

#時間割
設定通りに表示する

#科目関数
class
init
add_data()
edit_data()
delete_data()


#タスク関数
クラス
関数_タスクを新しく作る
    タイムスタンプでIDを決める
    繰り返しの場合は繰り返しであることがわかるようにIDをつける
    
    エラー締め日が始めより前にならない
関数_繰り返しの制作
関数_タスクの中身を編集する
関数_タスクを削除
繰り返してた場合それも消去するか確認する
関数_タスクの並び替え(期限順、重要科目、カスタムなど、状態管理)

#成績関数
クラス
関数_成績を新しく作る
関数_成績の中身を編集する
関数_成績を削除
関数_gpaの計算方法を記録する
関数_gpaの計算方法を編集する
関数_目標のgpaを記録する
→学期ごと？
関数_目標のgpaを編集する
関数_目標gpaから取りたい点数をそれぞれの科目で計算して取れそうなやつを多めに割り振って目標の点数を算出する
関数_目標からの距離で色を表示する

#リンク関数
クラス
関数_リンク集に乗ってるリンクを全て開く

#ノート関数
クラス
関数_ノートナンバリング 
    科目のナンバリングに合わせて第n回とつけて保存する
関数_ノートキャッシュ
    自動保存と開く前までのデータを持っておいて戻れるようにする

#カレンダー関数
クラス
関数_カレンダーにイベントを追加する
関数_カレンダーナンバリング
gwなどを除いて初めの日から科目の曜日でナンバリングを進める
てカレンダーの日付と数字を紐づけたデータベースを作る
#勉強記録関数
教材ごとに管理タグをつけられるようにする
指定アプリを閉じたら解いた問題数と正解数だけポップアップを出して記録して正答率や勉強管理を行う
忘却曲線を計算してタスクに重要度は低めで記録する
空いている日やよくタスクを行う日に多めに入れる
リスケ機能

通知選別、空いている時間、特定のアプリを起動してないときに通知、また保留したらタスクとして保存できる

#設定
クラス
関数_最初に開くページを設定する
関数_背景、目標からの距離などでカラーセットを設定する
関数_バックアップ
ワイファイに繋がっていたらバックアップするタイムスタンプを使って新しい方を採用する
暗号化
ハッシュの計算で改善されているか確認されてたら開かない

関数_設定保存


