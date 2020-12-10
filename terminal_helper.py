#!/usr/bin/python3
import os
import subprocess
import sys
from time import sleep
import glob

class Terminal_helper():
    
    def __init__(self, something, something_else):
        self.something=something
        self.something_else=something_else
        self.pwd=subprocess.call(["pwd"])
        pwd_str=str(subprocess.check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
        self.pwd_str=pwd_str
        self.home_str=pwd_str
        self.path_dict={0:(self.pwd_str)}
        self.counter=counter=0
        self.cd=subprocess.call(["cd", ".."], shell=True)
        self.cls=subprocess.call(["clear"])
   
    
    def cls(self):
        cls=subprocess.call(["clear"])

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
                print("------------dir------------------")
                print(f'{counter}:{name}')
                print("---------------------------------")
            counter +=1
        file_number=int(input('open file nr? or q for quit'))
        filename=self.ls_file_array[file_number]
        if os.path.isfile(filename):
            my_file = open(filename, 'r')
            contents=my_file.read()
            print(contents)
        else: 
            os.chdir(filename)
            
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
            pwd_str=str(subprocess.check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
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
        self.pwd=subprocess.call(["pwd"])
        pwd_str=str(subprocess.check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'' )
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

    def ta_bort_fil(self):
        fil_att_ta_bort=input("vilken fil vill du ta bort")
        os.remove(fil_att_ta_bort)

    def skapa_fil(self, plats, namn):
        plats=plats
        namn=namn
        #Path(plats+ namn).touch()
        subprocess.run(["touch", (plats), (namn)])


    def whoami(self):
        subprocess.call(["whoami"], shell=True)

        
    
    def main_menu(self):
        #subprocess.call(["clear"])
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        print("Terminal Helper  " +self.pwd_str + "     "+ (str(self.show_date()))+"                                                                                                       ")
        print(" options are < =cd..  >=fw  l=list o=open q for quit ")
        print("-------------------------------------------------------------------------------------------------------------------------------------")
        #print(self.current_location())
        #print(self.lista_filer())
        #print(self.check_os())
        #print(self.whoami())

    
    def file_menu(self):
        
        print("-------------------------------------------------------------------------------")
        print("            Terminal Helper FILE                                               ")
        print(" options are b=back l=list or q for quit                                       ")
        print("-------------------------------------------------------------------------------")
        #print(self.current_dir())
        #print(self.lista_filer())
    
    
    
    def keyboard_input(self):
        self.running=""
        while self.running !="q":
            self.main_menu()
            self.running=input()
            if self.running=="l":
                self.list_files()
                continue
            if self.running=="q":
                break
            if self.running=="f":
                self.file_menu()
            if self.running == "\x1b[C":
                print(self.path_dict[self.counter])
                if self.counter>0:
                    self.move_forward()
                    self.list_files()
                continue
            if self.running == "\x1b[D":
                self.move_out()
                self.list_files()
                continue
            if self.running=="^[[H":
                #print("home key")
                self.home()
                continue
            #if self.running=="x1b[3~":
                #print("delete key")
            if self.running=="open" or self.running=="o":
                self.file_reader()
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




subprocess.call(["clear"])
th=Terminal_helper("11", "12")
th.keyboard_input()
