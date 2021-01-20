import os

from .util import is_doc, normalize_href

# normalize href to #foo/bar/section:id
def transform_href(href: str, rel_url: str):
    head, tail = os.path.split(href)

    num_hashtags = tail.count('#')

    if tail.startswith('#'):
        head, section = os.path.split(rel_url)
        section = os.path.splitext(section)[0]
        id = tail[1:]
    elif num_hashtags is 1:
        section, ext = tuple(os.path.splitext(tail))
        ids = str.split(ext, '#')
        if len(ids) > 1:
            id = ids[1]
        else:
            section, id = str.split(tail, '#')
        
        if head == '..':
            href = normalize_href(href, rel_url)
            return '#{}:{}'.format(href, id)

    elif num_hashtags is 0:
        if not is_doc(href):
            return href

        href = normalize_href(href, rel_url)
        return '#{}:'.format(href)

    if head != '':
        head += '/'

    return '#{}{}:{}'.format(head, section, id)

# normalize id to foo/bar/section:id
def transform_id(id: str, rel_url: str):
    head, tail = os.path.split(rel_url)
    section, _ = os.path.splitext(tail)

    if len(head) > 0:
        head += '/'

    return '{}{}:{}'.format(head, section, id)
