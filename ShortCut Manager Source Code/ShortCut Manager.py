import subprocess
import sys
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser
import os
import sys
import ctypes
root = Tk()


def is_admin():
    """Vérifie si le script est exécuté en tant qu'administrateur."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Relance le script en tant qu'administrateur."""
    if is_admin():
        # Exécutez ici la commande ou le script en tant qu'administrateur
        print("Script en cours d'exécution en tant qu'administrateur.")
        # Exemple : Exécution d'une commande
        command = "mkdir C:\\TestAdmin"  # Remplacez par la commande souhaitée
        subprocess.run(command, shell=True)
    else :
        # Relance le script en demandant les privilèges d'administrateur
        print("Demande des droits d'administrateur...")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
def resource_path(relative_path):
    """Get absolute path to resource"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)
class Menu:
    def __init__(self, root):
        # icone
        self.icon_ShortCut_Manage = root.iconbitmap(resource_path(r'images\ShortCut-Manage.ico'))
        #geometry window
        root.geometry('600x695+300+0')
        #title
        root.title('ShortCut Manager')
        #background window
        root.configure(background='#235CB1')
        #resizable window
        root.resizable(False,False)
        #frame menu ShortCut Manager
        frame_menu = Frame(root,bg='black')
        frame_menu.place(x=0,y=0,width=600,height=100)
        #frame button
        frame_button = Frame(root,bg='green')
        frame_button.place(x=0,y=555,width=600,height=140)
        ######################################################
        self.var1 = IntVar()  # powershell
        self.var2 = IntVar()  # cmd
        self.var3 = IntVar()  # firewall
        self.var4 = IntVar()  # network
        self.var5 = IntVar()  # registry file
        self.var6 = IntVar()  # shell file
        self.var7 = IntVar()  # systemproperities
        self.on_img = PhotoImage(width=48, height=24)
        self.off_img = PhotoImage(width=48, height=24)
        self.on_img.put(('green'), to=(0, 0, 47, 23))
        self.off_img.put(('red'), to=(0, 0, 47, 23))
        #---------image ShortCut Manage
        #open image
        self.img_menu = Image.open(resource_path(r'images\ShortCutManage.png'))
        #resize image
        self.resize_img_menu = self.img_menu.resize((90,90))
        self.new_img_menu = ImageTk.PhotoImage(self.resize_img_menu)
        #
        self.label_menu = Label(frame_menu,image=self.new_img_menu,bg='black')
        self.label_menu.place(x=20,y=0)
        #label ShortCut Manage
        self.label_menu_text = Label(frame_menu,text='ShortCut Manager',bg='black',font=('Charlemagne Std',29,'bold'),fg='white')
        self.label_menu_text.place(x=110,y=20)
        #Tools ShortCut Manage
        self.frame_tools = Frame(root,bg='white')
        self.frame_tools.place(x=0,y=100,width=600,height=455)
        #add Powershell
        #open image
        self.img_powershell = Image.open(resource_path(r'images\powershell.png'))
        #resize image
        self.resize_img_powershell = self.img_powershell.resize((60,60))
        self.new_img_powershell = ImageTk.PhotoImage(self.resize_img_powershell)
        #
        self.label_img_powershell = Label(self.frame_tools,image=self.new_img_powershell,bg='white')
        self.label_img_powershell.place(x=100,y=0)
        #label powershell 
        self.label_powershell = Label(self.frame_tools,text='PowerShell',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_powershell.place(x=170,y=10)
        #add Command Promt
        #open image
        self.img_cmd = Image.open(resource_path(r'images\cmd.png'))
        #resize image
        self.resize_img_cmd = self.img_cmd.resize((60,60))
        self.new_img_cmd = ImageTk.PhotoImage(self.resize_img_cmd)
        #
        self.label_img_cmd = Label(self.frame_tools,image=self.new_img_cmd,bg='white')
        self.label_img_cmd.place(x=100,y=60)
        #label cmd
        self.label_cmd = Label(self.frame_tools,text='Command Promt',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_cmd.place(x=170,y=65)
        #add firewall
        #open image
        self.img_firewall = Image.open(resource_path(r'images\firewall.png'))
        #resize image
        self.resize_img_firewall = self.img_firewall.resize((60,60))
        self.new_img_firewall = ImageTk.PhotoImage(self.resize_img_firewall)
        #
        self.label_img_firewall = Label(self.frame_tools,image=self.new_img_firewall,bg='white')
        self.label_img_firewall.place(x=100,y=120)
        #label firewall 
        self.label_firewall = Label(self.frame_tools,text='Firewall',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_firewall.place(x=170,y=125)
        #add network
        #open image
        self.img_network = Image.open(resource_path(r'images\network.png'))
        #resize image
        self.resize_img_network = self.img_network.resize((60,60))
        self.new_img_network = ImageTk.PhotoImage(self.resize_img_network)
        #
        self.label_img_firewall = Label(self.frame_tools,image=self.new_img_network,bg='white')
        self.label_img_firewall.place(x=100,y=190)
        #label network 
        self.label_network = Label(self.frame_tools,text='Network',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_network.place(x=170,y=195)
        #add registry file
        #open image
        self.img_reg_file = Image.open(resource_path(r'images\reg_file.png'))
        #resize image
        self.resize_img_reg_file = self.img_reg_file.resize((70,70))
        self.new_img_reg_file = ImageTk.PhotoImage(self.resize_img_reg_file)
        #
        self.label_img_reg_file = Label(self.frame_tools,image=self.new_img_reg_file,bg='white')
        self.label_img_reg_file.place(x=100,y=250)
        #label registry file 
        self.label_reg_file = Label(self.frame_tools,text='Registry File',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_reg_file.place(x=170,y=265)
        #add shell file
        #open image
        self.img_shell_file = Image.open(resource_path(r'images\shell_file.png'))
        #resize image
        self.resize_img_shell_file = self.img_shell_file.resize((60,60))
        self.new_img_shell_file = ImageTk.PhotoImage(self.resize_img_shell_file)
        #
        self.label_img_shell_file = Label(self.frame_tools,image=self.new_img_shell_file,bg='white')
        self.label_img_shell_file.place(x=100,y=320)
        #label shell file 
        self.label_shell_file = Label(self.frame_tools,text='Shell File',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_shell_file.place(x=170,y=330)
        #add SystemProperties
        #open image
        self.img_SystemProperties = Image.open(resource_path(r'images\SystemProperties.png'))
        #resize image SystemProperties
        self.resize_img_SystemProperties = self.img_SystemProperties.resize((60,60))
        self.new_img_SystemProperties = ImageTk.PhotoImage(self.resize_img_SystemProperties)
        #
        self.label_img_SystemProperties = Label(self.frame_tools,image=self.new_img_SystemProperties,bg='white')
        self.label_img_SystemProperties.place(x=100,y=390)
        #label SystemProperties 
        self.label_SystemProperties = Label(self.frame_tools,text='SystemProperties',bg='white',fg='black',font=('Consolas',25,'bold'))
        self.label_SystemProperties.place(x=170,y=400)
        # Créer une seule fois le Checkbutton powershell
        self.cb1 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                               variable=self.var1, onvalue=1, offvalue=0, command=self.check_powershell)
        self.cb1.config(bg='red', activeforeground='red', activebackground='red')
        self.cb1.place(x=40, y=15)  
        # Créer une seule fois le Checkbutton Command Promt
        self.cb2 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                               variable=self.var2, onvalue=1, offvalue=0, command=self.check_cmd)
        self.cb2.config(bg='red', activeforeground='red', activebackground='red')
        self.cb2.place(x=40, y=75)
        # Créer une seule fois le Checkbutton firewall
        self.cb3 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                               variable=self.var3, onvalue=1, offvalue=0, command=self.check_firwall)
        self.cb3.config(bg='red', activeforeground='red', activebackground='red')
        self.cb3.place(x=40, y=140)
        # Créer une seule fois le Checkbutton network
        self.cb4 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                           variable=self.var4, onvalue=1, offvalue=0, command=self.check_network)
        self.cb4.config(bg='red', activeforeground='red', activebackground='red')
        self.cb4.place(x=40, y=210)
        # Créer une seule fois le Checkbutton check_reg_file
        self.cb5 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                           variable=self.var5, onvalue=1, offvalue=0, command=self.check_reg_file)
        self.cb5.config(bg='red', activeforeground='red', activebackground='red')
        self.cb5.place(x=40, y=275)
        # Créer une seule fois le Checkbutton check_shell_file
        self.cb6 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                           variable=self.var6, onvalue=1, offvalue=0, command=self.check_shell_file)
        self.cb6.config(bg='red', activeforeground='red', activebackground='red')
        self.cb6.place(x=40, y=340)
        # Créer une seule fois le Checkbutton check_system_properties
        self.cb7 = Checkbutton(self.frame_tools, image=self.off_img, selectimage=self.on_img, indicatoron=False, 
                           variable=self.var7, onvalue=1, offvalue=0, command=self.check_system_properties)
        self.cb7.config(bg='red', activeforeground='red', activebackground='red')
        self.cb7.place(x=40, y=400)
        #add button 
        add_btn = Button(frame_button,text='ADD',bg='white',bd='4',font=('Consolas',15,'bold'),activebackground='green',fg='gray',activeforeground='white',command=self.check_btn_add_all)
        add_btn.place(x=15,y=20,width=180,height=50)
        #delete button 
        delete_btn = Button(frame_button,text='DELETE',bg='white',bd='4',font=('Consolas',15,'bold'),activebackground='green',fg='gray',activeforeground='white',command=self.check_btn_delete_all)
        delete_btn.place(x=15,y=75,width=180,height=50)
        #select all button 
        select_btn = Button(frame_button,text='SELECT ALL',bg='white',bd='4',font=('Consolas',15,'bold'),activebackground='green',fg='gray',activeforeground='white',command=self.check_btn_selectall)
        select_btn.place(x=210,y=20,width=180,height=50)
        #deselect all button 
        deselect_btn = Button(frame_button,text='DESELECT ALL',bg='white',bd='4',font=('Consolas',15,'bold'),activebackground='green',fg='gray',activeforeground='white',command=self.check_btn_deselectall)
        deselect_btn.place(x=210,y=75,width=180,height=50)
        #about button 
        about_btn = Button(frame_button,text='ABOUT',bg='white',bd='4',font=('Consolas',15,'bold'),activebackground='green',fg='gray',activeforeground='white',command=self.about)
        about_btn.place(x=405,y=20,width=180,height=50)
        #exit button 
        exit_btn = Button(frame_button,text='EXIT',bg='white',bd='4',font=('Consolas',15,'bold'),activebackground='green',fg='gray',activeforeground='white',command=self.exit_root)
        exit_btn.place(x=405,y=75,width=180,height=50)
    def check_powershell(self):
        if self.var1.get() == 0:
            self.cb1.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')
        elif self.var1.get() == 1:
            self.cb1.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')

    def check_cmd(self):
        if self.var2.get() == 0:
            self.cb2.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')

        elif self.var2.get() == 1:
            self.cb2.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')

    def check_firwall(self):
        if self.var3.get() == 0:
            self.cb3.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')

        elif self.var3.get() == 1:
            self.cb3.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')

    def check_network(self):
        if self.var4.get() == 0:
            self.cb4.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')

        elif self.var4.get() == 1:
            self.cb4.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')

    def check_reg_file(self):
        if self.var5.get() == 0:
            self.cb5.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')

        elif self.var5.get() == 1:
            self.cb5.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')

    def check_shell_file(self):
        if self.var6.get() == 0:
            self.cb6.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')

        elif self.var6.get() == 1:
            self.cb6.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')

    def check_system_properties(self):
        if self.var7.get() == 0:
            self.cb7.config(image=self.off_img, bg='red', activeforeground='red', activebackground='red')

        elif self.var7.get() == 1:
            self.cb7.config(image=self.on_img, bg='green', activeforeground='green', activebackground='green')


    #check button
    def check_btn_add_1(self):
        if self.var1.get()==1:

            os.system(resource_path(r'outils\PowerShell.bat'))
    def check_btn_add_2(self):
        if self.var2.get()==1:
            os.system(resource_path(r'outils\CommandPrompt.bat'))
    def check_btn_add_3(self):            
        if self.var3.get()==1:
            os.system(resource_path(r'outils\Firewall.bat'))
    def check_btn_add_4(self):
        if self.var4.get()==1:
            os.system(resource_path(r'outils\Network.bat'))
    def check_btn_add_5(self):        
        if self.var5.get()==1:
            os.system(resource_path(r'outils\RegistryFile.bat'))
    def check_btn_add_6(self):
        if self.var6.get()==1:
            os.system(resource_path(r'outils\ShellFile.bat'))
    def check_btn_add_7(self):
        if self.var7.get()==1:
            os.system(resource_path(r'outils\SystemProperties.bat'))
    def check_btn_add_all(self):
        self.check_btn_add_1()
        self.check_btn_add_2()
        self.check_btn_add_3()
        self.check_btn_add_4()
        self.check_btn_add_5()
        self.check_btn_add_6()
        self.check_btn_add_7()
        self.check_btn_deselectall()
    def check_btn_delete_1(self):
        if self.var1.get()==1:
            os.system(resource_path(r'outils\PowerShellDELETE.bat'))
    def check_btn_delete_2(self):
        if self.var2.get()==1:
            os.system(resource_path(r'outils\CommandPromptDELETE.bat'))
    def check_btn_delete_3(self):            
        if self.var3.get()==1:
            os.system(resource_path(r'outils\FirewallDELETE.bat'))
    def check_btn_delete_4(self):
        if self.var4.get()==1:
            os.system(resource_path(r'outils\NetworkDELETE.bat'))
    def check_btn_delete_5(self):        
        if self.var5.get()==1:
            os.system(resource_path(r'outils\RegistryFileDELETE.bat'))
    def check_btn_delete_6(self):
        if self.var6.get()==1:
            os.system(resource_path(r'outils\ShellFileDELETE.bat'))
    def check_btn_delete_7(self):
        if self.var7.get()==1:
            os.system(resource_path(r'outils\SystemPropertiesDELETE.bat'))
    def check_btn_delete_all(self):
        self.check_btn_delete_1()
        self.check_btn_delete_2()
        self.check_btn_delete_3()
        self.check_btn_delete_4()
        self.check_btn_delete_5()
        self.check_btn_delete_6()
        self.check_btn_delete_7()
        self.check_btn_deselectall()
    def check_btn_selectall(self):
        if self.var1.get()==0:
            self.var1.set(1)
            self.check_powershell()
        if self.var2.get()==0:
            self.var2.set(1)
            self.check_cmd()
        if self.var3.get()==0:
            self.var3.set(1)
            self.check_firwall()
        if self.var4.get()==0:
            self.var4.set(1)
            self.check_network()
        if self.var5.get()==0:
            self.var5.set(1)
            self.check_reg_file()
        if self.var6.get()==0:
            self.var6.set(1)
            self.check_shell_file()
        if self.var7.get()==0:
            self.var7.set(1)
            self.check_system_properties()
    def check_btn_deselectall(self):
        if self.var1.get()==1:
            self.var1.set(0)
            self.check_powershell()
        if self.var2.get()==1:
            self.var2.set(0)
            self.check_cmd()
        if self.var3.get()==1:
            self.var3.set(0)
            self.check_firwall()
        if self.var4.get()==1:
            self.var4.set(0)
            self.check_network()
        if self.var5.get()==1:
            self.var5.set(0)
            self.check_reg_file()
        if self.var6.get()==1:
            self.var6.set(0)
            self.check_shell_file()
        if self.var7.get()==1:
            self.var7.set(0)
            self.check_system_properties()
    def about(self):
        #setting window
        self.root_info = tk.Toplevel()
        self.root_info.geometry('400x500+600+100')
        self.root_info.resizable(False,False)
        self.ico_info = self.root_info.iconbitmap(resource_path(r'images\ShortCut-Manage.ico'))
        self.root_info.title('Information ShortCut Manager')
        
        # frame name programme
        self.fr_name = Frame(self.root_info,bg='#BABABA')
        self.fr_name.place(x=0,y=0,width=400,height=80)
        #-----image programme 
        self.img_inf_l = Image.open(resource_path(r'images\ShortCutManage.png'))
        self.resize_inf_l = self.img_inf_l.resize((70,70))
        self.new_img_inf_l = ImageTk.PhotoImage(self.resize_inf_l)

        self.lb_img_inf_l = Label(self.fr_name,image=self.new_img_inf_l,bg='#BABABA')
        self.lb_img_inf_l.place(x=5,y=0)
        
        # text shortcut manager
        self.lb_menu_text = Label(self.fr_name,text='ShortCut Manager',bg='#BABABA',font=('Charlemagne Std',19,'bold'),fg='white')
        self.lb_menu_text.place(x=80,y=20)

        #frame info
        self.fr_inf = Frame(self.root_info,bg='#E7E6E8')
        self.fr_inf.place(x=0,y=80,width=400,height=370)

        #image info 
        self.img_inf = Image.open(resource_path(r'images\logo.png'))
        self.resize_img_inf = self.img_inf.resize((70,70))
        self.new_img_inf = ImageTk.PhotoImage(self.resize_img_inf)

        self.label_inf = Label(self.fr_inf,image=self.new_img_inf,bg='#E7E6E8')
        self.label_inf.place(x=5,y=0)
        self.shortcut_text = 'About The Context Menu Shortcut Manager'
        self.label_shortcat_text = Label(self.fr_inf,text=self.shortcut_text,bg='#E7E6E8')
        self.label_shortcat_text.place(x=100,y=30)
        shortcat_text_m ="""
