# Practice（刻意留低嘅問題）

呢度唔係標準答案。用嚟自己 trace、改、再跑。

## web/q3c.html

- 問題：`<body>` 內容寫完之後先寫 `</head>`，markup 順序錯。
- 練習：將 `<head>` / `<body>` 執返正確巢狀，用瀏覽器打開確認 18 區 list 排得整齊。

## web/q5j-css-examples.html

- 問題：inline / embedded / external 三種 CSS 混喺同一頁，而且有未閉合嘅 `<p>`。
- 練習：拆成三個清楚例子，令 `mystyle.css` 真係生效。

## python/q2a.py

- 問題：內層 `factorial(n)` 判斷咗外層嘅 `N == 1`，遞迴停唔到。
- 練習：改到可以計 `find_e(N)`，用細嘅 N（例如 5）測試。

## python/q1b.py

- 問題：可以運行，但 `total_price` 擺錯位置，多過一張 pizza 時總價唔啱。
- 練習：每一張 pizza 計完都要加進總價。

## python/q1d.py

- 問題：依賴 `EPLTeams.csv`，repo 冇放呢個檔（避免用到可能受版權保護嘅數據檔）。
- 練習：自己整一個三欄 CSV（隊名、已賽、勝場）再跑。
