#!/usr/bin/python3
import os
import subprocess
import subprocess as sp
from subprocess import call as spc
from subprocess import check_output as check_output
import sys
from time import sleep
import glob
import shutil
from shutil import rmtree as rmtree

class Terminal_helper():
    
    def __init__(self, meaning_of_life):
        self.meaning_of_life=meaning_of_life
        self.pwd=subprocess.call(["pwd"])
        pwd_str=str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
        self.pwd_str=pwd_str
        self.home_str=pwd_str
        self.path_dict={0:(self.pwd_str)}
        self.counter=counter=0
        self.cd=subprocess.call(["cd", ".."], shell=True)
        self.cls=subprocess.call(["clear"])
    
    def clear_screen(self):
        spc('clear', shell=True)
        
    #FILE SECTION
    #dir files and view them
    def file_reader(self):
        self.ls_file_array=glob.glob(self.pwd_str+"/*")
        counter=0
        for name in self.ls_file_array:
            file_checker=self.ls_file_array[counter]
            if os.path.isfile(str(file_checker)):
                print(f'{counter}:{name}')
            if os.path.isdir(str(file_checker)):
                print(f'{counter}:{name}'+ "(dir)")
            counter +=1
        file_number=int(input('open file nr? or q for quit'))
        filename=self.ls_file_array[file_number]
        if os.path.isfile(filename):
            try:
                my_file = open(filename, 'r')
                contents=my_file.read()
                print(contents)
            except:
                print("no go")
        else: 
            os.chdir(filename)
            self.pwd=spc(["pwd"])
            pwd_str=str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
            self.pwd_str=pwd_str
            self.counter+=1
            self.path_dict.update({self.counter:(self.pwd_str)})
       
    #should show current location
    def current_location(self):
        print(self.pwd_str)
        return self.pwd_str
        
        #should bring you to previous dir
    def move_forward(self):
        if self.counter>0:
            self.counter -=1
            path=self.path_dict.get(self.counter)
            move_forward=os.chdir(str(path))
            pwd_str=str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
            self.pwd_str=pwd_str

        #move_forward=subprocess.call(["cd "], shell=True)
        print(self.pwd_str)
        self.path_dict.update ({self.counter:self.pwd_str})


        #should move out from home and towards filesystem root
    def move_out(self):
        self.cls
        self.move_out_str=os.chdir("..")
        #self.move_out_str=subprocess.call(["cd ",".."], shell=True)
        #self.cd
        self.counter +=1
        self.pwd=spc(["pwd"])
        pwd_str=str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
        self.pwd_str=pwd_str
        self.path_dict.update({self.counter:(self.pwd_str)})

        #brings you back to startdir 
    def home(self):
        os.chdir(self.home_str)
        print(self.current_location_str)
        self.counter=0


    def change_owner(self,user, fil):
        subrocess.run(["chown", (user), (fil)])
            

    def list_files(self):
        self.current_dir=os.listdir()
        print(self.current_dir)
        return self.current_dir

    def remove_file(self):
       
        self.ls_file_array=glob.glob(self.pwd_str+"/*")
        counter=0
        for name in self.ls_file_array:
            file_checker=self.ls_file_array[counter]
            if os.path.isfile(str(file_checker)):
                print(f'{counter}:{name}')
            if os.path.isdir(str(file_checker)):
                print(f'{counter}:{name}'+ "(dir)")
            counter +=1
        file_number=int(input('remove file nr? or q for quit'))
        filename=self.ls_file_array[file_number]
        if os.path.isfile(filename):
            no_regrett=input("do you wish to delete" +(filename) +"answer yes or no")
            if no_regrett=="yes":
                try:
                    os.remove(filename)
                    self.list_files()
                except:
                    print("no go")
                    
            else:
                self.list_files()
        if os.path.isdir(filename):
            try:
                rmtree(filename)
                self.list_files()
            except:
                print("no go")
            
     
    def create_file(self,file_path, file_name):
        self.file_name=file_name
        self.file_path=file_path
        try:
            self.file_name=open((file_path+"/"+file_name), 'w+')
        except:
            print("no go")

    def whoami(self):
        subprocess.call(["whoami"], shell=True)

        
    
    def main_menu(self):
        #subprocess.call(["clear"])
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print("Terminal Helper  " +self.pwd_str + "     "+ (str(self.show_date()))+"                                                                                                       ")
        print(" options are < =cd..  >=fw  l=list o=open  c=create file d=delete  q for quit ")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
    
    
    
    
    def keyboard_input(self):
        self.running=""
        if int(self.meaning_of_life)!=42:
            quit()
        while self.running !="q":
            self.main_menu()
            self.running=input()
            if self.running=="l":
                spc('clear')
                self.main_menu()
                self.list_files()
                continue
            if self.running=="q":
                break
            if self.running == "\x1b[C":
                spc('clear')
                self.main_menu()
                print(self.path_dict[self.counter])
                if self.counter>0:
                    self.move_forward()
                    self.list_files()
                continue
            if self.running == "\x1b[D":
                spc('clear')
                self.main_menu()
                self.move_out()
                self.list_files()
                continue
            if self.running=="^[[H":
                self.home()
                continue
            #if self.running=="x1b[3~":
                #print("delete key")
            if self.running=="open" or self.running=="o" or self.running=="\x1b[A" or self.running=="^[[A" :
                spc('clear', shell=True)
                self.main_menu()
                self.file_reader()
                continue
            if self.running=="d":
                spc('clear', shell=True)
                self.main_menu()
                self.remove_file() 
            if self.running=="c":
                spc('clear', shell=True)
                self.create_file(self.pwd_str, (input("filename")))
                continue
    #SERVICES SECTION
    def show_date(self):
        subprocess.run(["date"])

    def create_user(self):
        username=input("ange username")
        pass
    def add_user_to_group(self):
        group=input("vilken vilka grupper")
        
    def ping_a_host(self, os_type):
        if os.name=="win":
            result = subprocess.run(['powershell.exe', mellan_lagring ], stdout=subprocess.PIPE)
        if os.name=="linux":
            subprocess.run(["ping", " 127.0.0.1"])
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




sp.call(["clear"])
th=Terminal_helper("42")
th.keyboard_input()
