#!/usr/bin/python3
import os
import subprocess
import sys
from time import sleep
#from pathlib import Path

#from getpass import getpass
#from getpass import getuser

#subprocess.run([sys.executable, "-c", "ls -la"])
#lines = output.split('\n')
#for line in lines:
   # print(line)

class Terminal_helper():

    pass
    
    def __init__(self, something, something_else):
        self.something=something
        self.something_else=something_else
        self.path_dict={'':''}
        self.framat_str="/home/jonny"
        self.counter=counter=0
        
        
    
    #FILE SECTION

    def nuvarande_plats(self):
        counter=self.counter
        path_dict=self.path_dict
        #subprocess.run(["echo", "hej"])
        #Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."]) 
        #subprocess.Popen(["usr/bin/pwd"]) 
        #,universal_newlines=True för att få string??
        subprocess.call(['pwd'], shell=True)
        nuvarande_plats_str=str(subprocess.check_output(['pwd'], shell=True))    
        nuvarande_plats_str=nuvarande_plats_str.strip('b\'')
        nuvarande_plats_str=nuvarande_plats_str.strip('\\n')
        #self.nuvarande_plats_str=str(nuvarande_plats_str)
        print(type(nuvarande_plats_str))
        print(nuvarande_plats_str)
        if self.counter >0:
            self.path_dict.update ({self.counter:nuvarande_plats_str})
        print(self.path_dict)
        print(self.path_dict[0])
        if self.counter== 0:
            self.path_dict[(self.counter)]=(nuvarande_plats_str)
            print(self.path_dict[self.counter])
            self.counter+=1
        #nuvarande_plats_str=subprocess.check_output(['ls','-l','-a'])
        #print(self.nuvarande_plats_str)
        return nuvarande_plats_str


    def foregaende_plats(self):
        #self.framat=subprocess.Popen(["/usr/bin/echo", "$OLDPWD"])
        #framat=subprocess.call(["/usr/bin/echo", "$OLDPWD"], shell=True)
        self.framat_str=self.path_dict[self.counter]
        print(self.framat_str)
        return self.framat_str 
        #should bring you to previous dir
    def framat(self):
        #subprocess.call(["/usr/bin/echo", " $OLDPWD"])
        #self.framat_str=subprocess.call(["env", "|", "grep", "OLDPWD"], shell=True)
        
        #self.framat_str=subprocess.check_output(["/usr/bin/echo", " $OLDPWD"], universal_newlines=True)
        print(self.framat_str)
        subprocess.call(["cd" ,(self.framat_str)], shell=True)
        print(self.nuvarande_plats())


        #brings you back to startdir 
    def home(self):
        subprocess.call(["cd","self.path_dict[0]:" ], shell=True)
        print(self.nuvarande_plats())


    def change_owner(self,user, fil):
        subrocess.run(["chown", (user), (fil)])
            

    def lista_filer(self):
        self.current_dir=os.listdir()
        #ls.stdin.write("ls.\n"
        #ls.stdin.close()
        print(self.current_dir)
        return self.current_dir
        #print(current_dir2)

    def ta_bort_fil(self):
        fil_att_ta_bort=input("vilken fil vill du ta bort")
        os.remove(fil_att_ta_bort)


    def flytta_bakat(self):
        flytta_bak=os.chdir("..")


    def byt_katalog(self, val):
        val=val
        byt_dir=os.chdir(val)

    def skapa_fil(self, plats, namn):
        plats=plats
        namn=namn
        #Path(plats+ namn).touch()
        subprocess.run(["touch", (plats), (namn)])


    def whoami(self):
        subprocess.call(["/usr/bin/whoami"], shell=True)

        
    
    def main_menu(self):
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("            Terminal Helper                                                                                                       ")
        print(" options are b=back l=list or ->forward <-back home       q for quit ")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print(self.nuvarande_plats())
        #print(self.lista_filer())
        #print(self.check_os())
        #print(self.whoami())

    
    def file_menu(self):
        print("-------------------------------------------------------------------------------")
        print("            Terminal Helper FILE                                               ")
        print(" options are b=back l=list or q for quit                                       ")
        print("-------------------------------------------------------------------------------")
        print(self.current_dir())
        #print(self.lista_filer())
    
    
    
    def keyboard_input(self):
        self.running=""
        while self.running!="q":
            self.running=input()
            if self.running == "b":
                self.flytta_bakat()
                self.lista_filer()
            if self.running=="l":
                self.lista_filer()
            if self.running=="q":
                break
            if self.running=="f":
                self.file_menu()
            if self.running == "\x1b[A":
                print("upp key")
            if self.running =="\x1b[B":
                print("down key")
            if self.running == "\x1b[C":
                print("right key")
                self.framat()

            if self.running == "\x1b[D":
                print("left key")
                self.flytta_bakat()
                self.lista_filer()
            if self.running=="\x1b[1~":
                print("home key")
                self.home()
            
            if self.running=="x1b[3~":
                print("delete key")

    #SERVICES SECTION
    def show_date(self):
        subprocess.run(["date"])

    def create_user(self):
        username=input("ange username")
        pass
    def add_user_to_group(self):
        group=input("vilken vilka grupper")
        
    def ping_a_host(self, os_type):
        if os_type=="win":
            result = subprocess.run(['powershell.exe', mellan_lagring ], stdout=subprocess.PIPE)
        if os_type=="linux":
            subprocess.run(["ping", "127.0.0.1"])
    def list_services(self, env):
        self.env=env
        if self.env=="init":
            subprocess.run(["service", "--status-all"])
        if self.env=="systemd":
            subprocess.run(["systemctl --list-units"])
    def change_rights(self, mode, filename):
        subprocess.run(["chmod", (mode), (filename)])
    
    def change_date(self, date,time):
        pass
    def open_ports(self):
        pass
    def search_for_program(self):
        pass
    def install_program(self):
        pass
    def remove_repositories(self):
        pass
    def add_repositories(self):
        pass
    def check_os(self):
        self.os_typ=subprocess.run(["uname", "-o"],stdout=subprocess.PIPE)
        os_typ=self.os_typ
        #print(os_typ)
        return os_typ





th=Terminal_helper("11", "12")
th.nuvarande_plats()
th.main_menu()
th.keyboard_input()
#skapa_fil("/home/jonny/", "rumpa.txt")
#th.ping_a_host("linux")
#th.show_date()
#th.list_services("init")
#th.check_os()
#th.nuvarande_plats()
#th.framat()
