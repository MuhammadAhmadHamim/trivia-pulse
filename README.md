<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:0a0a0a,40:141414,100:0a0a0a&height=200&section=header&text=trivia-pulse&fontSize=52&fontColor=e8e8e8&fontAlignY=45&desc=A%20self-updating%20fact%20card%20for%20your%20GitHub%20profile&descAlignY=67&descColor=a0a0a0&animation=fadeIn&fontFamily=Georgia" alt="trivia-pulse banner"/>

<br/>

![Language](https://img.shields.io/badge/Python-Automation-e8e8e8?style=for-the-badge&logo=python&logoColor=black)
![Action](https://img.shields.io/badge/GitHub%20Actions-Daily%20Cron-141414?style=for-the-badge&logo=githubactions&logoColor=e8e8e8)
![Cost](https://img.shields.io/badge/Cost-%240-e8e8e8?style=for-the-badge&logoColor=black)
![Updates](https://img.shields.io/badge/Updates-Every%20Midnight%20UTC-a0a0a0?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-0a0a0a?style=for-the-badge&logoColor=e8e8e8)

<br/><br/>

> *"A GitHub Action runs every night. A new fact appears every morning. You do nothing."*

<br/>

</div>

---

## ◈ What This Is

A fully automated **random fact card** that lives on your GitHub profile. Every day at midnight UTC a GitHub Action wakes up, eeks out a random fact from the bunch, generates a styled SVG card in terminal silver and acid yellow on void black, and commits it back silently. Your profile README embeds it as a raw image URL. The card updates itself. You never touch it again.

---

## ◈ How It Works

```
   GitHub Actions  (midnight UTC, every day)
        │
        ▼
   app/services.py    →   fetches a random fact
                        falls back to fully random if facts.json is unreachable
        │
        ▼
   app/utils.py       →   wraps text, calculates height, escapes XML
        │
        ▼
   app/main.py        →   assembles and renders the SVG card
        │
        ▼
   fact.svg           →   committed back to the repo automatically
        │
        ▼
   profile README     →   embeds via raw GitHub URL — always fresh
```

---

## ◈ The Card

![Daily Fact](./fact.svg)

---

## ◈ Embed It

```md
![Trivia Pulse](https://raw.githubusercontent.com/MuhammadAhmadHamim/trivia-pulse/main/fact.svg)
```

Drop that into any README. The card auto-updates every 24 hours.

---

## ◈ Structure

```
trivia-pulse/
│
├── app/
│   ├── main.py          ←  SVG assembly and entry point
│   ├── utils.py         ←  text wrapping, height calc, XML escaping
│   └── services.py      ←  fact fetch with fallback to random
│
├── .github/
│   └── workflows/
│       └── update.yml   ←  daily cron GitHub Action
│
├── fact.svg             ←  auto-generated — do not edit manually
├── facts.json           ←  fallback facts — reduces API dependency
└── README.md
```

---

## ◈ Run Locally

```bash
git clone https://github.com/MuhammadAhmadHamim/trivia-pulse
python app/main.py
```

---

## ◈ The Palette

<div align="center">

| Token | Hex | Role |
|:---:|:---:|:---|
| **Void Black** | `#0a0a0a` | Card background |
| **Terminal White** | `#e8e8e8` | Primary text and borders |
| **Dim Silver** | `#a0a0a0` | Secondary text and accents |
| **Acid Yellow** | `#e8ff00` | Fact body text |

</div>

---

## ◈ Skills This Project Demonstrates

<div align="center">

![](https://img.shields.io/badge/Python-SVG%20Generation-e8e8e8?style=flat-square&logo=python&logoColor=black)
![](https://img.shields.io/badge/GitHub%20Actions-Cron%20Workflow-141414?style=flat-square&logo=githubactions&logoColor=e8e8e8)
![](https://img.shields.io/badge/Data-JSON%20Processing-a0a0a0?style=flat-square&logo=json&logoColor=black)
![](https://img.shields.io/badge/XML-SVG%20Templating-e8e8e8?style=flat-square&logo=html5&logoColor=black)
![](https://img.shields.io/badge/Automation-Zero%20Touch%20Pipeline-141414?style=flat-square&logo=buffer&logoColor=e8e8e8)
![](https://img.shields.io/badge/Git-Automated%20Commits-a0a0a0?style=flat-square&logo=git&logoColor=black)

</div>

---

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=venom&color=0:141414,40:0a0a0a,100:141414&height=100&section=footer&text=Updates%20itself.%20Every%20single%20night.&fontSize=16&fontColor=a0a0a0&fontAlignY=55&animation=fadeIn" alt="footer"/>

</div>