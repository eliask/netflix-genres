# List of Netflix genres

The repository contains a [pre-fetched list of available genres](genres.html)

# The Script to fetch and post-process the list of genres ##

The script ```fetch_data.sh``` fetches a list of Netflix genres using Netflix's
Falcor API.

To use the script, open up netflix.com in browser, log in, and grab your cookie
and "authURL" from some request with "pathEvaluator". Such as the following URL:
```https://www.netflix.com/api/shakti/de471087/pathEvaluator```

Substitute these values in the bash script and run it.

Usage:
1. Edit ```fetch_data.sh``` and substitute in values for ```COOKIE``` and ```AUTH_URL```.
2. Run ```fetch_data.sh```
3. Verify that all JSON files under data/ are actually JSON. Delete the
   offending files and re-run the script otherwise.
4. Run ```postprocess.py``` to generate a clean listing of the data and errors.
