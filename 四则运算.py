#����randomģ��
import random
#�������ܣ�������Ŀ���𰸣����ش�
def question():
 #����randomģ���е�randint�������������
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,4)
    if(c==1):
        print a,"*",b,"=?"
        ans=a*b      
    elif( c==2):
        print a,"/",b,"=?"
        ans=a/b
    elif(c==3):
        print a,"+",b,"=?"
        ans=a+b
    else:
        print a,"-",b,"=?"
        ans=a-b
    return ans
ans=question()
#ѧ�������s_ans,��int����������Ĵ�ת��Ϊ������
s_ans=int(input())
#k������¼���������flag�������Ϊ����������˽�����һ�⻹�ǻش���ȷ������һ��
k=0
flag=1
while(s_ans!=ans):
  if(k!=2):
    print('wrong,please try again')
    k=k+1
    s_ans=int(input())
  else:
    print('wrong!you have tried three times!test over')
    flag=0
    break
if flag:
    print('right')
