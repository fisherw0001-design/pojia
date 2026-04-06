#!/usr/bin/env bash
set -euo pipefail
systemctl --user stop openclaw-session-patcher
systemctl --user status openclaw-session-patcher --no-pager || true
