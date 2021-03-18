from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil
import pyttsx3 #pip install pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")

    speak("Welcome to Files Sorting Application")    


class Sorting_App:

    def __init__(self,root):
        self.root=root
        self.root.title("Sorting Application")
        self.root.geometry("1525x790+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="F:\\project-clg\\images\\folder.png")
        title=Label(self.root,text="Files Sorting Application",padx=10,image=self.logo_icon,compound=LEFT,font=("impact",40),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        

        #-------------Section one----------------#
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("times new roman",25,"bold")).place(x=50,y=100)
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=250,y=105,height=35,width=600)
        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",bd=5,font=("times new roman",15,"bold"),bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=900,y=102,height=40,width=150)
        hr=Label(self.root,bg="lightgrey").place(x=50,y=160,height=2,width=1350)

        
         #-------------Section two----------------#
        self.image_extensions=["Image Extensions",".png",".jpg",".jpeg"]
        self.audio_extensions=["Audio Extensions",".wav",".mp3"]
        self.video_extensions=["Video Extensions",".mp4"]
        self.doc_extensions=["Document Extensions",".doc",".xls",".txt",".pdf",".zip",".rar"]

        self.folders={
                'videos':self.video_extensions,
                'audios':self.audio_extensions,
                'images':self.image_extensions,
                'documents':self.doc_extensions,
            }


        lbl_support_ext=Label(self.root,text="Various Supported Extensions",font=("times new roman",25)).place(x=50,y=200)
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15),state='readonly')
        self.image_box.place(x=50,y=260,width=260,height=35)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15),state='readonly')
        self.video_box.place(x=400,y=260,width=260,height=35)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15),state='readonly')
        self.audio_box.place(x=750,y=260,width=260,height=35)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15),state='readonly')
        self.doc_box.place(x=1100,y=260,width=260,height=35)
        self.doc_box.current(0)
        

        #-------------Section three----------------#
        #-------------Image Icons----------------#
        self.image_icon=PhotoImage(file="F:\\project-clg\\images\\image.png")
        self.audio_icon=PhotoImage(file="F:\\project-clg\\images\\music.png")
        self.video_icon=PhotoImage(file="F:\\project-clg\\images\\video.png")
        self.document_icon=PhotoImage(file="F:\\project-clg\\images\\docu.png")
        self.other_icon=PhotoImage(file="F:\\project-clg\\images\\other.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="White")
        Frame1.place(x=50,y=320,width=1350,height=300)

        self.lbl_total_files=Label(Frame1,text="Total Files:",font=("times new roman",18),bg="white")
        self.lbl_total_files.place(x=50,y=10)

        self.lbl_total_image=Label(Frame1,bd=5,relief=RAISED,image=self.image_icon,compound=TOP,font=("times new roman",16,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_image.place(x=40,y=50,width=220,height=200)

        self.lbl_total_audio=Label(Frame1,bd=5,relief=RAISED,image=self.audio_icon,compound=TOP,font=("times new roman",16,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_audio.place(x=300,y=50,width=220,height=200)

        self.lbl_total_video=Label(Frame1,bd=5,relief=RAISED,image=self.video_icon,compound=TOP,font=("times new roman",16,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_video.place(x=560,y=50,width=220,height=200)

        self.lbl_total_document=Label(Frame1,bd=5,relief=RAISED,image=self.document_icon,compound=TOP,font=("times new roman",16,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_document.place(x=820,y=50,width=220,height=200)

        self.lbl_total_other=Label(Frame1,bd=5,relief=RAISED,image=self.other_icon,compound=TOP,font=("times new roman",16,"bold"),bg="#0875B7",fg="white")
        self.lbl_total_other.place(x=1080,y=50,width=220,height=200)

        
        #-------------Section four----------------#

        lbl_status=Label(self.root,text="STATUS:",font=("times new roman",25,"bold"),bg="white").place(x=50,y=625)

        self.lbl_st_total=Label(self.root,text="",font=("times new roman",18,"bold"),bg="white",fg="green")
        self.lbl_st_total.place(x=310,y=632)

        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",18,"bold"),bg="white",fg="blue")
        self.lbl_st_moved.place(x=550,y=632)

        self.lbl_st_left=Label(self.root,text="",font=("times new roman",18,"bold"),bg="white",fg="#ff5722")
        self.lbl_st_left.place(x=790,y=632)

        #------------BUTTONS-----------------#
        self.btn_clear=Button(self.root,text="CLEAR",command=self.clear,bd=5,relief=RAISED,font=("times new roman",15,"bold"),bg="blue",fg="white",activebackground="#607d8b",cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=1000,y=625,height=40,width=160)
        
        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,text="START",bd=5,relief=RAISED,font=("times new roman",15,"bold"),bg="#D56135",fg="white",activebackground="#D56135",cursor="hand2",activeforeground="black")
        self.btn_start.place(x=1200,y=625,height=40,width=160)

    
    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        combine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="images":
                        images=images+1

                    if ext.lower() in folder_name[1] and folder_name[0]=="audios":
                        audios=audios+1

                    if ext.lower() in folder_name[1] and folder_name[0]=="videos":
                        videos=videos+1

                    if ext.lower() in folder_name[1] and folder_name[0]=="documents":
                        documents=documents+1
        
        #to calculate number of other files

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i))==True:
                ext="."+i.split(".")[-1]
                if ext.lower() not in combine_list:
                    others=others+1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other\n"+str(others))
        self.lbl_total_files.config(text="Total Files:"+str(self.count))
            

    
    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
            self.var_foldername.set(str(op))
            self.directory = self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directory)
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=DISABLED)
            c=0
            for i in self.all_files:
                    if os.path.isfile(os.path.join(self.directory,i))==True:
                        c=c+1
                        self.create_move(i.split(".")[-1],i)
                        self.lbl_st_total.config(text="Total:"+str(self.count))
                        self.lbl_st_moved.config(text="MOVED:"+str(c))
                        self.lbl_st_left.config(text="LEFT:"+str(self.count-c))
                        
                        self.lbl_st_total.update()
                        self.lbl_st_moved.update()
                        self.lbl_st_left.update()

            messagebox.showinfo("Success","All Files has moved Successfully!")
            self.btn_start.config(state=DISABLED)
            self.btn_clear.config(state=NORMAL)
        else:
            messagebox.showinfo("Error","PLease select folder!")
            
    def clear(self):
        self.btn_start.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")

        self.lbl_total_image.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files:")

    #for lower case folder names
    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,folder.lower()))

    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))    

if __name__ == "__main__":
    wishMe()
    root=Tk()
    obj = Sorting_App(root)
    root.mainloop()
