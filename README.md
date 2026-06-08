# ProjectIdeas AI

An early-stage Next.js + FastAPI app that uses OpenAI to generate cloud/security/AI project ideas.

<div align="center">

[![Stars](https://img.shields.io/github/stars/euginevd/projectideas-ai?style=for-the-badge&logo=github)](https://github.com/euginevd/projectideas-ai/stargazers)
[![Forks](https://img.shields.io/github/forks/euginevd/projectideas-ai?style=for-the-badge&logo=github)](https://github.com/euginevd/projectideas-ai/network/members)
[![Issues](https://img.shields.io/github/issues/euginevd/projectideas-ai?style=for-the-badge&logo=github)](https://github.com/euginevd/projectideas-ai/issues)
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

This repository is the starting point for a SaaS product. The frontend is a Next.js, React, TypeScript, and Tailwind CSS app; the backend is a small FastAPI service that calls the OpenAI API and persists results to Postgres. The home page asks the backend for a project idea at the intersection of cloud, security, and AI and renders the markdown response, users sign in with Clerk, and free accounts are capped at three generations before being routed to a Clerk-powered pricing page to upgrade. This README documents the project as it stands and will expand as real features land.

---

## ✨ Feature highlights

| Category | Description | Link |
| --- | --- | --- |
| 🤖 AI project idea generator | Home page fetches a cloud/security/AI project idea from the backend and renders it as markdown | [app/page.tsx](./app/page.tsx) |
| 🔌 FastAPI backend | Python API that calls the OpenAI Responses API, stores ideas in Postgres, and serves the result over CORS | [api/index.py](./api/index.py) |
| 🔐 Authentication | Clerk-powered sign-in and account controls on the home page | [proxy.ts](./proxy.ts) |
| 💳 Pricing & plans | Free accounts are capped at three generations; a Clerk pricing table handles upgrades to Premium | [app/pricing/page.tsx](./app/pricing/page.tsx) |
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
- Solution: the Next.js home page calls a FastAPI endpoint, which prompts OpenAI for a single short, actionable idea, stores it in Postgres, and returns it as markdown.
- Features:
  - Server-rendered page that fetches fresh data on every load (no caching)
  - FastAPI `/api` endpoint deployed as a Vercel Python serverless function, with CORS restricted to the local frontend origin in dev
  - Every generated idea is persisted to a Postgres `ideas` table (created on startup) and listable via `/api/ideas`
  - Markdown rendering via `react-markdown` with Tailwind typography styling
- Tech stack: Next.js, React, FastAPI, OpenAI Python SDK (Responses API, `gpt-5`), Postgres via `psycopg`
- Estimated running cost: roughly the cost of one short OpenAI `gpt-5` response per generation, plus a small Postgres instance; negligible at low traffic, scales with visits.

### Authentication & plans

- Problem solved: anonymous usage can't be metered or monetized, and there was no way to distinguish free from paying users.
- Solution: Clerk handles sign-in/sign-up and account state; the home page tracks how many ideas a session has generated and routes free users who hit the cap to a pricing page backed by Clerk's billing components.
- Features:
  - Clerk `ClerkProvider` wraps the app, with a `proxy.ts` request handler (this Next.js version's renamed `middleware.ts`) protecting routes
  - Sign-in button and account menu (`UserButton`) on the home page
  - Free accounts are capped at three generations (`FREE_GENERATION_LIMIT`); Premium plan subscribers (checked via `useAuth().has`) get unlimited generations
  - `/pricing` page renders Clerk's `PricingTable` for upgrading to Premium
- Tech stack: `@clerk/nextjs`, Next.js App Router
- Estimated running cost: Clerk's free tier covers low-volume usage; costs scale with monthly active users once past the free tier.

---

## 🌳 Repository structure

```
projectideas-ai/
├── app/
│   ├── layout.tsx       # Root layout (wraps the app in ClerkProvider)
│   ├── page.tsx         # Home page (fetches/renders ideas, sign-in, generation cap)
│   ├── pricing/
│   │   └── page.tsx     # Pricing page (Clerk PricingTable)
│   ├── globals.css      # Global styles (Tailwind)
│   └── favicon.ico
├── api/
│   └── index.py         # FastAPI app: /api and /api/ideas endpoints (OpenAI + Postgres)
├── public/              # Static assets
├── proxy.ts             # Clerk request handler (this Next.js version's middleware)
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

2. Add your OpenAI key, Postgres connection string, and Clerk keys to a `.env` file at the project root:

```bash
cat <<'EOF' > .env
OPENAI_API_KEY=sk-...
DATABASE_URL=postgresql://user:password@host:5432/dbname
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_...
CLERK_SECRET_KEY=sk_...
EOF
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
| Intermediate | Add new routes and shared layouts | ✅ |
| Intermediate | Connect a database and authentication | ✅ |
| Intermediate | Add billing and plan-based feature gating | ✅ |
| Advanced | Add background jobs and third-party integrations | 🔜 |

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
| FastAPI | Python web framework serving the `/api` and `/api/ideas` endpoints |
| Uvicorn | ASGI server for running the FastAPI app |
| python-dotenv | Loads environment variables (API keys, database URL) from a `.env` file |
| Postgres (`psycopg`) | Stores generated ideas in an `ideas` table |

### Integrations

| Tool | Purpose |
| --- | --- |
| react-markdown | Renders the AI-generated idea as formatted markdown |
| Clerk (`@clerk/nextjs`) | Sign-in, account management, plan checks, and pricing/billing UI |

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

This is a personal early-stage project. Questions and suggestions can go through [GitHub Issues](https://github.com/euginevd/projectideas-ai/issues). Pull requests are welcome — please open an issue first to discuss significant changes before submitting one.

---

## 📡 Connect & Support

<div align="center">

[![Email](https://img.shields.io/badge/Email-euginevd%40gmail.com-D14836?style=for-the-badge&logo=gmail)](mailto:euginevd@gmail.com)
[![Issues](https://img.shields.io/github/issues/euginevd/projectideas-ai?style=for-the-badge&logo=github)](https://github.com/euginevd/projectideas-ai/issues)

</div>

---

## 🗺️ Roadmap

| Quarter | Goal | Status |
| --- | --- | --- |
| Current (Q2 2026) | Set up project scaffolding and tooling | ✅ |
| Current (Q2 2026) | Ship the AI project idea generator (frontend + backend) | ✅ |
| Current (Q2 2026) | Add authentication, plan-based limits, and a pricing page | ✅ |
| Next (Q3 2026) | Add a deployment pipeline and surface saved idea history | 🔜 |
| Future | Add background jobs and third-party integrations | 🔜 |

---

## 📄 License

No license has been chosen yet. This section will be updated once one is selected.
