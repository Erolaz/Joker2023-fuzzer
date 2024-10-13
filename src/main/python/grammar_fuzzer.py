import random
import string
from html5lib import HTMLParser

def return_null():
    pass

def random_str(size=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, k=size))

def nested_tags(max_depth=30, current_depth=0):
    if current_depth > max_depth:
        return random_str()
    
    tag = random.choice(['section', 'article', 'header', 'footer', 'p', 'em'])
    inner_html = nested_tags(max_depth, current_depth + 1)
    return f"<{tag}>{inner_html}</{tag}>"

def random_attrs():
    tags = ['article', 'nav', 'aside', 'blockquote', 'code']
    html_components = ['<!DOCTYPE html><html><head><title>Page</title></head><body>']
    
    for _ in range(random.randint(2, 4)):
        tag = random.choice(tags)
        if random.random() < 0.5:
            attr = f"someAttr='{random_str()}'"
            html_components.append(f"<{tag} {attr}>{random_str()}</{tag}>")
        else:
            html_components.append(f"<{tag}>{random_str()}</{tag}>")
    
    html_components.append('</body></html>')
    return ''.join(html_components)

def simple_html_snippet():
    tag = random.choice(['div', 'span', 'p', 'b', 'i', 'u'])
    content = random_str()
    
    if random.random() < 0.3:
        attr = f"{random_str()}='{random_str()}'"
        return f"<{tag} {attr}>{content}</{tag}>"
    else:
        return f"<{tag}>{content}</{tag}>"

def missing_closing_tags():
    tags = ['table', 'tr', 'td', 'th', 'div', 'span', 'ul', 'li']
    html_components = ['<!DOCTYPE html><html><body>']
    
    for _ in range(random.randint(3, 6)):
        tag = random.choice(tags)
        html_components.append(f"<{tag}>{random_str()}")
        if random.random() >= 0.4:
            html_components.append(f"</{tag}>")
    
    html_components.append('</body></html>')
    return ''.join(html_components)

def weird_chars():
    special_chars = ['<', '>', '&', '#', '%', '\x00', '\x1F', '😊', '‼']
    html_components = ['<!DOCTYPE html><html><body>']
    
    for _ in range(random.randint(3, 7)):
        tag = random.choice(['header', 'footer', 'section'])
        content = ''.join(random.choice(string.ascii_letters + random.choice(special_chars)) for _ in range(10))
        html_components.append(f"<{tag}>{content}</{tag}>")
    
    html_components.append('</body></html>')
    return ''.join(html_components)

def broken_links():
    html_components = ['<!DOCTYPE html><html><body>']
    
    for _ in range(random.randint(2, 5)):
        href = random.choice(['', '#', 'http:// ', 'example.com'])
        link_text = random_str()
        html_components.append(f'<a href="{href}">{link_text}</a>')
    
    html_components.append('</body></html>')
    return ''.join(html_components)

def bad_escapes():
    html_components = ['<!DOCTYPE html><html><body>']
    
    for _ in range(random.randint(2, 5)):
        tag = random.choice(['h1', 'h2', 'h3', 'p'])
        content = "bla-bla-bla < and &"
        html_components.append(f"<{tag}>{content}</{tag}>")
    
    html_components.append('</body></html>')
    return ''.join(html_components)

def random_html():
    methods = [
        return_null,
        random_str,
        nested_tags,
        random_attrs,
        simple_html_snippet,
        missing_closing_tags,
        weird_chars,
        broken_links,
        bad_escapes
    ]
    
    method = random.choice(methods)
    return method()

def fuzz_parser(parse_func, cycles=10000):
    for _ in range(cycles):
        random_html_input = random_html()
        try:
            parse_func(random_html_input)
        except Exception as e:
            print(f"Error: {e} for input: {random_html_input}")

if __name__ == "__main__":
    parser = HTMLParser(strict=False)
    fuzz_parser(parser.parse)