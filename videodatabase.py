import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class VideoData:
    def __init__(self):
        self.DataCheck()
        
        # self.cur.execute("CREATE TABLE cancelbutton(name TEXT)")
        # self.cur.execute("INSERT INTO user VALUES('asdf')")
        # self.cur.execute('DROP TABLE 재생목록0')
        # self.cur.execute('DROP TABLE 재생목록1')
        # self.cur.execute('DROP TABLE 재생목록2')
        # self.cur.execute('DROP TABLE 재생목록3')
        # self.cur.execute('DROP TABLE 재생목록4')
        # self.cur.execute('DROP TABLE 재생목록5')
        # self.cur.execute('DROP TABLE 재생목록6')
        
        # self.cur.execute("UPDATE count SET count=0")
        # self.cur.execute("DELETE FROM buttonname")
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
        self.cur.execute("SELECT * from '"+self.name+"'")
        self.myurl=self.cur.fetchall()
        return( self.myurl)

       
    def CreatePlaylist(self,name):
        self.name=name
        self.cur.execute("CREATE TABLE '"+self.name+"'(name TEXT)")
        self.FindCount()
        self.cur.execute("INSERT INTO buttonname VALUES('"+self.name+"')")
        self.conn.commit()

    
    def StoreButtons(self):
        self.buttonlist=[]
        self.buttonlabellist=[]
        self.deletebutton=[]
        self.strbutton=[]
        self.cur.execute("SELECT * from buttonname")
        self.buttonlist2=self.cur.fetchall()
        try:
            for i in range(0,len(self.buttonlist2)):
                
                self.buttonlist.append(self.buttonlist2[i][0])
                self.buttonlabellist.append(self.buttonlist2[i][0])
                self.deletebutton.append(self.buttonlist2[i][0])
                self.strbutton.append(self.buttonlist2[i][0])
                
        except IndexError:
            pass
        
        
        return self.buttonlist,self.buttonlabellist,self.deletebutton
        

    

asdf=VideoData()
asdf.StoreButtons()
# asdf.AddVideo('재생목록0','https://www.youtube.com/watch?v=DCkqHOsjuFs')
