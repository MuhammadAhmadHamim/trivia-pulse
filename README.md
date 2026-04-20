# ⚡ trivia-pulse

> A self-updating random fact card for your GitHub profile — styled in acid yellow on void black.

![Daily Fact](./fact.svg)

---

## how it works

A GitHub Action runs every day at midnight UTC, calls the [uselessfacts API](https://uselessfacts.jsph.pl/), generates a styled SVG card, and commits it back to this repo automatically. Your profile README just embeds the image — no server, no cost, no maintenance.

```
GitHub Actions (daily cron)
       ↓
app/services.py  →  fetches random fact
app/utils.py     →  wraps + formats text
app/main.py      →  renders acid-yellow SVG
       ↓
fact.svg committed back to repo
       ↓
profile README embeds it via raw URL
```

## embed it

Drop this into any README:

```markdown
![Trivia Pulse](https://raw.githubusercontent.com/YOUR_USERNAME/trivia-pulse/main/fact.svg)
```

## run it locally

```bash
git clone https://github.com/YOUR_USERNAME/trivia-pulse
cd trivia-pulse
pip install -r requirements.txt
python app/main.py
```

## structure

```
trivia-pulse/
├── app/
│   ├── main.py        # SVG assembly + entry point
│   ├── utils.py       # text wrapping, height calc, XML escaping
│   └── services.py    # API fetch with fallback facts
├── .github/
│   └── workflows/
│       └── update.yml # daily cron action
├── fact.svg           # auto-generated (do not edit manually)
├── requirements.txt
├── README.md
└── .gitignore
```

## palette

| Token | Hex |
|---|---|
| Void Black | `#0a0a0a` |
| Acid Yellow | `#e8ff00` |
| Dim Yellow | `#b8cc00` |
| Ghost White | `#f0f0f0` |

---

<sub>powered by [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl) · auto-updated daily via GitHub Actions</sub>