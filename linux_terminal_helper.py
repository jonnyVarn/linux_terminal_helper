#!/usr/bin/python3
import os
import subprocess
import subprocess as sp
from subprocess import call as spc
from subprocess import check_output as check_output
import sys
from time import sleep as sleep
import glob
import shutil
from shutil import rmtree as rmtree
from getpass import getpass
from shutil import disk_usage as du
from shutil import unpack_archive as unpack
from os import getcwd as getcwd
from os.path import isfile
from os.path import isdir

class TerminalHelper():

    def __init__(self, meaning_of_life):
        self.meaning_of_life = meaning_of_life
        self.pwd = subprocess.call(["pwd"])
        pwd_str = str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'')
        self.pwd_str = pwd_str
        self.home_str = pwd_str
        self.path_dict = {0: (self.pwd_str)}
        self.counter = counter = 0
        self.cd = subprocess.call(["cd", ".."], shell=True)
        self.cls = subprocess.call(["clear"])
        self.print_on_the_menu = "test"
        self.print_on_the_menu1 = "test"
        self.print_on_the_menu2 = "test"
        self.print_on_the_menu3 = "test"
        self.menu_needed = False
        self.linux_init = ""

        

    # just starting bash from the program
    def bash(self):
        spc(["bash"], shell=True)
        print(getcwd())
        self.pwd = spc(["pwd"], shell=True)
        pwd_str = str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'')
        self.pwd_str = pwd_str
        self.counter = 99
        self.path_dict.update({self.counter: (self.pwd_str)})
        print(self.pwd_str)

    def write_note(self):
        note_name = input("input filename")
        # the current working directory will be pwd
        pwd = getcwd()
        # new_name will be cwd+/+inputed note_name
        new_name = pwd + "/" + note_name
        # if path provided already is a file:
        if isfile(new_name):
            try:
                # open the file in read mode
                file = open(new_name, 'r')
                # take input from keyboard and present the file content in input prompt
                note_input = input(file.read())
                # close the file
                file.close()
                # open the file in append mode
                file = open(new_name, 'a')
                # write the input to the file
                file.write(note_input)
                # close the file again.
                file.close()

            except:
                print("no go append")

        if isfile(new_name) == False:
            try:
                file = open(new_name, 'w+')
                note_input = input("write something")
                file.write(note_input)
                file.close()
            except:
                print("shit pomesfrites")

    def sudo(self):
        pass

    def th_help(self):
        print(
            "as the names states this is a terminal helper for linux you could print stuff and delete stuff. for writing notepad cd.. print left arrow for cd / print left arrow twice for going to privios dir press right key for home press right key twice for open a file press o. Delete press o and if you get bored print bash")

    def clear_screen(self):
        spc(["bash"], shell=True)

    # FILE SECTION
    # dir files and view them
    def file_reader(self):
        self.ls_file_array = glob.glob(self.pwd_str + "/*")
        counter = 0
        for name in self.ls_file_array:
            file_checker = self.ls_file_array[counter]
            if os.path.isfile(str(file_checker)):
                print(f'{counter}:{name}')
            if os.path.isdir(str(file_checker)):
                print(f'{counter}:{name}' + "(dir)")
            counter += 1
        file_number = int(input('open file nr? or q for quit'))
        filename = self.ls_file_array[file_number]
        if os.path.isfile(filename):
            try:
                my_file = open(filename, 'r')
                contents = my_file.read()
                print(contents)
            except:
                print("no go")
        else:
            os.chdir(filename)
            self.pwd = spc(["pwd"])
            pwd_str = str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'')
            self.pwd_str = pwd_str
            self.counter += 1
            self.path_dict.update({self.counter: (self.pwd_str)})

    # should show current location
    def current_location(self):
        print(self.pwd_str)
        print("-->")
        if os.name == 'nt':
            print(os.getcwd)
            os.get
        return self.pwd_str

        # should bring you to previous dir

    def move_forward(self):
        if self.counter > 0:
            self.counter -= 1
            path = self.path_dict.get(self.counter)
            move_forward = os.chdir(str(path))
            pwd_str = str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'')
            self.pwd_str = pwd_str

        # move_forward=subprocess.call(["cd "], shell=True)
        print(self.pwd_str)
        self.path_dict.update({self.counter: self.pwd_str})

        # should move out from home and towards filesystem root

    def move_out(self):
        self.cls
        self.move_out_str = os.chdir("..")
        # self.move_out_str=subprocess.call(["cd ",".."], shell=True)
        # self.cd
        self.counter += 1
        self.pwd = spc(["pwd"])
        pwd_str = str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'')
        self.pwd_str = pwd_str
        self.path_dict.update({self.counter: (self.pwd_str)})
        # should move you to file root /

    def move_out_fast(self):
        self.cls
        self.move_out_str = os.chdir("/")
        # self.move_out_str=subprocess.call(["cd ",".."], shell=True)
        # self.cd
        self.counter += 1
        self.pwd = spc(["pwd"])
        pwd_str = str(check_output(["pwd"], shell=True, )).strip('\'' '\\b' '\\n' '\'')
        self.pwd_str = pwd_str
        self.path_dict.update({self.counter: (self.pwd_str)})

        # brings you back to startdir

    def home(self):
        os.chdir(self.home_str)
        self.counter = 0
        self.pwd_str = self.home_str

    def change_owner(self):
        fil = input("filename")
        fil = self.pwd_str + "/" + fil
        user = os.geteuid()
        group = os.getegid()
        # user=input("username")
        print(str(user) + "  " + fil + str(group))
        os.chown(fil, user, group)

    def list_files(self):
        self.current_dir = os.listdir()
        print(self.current_dir)
        return self.current_dir
        self.print_on_the_menu1 = du(self.pwd_str)

    def remove_file(self):

        self.ls_file_array = glob.glob(self.pwd_str + "/*")
        counter = 0
        for name in self.ls_file_array:
            file_checker = self.ls_file_array[counter]
            if os.path.isfile(str(file_checker)):
                print(f'{counter}:{name}')
            if os.path.isdir(str(file_checker)):
                print(f'{counter}:{name}' + "(dir)")
            counter += 1
        file_number = int(input('remove file nr? or q for quit'))
        filename = self.ls_file_array[file_number]
        if os.path.isfile(filename):
            no_regrett = input("do you wish to delete" + (filename) + "answer yes or no")
            if no_regrett == "yes":
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

    def create_file(self, file_path, file_name):
        self.file_name = file_name
        self.file_path = file_path
        try:
            self.file_name = open((file_path + "/" + file_name), 'w+')
        except:
            print("no go")

    def create_dir(self, path):
        pass

    def whoami(self):
        subprocess.call(["whoami"], shell=True)

    # SERVICES SECTION
    def show_date(self):
        subprocess.run(["date"])

    def create_user(self):
        os.seteuid
        username = input("ange username")
        pass

    def add_user_to_group(self):
        group = input("vilken vilka grupper")

        # rather useless right now but you can ping a host

    def ping_a_host(self):
        # if os.name=="win":
        # result = subprocess.run(['powershell.exe', mellan_lagring ], stdout=subprocess.PIPE)
        # if os.name=="linux":
        host_name = input("enter host to ping")
        host_name = "ping" + " " + host_name + " -c 3"
        subprocess.run([host_name], shell=True)
        check_output([host_name], shell=True)

    def list_services(self):
        # spc("ps --no-headers")
        # test=check_output("ps --no-headers -o")
        # print(test)

        # spc("ps ", "--no" ,"-headers" ," -o" ," comm 1")
        # init_or_systemd=check_output("ps ", "--no", "-headers", " -o", "comm 1", shell=True)
        # print(init_or_systemd)
        # if init_or_systemd=="init":
        try:
            subprocess.run(["service --status-all"], shell=True)
            services = check_output(["service --status-all"], shell=True)
            print(services)
        except:
            print("you are not running init")
            self.linux_init = False
        try:
            spc(["systemctl --list-units"])
            services2 = check_output(["systemctl --list-units"])
            print(services2)
        except:
            print("running init")
            self.linux_init = True

    def change_rights(self, mode, filename):
        subprocess.run(["chmod", (mode), (filename)])

    def change_date(self, date, time):
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


    def main_menu(self, print_on_the_menu):
        self.print_on_the_menu = print_on_the_menu

        print(
            "-------------------------------------------------------------------------------------------------------------------------------------")
        print("Terminal Helper  " + self.pwd_str + "     " + (str(self.show_date())) + (self.print_on_the_menu1) + "  ")
        print(" options are < =cd..  >=fw  l=list o=open  c=create file d=delete  q for quit   " + (print_on_the_menu))
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------")

    def keyboard_input(self):
        menu_counter = 0
        self.running = ""
        spc('clear')
        if int(self.meaning_of_life) != 42:
            quit()
        while self.running != "q":
            menu_counter += 1
            self.write_on_the_menu = "welcome if menu is missing press <>^ once or twice followed by enter"
            if menu_counter == 1:
                self.main_menu(self.print_on_the_menu)
            if self.menu_needed == True:
                self.main_menu(self.print_on_the_menu)
            self.running = input()
            if self.running == "l":
                spc('clear')
                self.main_menu("")
                self.list_files()
                continue
            if self.running == "q":
                break
            if self.running == "\x1b[C":
                spc('clear')
                self.main_menu("")
                print(self.path_dict[self.counter])
                if self.counter > 0:
                    self.move_forward()
                    self.list_files()
                continue
            if self.running == "\x1b[D" or self.running == "<":
                spc('clear')
                self.main_menu("cd .. if you want more action press twice for cd /")
                self.move_out()
                self.list_files()
                continue
            if self.running == "^[[H":
                spc('clear')
                self.main_menu("home")
                self.home()
                continue

            if self.running == "\x1b[D\x1b[D" or self.running == "<<":
                spc('clear')
                self.main_menu("cd / wow that was fast")
                self.move_out_fast()
                self.list_files()
                continue

            if self.running=="x1b[3~":
                print("delete key function not enabled for safetyreasons")
                self.main_menu("")    
            if self.running == "open" or self.running == "o" or self.running == "\x1b[A" or self.running == "^[[A":
                spc('clear', shell=True)
                self.main_menu(self.print_on_the_menu)
                self.file_reader()
                self.menu_needed = False
                sleep(0.2)
                self.print_on_the_menu="exiting open"
                self.main_menu(self.print_on_the_menu)
                continue
            if self.running == "d":
                spc('clear', shell=True)
                self.main_menu("")
                self.remove_file()
                self.main_menu("exiting delete")
                continue
            if self.running == "c":
                spc('clear', shell=True)
                self.print_on_the_menu = "WRITE A FILE NAME"
                self.main_menu(self.print_on_the_menu)
                self.create_file(self.pwd_str, (input("")))
                spc('clear')
                self.main_menu("exiting c")
                continue
                continue
            if self.running == "\x1b[C\x1b[C" or self.running==">>":
                self.print_on_the_menu = ("not so fast ok ok bringing you home")
                self.home()
                spc('clear')
                self.main_menu("exiting cd")
                continue
            if self.running == "h" or self.running == "-h" or self.running == "help":
                self.th_help()
                continue
            if self.running == "bash":
                self.bash()
            if self.running == "notepad" or self.running == "^[[A^[[A" or self.running == "\x1b[A\x1b[A":
                self.write_note()
                sleep(0.2)
                spc('clear')
                self.main_menu("exit notepad")
                continue
            if self.running == "ping":
                self.ping_a_host()
            if self.running == "service":
                self.list_services()
            else:
                spc('clear')
                self.main_menu(self.print_on_the_menu)
                self.print_on_the_menu = ("this is a bit complicated press left,right or upp key one or twice and press enter")


