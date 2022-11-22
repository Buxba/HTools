from python_console_menu import AbstractMenu, MenuItem




class distros(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Linux" , menu=menu_linux()))
        self.add_menu_item(MenuItem(2, "Windows" ))
        self.add_menu_item(MenuItem(3, "Mac" ))
        self.add_menu_item(MenuItem(4, "Android" ))
        self.add_menu_item(MenuItem(5, "Ios \n" ))


################################  LINUX
################################  Basic cmds
#####################################  managing files
#####################################  network tools


class menu_linux(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Managing files" , menu=cmd_linux()))
        self.add_menu_item(MenuItem(2, "Networking tools \n" , menu=net_linux() ))
#        self.add_menu_item(MenuItem(3, "" ))
#        self.add_menu_item(MenuItem(4, "" ))
#        self.add_menu_item(MenuItem(5, " \n" ))



class cmd_linux(AbstractMenu):
    def __init__(self):
        super().__init__("Bienvenue dans le menu Linux.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "cp", lambda : print(" \n $ cp existing_file (path_to_new_file)new_file \n\n $ cp -r dossier(ou /dossier) \n\n  Option -r permet de copier de façcon récursive le fichier vers un autre emplacement \n")))
        self.add_menu_item(MenuItem(2, "ls=dir" , lambda : print(" \n $ ls [OPTION] [FILE] \n \n -l : liste fichiers et dossiers sur une même colonne avec droits user/group/other \n -a : permet de voir tous fichiers et dossiers mêmes ceux cachés \n -al : permet voir tous fichiers et dossiers + détails sur droits fichers/dossier \n -d : affiche seuelement le dossier d entrée visé et non son contenu  \n -i : affiche en plus d un -l les inodes/noeuds d index/numéros d index (stockage de données sur un système de fichiers qui stocke des infos sur un fichier à l exception du nom et de ses données = POINTEUR EN C ) \n -s : liste les fichiers par ordre de taille \n -h : affiche taille fichier lisible \n -t : permet d afficher fochiers/dossiers en fonction de la date de la dernière modification \n \n")))
        self.add_menu_item(MenuItem(3, "lshw", lambda : print('\n Short for List Hardware \n \n $ lshw  \n \n $ Détails sur hardware spécifique** ici carté réseau : \n $ lshw -C network \n') ))
        self.add_menu_item(MenuItem(4, "mkdir" , lambda : print('\n Make New Folders \n \n $ mkdir new_dir   \n \n quand déjà dans bon path \n $ mkdir path_du_dossier/nom_dossier \n')))
        self.add_menu_item(MenuItem(5, "mv" , lambda : print('\n Copie \n \n $ mv file.txt /another/location \n \n Renomme ficher/dossier \n $ mv file.txt new_name_file.txt \n $ mv dir new_name_dir \n\n Supprime fichier/dossier \n $ rm file_name \n $ rm -r dir_name \n')))





class net_linux(AbstractMenu):
    def __init__(self):
        super().__init__("Salut \n")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, 'Ip : \n $ ip a l \n show ip configuration \n '))
        self.add_menu_item(MenuItem(2, 'Change Ip/Mac :  \n $ ip link set dev eth0 down \n\n $ macchanger -m 23:05:13:37:42:21 eth \n\n $ ip link set dev eth0 up \n'))
        self.add_menu_item(MenuItem(3, "Ip Static : \n $ ip addr add 10.5.23.42/24 dev eth0 \n "))
        self.add_menu_item(MenuItem(4, "DNS Lookup : \n $ dig compass-security.com \n "))
        self.add_menu_item(MenuItem(5, "Reverse DNS Lookup  \n $ dig -x 10.5.23.42 \n\n " ))



################################ CYBER KILL CHAIN
################################ 1 . RECO

        
class reco(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Whois"))
        self.add_menu_item(MenuItem(2, "Network Scan (Nmap)", menu=menu_nmap()))
        self.add_menu_item(MenuItem(3, "Sniffing", menu=menu_snif()))



class menu_nmap(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Usefull Options",  lambda : print('\n -n : Disable name and port resolution \n -PR : ARP host Discovery \n -Pn : Disable host discovery \n -sn : Disable port scan \n -sS/-sT/-sU : SYN/TCP connect/UDP scan \n -top-ports 50 : scan 50 top ports \n -iL file : host input file \n -oA file : write outpouts files (3 types) \n -sC : Script scan \n --script <file/category> : specific scripts \n -sV : version detection \n -6 : IPv6 scan ')))
        self.add_menu_item(MenuItem(2, "ARP Scan", lambda: print("Demo sub menu item selected")))
        self.add_menu_item(MenuItem(3, "Host discovery", ()))
        self.add_menu_item(MenuItem(4, "Scripts", lambda: print("Demo sub menu item selected")))
        self.add_menu_item(MenuItem(5, "TCP scan", ()))
        self.add_menu_item(MenuItem(6, " ", lambda: print("Demo sub menu item selected")))
        self.add_menu_item(MenuItem(7, "Host discovery", ()))


class menu_snif(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "ARP Spoofing",  lambda : print('\n -n : Disable name and port resolution \n -PR : ARP host Discovery \n -Pn : Disable host discovery \n -sn : Disable port scan \n -sS/-sT/-sU : SYN/TCP connect/UDP scan \n -top-ports 50 : scan 50 top ports \n -iL file : host input file \n -oA file : write outpouts files (3 types) \n -sC : Script scan \n --script <file/category> : specific scripts \n -sV : version detection \n -6 : IPv6 scan ')))
        self.add_menu_item(MenuItem(2, "Graphic tool", lambda: print("Demo sub menu item selected")))
        self.add_menu_item(MenuItem(3, "Show ARP cache", ()))
        self.add_menu_item(MenuItem(4, "Delete ARP cache", lambda: print("Demo sub menu item selected")))
        self.add_menu_item(MenuItem(5, "Snif Traffice", ()))
        self.add_menu_item(MenuItem(6, "", lambda: print("Demo sub menu item selected")))
        self.add_menu_item(MenuItem(7, "Host discovery", ()))



class DemoSubMenu3(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the demo sub menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Demo sub menu item", lambda: print("Demo sub menu item selected")))

class DemoSubMenu4(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the demo sub menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Demo sub menu item", lambda: print("Demo sub menu item selected")))


class DemoMenu(AbstractMenu):
    show_hidden_menu = False

    def __init__(self):
        super().__init__("Fais comme chez toi \n")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Distros", menu=distros()))
        self.add_menu_item(MenuItem(2, "Reconaissance",menu=reco()))
        self.add_menu_item(MenuItem(3, "Weaponization", menu=DemoSubMenu3()))
        self.add_menu_item(MenuItem(4, "Delivery", menu=DemoSubMenu4()))
        self.add_menu_item(MenuItem(5, "Exploit", menu=()))
        self.add_menu_item(MenuItem(6, "Installation",menu=()))
        self.add_menu_item(MenuItem(7, "Command & Control", menu=DemoSubMenu3()))
        self.add_menu_item(MenuItem(8, "Actions on objectives\n", menu=DemoSubMenu4()))



demoMenu = DemoMenu()
demoMenu.display()
