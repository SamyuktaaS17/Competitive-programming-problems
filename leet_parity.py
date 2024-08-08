inp_list=input("enter: ")

cleaned_input =inp_list.strip('[]')
elements = cleaned_input.split(',')

int_list = [int(element) for element in elements]

flag=0
for i in range(len(int_list)):
    if(i!=len(int_list)-1):
        curr=int_list[i]%2;
        nex=(int_list[i+1])%2;
        if(curr!=nex):
            flag=1 
            continue
        else:
            flag=0
            break
    else:
        if(flag==1):
            print('true')
        elif(flag==0):
            print('false')