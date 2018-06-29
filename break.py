import time
import webbrowser

times = 2;
stop = 0;

print("This program started on "+time.ctime())
while(stop < times):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=izGwDsrQ1eQ")
    stop = stop + 1
