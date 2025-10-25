#!/usr/bin/env python3
"""
🔍 GLF Audit — Auditoría de visibilidad técnica en GitHub
Detecta archivos ignorados por .gitignore y excluidos por .gitattributes
Registra resultados en build.log con acrónimos: [GLF], [IGN], [EXC], [FOR]
"""

import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
BUILD_LOG = REPO_ROOT / "build.log"
GITATTRIBUTES = REPO_ROOT / ".gitattributes"
GITIGNORE = REPO_ROOT / ".gitignore"

def get_git_ignored():
    result = subprocess.run(["git", "ls-files", "--others", "--ignored", "--exclude-standard"],
                            capture_output=True, text=True)
    return set(result.stdout.strip().splitlines())

def get_all_files():
    return {str(p.relative_to(REPO_ROOT)) for p in REPO_ROOT.rglob("*") if p.is_file()}

def parse_gitattributes():
    excluded = set()
    forced = {}
    if not GITATTRIBUTES.exists():
        return excluded, forced
    with GITATTRIBUTES.open() as f:
        for line in f:
            line = line.strip()
            if "linguist-generated" in line or "linguist-documentation" in line:
                excluded.add(line.split()[0].rstrip("/"))
            elif "linguist-language=" in line:
                path, lang = line.split("linguist-language=")
                forced[path.strip()] = lang.strip()
    return excluded, forced

def audit():
    ignored = get_git_ignored()
    all_files = get_all_files()
    excluded, forced = parse_gitattributes()

    with BUILD_LOG.open("a") as log:
        log.write("\n[GLF] Auditoría de visibilidad técnica\n")
        for f in sorted(all_files):
            status = []
            if f in ignored:
                status.append("[IGN]")
            for excl in excluded:
                if f.startswith(excl):
                    status.append("[EXC]")
            for path in forced:
                if f.startswith(path) or f.endswith(path):
                    status.append(f"[FOR:{forced[path]}]")
            if status:
                log.write(f"{' '.join(status)} {f}\n")

if __name__ == "__main__":
    audit()
