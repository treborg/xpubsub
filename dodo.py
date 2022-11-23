from tasks.readme import compose_readme


def task_readme():
    """Create README.md from .readme.tpl"""

    return {
        "actions": [compose_readme],
    }


def task_hi():
    """hello cmd"""
    msg = 3 * "hi! "
    return {
        "actions": ["echo %s " % msg],
        "verbosity": 2,
    }
