import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#自作関数
import shutoku as sh



def main():
    cmd = ("df -h > data.txt")
    sh.out_cmd(cmd)
    F = open("data.txt",encoding="utf-8")
    s = F.read().splitlines()
    F.close()
    All = s[1].split()
    data = np.array([All[2].strip('Gi'),All[3].strip('Gi')])
    label = ["Used","Avail"]
    centre_circle = plt.Circle((0,0),0.6,color='black', fc='white',linewidth=1.25)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.pie(data,labels=label,counterclock=False,startangle=90)
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    main()
