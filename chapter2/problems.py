import re


def split_string():
    """Splitting Strings on Any of Multiple Delimiters"""
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    result = re.split(r'[;,\s]\s*', line)
    print(result)


def main():
    split_string()


if __name__ == "__main__":
    main()
