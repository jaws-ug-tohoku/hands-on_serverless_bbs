hands-on_serverless_bbs
==========

2016/09に開催するJAWSUG青森で利用するハンズオンのリポジトリです



# スライドについて

[reveal.js](http://lab.hakim.se/reveal-js/#/)というライブラリを利用して、markdownをスライド表示する想定です

## オンラインで表示する方法

[slideck](https://slideck.io/)というサービス経由でslies/slideck.mdをreveal.jsのフォーマットで表示します

URL: https://slideck.io/github.com/jaws-ug-tohoku/hands-on_serverless_bbs/slides/slideck.md

## オフラインで表示する場合

[revealgo](https://github.com/yusukebe/revealgo)というツールを利用して表示します。

##### 起動

```
$ go get github.com/yusukebe/revealgo/cmd/revealgo
$ revealgo slides/slideck.md
```
