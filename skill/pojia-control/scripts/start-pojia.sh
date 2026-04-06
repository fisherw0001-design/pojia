#!/usr/bin/env bash
set -euo pipefail
systemctl --user start openclaw-session-patcher
systemctl --user status openclaw-session-patcher --no-pager
