==========
 rst2inao
==========

reStructuredTextから技術評論社のinaoフォーマットに変換するスクリプトです。

実装には ``rst2textile`` を参考にさせて頂きました。
というよりまずまるごとコピーして必要なところを書き換えました。
なお ``rst2textile`` はApache Software Licenseです。

締め切りに追われながらやっつけで作ったので完成度はかなり低いです。
テストは動きません(そもそもどういう出力が正しいのかをイマイチ把握していません)
``markdown2inao`` の出力を参考にするといいのかな。まだやってません。

実装済み
========

見出し
------

::

   source code
   source code
   source code

- unordered list(これ)
- *em* 斜体
- **strong** 太字
- ``literal`` 文中等幅フォント

1. ordered list
2. ordered list
#. ordered list

既知の未実装
============

- 段落の頭は字下げが必要らしい？
- 入れ子になったリストはinaoでどう出力するべきかわからなかったのでサポートしていません
- inaoフォーマットは図にキャプションを要求しますが、reSTのimageは要求しないのでfigureを使うべきなんだろうけども原稿はimageで書いてしまったのでサポートしていません


参考文献
=========

- rst2textile https://bitbucket.org/shimizukawa/rst2textile/overview
- markdown2inao https://gist.github.com/2303592
