if __name__ == '__main__':
 
    msg=input('input your maessage:')
    
    chars = dict.fromkeys(msg,0)
    for c in msg:
            chars[c] += 1
            print(chars)

