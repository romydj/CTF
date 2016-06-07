
# create file tcp.dump from MagicPing.pcap
# tcpdump -x -r MagicPing.pcap icmp[icmptype] == 0 | grep 0x0050: > tcp.dump


f = open('tcp.dump','rb')
data = f.read()
data = data.replace('\t0x0050:  ','')
data = data.split('\n')

hasil = []
for i in xrange(0,len(data),3):
	hasil.append(data[i])

data = ''.join(hasil)
data = data.replace(' ','')
output = open("magic.bz2",'w')
output.write(data.decode('hex'))
