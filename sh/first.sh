#!/bin/sh

#脚本文件的顶行，告诉系统，应该去哪里用哪个解释器执行该脚本；
#https://www.cnblogs.com/dasusu/p/11919086.html
# #! 可以制定解释器 往往在开头部分  ，这样就可以直接 ./xx.sh 执行
# 否则只能手动指定解释器  sh xx.sh

name='xky'
echo $name

echo "I am $name"

echo "------"
name2="wst xky"

#切割字符串
echo "${name2:0:2}"

#长度
echo ${#name2}

#i=`expr index "$name2" x`


echo ls  #字符串
echo `ls` # 命令
echo $(ls)   #命令

echo `whoami`

#`ls` # 报错  因为他执行的结果会当做命令继续执行， 就会找不到当前结果了，所以报错

fileN=`ls` # 可以将结果赋值给变量， 这样就不会默认作为结果，直接执行了
echo $fileN

a=`expr 2 + 2`  # expr 执行表达式 注意表达式之间空格 ，反引号 用来表明是一个命令
echo $a

b=`expr 2 \* 2`  # 注意加转义

echo $b

c=`expr 2 \> 1`
echo $c  #1


d=`expr 2 = 2`
echo $d


echo $((a=2+2,$a+2))  # (()) 来执行语句  (()) 里的乘号，大于号等不需要加转义符，expr 需要加转义符

echo $a

b=$[2+2] #另一种写法  跟 expr 相比，$[] 好处就是一些运算符无需加转义符

echo $b


[ 2 -eq 21 ]  # 注意[]两边空格
echo $?  # 命令退出状态有两种，0 是正常，非 0 是异常，同时，可以用 $? 来获取上个命令的执行退出状态，所以可以来试试看：

if [ 1 -eq 2 ]; then
    echo true
else
  echo false
fi


if [ 3 -gt 2 -a 1 -eq 1 ]; then
    echo true
else
    echo false
fi


# 判断字符串相等

a='abcde'
if [ $a = abc ]; then
    echo true
elif [ $a = abcd ]; then
    echo 'ok'
else
    echo 'false'
fi


# -z -n 是有问题
b=''
if [ ${#a} -eq 5 ]; then
   echo $a
else
  echo 是0$a
fi

#文件测试运算符 -f -d -r -w -x -s -e

file='/Users/xiekongying/Desktop/xky/python/laonanhai/project_learn_py3/sh/first.sh'

if [ -e $file ]; then
    echo '文件存在'
else
    echo '文件不存在'
fi

if [[ -e $file ]]; then
    echo '文件存在'
else
    echo '文件不存在'
fi

# 也省略 function 关键字
#函数调用时，直接函数名即可，如果需要参数，跟其他编程语言不同，定义时不能指明参数，而是函数内部直接通过 $n 来获取参数，需要第几个，n 就是第几


function add() {
    echo '我是add函数'
    echo $*  # 打印入参
    echo $1
    echo $2
    echo $0 # 文件名
    echo $#  # 参数个数
}

add 1 2 3


#后者的话，纯粹就是执行一个可执行文件的方式，那就需要这个脚本文件是可执行类型的，同时脚本的解释器由脚本文件内部开头的 #! 声明


source  two.sh  # 可以执行另一个脚本文件 也可以用 .

sh two.sh # 可以执行另一个脚本文件 也可以用 ./two.sh


#每个脚本，如果正常执行结束，那么脚本内部最后应该通过 exit 0 来退出，表示当前脚本正常执行，如果执行过程出异常了，那么应该执行 exit 1 只要是非 0 即可，来表示当前脚本执行异常
#那么，调用执行这个脚本的，就可以通过 $? 来获取脚本执行结果，如：

# exit 0 代表正常运行程序并退出程序,
# exit 1 代表非正常运行导致退出程序
# 其实目的就是: 程序退出后, 用户可以 echo $? 来查看是 0 还是 1, 从而达到检测程序是正常结束退出还是产生错误而退出的目的.
if [[ $? -ne 0 ]]; then
    echo '异常'
    exit 1
fi

# for 循环

for (( i = 0; i < 10; i++ )); do
    echo $i
done

for loop in 1 3 5;do
  echo $loop
done


#$?  用来获取上个命令的执行之后的退出状态，或者获取上个函数执行的返回值，0 表示正常，非0 表示不正常
# 所以，脚本如期结束时，脚本内最后应该 exit 0 来退出命令（每个脚本的执行其实就是执行命令）

ls > a.txt

ls >> b.txt   # 追加输出到b.txt

ls > /dev/null  # 可以不输出到显示器


#b.txt < $?