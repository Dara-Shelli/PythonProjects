from random import choice

# Makes sense:
new_line = '\n'

tag_low_python = 'python'
tag_low_java = 'java'
tag_low_c = 'c'
tag_low_vb = 'visual basic'
tag_low_cobol = 'cobol'
tag_low_js = 'javascript'

tag_upper_python = 'Python'
tag_upper_java = 'Java'
tag_upper_c = 'C'
tag_upper_vb = 'Visual Basic'
tag_upper_cobol = 'COBOL'
tag_upper_js = 'JavaScript'

programming_languages = [
    tag_low_python,
    tag_low_java,
    tag_low_c,
    tag_low_cobol,
    tag_low_vb,
    tag_low_js,
    tag_upper_python,
    tag_upper_java,
    tag_upper_c,
    tag_upper_cobol,
    tag_upper_vb,
    tag_upper_js
]


class TagCloud:

    def __init__(self):
        self.tags = {}

    def add(self, tag):
        tag = tag.lower()
        self.tags[tag] = self.tags.get(tag, 0) + 1

    def __getitem__(self, item):
        item = item.lower()
        return self.tags.get(item)

    def __setitem__(self, key, value):
        self.tags[key.lower()] = value

    def __iter__(self):
        return iter(self.tags)

    def __str__(self):
        return str(self.tags)


cloud = TagCloud()

for i in range(100):
    cloud.add(choice(programming_languages))

print(cloud)


