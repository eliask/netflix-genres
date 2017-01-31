#!/usr/bin/env python3
import json
import sys
import glob

genres={}
errors=[]

for f in glob.glob('data/out_*.json'):
    x = json.load(open(f))

    if 'genres' in x['value']:
        for key, value in x['value']['genres'].items():
            if key in ('size', '$size'):
                continue

            assert value['$size'] == 1, value
            genres[key] = value['name']

    for key, value in x['error'].items():
        assert key == 'innerErrors', key
        for e in value:
            errors.append(e)

with open('genres.json', 'wt') as fh:
    json.dump(genres, fh, ensure_ascii=False, sort_keys=True, indent=2)
with open('errors.json', 'wt') as fh:
    json.dump(errors, fh, ensure_ascii=False, sort_keys=True, indent=2)

with open('genres.csv', 'wt') as fh:
    for id_, name in sorted(genres.items(), key=lambda x:int(x[0])):
        print('{},{}'.format(id_, name), file=fh)
with open('errors.csv', 'wt') as fh:
    for e in errors:
        print('{},{}'.format(e['pql'][1][0], e['message'] or ''), file=fh)

body = '\n'.join(
    '<li><a href="https://www.netflix.com/browse/genre/{}">{}</a></li>'.format(id_, name)
    for id_, name in sorted(genres.items(), key=lambda x:int(x[0]))
)

html = '''
<html>
<body>
<p>Number of genres: {num_genres} MinID={min_id} MaxID={max_id}</p>
<ul>
{body}
</ul>
</body>
</html>
'''.strip().format(
    num_genres=len(genres),
    min_id=min(map(int, genres)),
    max_id=max(map(int, genres)),
    body=body,
)
with open('genres.html', 'wt') as fh:
    fh.write(html)
