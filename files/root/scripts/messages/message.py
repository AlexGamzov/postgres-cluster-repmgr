#!/usr/bin/env python
#-*- coding: utf-8 -*-
# -*- coding: latin-1 -*-
import os, sys
import xmpp,sys
from datetime import datetime
USERS="user1 user2"
DOMAIN="@server.com"
NOW = datetime.now()
datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")

xmpp_jid = 'user@server.com'
xmpp_pwd = '04-fadetoblack'

msg = sys.argv[2]



for USER in USERS.split(" "):

        jid = xmpp.protocol.JID(xmpp_jid)
        client = xmpp.Client(jid.getDomain(),debug=[])
        client.connect()
        client.auth(jid.getNode(),str(xmpp_pwd),resource='xmpppy')
        client.send(xmpp.protocol.Message(str(USER) + DOMAIN,msg + '  ' + str(NOW)))
        to = str(USER)
        client.disconnect()


