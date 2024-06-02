# Twitter-Random-Bot
Bot that posts random letters with an image to Twitter.

## Config
This is an example for your `config.json`.
```
{
"CONSUMER_KEY": "a",
"CONSUMER_SECRET": "b",
"BEARER": "c",
"ACCESS": "d",
"ACCESS_SECRET": "e",
"COLORS": [
["#EAEBED", "#006989"],
["#F1DEDE", "#BBACC1"],
["#3A405A", "#F9DEC9"],
["#FFF8F0", "#9E2B25"],
["#001011", "#758BFD"],
["#50514F", "#BCB8B1"],
["#8BE8CB", "#303633"],
["#E6E6E6", "#FF8552"],
["#39393A", "#FF8552"]
],
"FONT_PATH": "JetBrainsMono-Bold.ttf",
"FONT_SIZE": 512,
"SMALL_FONT_SIZE": 64,
"PADDING": 64,
"HEIGHT": 810,
"BOTTOM_TEXT": "actually random letters every 10 minutes",
"CHAR_POOL": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
"MAX_LENGTH": 8,
"MIN_LENGTH": 3,
"TIME_BETWEEN_TWEETS": 600
}
```
Place all of the API keys into the correct places. The `COLORS` field takes an array of two hex codes, the first one is the background and the second one is the foreground. `TIME_BETWEEN_TWEETS` is in seconds.

**WARNING: YOU WILL PROBABLY GET RATE LIMITED WHEN USING THIS LMAO**
