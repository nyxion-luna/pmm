# Changelog

## 3.0.0-beta.2

### added

- added red() helper to colors.py
- added Ctrl+C handling to avoid tracebacks in the cli output
- improved cli output formatting

### changed

- removed the cyan_bold() helper in favour of both cyan() and bold()
- introduced run() helper for centralized subprocess calls and SIGINT capturing
- replaced all subprocess.run() usage with run()
- renamed renderer.py to render.py

### fixed

- fixed renderer.py formatting bug that caused a crash
- fixed unhandled unknown managers causing a crash
- stopped using check=True in subprocess.run() which caused unhandled crashes

## 3.0.0-beta.1

- removed the if \_\_name\_\_ == \_\_main\_\_ code as it was unnecessary
- changed all calls to exit() to sys.exit()
- changed the description to use dynamic \_\_ini\_\_.py's \_\_description\_\_
- removed an unnecessary comment line in colors.py

## 3.0.0-beta.0

- initial version
