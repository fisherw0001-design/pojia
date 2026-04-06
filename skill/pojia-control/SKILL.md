---
name: pojia-control
description: Control the “破甲” OpenClaw session patcher service. Use when the user says 开破甲, 关破甲, 看破甲状态, 看破甲日志, or wants to manually start/stop/check/log the openclaw-session-patcher daemon.
---

# Pojia Control

## Overview

This skill controls the **破甲** service: `openclaw-session-patcher`.

Use this skill when the user wants to:
- start the service
- stop the service
- check service status
- view recent service logs
- understand whether 破甲 is a skill or a background service

## Core mapping

Natural-language commands map to these actions:

- **开破甲** → `systemctl --user start openclaw-session-patcher`
- **关破甲** → `systemctl --user stop openclaw-session-patcher`
- **看破甲状态** → `systemctl --user status openclaw-session-patcher --no-pager`
- **看破甲日志** → `journalctl --user -u openclaw-session-patcher -n 50 --no-pager`

Default behavior: execute directly and return the result briefly.

## Workflow

1. Treat **破甲** as the canonical alias for `openclaw-session-patcher`.
2. Use the matching script in `scripts/` when the request is one of the 4 fixed actions.
3. Reply with the concrete result, not an explanation dump.
4. If the service is missing, report that the systemd user unit is not installed.

## Scope and limits

This skill controls the service only. The actual patching logic lives outside the skill in:
- `/root/tmp/codex-session-patcher/openclaw_session_patcher.py`
- `/root/tmp/codex-session-patcher/openclaw_session_patcher_daemon.py`
- `/root/.config/systemd/user/openclaw-session-patcher.service`

Do not claim this skill itself is the daemon. The daemon is a separate systemd user service.

## scripts/

Use these wrappers for deterministic control:
- `scripts/start-pojia.sh`
- `scripts/stop-pojia.sh`
- `scripts/status-pojia.sh`
- `scripts/logs-pojia.sh`
