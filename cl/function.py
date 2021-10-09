#SCRIPT MAKER BY AKSAL
#DONT SELL TO OTHERS WITHOUT PERMISSION BY AKSAL

from thrift.transport.THttpClient import THttpClient
from thrift.protocol.TCompactProtocol import TCompactProtocol
from BEService import TalkService
from BEService.ttypes import *
import time, json, requests, os, random, ast, datetime, sys, concurrent.futures, livejson, threading, random, tempfile, shutil, copy, base64, platform, subprocess
from humanfriendly import format_timespan
from random import randint

class BE_Team:
    LINE_HOST_DOMAIN            = 'https://gw.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'
    Headers         = {}
    _session        = requests.session()
    def __init__(self, myToken, myApp, pool=False):
        self.lineServer = "https://ga2.line.naver.jp"
        self.lineOBS = "https://obs-sg.line-apps.com"
        self.thisHeaders = {}
        splited = myApp.split("\t")
        self.thisHeaders["x-line-access"] = myToken
        self.thisHeaders["x-line-application"] = myApp
        self.thisHeaders["x-lal"] = "en_id"
        if splited[0] == "ANDROIDLITE":
            self.thisHeaders["user-agent"] = 'LLA/{} Mi5 {}'.format(splited[1], splited[3])
        elif splited[0] == "CHROMEOS":
            self.thisHeaders["user-agent"] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        elif splited[0] in ["IOS", "IOSIPAD"]:
            self.thisHeaders["user-agent"] = 'Line/{} Iphone8 {}'.format(splited[1], splited[3])
        else :
            self.thisHeaders["user-agent"] = 'Line/{}'.format(splited[1])
        self.talk = self.openTransport("/S4")
        self.polling = self.openTransport("/P4")
        self.profile = self.getProfile()
        self.serverTime = self.getServerTime()
        self.localRev = -1
        self.globalRev = 0
        self.individualRev = 0
        self.tokenOBS = self.acquireEncryptedAccessToken()
        print("[ Login ] Display Name: " + self.profile.displayName)
        print("[ Login ] Auth Token: " + myToken)

        self.dataHeaders = {
            "ANDROIDLITE\t2.16.0\tAndroid OS\t5.1.1": {
                "User-Agent": "LLA/2.11.1 samsung 5.1.1",
                "X-Line-Application": "ANDROIDLITE\t2.16.0\tAndroid OS\t5.1.1",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            },
            "android": {
                "User-Agent": "Line/10.1.1",
                "X-Line-Application": "ANDROID\t10.1.1\tAndroid OS\t5.1.1",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            },
            "ios_ipad": {
                "User-Agent": "Line/10.1.1",
                "X-Line-Application": "IOSIPAD\t10.1.1\tiPhone 8\t11.2.5",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            },
            "ios": {
                "User-Agent": "Line/10.1.1",
                "X-Line-Application": "IOS\t10.1.1\tiPhone 8\t11.2.5",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            },
            "chrome": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
                "X-Line-Application": "CHROMEOS\t2.3.2\tChrome OS\t1",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            },
            "desktopwin": {
                "User-Agent": "Line/5.12.3",
                "X-Line-Application": "DESKTOPWIN\t5.21.3\tWindows\t10",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            },
            "desktopmac": {
                "User-Agent": "Line/5.12.3",
                "X-Line-Application": "DESKTOPMAC\t5.21.3\tMAC\t10.15",
                "x-lal": "en_ID",
                "X-Line-Carrier": "51010,1-0"
            }
        }
        if myApp in self.dataHeaders:
            self.headers = self.dataHeaders[myApp]
            if myToken != None:
                self.headers["X-Line-Access"] = myToken
            else:
                self.headers["X-Line-Access"] = self.qrLogin(myApp)
        else:
            raise Exception('APP not found!!!')

    def tagall(self, to, mids=[]):
        parsed_len = len(mids)//20+1
        result = '┏━━━「 Mention Members 」\n'
        mention = '@aksalgntng\n'
        no = 0
        for point in range(parsed_len):
            mentionees = []
            for mid in mids[point*20:(point+1)*20]:
                no += 1
                result += '┣ %i. %s' % (no, mention)
                slen = len(result) - 12
                elen = len(result) + 3
                mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
                if mid == mids[-1]:
                    result += '┗━━━「 Mention Members 」\n'
            if result:
                if result.endswith('\n'): result = result[:-1]
                self.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
            result = ''


    def sendMention1(self, to, text="", mids=[]):
            arrData = ""
            arr = []
            mention = "@sal "
            if mids == []:
                raise Exception("Invalid mids")
            if "@!" in text:
                if text.count("@!") != len(mids):
                    raise Exception("Invalid mids")
                texts = text.split("@!")
                textx = ''
                h = ''
                for mid in range(len(mids)):
                    h+= str(texts[mid].encode('unicode-escape'))
                    textx += str(texts[mid])
                    if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                    else:slen = len(textx);elen = len(textx) + 13
                    arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                    arr.append(arrData)
                    textx += mention
                textx += str(texts[len(mids)])
            else:
                textx = ''
                slen = len(textx)
                elen = len(textx) + 18
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
                arr.append(arrData)
                textx += mention + str(text)
            self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

