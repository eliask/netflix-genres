#!/usr/bin/env bash
set -eu

AUTH_URL=XXX_EDIT_THIS
COOKIE=XXX_EDIT_THIS

# *Potentially* edit this:
URL='https://www.netflix.com/api/shakti/de471087/pathEvaluator?withSize=true&materialize=true&model=harris'

COUNT=999 # 1000 appears to be too much at once.

for i in {0..99}
do
    start=$(($COUNT * i))
    end=$(($start + $COUNT - 1))
    data='{"paths":[["genres",['$(seq -s, $start $end)'],"name"]],"authURL":"'$AUTH_URL'"}'

    echo "Start: $start End: $end"

    mkdir -p data
    filename=data/out_$(printf %03d $i).json
    if test -f "$filename"; then
        continue
    fi

    curl "$URL"
         -H 'Origin: https://www.netflix.com' \
         -H 'Accept-Encoding: gzip, deflate, br' \
         -H 'Accept-Language: en-GB,en;q=0.8,en-US;q=0.6,fi;q=0.4' \
         -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36' \
         -H 'Content-Type: application/json' \
         -H 'Accept: application/json, text/javascript, */*' \
         -H 'Referer: https://www.netflix.com/browse' \
         -H "Cookie: $COOKIE" \
         -H 'Connection: keep-alive' \
         --data-binary "$data" \
         --compressed \
         -o "$filename"
done

echo "Done."
