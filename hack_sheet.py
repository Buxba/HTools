from python_console_menu import AbstractMenu, MenuItem

class DemoSubMenu6(AbstractMenu):
    def __init__(self):
        super().__init__("Salut")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Ip" , lambda : print('\n $ ip a l \n show ip configuration')))
        self.add_menu_item(MenuItem(2, "Change Ip/Mac" , lambda : print('\n $ ip link set dev eth0 down \n $ macchanger -m 23:05:13:37:42:21 eth \n $ ip link set dev eth0 up')))
        self.add_menu_item(MenuItem(3, "Ip Static" , lambda : print('\n $ ip addr add 10.5.23.42/24 dev eth0 ')))
        self.add_menu_item(MenuItem(4, "DNS Lookup", lambda : print('\n $ dig compass-security.com ')))
        self.add_menu_item(MenuItem(5, "Reverse DNS Lookup" , lambda : print(' \n $ dig -x 10.5.23.42')))


class DemoSubMenu1(AbstractMenu):
    def __init__(self):
        super().__init__("Bienvenue dans le menu Linux.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "cp", lambda : print(" \n $ cp existing_file (path_to_new_file)new_file \n\n $ cp -r dossier(ou /dossier) \n\n  Option -r permet de copier de façcon récursive le fichier vers un autre emplacement \n")))
        self.add_menu_item(MenuItem(2, "ls/dir" , lambda : print('n dir = ls \n \n $ dir [OPTION] <FILE> \n \n $ dir /etc \n liste fichiers et dossiers d un chemin spécfique par ordre alphabétique \n \n $ dir -1 /etc \n liste fichiers et dossiers sur une même colonne \n \n $ dir -a / -al \n comme avec ls -a/al \n -a permet de voir tous fichiers et dossiers mêmes ceux cachés \n -al permet voir tous fichiers et dossiers + détails sur droits fichers/dossiers1 \n\n  $ dir -d/-dl \n -d affiche seuelement le fichier d entrée visé et non son contenu \n -dl liste répertoire comprenant le proprio, groupe propriétaire et autorisations \n \n $ dir -i /-il \n -i affiche en plus d un -l les inodes/noeuds d index/numéros d index (stockage de données sur un système de fichiers qui stocke des infos sur un fichier à l exception du nom et de ses données = POINTEUR EN C ) \n \n $ dir -shl \n -s liste les fichiers par ordre de taille \n -h permet d afficher taille fichiers lisible humainement \n\n  $ dir -t \n permet d afficher fochiers/dossiers en fonction de la date de la dernière modification \n \n \n')))
        self.add_menu_item(MenuItem(3, "lshw", lambda : print('\n Short for List Hardware \n \n $ lshw  \n \n $ Détails sur hardware spécifique** ici carté réseau : \n $ lshw -C network \n') ))
        self.add_menu_item(MenuItem(4, "mkdir" , lambda : print('\n Make New Folders \n \n $ mkdir new_dir   \n \n quand déjà dans bon path \n $ mkdir path_du_dossier/nom_dossier \n')))
        self.add_menu_item(MenuItem(5, "mv" , lambda : print('\n Copie \n \n $ mv file.txt /another/location \n \n Renomme ficher/dossier \n $ mv file.txt new_name_file.txt \n $ mv dir new_name_dir \n\n Supprime fichier/dossier \n $ rm file_name \n $ rm -r dir_name \n')))
        self.add_menu_item(MenuItem(6,"Networking tools" , menu=DemoSubMenu6()))
        
class DemoSubMenu2(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the demo sub menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Demo sub menu item", lambda: print("Demo sub menu item selected")))


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
        super().__init__("Fais comme chez toi n")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Linux", menu=DemoSubMenu1()))
        self.add_menu_item(MenuItem(2, "Windows",menu=DemoSubMenu2()))
        self.add_menu_item(MenuItem(3, "Recon-ng", menu=DemoSubMenu3()))
        self.add_menu_item(MenuItem(4, "Nmap \n", menu=DemoSubMenu4()))



demoMenu = DemoMenu()
demoMenu.display()