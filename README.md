# Pojia / 破甲

**Pojia** is an external OpenClaw session patcher built as a practical stack of:

- patch script
- daemon loop
- user-level systemd service
- control skill

**破甲** 是一个面向 OpenClaw 的外部 session patcher，采用以下实用结构：

- patch 脚本
- daemon 循环
- user-level systemd service
- 控制 skill

---

## Why this project / 这个项目是干什么的

Sometimes an OpenClaw session may contain assistant refusal text or error-shaped output that you want to patch in a controlled way.

有些时候，OpenClaw session 里会出现 assistant 的拒绝文本或错误形态输出，你可能希望用一种可控方式进行 patch。

Pojia provides a simple external workflow around session JSONL files instead of modifying OpenClaw itself.

Pojia 选择围绕 session JSONL 文件做外部处理，而不是直接改 OpenClaw 本体。

---

## What it does / 功能

- Scans OpenClaw session JSONL files
- Detects assistant refusal/error text
- Replaces matched text with a placeholder reply
- Removes `errorMessage` on patched assistant messages
- Creates `.bak` backups before writing
- Runs continuously through systemd if desired
- Can be controlled through a small skill wrapper

- 扫描 OpenClaw 的 session JSONL 文件
- 识别 assistant 的拒绝/错误文本
- 将命中文本替换成占位回复
- 对已 patch 的 assistant 消息移除 `errorMessage`
- 写回前自动创建 `.bak` 备份
- 如有需要可通过 systemd 常驻运行
- 可通过一个小型控制 skill 操作

---

## Project structure / 项目结构

```text
scripts/openclaw_session_patcher.py
scripts/openclaw_session_patcher_daemon.py
systemd/openclaw-session-patcher.service
skill/pojia-control/
```

---

## Quick start / 快速开始

### 1. One-shot patch / 单次执行

Dry run:

```bash
python3 scripts/openclaw_session_patcher.py --latest --dry-run
```

Real write:

```bash
python3 scripts/openclaw_session_patcher.py --latest
```

Patch all sessions:

```bash
python3 scripts/openclaw_session_patcher.py --all
```

### 2. Install the service / 安装常驻服务

```bash
mkdir -p ~/.config/systemd/user
cp systemd/openclaw-session-patcher.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now openclaw-session-patcher
```

### 3. Control commands / 控制命令

```bash
systemctl --user start openclaw-session-patcher
systemctl --user stop openclaw-session-patcher
systemctl --user status openclaw-session-patcher --no-pager
journalctl --user -u openclaw-session-patcher -n 50 --no-pager
```

---

## Why not skill-only / 为什么不能只做 skill

A skill is good for control entrypoints, but not for long-running background execution.

skill 很适合做控制入口，但不适合做长期后台常驻执行。

That is why this project separates:

- **service/daemon** for background work
- **skill** for natural-language control

所以本项目刻意拆成：

- **service/daemon** 负责后台工作
- **skill** 负责自然语言控制

---

## Notes / 说明

- This is **not** a native OpenClaw plugin.
- It is an external patching workflow.
- The default target is OpenClaw session JSONL files.
- Review and adjust matching rules before using in wider production scenarios.

- 这**不是** OpenClaw 原生插件。
- 这是一个外部 patch 工作流。
- 默认目标是 OpenClaw 的 session JSONL 文件。
- 在更大范围生产使用前，请先检查并调整匹配规则。

---

## Acknowledgements / 致谢

This project was inspired by and references the following repository:

本项目参考并致谢以下仓库：

- **ryfineZ / codex-session-patcher**  
  https://github.com/ryfineZ/codex-session-patcher

The original repository helped shape the session-patching idea, while this project adapts that idea for OpenClaw-oriented workflows.

原仓库提供了 session patching 的重要思路，本项目是在该思路基础上做的 OpenClaw 定向适配。