The Context Menu Shortcut Manager simplifies adding and removing
shortcut windows context menu.With a user-friendlyPython interface,
you can quickly customize access to essential tools like Powershell
and Command Promt.


Features:
Add Shortcuts : Easily integrate essential tools.
Remove Shortcuts : clean up unwanted entries.
Simple Interfaces : Navigate effortlessy through a command-line menu.
"""
        self.label_shortcat_text_m = Label(self.fr_inf,text=shortcat_text_m,bg='#E7E6E8',font=('Segoe UI',9),justify=LEFT)
        self.label_shortcat_text_m.place(x=10,y=65)
        #link github
        github_text = 'For more updates and more info,check us out on Github '
        label_github = Label(self.fr_inf,text=github_text,bg='#E7E6E8',justify=CENTER)
        label_github.place(x=40,y=260)

        link_github = Label(self.fr_inf,text='https://github.com/Aouane-S',fg="blue", cursor="hand2",bg='#E7E6E8')
        link_github.bind("<Button-1>", lambda Event : webbrowser.open_new("https://github.com/Aouane-S"))
        link_github.place(x=40,y=280)
        
        #link Linkedin
        Linkedin_text = 'Linkedln'
        label_Linkedin = Label(self.fr_inf,text=Linkedin_text,bg='#E7E6E8',justify=CENTER)
        label_Linkedin.place(x=40,y=310)

        link_Linkedin = Label(self.fr_inf,text='https://ma.linkedin.com/in/soufiane-aouane-a676122a3',fg="blue", cursor="hand2",bg='#E7E6E8')
        link_Linkedin.bind("<Button-1>", lambda Event : webbrowser.open_new("https://ma.linkedin.com/in/soufiane-aouane-a676122a3"))
        link_Linkedin.place(x=40,y=330)

        # Add the OK button with a blue border effect
        frame_bottom = Frame(self.root_info,bg='#E0E0E0')
        frame_bottom.place(x=0,y=450,width=400,height=50)
        frame_btn = Frame(frame_bottom,bg='white')
        frame_btn.place(x=320,y=15,width=70,height=20)
        btn_frame1 = Frame(frame_btn,highlightbackground="#007ECC",highlightthickness=1)
        btn_frame2 = Frame(btn_frame1,highlightbackground="#007ECC",highlightthickness=1)
        ok_button = Button(
            btn_frame2,
            text="OK",
            width=10,
            height=1,
            bg="#f0f0f0",  # Background color
            fg="black",    # Text color
            relief="flat",  # Flat relief style
            bd=0,
            command=lambda :self.root_info.destroy()
        )
        ok_button.bind('<Enter>', lambda e: ok_button.config(bg='#B8DDF5'))
        ok_button.bind('<Leave>', lambda e: ok_button.config(bg='whitesmoke'))
        btn_frame2.bind('<Enter>', lambda e: btn_frame2.config(highlightthickness=0))
        btn_frame2.bind('<Leave>', lambda e: btn_frame2.config(highlightthickness=1))

        ok_button.pack(pady=0,padx=0)  # Add some padding to space the button
        btn_frame1.pack(pady=0,padx=0)
        btn_frame2.pack(pady=0,padx=0)


        self.root_info.mainloop()

    def exit_root(self):
        root.destroy()



if __name__ == "__main__":
    run_as_admin()
    main=Menu(root)
    root.mainloop()
    

