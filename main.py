import requests, random
REST = '\033[0m'
B,R,G,Y,BL,M,C,W,P,O = '\033[38;2;18;20;19m', '\033[31m', '\033[38;2;62;198;172m', '\033[33m', '\033[34m', '\033[35m', '\033[38;2;50;149;212m', '\033[37m', '\033[38;2;119;100;176m', '\033[38;2;233;118;99m'

def tool():
    response = requests.post("https://discord.com/api/v9/hypesquad/online",json={"house_id": id},headers={"Authorization": token})
    if response.status_code == 204:
        print(f"{BL}{W}Good ~ Dev : Legend{REST}")
    else:
        print(response.text)
if __name__ == "__main__":
    print(f"""{BL}{O}1- Brilliance
{BL}{P}2- Bravery
{BL}{G}3- Balance
{BL}{Y}4- Delete Badge (Not Work On Every Accounts){REST}""")
    ch = input(f"{BL}{B}What Do You Need : ")
    token = input(f"{BL}{C}Token : {REST}")
    if ch == "1" :
        id = 1

    elif ch == "2" :
        id = 2
    elif ch == "4" :
        response = requests.delete("https://discord.com/api/v9/hypesquad/online",headers={"Authorization": token})
        if response.status_code == 204:
            print(f"{BL}{W}Good ~ Dev : Legend{REST}")
        else:
            print(response.text)
        exit()
    elif ch == "3" :
        id = 3

    else:
        print(f"{BL}{C}You Dog")
        exit()
    tool()
