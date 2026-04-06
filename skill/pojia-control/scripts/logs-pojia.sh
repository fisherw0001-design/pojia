#!/usr/bin/env bash
set -euo pipefail
journalctl --user -u openclaw-session-patcher -n 50 --no-pager
