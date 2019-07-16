# Change interval
## Rationale
If you were too generous with interval modifier, starting ease, easy bonus or whatever, you may have cards which now have intervals which are far too long. Jumping from 1 day to 10 days to 5 monthes... In this case, you may want to reduce the interval. Let's say divide the interval by two. So, you'll review more cards by day, you'll forget less, without having to reset everything.

This was a request from [reddit](https://www.reddit.com/r/Anki/comments/cc647d/is_there_a_way_to_reduce_the_delay_of_all_the/].

Or maybe you want to increase delay, because you found you were not generous enough with those parameters. This add-on also solve that.

## Usage
### All cards
In the main window, open ```tools``` then ```Shorten card delays```.

### Selected cards
In the browser, select every card you want to move. Select ```Edit```,
then select ```Shorten card delays```, and the delay will only be
added to cards which you have selecteds and which are due.

### Both cases
A window will ask you what percent you want to apply. If you enter 50, the delays will be divided by two. If you enter 200, the delay will be doubled. If you enter -100, then all cards will be considered late. Instead of being to review in 10 days, it'll be late by 10 days (I honestly don't know why you'd want to do that.)

If you always want to use the same percent, you can set it in the add-on configuration.

## Configuration
The documentation for the configuration file can be found on
[config.md](https://github.com/Arthur-Milchior/Anki-postpone-reviews/config.md).


## Internal
This add-on does not change any method. Of course, it adds actions in
menus.

## Version 2.0
There are nothing similar in version 2.0 as far as I know

## TODO
Merging in an inteligent way this add-on with [postpone reviews](https://ankiweb.net/shared/info/1152543397)

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>, Jasonbarc https://github.com/jasonsparc
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-change-interval
Addon number| [1869734310](https://ankiweb.net/shared/info/1869734310)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
