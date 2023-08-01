
import csv 
import getpass
import ldb
from samba.auth import system_session
from samba.credentials import Credentials
# from samba.dcerpc import security
# from samba.dcerpc.security import dom_sid
from samba.ndr import ndr_pack, ndr_unpack
from samba.param import LoadParm
from samba.samdb import SamDB


lp = LoadParm()
creds = Credentials()
creds.guess(lp)
creds.set_username('Administrator')
creds.set_password('P@ssw0rd')
samdb = SamDB(url='ldap://10.70.39.51:389', session_info=system_session(),credentials=creds, lp=lp)


#samdb.newuser( username="test22",password="P@ssw0rd",userou="users")

#samdb.newgroup(groupname="test123")


def test():
    print('test')
    csv_file = input('Csv Path')

    with open(csv_file, mode='r') as csv_file_opt:
        csv_read = csv.DictReader(csv_file_opt, delimiter=';')
        for row in csv_read:
            samdb.newuser(username=row['username'],password='P@ssw0rd')
            samdb.newgroup(groupname=row['group'])


def create_groups_from_csv():
    csv_file = input('Csv Path: ')

    with open(csv_file, mode='r') as csv_file_opt:
        csv_read = csv.DictReader(csv_file_opt, delimiter=';')
        for row in csv_read:

            try: 
                samdb.newgroup(groupname=row["level1"])
            except Exception:
                print("This group already exsist")

            try: 
                samdb.newgroup(groupname=row["level2"])
            except Exception:
                print("This group already exsist")

            try: 
                samdb.newgroup(groupname=row["level3"],)
            except Exception:
                print("This group already exsist")
            samdb.add_remove_group_members()


    


# res = samdb.search(base='CN=Users,DC=inno,DC=local')
