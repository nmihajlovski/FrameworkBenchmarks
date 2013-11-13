
import subprocess
import sys
import setup_util
import os
from zipfile import ZipFile

def start(args, logfile):
  setup_util.replace_text("play-slick/conf/application.conf", "jdbc:mysql:\/\/.*:3306", "jdbc:mysql://" + args.database_host + ":3306")

  subprocess.check_call("play clean dist", shell=True, cwd="play-slick", stderr=logfile, stdout=logfile)

  if os.name == 'nt':
    ZipFile("./play-slick/target/universal/play-slick-1.0-SNAPSHOT.zip").extractall("./play-slick/target/universal")
    with open("./play-slick/target/universal/play-slick-1.0-SNAPSHOT/bin/play-slick.bat", "w+") as f:
      f.write("java %1 -cp \"./lib/*;\" play.core.server.NettyServer .")
    subprocess.Popen("play-slick.bat", shell=True, cwd="play-slick/target/universal/play-slick-1.0-SNAPSHOT/bin", stderr=logfile, stdout=logfile)
  else:
    subprocess.check_call("unzip play-slick-1.0-SNAPSHOT.zip", shell=True, cwd="play-slick/target/universal", stderr=logfile, stdout=logfile)
    subprocess.check_call("chmod +x play-slick", shell=True, cwd="play-slick/target/universal/play-slick-1.0-SNAPSHOT/bin", stderr=logfile, stdout=logfile)
    subprocess.Popen("./play-slick", shell=True, cwd="play-slick/target/universal/play-slick-1.0-SNAPSHOT/bin", stderr=logfile, stdout=logfile)

  return 0
def stop(logfile):
  if os.name == 'nt':
    with open("./play-slick/target/universal/play-slick-1.0-SNAPSHOT/RUNNING_PID") as f:
      pid = int(f.read())
      os.kill(pid, 9)
  else:
    #p = subprocess.Popen(['ps', 'ef'], stdout=subprocess.PIPE)
    #out, err = p.communicate()
    #for line in out.splitlines():
    #  if 'NettyServer' in line:
    #    pid = int(line.split(None, 2)[1])
    #    os.kill(pid, 9)
    with open("./play-slick/target/universal/play-slick-1.0-SNAPSHOT/play-slick-1.0-SNAPSHOT/RUNNING_PID")

  try:
    #os.remove("play-slick/target/universal/play-slick-1.0-SNAPSHOT/RUNNING_PID")
    os.remove("play-slick/target/universal/play-slick-1.0-SNAPSHOT/play-slick-1.0-SNAPSHOT/RUNNING_PID")
  except OSError:
    pass

  return 0
