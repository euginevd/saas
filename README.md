# SaaS

An early-stage Next.js + FastAPI app that uses OpenAI to generate cloud/security/AI project ideas.

<div align="center">

[![Stars](https://img.shields.io/github/stars/euginevd/saas?style=for-the-badge&logo=github)](https://github.com/euginevd/saas/stargazers)
[![Forks](https://img.shields.io/github/forks/euginevd/saas?style=for-the-badge&logo=github)](https://github.com/euginevd/saas/network/members)
[![Issues](https://img.shields.io/github/issues/euginevd/saas?style=for-the-badge&logo=github)](https://github.com/euginevd/saas/issues)
[![License](https://img.shields.io/badge/License-TBD-lightgrey?style=for-the-badge)](#-license)
[![Next.js](https://img.shields.io/badge/Next.js-16-000000?style=for-the-badge&logo=nextdotjs)](https://nextjs.org)

[![Email](https://img.shields.io/badge/Email-euginevd%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:euginevd@gmail.com)

</div>

<div align="center">

![Screenshot placeholder](./docs/screenshot.png)

</div>

> A screenshot will be added once the app has a UI worth showing — the current codebase is the default `create-next-app` landing page.

---

## 📖 What is this?

This repository is the starting point for a SaaS product. The frontend is a Next.js, React, TypeScript, and Tailwind CSS app; the backend is a small FastAPI service that calls the OpenAI API. The one feature shipped so far: the home page asks the backend for a project idea at the intersection of cloud, security, and AI, and renders the markdown response. This README documents the project as it stands and will expand as real features land.

---

## ✨ Feature highlights

| Category | Description | Link |
| --- | --- | --- |
| 🤖 AI project idea generator | Home page fetches a cloud/security/AI project idea from the backend and renders it as markdown | [app/page.tsx](./app/page.tsx) |
| 🔌 FastAPI backend | Python API that calls the OpenAI Responses API and serves the result over CORS | [api/index.py](./api/index.py) |
| 🏗️ App Router | Next.js 16 App Router project structure, ready for pages and layouts | [app/](./app) |
| 🎨 Styling | Tailwind CSS 4 configured for utility-first styling | [app/globals.css](./app/globals.css) |
| 🔠 Type safety | TypeScript configured across the project | [tsconfig.json](./tsconfig.json) |

---

## 🗂️ Feature directory

No features or agents have been built yet — this section will list them, grouped by category, as they're added.

---

## 🔍 Featured deep dives

### AI project idea generator

- Problem solved: coming up with a concrete, actionable project idea at the intersection of cloud, security, and AI takes time and research.
- Solution: the Next.js home page calls a FastAPI endpoint, which prompts OpenAI for a single short, actionable idea and returns it as markdown.
- Features:
  - Server-rendered page that fetches fresh data on every load (no caching)
  - FastAPI `/api` endpoint deployed as a Vercel Python serverless function, with CORS restricted to the local frontend origin in dev
  - Markdown rendering via `react-markdown` with Tailwind typography styling
- Tech stack: Next.js, React, FastAPI, OpenAI Python SDK (Responses API, `gpt-5`)
- Estimated running cost: roughly the cost of one short OpenAI `gpt-5` response per page load; negligible at low traffic, scales with visits.

---

## 🌳 Repository structure

```
saas/
├── app/
│   ├── layout.tsx       # Root layout
│   ├── page.tsx         # Home page (fetches and renders the project idea)
│   ├── globals.css      # Global styles (Tailwind)
│   └── favicon.ico
├── api/
│   └── index.py         # FastAPI app: /api endpoint calling OpenAI (Vercel Python function)
├── public/              # Static assets
├── requirements.txt     # Python dependencies
├── next.config.ts       # Next.js configuration
├── tsconfig.json        # TypeScript configuration
└── package.json         # Dependencies and scripts
```

---

## 🚀 Quick start

1. Install frontend and backend dependencies:

```bash
npm install
pip install -r requirements.txt
```

2. Add your OpenAI key to a `.env` file at the project root:

```bash
echo "OPENAI_API_KEY=sk-..." > .env
```

3. Start the backend, then the frontend (in separate terminals):

```bash
cd api && uvicorn index:app --reload --port 8000
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🧭 Learning roadmap

| Tier | Topic | Status |
| --- | --- | --- |
| Beginner | Run the dev server and edit `app/page.tsx` | ✅ |
| Beginner | Understand the App Router layout/page structure | ✅ |
| Beginner | Run the FastAPI backend and call the OpenAI API | ✅ |
| Intermediate | Add new routes and shared layouts | 🔜 |
| Intermediate | Connect a database and authentication | 🔜 |
| Advanced | Add background jobs, billing, and integrations | 🔜 |

---

## 🛠️ Tech stack

### Core Frameworks

| Tool | Purpose |
| --- | --- |
| Next.js 16 | React framework with App Router |
| React 19 | UI library |
| TypeScript | Static typing |

### Backend & Data

| Tool | Purpose |
| --- | --- |
| FastAPI | Python web framework serving the `/api` endpoint |
| Uvicorn | ASGI server for running the FastAPI app |
| python-dotenv | Loads the OpenAI API key from a `.env` file |

### Integrations

| Tool | Purpose |
| --- | --- |
| react-markdown | Renders the AI-generated idea as formatted markdown |

### AI & ML

| Tool | Purpose |
| --- | --- |
| OpenAI Python SDK | Calls the Responses API (`gpt-5`) to generate project ideas |

---

## 📊 Comparison table

There is only one variant of this project today, so a comparison table doesn't apply yet. This section will compare features across agents/variants once more than one exists.

---

## 💰 Use cases & ROI

No shipped features exist yet, so there are no realistic ROI figures to report. This section will describe, per feature: who it's for, time/cost saved, and break-even — based on real usage once available.

---

## 🤝 Contributing

This is a personal early-stage project. Questions and suggestions can go through [GitHub Issues](https://github.com/euginevd/saas/issues). Pull requests are welcome — please open an issue first to discuss significant changes before submitting one.

---

## 📡 Connect & Support

<div align="center">

[![Email](https://img.shields.io/badge/Email-euginevd%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:euginevd@gmail.com)
[![Issues](https://img.shields.io/github/issues/euginevd/saas?style=for-the-badge&logo=github)](https://github.com/euginevd/saas/issues)

</div>

---

## 🗺️ Roadmap

| Quarter | Goal | Status |
| --- | --- | --- |
| Current (Q2 2026) | Set up project scaffolding and tooling | ✅ |
| Current (Q2 2026) | Ship the AI project idea generator (frontend + backend) | ✅ |
| Next (Q3 2026) | Define and build the next core feature | 🔜 |
| Future | Add authentication, billing, and deployment pipeline | 🔜 |

---

## 📄 License

No license has been chosen yet. This section will be updated once one is selected.
