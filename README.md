# my_test

Test repository for sharing Claude Code skills.

## Skills

| Skill | What it does |
| --- | --- |
| `herdr-agent-fleet` | Runs Claude, a DeepSeek-backed OpenCode agent and (when available) Codex as [Herdr](https://herdr.dev) panes working one task together. Two unanimous gates: no code before every seat returns `PLAN-APPROVED`, nothing pushed or deployed before every seat returns `IMPL-APPROVED`. |

> The skill files are not in this repo yet. Once a skill folder is added under `skills/`, install it as shown below.

## Install

Copy or symlink a skill folder into `~/.claude/skills/`:

```bash
git clone https://github.com/zexu999/my_test.git
ln -s "$PWD/my_test/skills/herdr-agent-fleet" ~/.claude/skills/herdr-agent-fleet
```

### Requirements for `herdr-agent-fleet`

- [Herdr](https://herdr.dev), with Claude Code started inside a Herdr pane
- [OpenCode](https://opencode.ai) on `PATH`
- `DEEPSEEK_API_KEY` exported in the shell Herdr panes start
- Optional: [Codex CLI](https://github.com/openai/codex) for the third seat (the skill checks whether it actually runs; a two-seat roster needs your explicit OK)

## Hello world

A minimal Python 3 program (standard library only).

```bash
python3 hello.py            # prints: Hello, world!
python3 -m unittest -v      # runs test_hello.py
```
