from pathlib import Path

def absolutepath(filepath):
    """defines absolute path"""
    relative = Path(filepath)
    return relative.absolute()
