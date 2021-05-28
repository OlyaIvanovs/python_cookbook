from calendar import month_abbr
from collections import namedtuple
import re


def split_string():
    """Splitting Strings on Any of Multiple Delimiters"""
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    return re.split(r'[;,\s]\s*', line)


def match_end_string():
    """Matching Text at the Start or End of a String"""
    filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
    matching_files = [
        file for file in filenames if file.endswith(('.c', '.h'))]
    return matching_files


def change_date(m):
    month = month_abbr[int(m.group(1))]
    return f'{m.group(2)} {month} {m.group(3)}'


def find_all_matches():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    new_text = datepat.sub(change_date, text)
    print(new_text)
    for month, day, year in datepat.findall(text):
        print(f"{day}-{month}-{year}")


def replace_text():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scanner = re.finditer(pat, text)
    for m in scanner:
        yield Token(m.lastgroup, m.group())


def tokenize_text():
    """Tokenizing Text"""
    # define all possible tokens
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>\=)'
    WS = r'(?P<WS>\s+)'

    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    text = 'foo = 23 + 42 * 10'
    m = master_pat.findall(text)
    tokens = []
    for token in m:
        if token[0]:
            tok = Token('NAME', token[0])
        elif token[1]:
            tok = Token('NUM', token[1])
        elif token[2]:
            tok = Token('PLUS', token[2])
        elif token[3]:
            tok = Token('TIMES', token[3])
        elif token[4]:
            tok = Token('EQ', token[4])
        elif token[5]:
            tok = Token('WS', token[5])
        tokens.append(tok)
    print(tokens)

    tokens = []
    for tok in generate_tokens(master_pat, text):
        tokens.append(tok)
    print(tokens)


def main():
    tokenize_text()


if __name__ == "__main__":
    main()