spc(["clear"])
th = TerminalHelper("42")
# th.change_owner()
th.keyboard_input()

"""
Rapport till uppgift 2 i Linux och skriptspråk av Jonny Värn.
Jag använder mig av VIM med plugin airline, justify, matchit, powerline och python-jedi för att få en trevlig utvecklingsmiljö med autokomplettering och lite finare vim.                
Jag använder mig av VIM eftersom jag sitter på en Linux konsol via ssh.
Jag hade använt en annan terminalbaserad kanske emacs eftersom jag valt att inte köra grafiskt. Om jag hade kört grafiskt så hade jag antagligen kört visualstudiocode, pycharm, atom eller någon annan IDE.
Jag valde filhanterare eftersom den låg på först och verkade vara den mest användbara applikationen. 
Filhanteraren började växa och utvecklades till Linux-terminal-helper när jag tänkte att den skulle kunna vara lite stöd för andra när de jobbar i Linux/Unix möjligtvis finns det en  en framtid i windows i terminalmiljö.  
Linux är ju egentligen en Kärna Linux/GNU är ett operativsystem och det finns många olika varianter av GNU/Linux några av de största listas nedan.
RHEL eller RedhatEnterprise där även Linus Torvalds huserar med community drivna varianter som Centos.
Debian med varianter som Ubuntu som nästan har gått om Debian i antal användare.
Suse Enterprise Linux som från början startade i Tyskland ursprungligen från Slackware Linux.
Det alla Linux varianter delar är som sagt Linux kärnan.
I alla Linux varianter kan man installera .tgz paket eller så kallade tar bollar.
Enklast kan vara att dela upp Linux i vilken pakethanterare de använder för att lättare se släktskapet.
RHEL och Centos är i princip samma Os förutom enterprise supporten och de använder sig av pakhethanteraren yum som kom ifrån yellowdog-linux som var det enda linux som fungerade för mac powerpc på den tiden det begav sig. 
En lite mer krånglig variant är rpm RedhatPacketManager där man själv får hålla ordning på vilka dependencies som behövs.

Debian, ubuntu, ubuntu mate etc använder sig av pakethanteraren apt. Eller den lite krångligare varianten där man får använda sig av dependencies själv dpkg
i
Av de som står själva förtjänar Alpine linux att nämnas ett minimalt komplett Linux/GNU som från början var avsett att användas på accesspunkter och mindre inbyggda enheter.


Vad finns det för användningsområden inom Linux?
Användningsområden inom Linux är oändliga men för att ge några exempel kan man tala om olika typer av servrar exempelvis DHCP-server.
Det finns olika styrdatorer.
Jag skulle ju klassificera Android som en Linux kärna så telefoner är ju ett annat område där vi använder Linux.

Beskriv hur ni använt er av Linux i denna applikation
Jag har utvecklat min applikation på antix linux (ett debian derrivat med init istället för systemd)
Jag har använt Vim och kört den ifrån en Linux terminal, jag har även testat applikationen på ubuntu och en openbsd, vilket inte är linux.
Beskriv de olika tjänster ni känner till som finns i Linux
Ja eftersom en tjänst är ett program som körs i bakgrunden så blir ju svaret nästan oändligt.
Jag väljer att lista några av de vanligaste.
Brandväggar firewalld, ufw, ip-tables. Dessa är tjänster som kan kontrollera vilka TCP/UDP portar som är öppna in eller ut på Linux.
FTP File Transfer Protocol som erbjuder fildelning. Det finns såklart en uppsjö utav FTP varianter.
 Cron/cronnyd etc är en tjänst som startar tjänster efter tid.
 Cups erbjuder delning av skrivare och skrivartjänster.
 Ntp är NetworkTimeProtocol och erbjuder tidssynkronisering.
 Systemlog tjänster som loggar händelser på systemet. några exempel är syslog-ng och rsyslog.
 SSH secureShell bjuder möjlighet att logga in på en dator via TCP/IP och är ersättaren till det mindre säkrare Telnet. Det ju många olika varianter av ssh servrar men min favorit kommer från en av mina favorit operativsystem openbsd och heter openssh.

  LinuxTerminalHelper är ett embryo för närvarande så är det en filhanterare med funktionerna 
  Notepad(write_note) som öppnar en fil och låter användaren skriva till den och sedan stänga.
  Flytta runt med hjälp av vänster, höger och uppåtpil. Skapa fil och ta bort fil med c respektive d lista filer med l.resterande funktioner är inte implementerade och bör därför inte användas.
Skriv en applikation som tillåter dig att flytta runt i filsystemet på din dator. Som en användare skall man kunna gå in i mappar, backa ur mappar, lista filer, skapa filer.
"""
