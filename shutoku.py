import subprocess

def out_cmd(cmd):
    return subprocess.Popen(
      cmd, stdout=subprocess.PIPE,
      shell=True).stdout.readlines()

#def main():
#  cmd = ("df -h >> data.txt")
#  res_cmd_lfeed(cmd)
#  a_file = open("data.txt",encoding="utf-8")
#  s = a_file.read().splitlines() #行毎のデータの取得
#  a_file.close()
#  print(s[0].split()[1]) #行の取得データ

#if __name__ == '__main__':
#  main()
