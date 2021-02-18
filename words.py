#!/usr/bin/env python3
"""Retrieve and print words from a given URL.


Usage:

    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch list of words form a URL.


    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

    for word in story_words:
        print(word)

        
def print_items(items):
    """Print given iterabe object, one per line


    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)

        
def main(url):
    """Print each word from a text UTF-8 document by a given URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    items = fetch_words(url)
    print_items(items)
        
    
if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
