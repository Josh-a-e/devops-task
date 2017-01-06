
# `name_old_repositories.pex`

**Parses a target html file (default git.html) and prints a list (repository name and days since last updated) of contained repositories that are older than a given number of days (default 30).**

Packaged as a [.pex (python executable)](https://pex.readthedocs.io/en/stable/) file so dependencies (namely [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/) and [dateparser](https://dateparser.readthedocs.io/en/latest/)) don't need to be installed wherever it's being run.

Runs on both python 2.7 and 3.6

## Example Usage

```sh
    $ ./name_old_repositories.pex
    client-web-application/configs/babel-preset-lloyds - last updated approximately 34 days ago
    core-payments-webapi                               - last updated approximately 48 days ago
    sc-webapi-dcfm-cj                                  - last updated approximately 55 days ago
    sc-webapi-dcfm                                     - last updated approximately 55 days ago
    client-web-application/servicing/ib                - last updated approximately 62 days ago
    ...
```

```sh
    $ ./name_old_repositories.pex -h
    usage: name_old_repositories.py [-h] [-f FILE] [-d DAYS_OLD]

    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  target file to parse for old repos, default ./git.html
      -d DAYS_OLD, --days-old DAYS_OLD
                            how recently a repo needs to have been updated,
                            default 30
    ...
```
