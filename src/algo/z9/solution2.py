"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def get_latest(versions: list[str]) -> str:
    if not versions:
        return ''

    major, minor, patch = versions[0].split(".")
    
    for version in versions:
        second_major, second_minor, second_patch = version.split(".")
        if (int(second_major) > int(major)) or \
                (int(second_major) == int(major) and int(second_minor) > int(minor)) or \
                (int(second_major) == int(major) and int(second_minor) == int(minor) and int(second_patch) > int(patch)):
            major, minor, patch = second_major, second_minor, second_patch
        
    return f'{major}.{minor}.{patch}'


def next_version(version: str, level: int) -> str:
    """
    :param version: Current version
    :param level: Which part should be incremented; 0: major, 1: minor, 2: patch
    :return: Properly incremented version
    """
    major,minor,patch = version.split(".")
    major,minor,patch = int(major),int(minor),int(patch)
    if level == 0:
        major +=1
        patch = 0
        minor = 0

    elif level == 1:
        minor +=1
        patch = 0

    elif level == 2:
        patch += 1
        
    return f'{major}.{minor}.{patch}'
