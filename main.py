import argparse
from scripts.vigiato import login_vigiato
from scripts.digikala import digikala_login


def main():

        
    parser = argparse.ArgumentParser(description='this script will login different sites with selenium')
    parser.add_argument('--vgt', help='login to vigiato', action='store_true')
    parser.add_argument('--dgi', help='login to digikala', action='store_true')
    
    args = parser.parse_args()

    
    if args.vgt:
        login_vigiato()
    elif args.dgi:
        digikala_login()
    else:
        print('please add --vgt or --dgi')

if __name__ == "__main__":
    main()
    
