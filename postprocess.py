#!/usr/bin/env python3
import json
import pandas as pd

genres={}

df_genres = pd.read_csv('genres.csv')

for id_, name in zip(df_genres.id, df_genres.name):
    genres[int(id_)] = name

with open('genres.json', 'wt') as fh:
    json.dump(genres, fh, ensure_ascii=False, sort_keys=True, indent=2)

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