#    def genTempFile(self):
#        name, path = '/root/simple/foto/profile.jpg',tempfile.gettempdir()
#        return os.path.join(path, name)

#   def genOBSParams(self, params):
#        return base64.b64encode(json.dumps(params).encode('utf-8'))

#    def updateProfilePicture(self, picture):
#        headers = copy.deepcopy(self.headers)
#        headers["X-Line-Access"] = self.tokenOBS
#        headers["content-type"] = "image/png"
#        obs = self.genOBSParams(
#            {"name": "profile.jpg", "type": "image", "ver": "2.0"})
#        headers["x-obs-params"] = obs
#        folder = '/root/simple/foto/profile.jpg'
#        result = requests.post(self.lineOBS + "/r/talk/p/" +
#                               self.profile.mid, headers=headers, data=open(picture, 'rb'))
#        if result.status_code != 201:
#            raise Exception('[ Error ] Upload object')
#        return objId

#    def downloadObjectMsg(self, messageId):
#        path = self.genTempFile()
#        r = requests.get(self.lineOBS+"/talk/m/download.nhn?oid="+messageId, headers=self.headers, stream=True)
#        if r.status_code == 200:
#            with open(path, 'wb') as f:
#                shutil.copyfileobj(r.raw, f)
#                f.close()
#            return path
#            if returnAs == 'path':
#                return saveAs
#            elif returnAs == 'bool':
#                return True
#            elif returnAs == 'bin':
#               return r.raw
#        else:
#            raise Exception('[ Error ] Download object')

    def restart_program(self):
        #os.system('clear')
        python = sys.executable
        os.execl(python, python, * sys.argv)

    def openTransport(self, endPoint):
        transport = THttpClient(self.lineServer + endPoint)
        transport.setCustomHeaders(self.thisHeaders)
        protocol = TCompactProtocol(transport)
        return TalkService.Client(protocol)

    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    def acceptChatInvitation(self, chatMid):
        return self.talk.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))
    
    def acceptChatInvitationByTicket(self, chatMid, ticketId):
        return self.talk.acceptChatInvitationByTicket(AcceptChatInvitationByTicketRequest(0,chatMid,ticketId))

    def blockContact(self, mid):
        return self.talk.blockContact(0,mid)
    
    def cancelChatInvitation(self,chatMid, targetUserMids):
        return self.talk.cancelChatInvitation(CancelChatInvitationRequest(0,chatMid,targetUserMids))
    
    def createChat(self, name, targetUserMids, picturePath=""):
        return self.talk.createChat(CreateChatRequest(0,0,name,targetUserMids,picturePath))

    def deleteSelfFromChat(self, chatMid):
        return self.talk.deleteSelfFromChat(DeleteSelfFromChatRequest(0,chatMid,0,None,0,""))
                                     
    def deleteOtherFromChat(self, chatMid, targetUserMids):
        return self.talk.deleteOtherFromChat(DeleteOtherFromChatRequest(0,chatMid,targetUserMids))
    
    def fetchOperations(self, deviceId, offsetFrom):
        return self.polling.fetchOperations(FetchOperationsRequest(deviceId,offsetFrom))

    def fetchOps(self):
        return self.polling.fetchOps(self.localRev,15,self.globalRev,self.individualRev)

    def findAndAddContactsByMid(self, mid, reference=""):
        return self.talk.findAndAddContactsByMid(0,mid,0,reference)
    
    def findAndAddContactsByUserid(self, searchId, reference=""):
        return self.talk.findAndAddContactsByUserid(0,searchId,reference)
    
    def findContactByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    def findChatByTicket(self, ticketId):
        return self.talk.findChatByTicket(FindChatByTicketRequest(ticketId))

    def getAllChatMids(self, withMemberChats=True, withInvitedChats=True, syncReason=0):
        return self.talk.getAllChatMids(GetAllChatMidsRequest(withMemberChats,withInvitedChats),syncReason)

    def getProfile(self, syncReason=0):
        return self.talk.getProfile(syncReason)

    def getContact(self, mid):
        return self.talk.getContact(mid)

    def getCountryWithRequestIp(self):
        return self.talk.getCountryWithRequestIp()

    def getServerTime(self):
        return self.talk.getServerTime()

    def getContacts(self, mids):
        return self.talk.getContacts(mids)

    def getAllContactIds(self, syncReason=0):
        return self.talk.getAllContactIds(syncReason)
        
    def getChats(self, chatMids, withMembers=True, withInvitees=True):
        return self.talk.getChats(GetChatsRequest(chatMids,withMembers,withInvitees))

    def inviteIntoChat(self, chatMid, targetUserMids=[]):
        return  self.talk.inviteIntoChat(InviteIntoChatRequest(0,chatMid,targetUserMids))
    
    def reissueChatTicket(self, chatMid):
        return self.talk.reissueChatTicket(ReissueChatTicketRequest(0,chatMid))
    
    def rejectChatInvitation(self, chatMid):
        return self.talk.rejectChatInvitation(RejectChatInvitationRequest(0,chatMid))
    
    def getRecentMessagesV2(self, chatId, count=1001):
        return self.talk.getRecentMessagesV2(chatId,count)
    
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        return self.talk.sendMessage(0,msg)
    
    def sendMessageReply(self, to, text, msgId):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = 0, {}
        msg.relatedMessageId = msgId
        msg.messageRelationType = 3
        msg.relatedMessageServiceCode = 1
        return self.talk.sendMessage(0,msg)
    
    def sendMention(self, to, mid, text):
        mentiones = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x  {}'.format(text)
        return self.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+mentiones+']}'}, contentType=0)

    def acquireEncryptedAccessToken(self, featureType=1):
        return self.talk.acquireEncryptedAccessToken(featureType)

    def unsendMessage(self, messageId):
        return self.talk.unsendMessage(0,messageId)

    def updateChat(self, chat, updatedAttribute):
        return self.talk.updateChat(UpdateChatRequest(0,chat,updatedAttribute))
    
    def updateProfileAttribute(self, attr, value):
        return self.talk.updateProfileAttribute(0,attr,value)

    def removeAllMessages(self, lastMessageId):
        return self.talk.removeAllMessages(0, lastMessageId)

    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)

    def getGroupIdsJoined(self):
        return self.talk.getGroupIdsJoined()

    def datamention(self, to, text, data, ps=''):
        if(data == [] or data == {}):return self.sendMention(to," 「 {} 」\nSorry @! I can't found maybe empty".format(text),text,[msg._from])
        k = len(data)//20
        for aa in range(k+1):
            if aa == 0:dd = '╭「 {} 」─{}'.format(text,ps);no=aa
            else:dd = '├「 {} 」─{}'.format(text,ps);no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n╰{}. @!'.format(no)
                else:msgas+='\n│{}. @!'.format(no)
            self.sendMention2(to, msgas,' 「 {} 」'.format(text), data[aa*20 : (aa+1)*20])

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.headers
        return self._session.get(url, headers=self.headers, stream=True)

    def saveFile(self, path, raw):
        with open(path, 'wb') as f:
            shutil.copyfileobj(raw, f)

    def downloadFileURL(self, fileUrl, returnAs='path', saveAs='', headers=None):
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        if saveAs == '':
            saveAs = self.genTempFile()
        r = self.getContent(fileUrl, headers=self.headers)
        if r.status_code != 404:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download file failure.')

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.headers,
        return self._session.post(url, headers=self.headers, data=data, files=files)

    def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.postContent(self.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True

    def genTempFile(self, returnAs='path'):
        try:
            if returnAs not in ['file','path']:
                raise Exception('Invalid returnAs value')
            fName, fPath = 'profile.jpg' , tempfile.gettempdir()
            if returnAs == 'file':
                return fName
            elif returnAs == 'path':
                return os.path.join(fPath, fName)
        except:
            raise Exception('tempfile is required')

    def genOBSParams(self, newList, returnAs='json'):
        oldList = {'name': self.genTempFile('file'),'ver': '1.0'}
        if returnAs not in ['json','b64','default']:
            raise Exception('Invalid parameter returnAs')
        oldList.update(newList)
        if 'range' in oldList:
            new_range='bytes 0-%s\/%s' % ( str(oldList['range']-1), str(oldList['range']) )
            oldList.update({'range': new_range})
        if returnAs == 'json':
            oldList=json.dumps(oldList)
            return oldList
        elif returnAs == 'b64':
            oldList=json.dumps(oldList)
            return base64.b64encode(oldList.encode('utf-8'))
        elif returnAs == 'default':
            return oldList