#!/usr/bin
APP=$1
#检查进程
ps -ef | grep flask | grep -v grep | cut -c 9-15 | xargs kill -s 9 
export FLASK_APP=$APP
nohup flask run  &
echo "flask小应用启动成功”
# pid=`ps -ef | grep flask | grep -v grep | awk '{print $2}'`
# echo $pid
