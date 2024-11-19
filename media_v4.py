# d) Uma função que calcula a média de 3 números inteiros
def MediaD(n1,n2,n3):
    media = 0
    media = n1 + n2 + n3
    media = media / 3
    return media
def main():
    print(MediaD(2,3,4))
if __name__=='__main__':
    main()