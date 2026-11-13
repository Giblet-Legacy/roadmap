"""
audit.py — local repo auditor for the Forge Stack.
"""
import os
import re
import subprocess

repos = sorted([d for d in os.listdir('.') if os.path.isdir(d) and os.path.isdir(os.path.join(d, '.git')) and d != 'old-substrate'])

print(f"🔍 Auditing {len(repos)} repositories...\n")

failures = 0

for repo in repos:
    os.chdir(repo)
    issues = []

    # 1. Check required files
    required = ['VERSION', 'CHANGELOG.md', 'CLAUDE.md', 'SPEC.md', '.gitattributes', '.gitignore']
    for f in required:
        if not os.path.exists(f):
            issues.append(f"missing {f}")

    # 2. Check git status
    try:
        status = subprocess.check_output(['git', 'status', '--porcelain']).decode().strip()
        if status:
            issues.append("uncommitted changes")
    except Exception:
        issues.append("git status failed")

    # 3. Check version vs changelog
    if os.path.exists('VERSION') and os.path.exists('CHANGELOG.md'):
        try:
            with open('VERSION') as f:
                v_text = f.read()
            # Strip comment lines and blank lines, then find the version
            version_lines = [
                ln.strip() for ln in v_text.splitlines()
                if ln.strip() and not ln.strip().startswith('#')
            ]
            v_text_clean = '\n'.join(version_lines)
            match = re.search(r'\b(\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?)\b', v_text_clean)
            
            if not match:
                issues.append("VERSION has no semver format")
            else:
                v = match.group(1)
                with open('CHANGELOG.md') as f:
                    c_text = f.read()
                
                # Look for the version in a header, e.g., ## [v1.0.0] or ## [1.0.0]
                if f"[v{v}]" not in c_text and f"[{v}]" not in c_text:
                    issues.append(f"VERSION {v} not found in CHANGELOG")
        except Exception as e:
            issues.append(f"version check failed: {e}")

    if issues:
        print(f"❌ {repo}")
        for i in issues:
            print(f"   - {i}")
        failures += 1
    else:
        print(f"✅ {repo}")

    os.chdir('..')

print(f"\nAudit complete: {len(repos) - failures} clean, {failures} with issues.")
