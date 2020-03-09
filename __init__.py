from anki.find import Finder
from anki.hooks import addHook
from anki.lang import _
from aqt import mw
from aqt.qt import QAction
from aqt.utils import getText, showWarning, tooltip

from .config import *

QUEUE_REV = 2

# From https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except


def RepresentsInt(s):
    try:
        return int(s)
    except ValueError:
        return None


def getPercent():
    return getPercentWithResponse()[0]


def getPercentWithResponse():
    s = getUserOption("percent")
    if s is None:
        (s, r) = getText(
            "By which percent do you want to increase/decrease percent for your card. (50% means half, 200% means double...)")
    else:
        r = " in the add-on configuration"
    if r:
        return (RepresentsInt(s), ".")
    return (None, False)


def getReviewCards():
    finder = Finder(mw.col)
    cids = finder.findCards("is:review")
    return cids


def decreaseDelay(cids):
    (percent, percentResp) = getPercentWithResponse()
    if percent is None:
        if percentResp:
            showWarning("Please enter an integral number of days{percentResp}")
        return

    mw.checkpoint("Decreasing percent")
    mw.progress.start()

    for cid in cids:
        card = mw.col.getCard(cid)
        whichDue = "odue" if card.odid else "due"
        if getattr(card, whichDue) < card.col.sched.today and not getUserOption("Also change late cards", False):
            continue
        if card.type != QUEUE_REV:
            continue
        curentIvl = card.ivl if getUserOption("Consider last review date", False) else getattr(
            card, whichDue) - card.col.sched.today
        decrease = curentIvl*(100-percent)/100
        setattr(card, whichDue, getattr(card, whichDue)-decrease)
        card.ivl -= decrease
        card.flush()

    mw.progress.finish()
    mw.col.reset()
    mw.reset()

    tooltip(_("""Delay changed."""))


def runMain():
    decreaseDelay(getReviewCards())


def runBrowser(browser):
    cids = browser.selectedCards()
    decreaseDelay(cids)


text = _("Shorten card delays")


def setupBrowserMenu(browser):
    a = QAction(text, browser)
    a.triggered.connect(lambda: runBrowser(browser))
    browser.form.menuEdit.addAction(a)


addHook("browser.setupMenus", setupBrowserMenu)
action = QAction(mw)
action.setText(text)
mw.form.menuTools.addAction(action)
action.triggered.connect(runMain)
