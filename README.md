# logging-
自定义logging日志
普通的logging日志定义你会发现,不适用与多进程日志
当跑了几天后,你会发现只有一个进程的日志在打印,你就会以为出现了bug
其实不然,而是日志在切换的时候只保留了一个进程的日志
