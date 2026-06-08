<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

# Coding style

- Keep code simple. Don't over-engineer — follow industry norms and avoid unnecessary abstractions.
- Prefer the straightforward solution over the clever one. Three similar lines beats a premature helper.
- Add 1-line comments only where they help readability (non-obvious logic, the "why" not the "what").
- Don't add error handling, config options, or flexibility for cases that don't exist yet.

# Workflow

- Work step by step: break tasks into small steps, implement and verify one at a time rather than writing everything at once.

# README

Keep README.md accurate and right-sized for the project's current state — don't pad it with sections that have nothing real to say.

- Title + one-line description of what the project is and why it exists
- Tech stack (frameworks, languages, key libraries/services actually used)
- Prerequisites (runtime versions, accounts/services needed)
- Quick start: install + run, in copy-pasteable bash code blocks
- Available scripts/commands (from package.json or equivalent)
- Project structure: brief directory tree with one-line notes on key folders
- Environment variables / configuration, if any exist
- Deployment notes, if applicable
- License, if one is set

Formatting:
- Use tables for structured comparisons (scripts, env vars), prose for everything else
- All code blocks must have a language tag
- No marketing language ("powerful", "cutting-edge", "revolutionary") — describe what it does plainly
- No placeholder sections, fake badges, or links to things that don't exist (screenshots, social links, license) — add them when they're real

As the project grows real features, agents, or integrations, expand the README to cover them (e.g. a features table, architecture overview, comparison of variants) — but only once there's substance to document.
