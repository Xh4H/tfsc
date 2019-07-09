# tfsc - Temporary File Source Code (disclosure script)
tfsc is an automated and standalone tool to find backup files that may disclose the website's source code.

## Usage example
tfcs.py is based in two required parameters (-u [url] and -f [file(s)]) and an optional one, -v (verbose):

```pyhton
python tfsc.py -u http://somesite.com/launcher -f index.php,stats.php
```

![example](https://xh4h.com/img/upload/tfsc3.png)

## Parameters
| Command                                                    | Description                                                             |
|------------------------------------------------------------|-------------------------------------------------------------------------|
| -f (--file)                                                | file (or comma separated list of files to be searched)                  |
| -u (--url)                                                 | base url                                                                |
| -v (--verbose)                                             | enable verbose debugging (accepts any value)                            |


## More info
More info about Temporary File Source Code Disclosure Vulnerability [here](https://www.rapid7.com/db/vulnerabilities/http-php-temporary-file-source-disclosure).

## Disclaimer
All the information in this repository is for educational purposes only. The author of the repository is not responsible for any misuse of the information. This script has been created for educational purposes.
