from conf import setting


def log(content: str = ...):
    with open(setting.LOG_DIR, mode='at', encoding='utf-8') as f:
        f.write(content)
