from collective.grok import gs
from reddplusid.stream import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.stream', 
    title=_('reddplusid.stream import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.stream.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
