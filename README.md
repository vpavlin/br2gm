# br2gm
BBC Radio 1 Chart to Google Music Playlist

## Why
I like the music BBC Radio 1 presents, but I am not big fan of listening to a radio - I like music not talking. This tool let's you automatically generate playlist from current BBC Radio 1 Official Chart which should be list of the most popular songs in UK - this promises certain level of quality (if you like mainstream, obviously).

## How
As you can see, there is nothing implemented yet, but I hope to get it done soon. I want to parse BBC Radio 1's chart site and then use Simon Weber's https://github.com/simon-weber/Unofficial-Google-Music-API to query for songs and add them to some playlist. I am thinking of hosting this on Openshift so that it can run without any manual interaction and playlist would just appear in my Google Music All Access profile regularly...we will se..:)

## How To Use
### Install
Simply run

```
python setup.py install
```

### Login information
This app needs to login to you Google Music account to be able to search through your All Access library and to create a playlist. You have 3 options to privide your login data

1. Use `-u` or `--user` option and you will be asked for password (password is not stored anywhere, thus you would have to provide it everytime)
2. Create a file `$HOME/.br2gm_auth` with content bellow
3. Create any file with the content bellow and pass it to the app via the option `-l` or `--credentials`

```
[credentials]
user=example@gmail.com
password=my_password
```

I strongly recommend to give it some sane access rights

```
chmod 600 $HOME/.br2gm_auth
```

### Show me my future playlist
You can use option `--dry-run` to parse a web site and query Google Music for songs. Output will be printed but nothing will be changed in your GM account

```
br2gm --dry-run http://www.bbc.co.uk/radio1/chart/updatesingles
```

### Create my playlist, please
Simply remove the `--dry-run` option and everything you see will be added to a [public playlist](https://play.google.com/music/playlist/AMaBXynqxZs9dl7PgifFI48_kzdgdiAa1mm6wcc3F392b7R2H-cwxaBFvMBiAHoncFlOD_wvpZ9vhfxWV5O-x5EdREDSIimz-g==) named `BBC Radio 1 YYYY-MM-DD`

```
br2gm [-u USER] [-l PATH_TO_CREDENTIALS] http://www.bbc.co.uk/radio1/chart/updatesingles
```


