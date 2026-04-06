#!/usr/bin/env python3
from __future__ import annotations
import os, sys, time, subprocess
PYTHON = sys.executable or 'python3'
PATCHER = '/root/tmp/codex-session-patcher/openclaw_session_patcher.py'
INTERVAL = int(os.environ.get('OPENCLAW_PATCHER_INTERVAL', '20'))

print(f'[openclaw-session-patcher] start interval={INTERVAL}s', flush=True)
while True:
    try:
        proc = subprocess.run([PYTHON, PATCHER, '--latest'], capture_output=True, text=True)
        out = (proc.stdout or '').strip()
        err = (proc.stderr or '').strip()
        if out:
            print(out, flush=True)
        if err:
            print(err, file=sys.stderr, flush=True)
    except Exception as e:
        print(f'[openclaw-session-patcher] error: {e}', file=sys.stderr, flush=True)
    time.sleep(INTERVAL)
