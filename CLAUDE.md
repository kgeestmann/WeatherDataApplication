# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Weather Data Application fetches the current weather for a city from OpenWeatherMap on an interval, stores it in SQLite, and serves the stored data through a FastAPI endpoint. The README, the code comments and the CLI prompts are in **German**, so keep it that way. The main dev machine is Windows.

## Commands

```bash
pip install -r requirements.txt     # in a venv (.venv/ is gitignored)
cp .env_example .env                # then set OPENWEATHER_API_KEY
python main.py                      # interactive: choose or create a config, then fetches until Ctrl+C
uvicorn app.api:app --reload        # GET /weather and GET /weather?city=<name>
```

There are no tests and no linter yet.

## Code comments

- Give functions and methods a short docstring directly under the signature that says what they do. Mention parameters or return values only when they aren't obvious.
- Keep inline comments short, and add them only where the code isn't self-explanatory. They describe the current code.
- Don't write comments about history or the change itself ("previously", "now", "fixed", "without this … would …"), comments that only restate the code, or long justifications. Those belong in the commit message or the PR description.

## Architecture

- **Two independent processes, one database.** `main.py` (CLI + fetch loop) writes, and `app/api.py` (FastAPI) reads. They share nothing except the SQLite files `weather.db` and `config.db` in the repo root (gitignored, paths in `app/database.py`).
- **Fetch loop:** `main.py` asks for a config (stored city, new city + interval, or the default Bremen/1800 s). It then calls `periodic_scheduler.start_scheduler(weather_task(city), interval)`, a daemon thread with a `while True: task(); sleep(interval)` loop. The main thread just sleeps until Ctrl+C.
- **`app/weather_api.py`** loads `.env` at import time. `get_weather_data(city)` returns a flat dict (`city, description, temperature, humidity, rain_1h, snow_1h, timestamp`), or `{"error": ...}` on request errors. If the key is missing it **raises** instead of returning an error dict.
- **`app/database.py`** uses plain `sqlite3` with one connection per call. Tables are created with `CREATE TABLE IF NOT EXISTS`, and there are no migrations. Rows come back as tuples, and `api.py` maps the `weather` columns **by index**. If you change the table, update that mapping too.
- **Roadmap:** the README's "Funktionale Anforderungen" are the assignment's levels 1–3. Level 1 and part of level 2 (configurable city/interval, persisted) are done. The GUI and search are not.

## Keeping docs in sync

The README is the documentation (requirements, API key setup, how to start). If a change affects setup, configuration, endpoints or which levels are done, update the README **in the same PR**. If the README and the code disagree, the code wins: fix the README, or file an issue if the code is wrong.

## Filing issues

If you find a bug, a gap or a docs/code mismatch outside the current task, **file it right away** with `gh issue create`. Don't silently fix it inside an unrelated change. Include the `file:line`, a concrete failure scenario and the expected behaviour. Mention the issue number in your summary or PR description.

## Git & PR workflow

Every change (feature, fix or docs) starts from a GitHub issue and gets its own branch and PR:

1. **Issue:** use the existing one, or create it first with `gh issue create`. One issue = one branch = one PR.
2. **Branch from the issue:**
   ```bash
   gh issue develop <n> --name <type>/<n>-short-description --base master --checkout
   ```
   This links the branch under the issue's *Development* section. `<type>` is the Conventional Commit type (`feat`, `fix`, `docs`, …). Never commit directly to `master`.
3. **Commit** using Conventional Commits.
4. **Before the PR:** run what you changed (`python main.py` / `uvicorn app.api:app`), since there is no test suite yet.
5. **PR:** put `Closes #<n>` in the description so the merge closes the issue and links it to the PR.
6. **Review and merge:** the `claude-code-review` workflow reviews each PR automatically. For an on-demand review or a question, write `@claude` in a PR or issue comment. Act on valid findings, then merge with `gh pr merge <n> --merge --delete-branch`.

No confirmation is needed in this repo to commit, push, open or merge your own PRs (approved by the owner). Force-push and history rewrites still need explicit approval.

Gotchas for the review workflow:

- It does not review PRs that change `.github/workflows/claude*.yml`, because the action only runs when the workflow file matches `master`.
- It skips PRs that Claude has already commented on. Use `@claude` to get a re-review.
