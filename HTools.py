from python_console_menu import AbstractMenu, MenuItem




class distros(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
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
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Managing files" , menu=cmd_linux()))
        self.add_menu_item(MenuItem(2, "Networking tools \n" , menu=net_linux()))
#        self.add_menu_item(MenuItem(3, "" ))
#        self.add_menu_item(MenuItem(4, "" ))
#        self.add_menu_item(MenuItem(5, " \n" ))



class cmd_linux(AbstractMenu):
    def __init__(self):
        super().__init__(" Commandes basiques : \n\n")

    def initialise(self):
        self.add_menu_item(MenuItem(0, ".. \n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "cp", lambda : print(" \n $ cp existing_file (path_to_new_file)new_file \n\n $ cp -r dossier(ou /dossier) \n\n  Option -r permet de copier de façcon récursive le fichier vers un autre emplacement \n")))
        self.add_menu_item(MenuItem(2, "ls=dir" , lambda : print(" \n $ ls [OPTION] [FILE] \n \n -l : liste fichiers et dossiers sur une même colonne avec droits user/group/other \n -a : permet de voir tous fichiers et dossiers mêmes ceux cachés \n -al : permet voir tous fichiers et dossiers + détails sur droits fichers/dossier \n -d : affiche seuelement le dossier d entrée visé et non son contenu  \n -i : affiche en plus d un -l les inodes/noeuds d index/numéros d index (stockage de données sur un système de fichiers qui stocke des infos sur un fichier à l exception du nom et de ses données = POINTEUR EN C ) \n -s : liste les fichiers par ordre de taille \n -h : affiche taille fichier lisible \n -t : permet d afficher fochiers/dossiers en fonction de la date de la dernière modification \n \n")))
        self.add_menu_item(MenuItem(3, "lshw", lambda : print('\n Short for List Hardware \n \n $ lshw  \n \n $ Détails sur hardware spécifique** ici carté réseau : \n $ lshw -C network \n') ))
        self.add_menu_item(MenuItem(4, "mkdir" , lambda : print('\n Make New Folders \n \n $ mkdir new_dir   \n \n quand déjà dans bon path \n $ mkdir path_du_dossier/nom_dossier \n')))
        self.add_menu_item(MenuItem(5, "mv" , lambda : print('\n Copie \n \n $ mv file.txt /another/location \n \n Renomme ficher/dossier \n $ mv file.txt new_name_file.txt \n $ mv dir new_name_dir \n\n Supprime fichier/dossier \n $ rm file_name \n $ rm -r dir_name \n')))
        self.add_menu_item(MenuItem(6, "du" , lambda : print('\n Affiche quantité d espace utilisé pour chaucun des dossier')))
        self.add_menu_item(MenuItem(7, "df" , lambda : print('\n Affiche espace utilisé sur système')))
        self.add_menu_item(MenuItem(8, "duf" , lambda : print('\n du + df \n check used and free space in a structured and eye-pleasing way ')))
        self.add_menu_item(MenuItem(9, "top" , lambda : print('\n Gestionnaire de tâche dans terminal')))
        self.add_menu_item(MenuItem(10, "sort" , lambda : print('\n Tri fichier alphabétique : \n $ sort [options] <filename> \n Numbers are sorted by their leading characters only \n\n $ sort file.txt -n : numerical value of the string is now being evaluated rather than only the first character \n\n $ sort filename.txt -r : sort un reverse order \n $ sort filename.txt -R : random sort \n\n $ sort filename.txt -M : sort by month \n\n $ sort filename.txt -n > filename_sorted.txt : save the sorted results to another file \n\n $ sort filename.txt -k 2 : sort specific column \n $ sort filename.txt -k 3n \n\n $ sort filename.txt -u > filename_duplicates.txt : sort and remove duplicates + copy results to another file \n\n $ sort filename.txt -f : ignore case while sorting \n\n $ sort filename.txt -h : sort by human numeric values \n\n\n')))
        self.add_menu_item(MenuItem(11, "find \n\n" , lambda : print('\n Affiche espace utilisé sur système : \n $ find [directory to search] [options] [expression] \n\n expressions : specify the search  \n\n\n $ find . -name SEARCH_NAME : files and directories by name, since no file type mentioned it searches for both \n\n $ find . -type f -name SEARCH_NAME : specific for files \n $ find . -type d -name SEARCH_NAME : specific for direcories \n\n $ find . -iname SEARCH_NAME : for a cas insensitive \n\n $ find . -type f -name "*.extension" : Search files by their extension \n find . -type f -name "*.cpp" -o -name "*.txt" : search multiple files with multiple extensions \n -o : works as a logical OR condition \n\n  $ find ./location1 /second/location -type f -name "pattern" : search for files in multiple directories \n\n SEARCH BASED ON FILE SIZE : $ find . -size 20k \n\n c : bytes \n k: kilobytes \n M : Megabytes \n G :Gigabytes \n\n\n')))
        self.add_menu_item(MenuItem(12, "grep" , lambda : print('\n tool used to search a string a characters in a specified file \n $ grep [option] <file> ')))






class net_linux(AbstractMenu):
    def __init__(self):
        super().__init__("Salut \n")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, 'Ip'  , lambda : print(' \n $ ip a l : show ip configuration \n ')))
        self.add_menu_item(MenuItem(2, 'Change Ip/Mac', lambda : print('\n $ ip link set dev eth0 down \n $ macchanger -m 23:05:13:37:42:21 eth \n $ ip link set dev eth0 up \n' )))
        self.add_menu_item(MenuItem(3, "Ip Static" , lambda : print('\n $ ip addr add 10.5.23.42/24 dev eth0 \n ')))
        self.add_menu_item(MenuItem(4, "DNS Lookup"  ,lambda : print(' \n $ dig compass-security.com \n')))
        self.add_menu_item(MenuItem(5, "Reverse DNS Lookup\n\n"  ,lambda : print('\n $ dig -x 10.5.23.42 \n\n')))



################################ CYBER KILL CHAIN
################################ 1 . RECO

        
class reco(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Information Gathering" , menu=menu_info()))
        self.add_menu_item(MenuItem(2, "Network Scan (Nmap)", menu=menu_nmap()))
        self.add_menu_item(MenuItem(3, "Sniffing \n\n\n", menu=menu_snif()))



class menu_nmap(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Usefull Options",  lambda : print('\n -n : Disable name and port resolution \n -PR : ARP host Discovery \n -Pn : Disable host discovery \n -sn : Disable port scan \n -sS/-sT/-sU : SYN/TCP connect/UDP scan \n -top-ports 50 : scan 50 top ports \n -iL file : host input file \n -oA file : write outpouts files (3 types) \n -sC : Script scan \n --script <file/category> : specific scripts \n -sV : version detection \n -6 : IPv6 scan ')))
        self.add_menu_item(MenuItem(2, "ARP Scan", lambda: print("$ nmap -n -sn -PR 10.5.23.0/24")))
        self.add_menu_item(MenuItem(3, "Reverse DNS lookup of IP range", lambda: print("$ nmap -sL 10.2.23.0/24")))
        self.add_menu_item(MenuItem(4, "Host discovery", lambda : print("$ nmap -sL -n 10.5.23.0/24")))
        self.add_menu_item(MenuItem(5, "List Scripts", lambda: print("$ ls /usr/share/nmap/scripts")))
        self.add_menu_item(MenuItem(6, "TCP scan", lambda : print("$ nmap -Pn -n -sS -p")))
        self.add_menu_item(MenuItem(7, "Scan for vulnerabilities", lambda: print("$ nmap -n -Pn --script 'vuln and safe' 10.5.23.0/24 \n\n\n")))


class menu_snif(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "ARP Spoofing",  lambda : print('\n $ arpspoof -t 10.5.23.85 10.5.23.1')))
        self.add_menu_item(MenuItem(2, "Graphic tool", lambda: print("Demo sub menu item selected")))
        #self.add_menu_item(MenuItem(3, "Show ARP cache", ()))
        #self.add_menu_item(MenuItem(4, "Delete ARP cache", lambda: print("Demo sub menu item selected")))
        #self.add_menu_item(MenuItem(5, "Snif Traffice", ()))
        #self.add_menu_item(MenuItem(6, "", lambda: print("Demo sub menu item selected")))
        #self.add_menu_item(MenuItem(7, "Host discovery", ()))


class menu_info(AbstractMenu):
    def __init__(self):
        super().__init__("")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Whois",  lambda : print('\n $ whois compass-sercutity.com : \n\n Find owner of domain or IP address')))
        self.add_menu_item(MenuItem(2, "DNS Information", lambda: print("\n dig : Domain Information Groper \n\n https://www.ibm.com/docs/en/zos/2.2.0?topic=uzudc-dig-command-query-name-servers \n\n  $ dig [server] [name] [type]\n\n [server] : hostname or IP address the query is directed to \n [name] : The DNS of the server to query \n [type] : type of DNS record to retrieve, by default dig uses A record type \n\n A : address record which directly maps hostname to an IP address \n MX : Mail Exchange which maps message transfer to agents for the domain \n SIG : Signature record which is used in encryption protocols \n\n IN ANSWER SECTION : \n -1st column : name of the server \n -2nd : Time to live, a set timeframe after which the record is refreshed \n -3rd : class of query :  '   ")))
        #self.add_menu_item(MenuItem(3, "Show ARP cache", ()))
        #self.add_menu_item(MenuItem(4, "Delete ARP cache", lambda: print("Demo sub menu item selected")))
        #self.add_menu_item(MenuItem(5, "Snif Traffice", ()))
        #self.add_menu_item(MenuItem(6, "", lambda: print("Demo sub menu item selected")))
        #"self.add_menu_item(MenuItem(7, "Host discovery", ()))


class DemoSubMenu3(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the demo sub menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Demo sub menu item", lambda: print("Demo sub menu item selected")))

class DemoSubMenu4(AbstractMenu):
    def __init__(self):
        super().__init__("Welcome to the demo sub menu.")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
        self.add_menu_item(MenuItem(1, "Demo sub menu item", lambda: print("Demo sub menu item selected")))


class DemoMenu(AbstractMenu):
    show_hidden_menu = False

    def __init__(self):
        super().__init__("Fais comme chez toi \n")

    def initialise(self):
        self.add_menu_item(MenuItem(0, "..\n").set_as_exit_option())
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
