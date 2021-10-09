#SCRIPT MAKER BY AKSAL
#DONT SELL TO OTHERS WITHOUT PERMISSION BY AKSAL
from function import *

cl = BE_Team(myToken="TOKEN DI SINI",
            myApp="ANDROIDLITE\t2.16.0\tAndroid OS\t5.1.1")

MID = cl.getProfile().mid
botStart = time.time()
resp = cl.getProfile().displayName

status = livejson.File('status5.json', True, False, 4)
with open("settings5.json","r",encoding="utf-8") as fp:
    settings = json.load(fp)
creator = status["creator"]
owner = status["owner"]
admin = status["admin"]
staff = status["staff"]
white = status["whitelist"]
mybots = status["bots"]
prokick = status["protect"]["prokick"]
proinvite = status["protect"]["proinvite"]
procancel = status["protect"]["procancel"]
proqr = status["protect"]["proqr"]
solo = status["solo"]
squad = status["squad"]

def backupData():
    try:
        back = settings
        f = codecs.open('settings5.json','w','utf-8')
        json.dump(settings, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except:pass

def worker(op):
    try:
########PROTECT########
        if op.type == 13 or op.type == 124:
            if cl.getProfile().mid in op.param3:
                cl.acceptChatInvitation(op.param1)

        if op.type == 5:
            cl.findAndAddContactsByMid(op.param1)
            cl.sendMessage(op.param1, "Succes add back")
            print ("++ OPERATION : [ 5 ] NOTIFIED AUTO ADD ANTIJS")

        if op.type == 60:
            if op.param2 in status["blacklist"]:
                cl.deleteOtherFromChat(op.param1,[op.param2])
#=====================PROTECT KICK====================
        if op.type == 19 or op.type == 133:
            if op.param1 in status["protect"]["prokick"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["bots"] or op.param2 in status["admin"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["bots"] or op.param2 not in status["admin"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        cl.deleteOtherFromChat(op.param1,[op.param2])
                    except Exception as e:print(e)

            if op.param3 in status["creator"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["creator"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except Exception as e:
                        print(e)

            if op.param3 in status["owner"]:
                if op.param2 in status["creator"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["bots"]:
                    if op.param2 not in status["blacklist"]:
                        try:
                            status["blacklist"][op.param2] = True
                        except:pass
                    time.sleep(0.5)
                    chat = cl.getChats([op.param1]).chats[0]
                    if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["owner"]:
                        cl.inviteIntoChat(op.param1, [op.param3])
                        cl.deleteOtherFromChat(op.param1,[op.param2])
                            
            if op.param3 in status["admin"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["admin"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if op.param3 in status["staff"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["bots"] or op.param2 in status["admin"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["bots"] or op.param2 not in status["admin"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["staff"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if op.param3 in status["whitelist"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["bots"] or op.param2 in status["admin"] or op.param2 in status["staff"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["bots"] or op.param2 not in status["admin"] or op.param2 not in status["staff"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["whitelist"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if op.param3 in status["bots"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["bots"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if MID in op.param3:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                    except:pass
#=========================PROTECT QR===========================
        if op.type == 11 or op.type == 122:
            if op.param1 in status["protect"]["proqr"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        cl.deleteOtherFromChat(op.param1,[op.param2])
                        chat = cl.getChats([op.param1])
                        chat.chats[0].extra.groupExtra.preventedJoinByTicket = True
                        cl.updateChat(chat.chats[0],4)
                    except:pass
#========================PROTECT CANCEL=========================
        if op.type == 32 or op.type == 126:
            if op.param1 in status["protect"]["procancel"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        cl.deleteOtherFromChat(op.param1,[op.param2])
                    except Exception as error:
                        print(error)

            if op.param3 in status["creator"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["creator"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass
                            
            if op.param3 in status["owner"]:
                if op.param2 in status["creator"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["owner"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass
                            
            if op.param3 in status["admin"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["admin"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if op.param3 in status["staff"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["staff"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if op.param3 in status["whitelist"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["whitelist"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass

            if op.param3 in status["bots"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        time.sleep(0.5)
                        chat = cl.getChats([op.param1]).chats[0]
                        if op.param3 not in list(chat.extra.groupExtra.inviteeMids) or op.param3 not in list(chat.extra.groupExtra.memberMids) or op.param3 in status["bots"]:
                            cl.inviteIntoChat(op.param1, [op.param3])
                            cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass
#=======================PROTECT INVITE====================
        if op.type == 13 or op.type == 124:
            if op.param1 in status["protect"]["proinvite"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    if op.param2 not in status["blacklist"]:
                        status["blacklist"][op.param2] = True
                    mids = op.param3.replace('\x1e',',').split(',')
                    if len(mids) >= 10:
                         mids = mids[0:10]
                    for target in mids:
                        if target not in status["owner"] and target not in status["bots"] and target not in status["creator"] and target not in status["admin"] and target not in status["staff"] and target not in status["whitelist"]:
                            if target in op.param3:
                                try:
                                    cl.cancelChatInvitation(op.param1, [target])
                                    cl.deleteOtherFromChat(op.param1,[op.param2])
                                    cl.deleteOtherFromChat(op.param1,[target])
                                except:pass

        if op.type == 13 or op.type == 124:
            if op.param2 in status["blacklist"]:
                if op.param2 in status["creator"] or op.param2 in status["owner"] or op.param2 in status["admin"] or op.param2 in status["staff"] or op.param2 in status["whitelist"] or op.param2 in status["bots"]:return
                elif op.param2 not in status["creator"] or op.param2 not in status["owner"] or op.param2 not in status["admin"] or op.param2 not in status["staff"] or op.param2 not in status["whitelist"] or op.param2 not in status["bots"]:
                    try:
                        if op.param2 not in status["blacklist"]:
                            try:
                                status["blacklist"][op.param2] = True
                            except:pass
                        group = cl.getCompactGroup(op.param1)
                        targets = [contact.mid for contact in group.invitee]
                        for target in targets:
                            if target in op.param3:
                                try:
                                    cl.cancelChatInvitation(op.param1,[target])
                                    cl.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    cl.deleteOtherFromChat(op.param1,[target])
                                    cl.deleteOtherFromChat(op.param1,[op.param2])
                    except:pass
#######END#############################
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            msg.from_ = msg._from
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 and sender != cl.profile.mid: to = sender
            else: to = receiver
            if msg.contentType == 1:
                if settings["ChangeDP"] == True:
                    try:
                        path = cl.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+msg.id, 'path')
                        cl.updateProfilePicture(path)
                        cl.sendMessage(msg.to, " 「 Profile 」\nType: Change Profile Picture\nStatus: Profile Picture Hasbeen change♪")
                    except Exception as e:
                        print(e)
                    settings["ChangeDP"] = False
#            if msg.contentType == 1:
#                if settings["ChangeDP"] == True:
#                    path = cl.downloadObjectMsg(msg_id)
#                    settings["ChangeDP"] = False
#                    print(path)
#                    cl.updateProfilePicture(path)
#                    cl.sendMessage(to,"Profile Image Updated.")
            if sender == MID:
                if to not in settings["unsend"]:
                    try:
                        settings["unsend"][to] = {}
                    except Exception as e:print(e)
                if msg_id not in settings["unsend"][to]:
                    settings["unsend"][to][msg_id] = msg_id
                    backupData()
            if cmd in [solo + " help", squad + " help"]:
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    if status["solo"] == '':ab = ''
                    else:ab = status["solo"] + ' '
                    a ="--- 𝗛𝗲𝗹𝗽 𝗚𝘂𝗶𝗱𝗲 ---" \
                    +"\n𝐓𝐢𝐭𝐞𝐥 𝐇𝐞𝐥𝐩: {}".format(status["help"]) \
                    +"\n𝐑𝐧𝐚𝐦𝐞: {}".format(status["solo"]) \
                    +"\n𝐒𝐧𝐚𝐦𝐞: {}".format(status["squad"]) \
                    +"\n\n--- 𝐆𝐞𝐧𝐞𝐫𝐚𝐥 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n1. Me" \
                    +"\n2. Respon" \
                    +"\n3. Rname" \
                    +"\n4. Sname" \
                    +"\n5. Maker" \
                    +"\n6. About" \
                    +"\n7. Say [𝐓𝐞𝐱𝐭]" \
                    +"\n8. "+ab+"unsend" \
                    +"\n9. "+ab+"sp" \
                    +"\n10. "+ab+"out" \
                    +"\n11. "+ab+"check" \
                    +"\n12. "+ab+"runtime" \
                    +"\n13. "+ab+"clear chats" \
                    +"\n14. "+ab+"rest" \
                    +"\n\n--- 𝐆𝐫𝐨𝐮𝐩 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n15. "+ab+"list" \
                    +"\n16. "+ab+"prolist" \
                    +"\n17. "+ab+"ownlist" \
                    +"\n18. "+ab+"adminlist" \
                    +"\n19. "+ab+"stafflist" \
                    +"\n20. "+ab+"botlist" \
                    +"\n21. "+ab+"whitelist" \
                    +"\n22. "+ab+"blacklist" \
                    +"\n23. "+ab+"kick [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n24. "+ab+"invite [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n25. "+ab+"reinvt [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n26. "+ab+"ulti [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n\n--- 𝗣𝗿𝗼𝘁𝗲𝗰𝘁𝗶𝗼𝗻 𝗚𝘂𝗶𝗱𝗲 ---" \
                    +"\n27. "+ab+"prokick [𝐨𝐧/𝐨𝐟𝐟]" \
                    +"\n28. "+ab+"proinvite [𝐨𝐧/𝐨𝐟𝐟]" \
                    +"\n29. "+ab+"procancel [𝐨𝐧/𝐨𝐟𝐟]" \
                    +"\n30. "+ab+"proqr [𝐨𝐧/𝐨𝐟𝐟]" \
                    +"\n31. "+ab+"maxpro [𝐨𝐧/𝐨𝐟𝐟/𝐜𝐡𝐞𝐜𝐤]" \
                    +"\n\n--- 𝐏𝐞𝐫𝐦𝐢𝐬𝐨𝐧 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n32. "+ab+"addstaff [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n33. "+ab+"delstaff [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n34. "+ab+"addbl [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n35. "+ab+"delbl [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n36. "+ab+"addwl [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n37. "+ab+"delwl [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n\n--- 𝐎𝐰𝐧𝐞𝐫 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n38. "+ab+"upstkout" \
                    +"\n39. "+ab+"upstkcban" \
                    +"\n40. "+ab+"upstkrespon" \
                    +"\n41. "+ab+"upstkspeed" \
                    +"\n42. "+ab+"upstkunsend" \
                    +"\n43. "+ab+"uppict" \
                    +"\n44. "+ab+"upname:[𝐓𝐞𝐱𝐭]" \
                    +"\n45. "+ab+"upstatus:[𝐓𝐞𝐱𝐭]" \
                    +"\n46. "+ab+"soloset:[𝐓𝐞𝐱𝐭]" \
                    +"\n47. "+ab+"squadset:[𝐓𝐞𝐱𝐭]" \
                    +"\n48. "+ab+"helpset:[𝐓𝐞𝐱𝐭]" \
                    +"\n\n--- 𝐏𝐞𝐫𝐦𝐢𝐬𝐨𝐧 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n49. "+ab+"addbots [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n50. "+ab+"delbots [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n51. "+ab+"addadmin [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n52. "+ab+"deladmin [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n53. "+ab+"cadmin/cbots/cban" \
                    +"\n54. "+ab+"cwhite/cpro" \
                    +"\n\n--- 𝐑𝐞𝐦𝐨𝐭𝐞 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n55. "+ab+"grouplist" \
                    +"\n56. "+ab+"leaveallgroups" \
                    +"\n57. "+ab+"leave:[𝐍𝐮𝐦𝐛𝐞𝐫]" \
                    +"\n58. "+ab+"inviteme:[𝐍𝐮𝐦𝐛𝐞𝐫]" \
                    +"\n\n--- 𝐌𝐚𝐤𝐞𝐫 𝐆𝐮𝐢𝐝𝐞 ---" \
                    +"\n59. "+ab+"addowner [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" \
                    +"\n60. "+ab+"delowner [@𝗠𝗲𝗻𝘁𝗶𝗼𝗻]" 
                    zxc = a.title()
                    return cl.sendMessage(to,zxc.strip())

            if cmd in [solo + " about", squad + " about"]:
                timeNow = time.time()
                runtime = timeNow - botStart
                runtime = format_timespan(runtime)
                cr = "u2acde3fbd0fe42d609218c0c3543bf51"
                make = cl.getContact(cr).displayName
                fakesp = '567'
                sp = "".join([random.choice(fakesp) for x in range(5)])
                hsl = "0.00" + sp
                fid = cl.getAllContactIds()
                frien = len(fid)
                python_imp = platform.python_implementation()
                python_ver = platform.python_version()
                ac = subprocess.getoutput('lsb_release -a')
                bot = len(status["bots"])
                own = len(status["owner"])
                adm = len(status["admin"])
                stf = len(status["staff"])
                wl = len(status["whitelist"])
                bl = len(status["blacklist"])
                for line in ac.splitlines():
                    if 'Description:' in line:
                        oss = line.split('Description:')[1].replace(' ','')
                res = "┏━━━「 About Bots 」"
                res += "\n┣ Solo : {}".format(status["solo"])
                res += "\n┣ Squad : {}".format(status["squad"])
                res += "\n┣ Creator : {}".format(make)
                res += "\n┣ Owner : {}".format(own)
                res += "\n┣ Admin : {}".format(adm)
                res += "\n┣ Staff : {}".format(stf)
                res += "\n┣ Whitelist : {}".format(wl)
                res += "\n┣ Blacklist : {}".format(bl)
                res += "\n┣ Bots : {}".format(bot)
                res += "\n┣ Friends : {}".format(frien)
                res += "\n┣ Runtime : {}".format(runtime)
                res += "\n┣ Response : {} secs".format(hsl)
                res += "\n┣━「 About System 」"
                res += "\n┣ OS: {}".format(oss)
                res += "\n┣ Language: {}".format(python_imp)
                res += "\n┣ Lang Version: {}".format(python_ver)
                res += "\n┣ Type : Bots Protect"
                res += "\n┣ Lib : BE-Team"
                res += "\n┣ Version : V.1.5"
                res += "\n┣ Maker : Salzcorps"
                res += "\n┣━「 Thanks To 」"
                res += "\n┣ Be-Team"
                res += "\n┣ Hello World"
                res += "\n┣ Katok Suwek"
                res += "\n┣ Dreams"
                res += "\n┣ Herri Winarto"
                res += "\n┗━━━"
                cl.sendMessage(to,res)
                cl.sendContact(to, cr)

            elif cmd.startswith("!!!exec"):
                if sender in creator:
                    tx = text.replace("!!!exec\n", "")
                    try:exec(tx)
                    except Exception as x:print(x)  

            if cmd in [solo + " runtime", squad + " runtime"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessageReply(to, "「 Runtime Bots 」\n"+str(runtime),msg.id)

            if cmd == "ping":
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    cl.sendMessage(to,'pong')

            if cmd == "me":
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    cl.sendContact(to,sender)

            if cmd in [solo + " invitebot"]:
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    cl.inviteIntoChat(to,mybots)

            if cmd in [solo + " clear chats", squad + " clear chats"]:
                if sender in creator or sender in owner or sender in admin:
                    cl.removeAllMessages(msg.id)
                    cl.sendMessageReply(to, "Success Clear AllChats...",msg.id)

            if cmd == 'respon':
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    cl.sendMessageReply(to,resp,msg.id)

            if cmd == 'rname':
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    cl.sendMessageReply(to,status["solo"],msg.id)

            if cmd == 'sname':
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    cl.sendMessageReply(to,status["squad"],msg.id)

            if cmd in [solo + " uppict", squad + " uppict"]:
                if msg._from in owner or msg._from in creator:
                    settings["ChangeDP"] = True
                    cl.sendMessage(to, " 「 Profile 」\nType: Change Profile Picture\nStatus: Send the image....")

            if cmd == "maker":
                cl.sendContact(to, "u2acde3fbd0fe42d609218c0c3543bf51")

            if cmd in [solo + " out", squad + " out"]:
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    if msg.to in status["protect"]["proinvite"] or msg.to in status["protect"]["prokick"] or msg.to in status["protect"]["procancel"] or msg.to in status["protect"]["proqr"]:
                        del status["protect"]["proinvite"][msg.to]
                        del status["protect"]["prokick"][msg.to]
                        del status["protect"]["procancel"][msg.to]
                        del status["protect"]["proqr"][msg.to]
                    cl.sendMessage(to, "Thanks For Using Me ♪")
                    cl.deleteSelfFromChat(to)

            elif cmd.startswith(solo + " sp") or cmd.startswith(squad + " sp"):
                if sender in creator or sender in owner or sender in admin or sender in staff:
                  start = time.time()
                  cl.sendMessage("uf17fc29cc193257aa28b839c4edc5e9a",".")
                  endTime = time.time() - start
                  cl.sendMessageReply(to,f'{int(endTime*1000)} Ms',msg_id)

            elif cmd.startswith(solo + " check") or cmd.startswith(squad + " check"):
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        try:cl.inviteIntoChat(to, [MID]);has = "OK"
                        except:has = "NOT"
                        if has == "OK":sil = "Normal"
                        else:sil = "Limit!"
                        cl.sendMessage(to, "「 Status Bots 」\n • {}".format(sil))
                    except Exception as e:
                        print(e)

            elif cmd in [solo + " rest", squad + " rest"]:
                if sender in creator or sender in owner or sender in admin:
                    cl.sendMessage(to, " 「 Restarting 」\nPlease wait 3 seconds...")
                    os.system("clear")
                    print("RESTARTING!!")
                    cl.restart_program()

            elif cmd.startswith("say "):
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    sep = cmd.split(" ")
                    args = cmd.replace(sep[0] + " ","")
                    cl.sendMessage(to, args)

            elif cmd.startswith(solo + " unsend") or cmd.startswith(squad + " unsend"):
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    for i in settings["unsend"][to]:
                        cl.unsendMessage(settings["unsend"][to][i])
                    del settings["unsend"][to]

            if cmd in [solo + " mentionall",squad + " mentionall"]:
                if msg._from in owner or msg._from in creator or msg._from in admin or msg.id in staff:
                    members = []
                    if msg.toType == 1:
                       room = cl.getChats(to)
                       members = [mem.mid for mem in room.contacts]
                    elif msg.toType == 2:
                        group = cl.getChats(to)
                        members = [mem.mid for mem in group.members]
                    else:
                        return cl.sendMessage(to,"Use Only Group Chat")
                    if members:
                        tagall(to, members)

            elif cmd.startswith(solo + " soloset:") or cmd.startswith(squad + " soloset:"):
                if msg._from in owner or msg._from in creator:    
                    sep = cmd.split(":")
                    args = cmd.replace(sep[0] + ":","")
                    try:
                        status["solo"] = args
                        cl.sendMessage(to,"Solo Key Changed to : " + args)
                    except:
                        cl.sendMessage(to,"The message could not be changed")

            elif cmd.startswith(solo + " squadset:") or cmd.startswith(squad + " squadset:"):
                if msg._from in owner or msg._from in creator:    
                    sep = cmd.split(":")
                    args = cmd.replace(sep[0] + ":","")
                    try:
                        status["squad"] = args
                        cl.sendMessage(to,"Key Key Changed to : " + args)
                    except:
                        cl.sendMessage(to,"The message could not be changed")

            elif cmd.startswith(solo + " helpset:") or cmd.startswith(squad + " helpset:"):
                if msg._from in owner or msg._from in creator:    
                    sep = cmd.split(":")
                    args = cmd.replace(sep[0] + ":","")
                    try:
                        status["help"] = args
                        cl.sendMessage(to,"Help Msg Changed to : " + args)
                    except:
                        cl.sendMessage(to,"The message could not be changed")

            elif cmd.startswith(solo + " upname:") or cmd.startswith(squad + " upname:"):
                if msg._from in owner or msg._from in creator:      
                    sep = cmd.split(":")
                    text = cmd.replace(sep[0] + ":","")
                    if len(text) <= 200:
                        profile = cl.getProfile().displayName
                        profile = text
                        cl.updateProfileAttribute(ProfileAttribute.DISPLAY_NAME,text)
                        cl.sendMessage(to,"Name changed to %s"%(text))

            elif cmd.startswith(solo + " upstatus:") or cmd.startswith(squad + " upstatus:"):
                if msg._from in owner or msg._from in creator:      
                    sep = cmd.split(":")
                    text = cmd.replace(sep[0] + ":","")
                    if len(text) <= 200:
                        profile = cl.getProfile().displayName
                        profile = text
                        cl.updateProfileAttribute(ProfileAttribute.STATUS_MESSAGE,text)
                        cl.sendMessage(to,"Status changed to %s"%(text))

            elif cmd.startswith(solo + "#inviteme: ") or cmd.startswith(squad + "#inviteme:"):
                if msg._from in owner or msg._from in creator:
                    cond = cmd.split(":")
                    num = int(cond[1])
                    gid = cl.getGroupIdsJoined()
                    group = cl.getChats(gid[num-1])
                    cl.findAndAddContactsByMid(sender)
                    cl.inviteIntoChat(gid[num-1],[sender])
                    cl.sendMessage(to,"Success invite to group: {}".format(group.chat.chats[0].chatName))

            elif cmd.startswith(solo + " leave:") or cmd.startswith(squad + " leave:"):
                if msg._from in owner or msg._from in creator:
                    try:
                        separate = cmd.split(":")
                        number = cmd.replace(separate[0] + ":","")
                        groups = cl.getGroupIdsJoined()
                        group = groups[int(number)-1]
                        cl.deleteSelfFromChat(group)
                        cl.sendMessage(to,"Success Leave Group : {}".format(str(cl.getChats([group]).chats[0].chatName)))
                    except:pass

            elif cmd.startswith(solo + " inviteme:") or cmd.startswith(squad + " inviteme:"):
                if msg._from in owner or msg._from in creator:
                    try:
                        separate = cmd.split(":")
                        number = cmd.replace(separate[0] + ":","")
                        groups = cl.getGroupIdsJoined()
                        group = groups[int(number)-1]
                        if msg._from not in cl.getAllContactIds():
                             cl.findAndAddContactsByMid(msg._from)
                             if msg._from not in cl.getGroupIdsJoined():
                                try:
                                    cl.inviteIntoChat(group,[msg._from])
                                    cl.sendMessage(to,"Success invite to group: {}".format(str(cl.getChats([group]).chats[0].chatName)))
                                except:
                                    cl.sendMessageReply(to, "Sorry...You already joined that group",msg_id)
                        else:
                             if msg._from not in cl.getGroupIdsJoined():
                                try:
                                    cl.inviteIntoChat(group,[msg._from])
                                    cl.sendMessage(to,"Success invite to group: {}".format(str(cl.getChats([group]).chats[0].chatName)))
                                except:
                                    cl.sendMessageReply(to, "Sorry...You already joined that group",msg_id)
                    except:pass

            elif cmd.startswith(solo + " leaveallgroups") or cmd.startswith(squad + " leaveallgroups"):
                if sender in creator or sender in owner:
                    groups = cl.getGroupIdsJoined()         
                    for i in groups:
                        try:
                            cl.deleteSelfFromChat(i)                                                                                                                
                        except:pass    

            elif cmd.startswith(solo + " grouplist") or cmd.startswith(squad + " grouplist"):
                if msg._from in owner or msg._from in creator or msg._from in admin:
                    ma = ""
                    a = 0
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                        chat = cl.getChats([i])
                        a = a + 1
                        end = "\n"
                        ma += "║*" + str(a) + ". " +chat.chats[0].chatName+ "\n"
                    cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
#===============COMMANDER==================
            if cmd in [solo + " cban",squad + " cban"]:
                if msg._from in owner or msg._from in creator:
                    sal = status["blacklist"]
                    if status["blacklist"] == {}:
                        cl.sendMessage(to, "Sorry nothing blacklist user")
                    else:                                
                        cl.sendMessage(to, "Done clear ["+str(len(sal))+"] blacklist user")
                        status["blacklist"] = {}

            if cmd in [solo + " cadmin",squad + " cadmin"]:
                if msg._from in owner or msg._from in creator:
                    sal = status["admin"]
                    if status["admin"] == {}:
                        cl.sendMessage(to, "Sorry nothing adminlist user")
                    else:
                        cl.sendMessage(to, "Done clear ["+str(len(sal))+"] adminlist user")
                        status["admin"] = {}

            if cmd in [solo + " cstaff",squad + " cstaff"]:
                if msg._from in owner or msg._from in creator:
                    sal = status["staff"]
                    if status["staff"] == {}:
                        cl.sendMessage(to, "Sorry nothing stafflist user")
                    else:
                        cl.sendMessage(to, "Done clear ["+str(len(sal))+"] stafflist user")
                        status["staff"] = {}

            if cmd in [solo + " cwhite",squad + " cwhite"]:
                if msg._from in owner or msg._from in creator:
                    sal = status["whitelist"]
                    if status["whitelist"] == {}:
                        cl.sendMessage(to, "Sorry nothing whitelist user")
                    else:
                        cl.sendMessage(to, "Done clear ["+str(len(sal))+"] whitelist user")
                        status["whitelist"] = {}

            if cmd in [solo + " cbots",squad + " cbots"]:
                if msg._from in owner or msg._from in creator:
                    sal = status["bots"]
                    if status["bots"] == {}:
                        cl.sendMessage(to, "Sorry nothing botslist user")
                    else:
                        cl.sendMessage(to, "Done clear ["+str(len(sal))+"] botlist user")
                        status["bots"] = {}

            if cmd in [solo + " cpro",squad + " cpro"]:
                if msg._from in owner or msg._from in creator:
                    cl.sendMessage(to, "Done clear protection all groups")
                    status["protect"]["prokick"] = {}
                    status["protect"]["procancel"] = {}
                    status["protect"]["proqr"] = {}
                    status["protect"]["proinvite"] = {}
  #=========ADDEDD===========
            elif cmd.startswith(solo + " addbots") or cmd.startswith(squad + " addbots"):
                if sender in creator or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target not in cl.getAllContactIds():
                                try:
                                    if target not in status["bots"]:
                                        status["bots"][target] = True
                                        cl.findAndAddContactsByMid(target)
                                        time.sleep(5)
                                        cl.sendMention1(to,'Succes Added @!        to Botlist',[target])
                                    else:cl.sendMessage(to,'Target Already In Bolist')
                                except Exception as e:pass
                            else:
                                try:
                                    if target not in status["bots"]:
                                        status["bots"][target] = True
                                        cl.sendMention1(to,'Succes Added @!        to Botlist',[target])
                                    else:cl.sendMessage(to,'Target Already In Bolist')
                                except Exception as e:pass

            elif cmd.startswith(solo + " addowner") or cmd.startswith(squad + " addowner"):
                if sender in creator:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target not in cl.getAllContactIds():
                                try:
                                    if target not in status["owner"]:
                                        status["owner"][target] = True
                                        cl.findAndAddContactsByMid(target)
                                        time.sleep(5)
                                        cl.sendMention1(to,'Succes Added @!        to Ownerlist',[target])
                                    else:cl.sendMessage(to,'Target Already In Ownerlist')
                                except Exception as e:pass
                            else:
                                try:
                                    if target not in status["owner"]:
                                        status["owner"][target] = True
                                        cl.sendMention1(to,'Succes Added @!        to Ownerlist',[target])
                                    else:cl.sendMessage(to,'Target Already In Ownerlist')
                                except Exception as e:pass

            elif cmd.startswith(solo + " addadmin") or cmd.startswith(squad + " addadmin"):
                if sender in creator or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target not in cl.getAllContactIds():
                                try:
                                    if target not in status["admin"]:
                                        status["admin"][target] = True
                                        cl.findAndAddContactsByMid(target)
                                        time.sleep(5)
                                        cl.sendMention1(to,'Succes Added @!        to Adminlist',[target])
                                    else:cl.sendMessage(to,'Target Already In Adminlist')
                                except Exception as e:pass
                            else:
                                try:
                                    if target not in status["admin"]:
                                        status["admin"][target] = True
                                        cl.sendMention1(to,'Succes Added @!        to Adminlist',[target])
                                    else:cl.sendMessage(to,'Target Already In Adminlist')
                                except Exception as e:pass

            elif cmd.startswith(solo + " addstaff") or cmd.startswith(squad + " addstaff"):
                if sender in creator or sender in owner or sender in admin:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target not in cl.getAllContactIds():
                                try:
                                    if target not in status["staff"]:
                                        status["staff"][target] = True
                                        cl.findAndAddContactsByMid(target)
                                        time.sleep(5)
                                        cl.sendMention1(to,'Succes Added @!        to Stafflist',[target])
                                    else:cl.sendMessage(to,'Target Already In Stafflist')
                                except Exception as e:pass
                            else:
                                try:
                                    if target not in status["staff"]:
                                        status["staff"][target] = True
                                        cl.sendMention1(to,'Succes Added @!        to Stafflist',[target])
                                    else:cl.sendMessage(to,'Target Already In Stafflist')
                                except Exception as e:pass

            elif cmd.startswith(solo + " addwl") or cmd.startswith(squad + " addwl"):
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target not in cl.getAllContactIds():
                                try:
                                    if target not in status["whitelist"]:
                                        status["whitelist"][target] = True
                                        cl.findAndAddContactsByMid(target)
                                        time.sleep(5)
                                        cl.sendMention1(to,'Succes Added @!        to Whitelist',[target])
                                    else:cl.sendMessage(to,'Target Already In Whitelist')
                                except Exception as e:pass
                            else:
                                try:
                                    if target not in status["whitelist"]:
                                        status["whitelist"][target] = True
                                        cl.sendMention1(to,'Succes Added @!        to Whitelist',[target])
                                    else:cl.sendMessage(to,'Target Already In Whitelist')
                                except Exception as e:pass

            elif cmd.startswith(solo + " addbl") or cmd.startswith(squad + " addbl"):
                if sender in creator or sender in owner or sender in admin or sender in staff:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target not in status["blacklist"]:
                                    status["blacklist"][target] = True
                                    cl.sendMention1(to,'Succes Added @!        to Blacklist',[target])
                                else:cl.sendMessage(to,'Target Already In Blacklist')
                            except Exception as e:pass
  #========END ADDED==========
  #========DEMOTE=============
            elif cmd.startswith(solo + " delbots") or cmd.startswith(squad + " delbots"):
                if sender in creator or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target in status["bots"]:
                                    del status["bots"][target]
                                    cl.sendMention1(to,'Succes Delete @!        From Botlist',[target])
                                else:cl.sendMessage(to,'Target Not In Botlist')
                            except Exception as e:pass

            elif cmd.startswith(solo + " delowner") or cmd.startswith(squad + " delowner"):
                if sender in creator:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target in status["owner"]:
                                    del status["owner"][target]
                                    cl.sendMention1(to,'Succes Delete @!        From Ownerlist',[target])
                                else:cl.sendMessage(to,'Target Not In Ownerlist')
                            except Exception as e:pass

            elif cmd.startswith(solo + " deladmin") or cmd.startswith(squad + " deladmin"):
                if sender in creator or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target in status["admin"]:
                                    del status["admin"][target]
                                    cl.sendMention1(to,'Succes Delete @!        From Adminlist',[target])
                                else:cl.sendMessage(to,'Target Not In Adminlist')
                            except Exception as e:pass

            elif cmd.startswith(solo + " delstaff") or cmd.startswith(squad + " delstaff"):
                if sender in creator or sender in admin or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target in status["staff"]:
                                    del status["staff"][target]
                                    cl.sendMention1(to,'Succes Delete @!        From Stafflist',[target])
                                else:cl.sendMessage(to,'Target Not In Stafflist')
                            except Exception as e:pass

            elif cmd.startswith(solo + " delwl") or cmd.startswith(squad + " delwl"):
                if sender in creator or sender in admin or sender in staff or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target in status["whitelist"]:
                                    del status["whitelist"][target]
                                    cl.sendMention1(to,'Succes Delete @!        From Whitelist',[target])
                                else:cl.sendMessage(to,'Target Not In Whitelist')
                            except Exception as e:pass

            elif cmd.startswith(solo + " delbl") or cmd.startswith(squad + " delbl"):
                if sender in creator or sender in admin or sender in staff or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                if target in status["blacklist"]:
                                    del status["blacklist"][target]
                                    cl.sendMention1(to,'Succes Delete @!        From Blacklist',[target])
                                else:cl.sendMessage(to,'Target Not In Blacklist')
                            except Exception as e:pass

            elif cmd.startswith(solo + " kick") or cmd.startswith(squad + " kick"):
                if sender in creator or sender in admin or sender in staff or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                cl.deleteOtherFromChat(to,[target])
                            except:cl.sendMessage(to,"Sorry bots limited!")

            elif cmd.startswith(solo + " invite") or cmd.startswith(squad + " invite"):
                if sender in creator or sender in admin or sender in staff or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoChat(to,[target])
                            except:cl.sendMessage(to,"Sorry bots limited!")

            elif cmd.startswith(solo + " reinvt") or cmd.startswith(squad + " reinvt"):
                if sender in creator or sender in admin or sender in staff or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                cl.deleteOtherFromChat(to,[target])
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoChat(to,[target])
                            except:cl.sendMessage(to,"Sorry bots limited!")

            elif cmd.startswith(solo + " ulti") or cmd.startswith(squad + " ulti"):
                if sender in creator or sender in admin or sender in staff or sender in owner:
                    if 'MENTION' in msg.contentMetadata.keys()!=None:
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                cl.deleteOtherFromChat(to,[target])
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoChat(to,[target])
                                cl.cancelChatInvitation(to,[target])
                            except:cl.sendMessage(to,"Sorry bots limited!")
  #=========END DEMOTED=============
  #==========LIST===========
            elif cmd in [solo + " blacklist", squad + " blacklist"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Blacklist:"
                    if status["blacklist"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["blacklist"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error)) 

            elif cmd in [solo + " ownlist", squad + " ownlist"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Ownerlist:"
                    if status["owner"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["owner"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error)) 

            elif cmd in [solo + " adminlist", squad + " adminlist"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Adminlist:"
                    if status["admin"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["admin"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error)) 

            elif cmd in [solo + " stafflist", squad + " stafflist"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Stafflist:"
                    if status["stafflist"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["stafflist"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error)) 

            elif cmd in [solo + " whitelist", squad + " whitelist"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Whitelist:"
                    if status["whitelist"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["whitelist"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error)) 

            elif cmd in [solo + " botlist", squad + " botlist"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Botlist:"
                    if status["bots"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["bots"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error)) 

            elif cmd in [solo + " list", squad + " list"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    listText = "Creator:"
                    if status["creator"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lo in status["creator"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lo).displayName)
                            num += 1                         
                    listText += "\n\nOwnerList:"
                    if status["owner"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lo in status["owner"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lo).displayName)
                            num += 1                        
                    listText += "\n\nAdminList:"
                    if status["admin"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lc in status["admin"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lc).displayName)
                            num += 1
                    listText += "\n\nStaffList:"
                    if status["staff"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lc2 in status["staff"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lc2).displayName)
                            num += 1
                    listText += "\n\nBotlist:"
                    if status["bots"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lb in status["bots"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lb).displayName)
                            num += 1
                    listText += "\n\nWhitelist:"
                    if status["whitelist"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lb in status["whitelist"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lb).displayName)
                            num += 1
                    listText += "\n\nBlacklist:"
                    if status["blacklist"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lbl in status["blacklist"]:
                            listText += "\n  {}. {}".format(str(num), cl.getContact(lbl).displayName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error))
  #=======END LIST========
#===============END COMMANDER==============

#===============PROTECTION=================
            elif cmd in [solo + " procancel on", squad + " procancel on"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to in status["protect"]["procancel"]:
                            cl.sendMessage(to, "Protect cancel has been enabled ✓")
                        else:
                            status["protect"]["procancel"][msg.to] = True
                            cl.sendMessage(to, "Protect cancel enabled ✓")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " procancel off", squad + " procancel off"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to not in status["protect"]["procancel"]:
                            cl.sendMessage(to, "Protect cancel has been disabled ✖️")
                        else:
                            del status["protect"]["procancel"][msg.to]
                            cl.sendMessage(to, "Protect cancel already disabled ✖️")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " proinvite on", squad + " proinvite on"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to in status["protect"]["proinvite"]:
                            cl.sendMessage(to, "Protect invite has been enabled ✓")
                        else:
                            status["protect"]["proinvite"][msg.to] = True
                            cl.sendMessage(to, "Protect invite enabled ✓")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " proinvite off", squad + " proinvite off"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to not in status["protect"]["proinvite"]:
                            cl.sendMessage(to, "Protect invite has been disabled ✖️")
                        else:
                            del status["protect"]["proinvite"][msg.to]
                            cl.sendMessage(to, "Protect invite already disabled ✖️")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " prokick on", squad + " prokick on"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to in status["protect"]["prokick"]:
                            cl.sendMessage(to, "Protect kick has been enabled ✓")
                        else:
                            status["protect"]["prokick"][msg.to] = True
                            cl.sendMessage(to, "Protect kick enabled ✓")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " prokick off", squad + " prokick off"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to not in status["protect"]["prokick"]:
                            cl.sendMessage(to, "Protect kick has been disabled ✖️")
                        else:
                            del status["protect"]["prokick"][msg.to]
                            cl.sendMessage(to, "Protect kick already disabled ✖️")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " proqr on", squad + " proqr on"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to in status["protect"]["proqr"]:
                            cl.sendMessage(to, "Protect qr has been enabled ✓")
                        else:
                            status["protect"]["proqr"][msg.to] = True
                            cl.sendMessage(to, "Protect qr enabled ✓")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " proqr off", squad + " proqr off"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to not in status["protect"]["proqr"]:
                            cl.sendMessage(to, "Protect qr has been disabled ✖️")
                        else:
                            del status["protect"]["proqr"][msg.to]
                            cl.sendMessage(to, "Protect qr already disabled ✖️")
                    except Exception as error:
                        print(error)

            elif cmd in [solo + " maxpro on", squad + " maxpro on"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to not in status["protect"]["proinvite"]:
                            try:
                                status["protect"]["proinvite"][msg.to] = True
                            except: pass
                        else:pass
                        if to not in status["protect"]["prokick"]:
                            try:
                                status["protect"]["prokick"][msg.to] = True
                            except: pass
                        else:pass
                        if to not in status["protect"]["procancel"]:
                            try:
                                status["protect"]["procancel"][msg.to] = True
                            except: pass
                        else:pass
                        if to not in status["protect"]["proqr"]:
                            try:
                                status["protect"]["proqr"][msg.to] = True
                            except: pass
                        else:pass
                        cl.sendMessage(to, "Protect Max Has Been Enabled ✓")
                    except: pass

            elif cmd in [solo + " maxpro off", squad + " maxpro off"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    try:
                        if to in status["protect"]["proinvite"]:
                            try:
                                del status["protect"]["proinvite"][msg.to]
                            except: pass
                        else:pass
                        if to in status["protect"]["prokick"]:
                            try:
                                del status["protect"]["prokick"][msg.to]
                            except: pass
                        else:pass
                        if to in status["protect"]["procancel"]:
                            try:
                                del status["protect"]["procancel"][msg.to]
                            except: pass
                        else:pass
                        if to in status["protect"]["proqr"]:
                            try:
                                del status["protect"]["proqr"][msg.to]
                            except: pass
                        else:pass
                        cl.sendMessage(to, "Protect Max Has Been Disabled ✖️")
                    except: pass

            elif cmd in [solo + " maxpro check", squad + " maxpro check"]:
                if sender in owner or sender in creator or sender in admin or sender in staff:
                    md = "┏━「 Status Protection 」\n"                     
                    if to in status["protect"]["proqr"]: md+="┣ Protect Qr On\n"
                    else: md+="┣ Protect Qr Off\n"
                    if to in status["protect"]["proinvite"]: md+="┣ Protect Invite On\n"
                    else: md+="┣ Protect Invite Off\n"
                    if to in status["protect"]["prokick"]: md+="┣ Protect Kick On\n"
                    else: md+="┣ Protect Kick Off\n"
                    if to in status["protect"]["procancel"]: md+="┣ Protect Cancel On\n"
                    else: md+="┣ Protect Cancel Off\n"                                           
                    ret_ = str(md)
                    ret_ += "┗━━━"
                    cl.sendMessage(to,ret_)

            elif cmd in [solo + " prolist", squad + " prolist"]:
                if msg._from in owner or msg._from in creator or msg._from in admin:
                    listText = "「 Protect Kick 」"
                    if status["protect"]["prokick"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lo in status["protect"]["prokick"]:
                            listText += "\n  {}. {}".format(str(num), cl.getChats([lo]).chats[0].chatName)
                            num += 1
                    listText += "\n\n「 Protect Invite 」"                    
                    if status["protect"]["proinvite"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for li in status["protect"]["proinvite"]:
                            listText += "\n  {}. {}".format(str(num), cl.getChats([li]).chats[0].chatName)
                            num += 1
                    listText += "\n\n「 Protect Cancel 」"
                    if status["protect"]["procancel"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lp in status["protect"]["procancel"]:
                            listText += "\n  {}. {}".format(str(num), cl.getChats([lp]).chats[0].chatName)
                            num += 1
                    listText += "\n\n「 Protect QR 」"
                    if status["protect"]["proqr"] == {}:
                        listText += "\n  Nothing!"
                    else:
                        num = 1
                        for lz in status["protect"]["proqr"]:
                            listText += "\n  {}. {}".format(str(num), cl.getChats([lz]).chats[0].chatName)
                            num += 1
                    try:cl.sendMessage(to, listText)
                    except Exception as error:cl.sendMessage(to, str(error))
#===============END PROTECT=================
            elif cmd in [solo + " upstkcban", squad + " upstkcban"]:
                if sender in creator or sender in owner:
                    status["stickercban"]["addstickercban"] = True
                    cl.sendMessage(to,"Please Send Sticker")

            elif cmd in [solo + " upstkunsend", squad + " upstkunsend"]:
                if sender in creator or sender in owner:
                    status["stickerunsend"]["addstickerunsend"] = True
                    cl.sendMessage(to,"Please Send Sticker")

            elif cmd in [solo + " upstkrespon", squad + " upstkrespon"]:
                if sender in creator or sender in owner:
                    status["stickerrespon"]["addstickerrespon"] = True
                    cl.sendMessage(to,"Please Send Sticker")

            elif cmd in [solo + " upstkout", squad + " upstkout"]:
                if sender in creator or sender in owner:
                    status["stickerout"]["addstickerout"] = True
                    cl.sendMessage(to,"Please Send Sticker")

            elif cmd in [solo + " upstkspeed", squad + " upstkspeed"]:
                if sender in creator or sender in owner:
                    status["stickersp"]["addstickersp"] = True
                    cl.sendMessage(to,"Please Send Sticker")

            elif msg.contentType == 7:
                if msg.contentMetadata["STKID"] == status["stickercban"]["STKID"] and msg.contentMetadata["STKPKGID"] == status["stickercban"]["STKPKGID"]:
                    if sender in owner or sender in creator or sender in admin or sender in staff:
                        try:
                            sal = status["blacklist"]
                            if status["blacklist"] == {}:
                                cl.sendMessage(to, "Sorry nothing blacklist user")
                            else:                                
                                cl.sendMessage(to, "Done clear ["+str(len(sal))+"] blacklist user")
                                status["blacklist"] = {}
                        except Exception as e:print(e)

                if msg.contentMetadata["STKID"] == status["stickerunsend"]["STKID"] and msg.contentMetadata["STKPKGID"] == status["stickerunsend"]["STKPKGID"]:
                    if sender in owner or sender in creator or sender in admin or sender in staff:
                        try:
                            for i in settings["unsend"][to]:
                                cl.unsendMessage(settings["unsend"][to][i])
                            del settings["unsend"][to]
                        except Exception as e:print(e)

                if msg.contentMetadata["STKID"] == status["stickersp"]["STKID"] and msg.contentMetadata["STKPKGID"] == status["stickersp"]["STKPKGID"]:
                    if sender in owner or sender in creator or sender in admin or sender in staff:
                        try:
                            start = time.time()
                            cl.sendMessage("uf17fc29cc193257aa28b839c4edc5e9a",".")
                            endTime = time.time() - start
                            cl.sendMessage(to,f'{int(endTime*1000)} Ms')
                        except Exception as e:print(e)

                if msg.contentMetadata["STKID"] == status["stickerrespon"]["STKID"] and msg.contentMetadata["STKPKGID"] == status["stickerrespon"]["STKPKGID"]:
                    if sender in owner or sender in creator or sender in admin or sender in staff:
                        try:
                            cl.sendMessage(to,resp)
                        except Exception as e:print(e)

                if msg.contentMetadata["STKID"] == status["stickerout"]["STKID"] and msg.contentMetadata["STKPKGID"] == status["stickerout"]["STKPKGID"]:
                    if sender in owner or sender in creator or sender in admin or sender in staff:
                        try:
                            if msg.to in status["protect"]["proinvite"] or msg.to in status["protect"]["prokick"] or msg.to in status["protect"]["procancel"] or msg.to in status["protect"]["proqr"]:
                                del status["protect"]["proinvite"][msg.to]
                                del status["protect"]["prokick"][msg.to]
                                del status["protect"]["procancel"][msg.to]
                                del status["protect"]["proqr"][msg.to]
                            cl.sendMessage(to, "okay im out!")
                            cl.deleteSelfFromChat(to)
                        except Exception as e:print(e)
                
                if status["stickercban"]["addstickercban"] == True:
                    if sender in creator or sender in owner:
                        status["stickercban"]["STKVER"] = msg.contentMetadata["STKVER"]
                        status["stickercban"]["STKID"] = msg.contentMetadata["STKID"]
                        status["stickercban"]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        cl.sendMessage(to,"Success Update Sticker Respon")
                        status["stickercban"]["addstickercban"] = False

                if status["stickersp"]["addstickersp"] == True:
                    if sender in creator or sender in owner:
                        status["stickersp"]["STKVER"] = msg.contentMetadata["STKVER"]
                        status["stickersp"]["STKID"] = msg.contentMetadata["STKID"]
                        status["stickersp"]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        cl.sendMessage(to,"Success Update Sticker Respon")
                        status["stickersp"]["addstickersp"] = False

                if status["stickerrespon"]["addstickerrespon"] == True:
                    if sender in creator or sender in owner:
                        status["stickerrespon"]["STKVER"] = msg.contentMetadata["STKVER"]
                        status["stickerrespon"]["STKID"] = msg.contentMetadata["STKID"]
                        status["stickerrespon"]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        cl.sendMessage(to,"Success Update Sticker Respon")
                        status["stickerrespon"]["addstickerrespon"] = False

                if status["stickerout"]["addstickerout"] == True:
                    if sender in creator or sender in owner:
                        status["stickerout"]["STKVER"] = msg.contentMetadata["STKVER"]
                        status["stickerout"]["STKID"] = msg.contentMetadata["STKID"]
                        status["stickerout"]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        cl.sendMessage(to,"Success Update Sticker Out")
                        status["stickerout"]["addstickerout"] = False

                if status["stickerunsend"]["addstickerunsend"] == True:
                    if sender in creator or sender in owner:
                        status["stickerunsend"]["STKVER"] = msg.contentMetadata["STKVER"]
                        status["stickerunsend"]["STKID"] = msg.contentMetadata["STKID"]
                        status["stickerunsend"]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        cl.sendMessage(to,"Success Update Sticker Out")
                        status["stickerunsend"]["addstickerunsend"] = False

    except Exception as catch:
        trace = catch.__traceback__
        print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    while True:
        backupData()
        try:
            ops = cl.fetchOps()
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    cl.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                    cl.individualRev = int(op.param1.split("\x1e")[0])
                cl.localRev = max(op.revision, cl.localRev)
                executor.submit(worker,op)
        except:
            pass
            
