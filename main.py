#Config loader

d = {}
filename = 'cuong.txt'

def config_Loader():
		with open (filename,'r') as fs:
				content = fs.read()
				#print content
				path = content.split("\n")
				print path
				for i in path:
						p = i.split("=")
						#print p
						#print p[1]
						#l.append(p)
						#print l
						d[p[0]]= p[1]
						print d
config_Loader()		

# def main ():
# 	config_Loader()
# 	print "User name:%s" + d['username']
# 	print "Password:%s" + d['Password']
# 	print "Link:%s" + d['link']
# main()