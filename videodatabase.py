import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class VideoData:
    def __init__(self):
        self.DataCheck()
        
        # self.cur.execute("CREATE TABLE cancelbutton(name TEXT)")
        # self.cur.execute("INSERT INTO user VALUES('asdf')")
        # self.cur.execute('DROP TABLE 브금')
        # self.cur.execute('DROP TABLE 브금2')
        # self.cur.execute('DROP TABLE 브금3')
        # self.cur.execute('DROP TABLE 재생목록3')
        # self.cur.execute('DROP TABLE 재생목록4')
        # self.cur.execute('DROP TABLE 재생목록5')
        # self.cur.execute('DROP TABLE 재생목록6')
        # self.cur.execute('DROP TABLE 재생목록7')
        # self.cur.execute('DROP TABLE 재생목록9')
        # self.cur.execute('DROP TABLE 재생목록10')
        # self.cur.execute('DROP TABLE 브금')
        
        # self.cur.execute("UPDATE count SET count=0")
        # self.cur.execute("DELETE FROM buttonname")
        # self.cur.execute("ALTER TABLE '게임영상' RENAME TO '123'")
        # self.conn.commit()
    def __del__(self):
        self.conn.close()
    

    def DataCheck(self):
        self.conn=sqlite3.connect("PlaylistData.db")
        self.cur=self.conn.cursor()

    def FindCount(self):
        self.cur.execute("SELECT count from count")
        self.result=self.cur.fetchall()

    def UpdateCount(self):
        self.cur.execute("UPDATE count set count=count+1")
        self.conn.commit()

    def AddVideo(self,name,url):
        self.url=url
        self.name=name
        self.cur.execute("INSERT INTO '"+self.name+"' VALUES('"+self.url+"')")
        self.conn.commit()

    def FindVideoUrl(self,name):
        self.name=name
        self.urlbuttonlist=[]
        self.urltitle=[]
        self.titlelist=[]
        self.urltitle_forminiplayer=[]
        self.cur.execute("SELECT * from '"+self.name+"'")
        self.myurl=self.cur.fetchall()
        for i in range(0,len(self.myurl)):
            self.urlbuttonlist.append(self.myurl[i][0])
            self.urltitle.append(self.myurl[i][0])
            self.urltitle_forminiplayer.append(self.myurl[i][0])
            self.titlelist.append(self.myurl[i][0])

    def AddVideoToPlayList(self,playlist,url):
        self.playlist=playlist
        self.url=url
        self.cur.execute("INSERT INTO '"+self.playlist+"' VALUES('"+self.url+"')")
        self.conn.commit()

       
    def CreatePlaylist(self,name):
        self.name=name
        self.cur.execute("CREATE TABLE '"+self.name+"'(name TEXT)")
        self.FindCount()
        self.cur.execute("INSERT INTO buttonname VALUES('"+self.name+"')")
        self.conn.commit()

    def ChangePlaylist(self,name,changename):
        self.name=name
        self.changename=changename
        self.cur.execute("UPDATE buttonname SET name= '"+self.changename+"' WHERE name='"+self.name+"'")
        #self.cur.execute("ALTER TABLE '"+self.name+"' RENAME TO '"+self.changename+"'")
        self.conn.commit()

    def DeleteVideo(self,playlist,video):
        self.playlist=playlist
        self.video=video
        self.cur.execute("DELETE from '"+self.playlist+"' where name = '"+self.video+"'")
        self.conn.commit()

    def ChangeTable(self,name,changename):
        self.name=name
        self.changename=changename
        self.cur.execute("ALTER TABLE '"+self.name+"' RENAME TO '"+self.changename+"'")
        self.conn.commit()

    def DeletePlaylist(self,name,label):
        self.name=name
        self.label=label
        self.cur.execute("DELETE TABLE '"+self.name+"' ")
        self.cur.execute("UPDATE count set count=count-1")
        self.conn.commit()
        
    
    def StoreButtons(self):
        self.buttonlist=[]
        self.buttonlabellist=[]
        self.mybuttonlabellist=[]
        self.deletebutton=[]
        self.strbutton=[]
        self.deletebutton2=[]
        self.cur.execute("SELECT * from buttonname")
        self.buttonlist2=self.cur.fetchall()
        try:
            for i in range(0,len(self.buttonlist2)):
                
                self.buttonlist.append(self.buttonlist2[i][0])
                self.buttonlabellist.append(self.buttonlist2[i][0])
                self.deletebutton.append(self.buttonlist2[i][0])
                self.strbutton.append(self.buttonlist2[i][0])
                self.mybuttonlabellist.append(self.buttonlist2[i][0])
                self.deletebutton2.append(self.buttonlist2[i][0])
        except IndexError:
            pass
        
        
        return self.buttonlist,self.buttonlabellist,self.deletebutton
        

    

asdf=VideoData()
asdf.StoreButtons()


