# Title: 豊川市内通学・通勤ヒヤリハットマップ
PythonのフレームワークDjangoで作成した豊川市内限定のヒヤリハットマップサイト

サイトのURL： https://geomapapp.awsmikawa.com/（Google Chromeでの閲覧推奨）

ソースコードの保存先　GitHub： https://github.com/ozawaseiya/geo-map-app

# geo-map-app(name of repository)
豊川市内に３カ所あるヒヤリハットの場所（架空）をGoogle Maps APIを用いて表示し、市内の通勤・通学者への交通道路事情の情報提供を行う。シェアリング機能により将来的に事故の起こりそうな市内の場所が上位に表示される仕組みとなっている。なお、当システムは豊川市役所を顧客と想定したシステムである。

# Dependency
Python 3.6.9, HTML5, CSS3, sqlite3, フレームワーク:Django2.2.16, Bootstrap4, nginx, gunicorn

# Setup
AWS(IAM,VPC,EC2,ELB,EIP,Route53,Certificate Manager), Github, ubuntu18.04, Visual Stadio Code, Docker Desktop for Mac

# Usage
Webシステム機能一覧

1.Google Mapマーカー・リンク先機能, 2.危険度投票機能, 3.危険度シェアリング上位表示機能, 4危険箇所詳細表示機能

# License
Copyright(c) 2020 Seiya Ozawa
This software is released under the MIT License, see LICENSE.
https://opensource.org/licenses/mit-license.php

# Authors and References
Web API （Google Maps Platform）

