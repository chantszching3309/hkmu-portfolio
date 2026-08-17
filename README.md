# HKMU Portfolio

Hong Kong Metropolitan University 課堂練習／功課 code 整理。只放**自己寫**嘅 HTML、CSS、JavaScript、Python 同文字答案。

## 目錄

```
hkmu-portfolio/
├── web/                 HTML + CSS + JavaScript（原文）
│   ├── tma1.html
│   ├── q2b.html
│   ├── q3b.html
│   ├── q3c.html         ← 結構有問題，練習用
│   ├── q4a.html
│   ├── q4b.html
│   └── tma3.html
├── python/              Python（原文）
│   ├── q1a.py
│   ├── q1b.py           ← 計總價有 bug，練習用
│   ├── q2a.py           ← 遞迴會爆，練習用
│   ├── q2b.py
│   └── q3a.py
├── completed/           可以開／可以跑嘅示範
│   ├── web/
│   └── python/
├── practice/            刻意保留問題，用嚟自己 debug
│   ├── web/
│   └── python/
└── docs/
    ├── README.md
    └── assignment-notes.md
```

## 邊啲可以行、邊啲唔得

| 檔案 | 狀態 | 點用 |
| --- | --- | --- |
| `completed/web/*.html` | 得 | 用瀏覽器直接打開 |
| `completed/python/q1a.py` `q2b.py` `q2c.py` `q3a.py` | 得 | `python3 檔名.py` |
| `web/q3c.html` | 唔得 | `</head>` 放錯位，練習修正 HTML |
| `python/q2a.py` | 唔得 | `factorial` 用錯變數，會 RecursionError |
| `python/q1d.py` | 唔得 | 缺 `EPLTeams.csv` |
| `python/q1b.py` | 跑到但答案錯 | 多張 pizza 嘅總價只加最後一張 |

詳細練習提示睇 [`practice/README.md`](practice/README.md)。

## 冇放上去嘅嘢（版權／私隱）

- 學校官方題目紙、checklist 範本、教材截圖
- 老師評語、分數
- 電話號碼等個人資料
- 論文原文整句抄錄

## 點樣喺本地睇

```bash
# 網頁
open completed/web/tma1.html

# Python
cd completed/python
python3 q1a.py
python3 q3a.py
```

## 授權

呢個 repo 入面嘅 code 同文字係作者自己嘅習作。學校課程內容版權仍屬香港都會大學。
