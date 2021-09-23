import frida
import sys

# hook逻辑脚本
jscode = """
Java.perform(function () {
//获取bli类型，使用js将其包状成代理对象
  var bil = Java.use('com.softgarden.baselibrary.utils.MD5Util');


  var function_a = bil.ToMD5NOKey;
  //重写方法a
  function_a.implementation = function (str) {
    // Show a message to know that the function got called
     send('ToMD5NOKey');
	 send(str);
    // Call the original onClick handler
    //调用实际的a方法（即包装之前的a方法，类似于装饰器工能）
    return  this.ToMD5NOKey(str);
  };
});
"""

# 注入进程,attach传入进程名称（字符串）或者进程号（整数）
rdev = frida.get_remote_device()
session = rdev.attach("com.ljhhr.mobile")
script = session.create_script(jscode)
#int()函数把字符串表示的16进制数转换成整数
#上面的jscode % int(sys.argv[1], 16)是python格式化字符串的语法

# 接收脚本信息的回调函数
# message是一个对象，type属性为send则表示send函数发送的信息，其内容在payload里
# 下面这个on_message函数可以做固定用法，一般无需改动，当然也可直接打印message看看里边的内容
def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])
# 应该是设置message事件的回调函数
script.on('message', on_message)
# 加载hook脚本
script.load()
# 保持主线程不结束（也可以使用time.sleep循环）
sys.stdin.read()