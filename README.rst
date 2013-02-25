==========
 rst2inao
==========

reStructuredTextから技術評論社のinaoフォーマットに変換するスクリプトです。

実装には ``rst2textile`` を参考にさせて頂きました。
というよりまずまるごとコピーしてから必要なところを書き換えました。

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

- unordered list
- unordered list
- unordered list

1. ordered list
2. ordered list
#. ordered list

- *em* 斜体
- **strong** 太字
- ``literal`` 文中等幅フォント

既知の未実装
============

- 段落の頭は字下げが必要らしい？
- 入れ子になったリストはinaoでどう出力するべきかわからなかったのでサポートしていません

参考文献
=========

- rst2textile https://bitbucket.org/shimizukawa/rst2textile/overview
- markdown2inao https://gist.github.com/2303592
