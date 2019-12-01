#导入random模块
import random
#函数功能：生成题目及答案，返回答案
def question():
 #调用random模块中的randint函数随机生成数
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
#学生输入答案s_ans,用int函数将输入的答案转化为整数型
s_ans=int(input())
#k用来记录错误次数，flag标记是因为错误次数多了进入下一题还是回答正确进入下一题
k=0
flag=1
while(s_ans!=ans):
  if(k!=2):
    print "wrong,please try again"
    k=k+1
    s_ans=int(input())
  else:
    print "wrong!you have tried three times!test over"
    flag=0
    break
if flag:
    print "right"
