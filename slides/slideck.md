# サーバレスでWebアプリを作ろう

JAWSUG青森 (石澤・福井)

2016/09/xｘ

---



## 自己紹介
- - -

さくっと

---



## 自己紹介(石澤)
- - -

---



## 自己紹介(福井)
- - -

- 福井 烈 (Takeshi Fukui)
- Engineer @ Piece of Cake, inc. (since 2015. 3 ~)
  - cakes (https://cakes.mu)
  - note (https://note.mu)
- リモートワーカー (東京 <=> 青森県大鰐町)
- 1児の父
- http://fukuiretu.com

---



## アジェンダ
- - -

1. ハンズオン概要
1. 今回利用するAWSのサービス概要
1. 題材ダウンロード
1. Dynamo DBの設定
1. Lambdaの設定
1. API Gatewayの設定
1. Webアプリから接続
1. Webアプリのカスタマイズ

---

## ハンズオン概要
- - -

API Gateway + Lambda + DynamoDBで掲示板を作ろう

(ついでにReact.jsも使っちゃおう)

---

## 題材ダウンロード
- - -

以下のURLよりダウンロードし、

zipファイルを解凍してください

https://github.com/jaws-ug-tohoku/hands-on_serverless_bbs/archive/master.zip

<br/>

gitを利用している方は以下のコマンドでも可能です

```
$ git clone https://github.com/jaws-ug-tohoku/hands-on_serverless_bbs.git
```

---

## Dynamo DBの設定
- - -

石澤san担当でOK?

---

## API Gatewayの設定
- - -

石澤san担当でOK?

---

## Lambdaの設定
- - -

石澤san担当でOK?

---

## WebアプリからAPIへ接続

---

## その前に... ちょっとだけReact.jsの説明

---



## React.jsとは
- - -
- UIのパーツ(コンポーネント)を作るViewのためのライブラリ
- Facebook製のOSS (https://github.com/facebook/react)
- もちろんFacebook自身もReact.js製
- ちなみにcakesとnoteは...

---


## React.jsのメリット/デメリット
- - -

メリット

- パフォーマンスが良い
  - リアルなDOMはなぜ遅いのか (http://steps.dodgson.org/b/2014/12/11/why-is-real-dom-slow/)
- ある程度のルールを強制されるので、メンテナンス性も期待できる


デメリット

- 学習コスト
- jQueryをベースにしたライブラリとは相性が悪いので、エコシステムが生かせない可能性がある

---

## React.jsのコンポーネント実装例
- - -

```
var PostForm = React.createClass({
  render: function() {
    return (
      <div className="panel panel-default">
        <div className="panel-heading">
          <h4>投稿</h4>
        </div>
        <div className="panel-body">
          <form onSubmit={this.props.handleSubmit}>
            <div className="form-group">
              <label htmlfor="userName">ユーザ名</label>
              <input type="text" name="userName" value={this.props.userName}
                onChange={this.props.changeUserName}
                className="form-control"
                placeholder="ユーザ名を入力してください" />
            </div>
            <div className="form-group">
              <label htmlfor="message">メッセージ</label>
              <textarea name="message" className="form-control" rows="3"
                onChange={this.props.changeMessage} placeholder="メッセージを入力してください">
                {this.props.message}
              </textarea>
            </div>
            <button type="submit" className="btn btn-default">投稿する</button>
          </form>
        </div>
      </div>
    );
  }
});
```
---

## WebアプリからAPIへ接続(1/3)
- - -

web/bbs.htmlをお使いのエディタ(vim, Atom, サクラエディタ etc)で開き、

以下の定数(const)をAPI Gatewayで設定したエンドポイントに書き換える

```
Line:88
  const ENDPOINT = "https://xxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com";
```

---



## WebアプリからAPIへ接続(2/3)
- - -

web/bbs.htmlをお好みのWebブラウザ(Google Chrome, Internet Exproler etc)で開く

![bbs](slides/images/bbs_1.png)

---

## WebアプリからAPIへ接続(3/3)
- - -

ユーザ名、メッセージを入力して投稿してみましょう

![bbs](slides/images/bbs_2.png)

---



## Webアプリのカスタマイズ
- - -

- 投稿内容の削除機能
- 投稿内容のソート機能
- 投稿項目の追加

etc...

---

# FIN
