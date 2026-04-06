# Pojia / 破甲

Pojia is a lightweight OpenClaw session patcher setup built as an external script + daemon + systemd service + control skill.

破甲是一个轻量级 OpenClaw 会话修补方案，采用“外挂脚本 + 常驻 daemon + systemd service + 控制 skill”的结构。

## What it does / 它做什么

- Scans OpenClaw session JSONL files
- Detects assistant refusal/error text
- Patches matched messages with a placeholder reply
- Runs continuously as a user-level systemd service
- Can be controlled with simple commands or a skill wrapper

- 扫描 OpenClaw 的 session JSONL 文件
- 识别 assistant 的拒绝/错误文本
- 将命中内容替换为占位回复
- 以 user-level systemd service 常驻运行
- 可通过简单命令或控制 skill 操作

## Structure / 项目结构

```text
scripts/openclaw_session_patcher.py
scripts/openclaw_session_patcher_daemon.py
systemd/openclaw-session-patcher.service
skill/pojia-control/
```

## Quick start / 快速开始

### 1) One-shot patch / 单次执行

```bash
python3 scripts/openclaw_session_patcher.py --latest --dry-run
python3 scripts/openclaw_session_patcher.py --latest
```

### 2) Install service / 安装常驻服务

```bash
mkdir -p ~/.config/systemd/user
cp systemd/openclaw-session-patcher.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now openclaw-session-patcher
```

### 3) Control / 控制命令

```bash
systemctl --user start openclaw-session-patcher
systemctl --user stop openclaw-session-patcher
systemctl --user status openclaw-session-patcher --no-pager
journalctl --user -u openclaw-session-patcher -n 50 --no-pager
```

## Notes / 说明

- This is **not** a native OpenClaw plugin.
- It is an external patcher workflow around OpenClaw session files.
- Skill and service are separate layers by design.

- 这**不是** OpenClaw 原生插件。
- 它是围绕 OpenClaw session 文件工作的外部修补方案。
- skill 和 service 是刻意拆开的两层。

## Acknowledgements / 致谢

This project was inspired by and references the following repository:

本项目参考并致谢以下仓库：

- ryfineZ / codex-session-patcher  
  https://github.com/ryfineZ/codex-session-patcher

The original repository helped shape the session-patching approach, while this project adapts the idea for OpenClaw-oriented workflows.

原仓库提供了 session patching 的核心思路，本项目是在这个思路基础上，针对 OpenClaw 工作流做的适配。
