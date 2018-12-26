import pandas as pd
import csv
import timeit
from random import randrange,shuffle
import fileinput
import sys

class tweets:
	def __init__(self):
		self.label=[]
		self.sentence=[]
		self.e=[]
		self.trending=[]
		self.user=[]
		self.f1=open("user.dat","w+")
		self.f2=open("trend.dat","w+")
		self.f3=open("topic.dat","w+")
	def filter(self,dataset):
		for i in dataset:
			l=i[3].split()
			for j in l:
				q=j.lower()
				x=self.findindex(q,self.label)
				if (i[1]==0):
					if (x==-1):
						self.label.append([q,0,1])
					else:
						#print(self.label[x][2])
						self.label[x][2]=self.label[x][2]+1
				else:
					if (x==-1):
						self.label.append([q,1,0])
					else:
						self.label[x][1]=self.label[x][1]+1
		for i in self.label:
			h1=i[0].lower()
			dc=self.validate(h1)
			if (dc==1):
				if (i[2]!=0) and (i[1]!=0):
					pr=float(i[1])/float(i[2])
					nr=float(i[2])/float(i[1])
					if (abs(pr-nr)<1):
						self.tasclist(h1,str(float(i[1])/float(i[1]+i[2])),str(float(i[2])/float(i[1]+i[2])))
						#print(i,h1,pr,nr)
			self.sentence.append([i[0],float(i[1])/float(i[1]+i[2]),float(i[2])/float(i[1]+i[2])])
		self.f3.close()
		#for i in self.sentence:
			#print(i)
	def train(self):
		f=open("train.dat","w+")
		g=0
		for i in self.sentence:
			e=1
			g=g+1
			for j in range(len(i[0])):
				if (i[0][j]==","):
					k=i[0][:j]
					h=k.lower()
					c=0
					u=0
					for z in range(len(h)):
						if ((ord(h[z])>64) and (ord(h[z])<91)) or ((ord(h[z])>96) and (ord(h[z])<124)) or (ord(h[z])==32):
							c=c+1
							u=u+1
					if (abs(len(h)-c)<3) and (u>2):
						if (h[0]=="@"):
							self.userlist(h,str(i[1]),str(i[2]))
						elif (h[0]=="#"):
							self.trendlist(h,str(i[1]),str(i[2]))
						else:
							f.write(h)
							f.write(",")
							f.write(str(i[1]))
							f.write(",")
							f.write(str(i[2]))
							f.write("\n")
					e=0
					break
			if (e==1):
				h=i[0].lower()
				c=0
				u=0
				for z in range(len(h)):
					if ((ord(h[z])>64) and (ord(h[z])<91)) or ((ord(h[z])>96) and (ord(h[z])<124)) or (ord(h[z])==32):
						c=c+1
						u=u+1
				if (abs(len(h)-c)<3) and (u>2):
					if (h[0]=="@"):
						self.userlist(h,str(i[1]),str(i[2]))
					elif (h[0]=="#"):
						self.trendlist(h,str(i[1]),str(i[2]))
					else:
						f.write(h)
						f.write(",")
						f.write(str(i[1]))
						f.write(",")
						f.write(str(i[2]))
						f.write("\n")
		f.close()
		self.f1.close()
		self.f2.close()
		#print(g)
	def findindex(self,j,label):
		for i in range(len(label)):
			#print(label[0][0])
			if (label[i][0]==j):
				return i
		return -1
	def userlist(self,str1,pco,nco):
		self.f1.write(str1)
		self.f1.write(",")
		self.f1.write(pco)
		self.f1.write(",")
		self.f1.write(nco)
		self.f1.write("\n")
	def trendlist(self,str1,pco,nco):
		self.f2.write(str1)
		self.f2.write(",")
		self.f2.write(pco)
		self.f2.write(",")
		self.f2.write(nco)
		self.f2.write("\n")
	def tasclist(self,str1,pco,nco):
		self.f3.write(str1)
		self.f3.write(",")
		self.f3.write(pco)
		self.f3.write(",")
		self.f3.write(nco)
		self.f3.write("\n")
	def writefile(self,file,str1,pc,nc):
		f99=open(file,"a+")
		f99.write(str1)
		f99.write(",")
		f99.write(pc)
		f99.write(",")
		f99.write(nc)
		f99.write("\n")
		f99.close()
	def validate(self,word):
		c=0
		u=0
		for i in range(len(word)):
			if ((ord(word[i])>64) and (ord(word[i])<91)) or ((ord(word[i])>96) and (ord(word[i])<124)) or (ord(word[i])==32):
				c=c+1
				u=u+1
		if (abs(len(word)-c)<3) and (u>2):
			return 1
		return 0
	def update(self,line,con):
		l=line[3].split()
		for j in l:
			q=j.lower()
			x=self.findindex(q,self.label)
			if (x==-1):
				if (con==0):
					pc=str(0.0)
					nc=str(1.0)
					if (q[0]=="@"):
						#continue
						#f11=open("user.dat","a+")
						self.writefile("user.dat",q,pc,nc)
						#f11.close()
					elif (q[0]=="#"):
						#continue
						#f22=open("trend.dat","a+")
						self.writefile("trend.dat",q,pc,nc)
						#f22.close()
					else:
						f0=open("train.dat","a+")
						f0.write(q)
						f0.write(",")
						f0.write(pc)
						f0.write(",")
						f0.write(nc)
						f0.write("\n")
						f0.close()
				else:
					pc=str(1.0)
					nc=str(0.0)
					if (q[0]=="@"):
						#continue
						self.writefile("user.dat",q,pc,nc)
					elif (q[0]=="#"):
						#continue
						self.writefile("trend.dat",q,pc,nc)
					else:
						f0=open("train.dat","a+")
						f0.write(q)
						f0.write(",")
						f0.write(pc)
						f0.write(",")
						f0.write(nc)
						f0.write("\n")
						f0.close()
			else:
				pc=self.label[x][1]
				nc=self.label[x][2]
				if (pc!=0) and (nc!=0):
					if (con==0):
						pco=str(float(pc)/float(pc+nc))
						nco=str(float(nc)/float(pc+nc))
						pr1=float(pc)/float(nc)
						nr1=float(nc)/float(pc)
						nc=nc+1
						pr2=float(pc)/float(nc)
						nr2=float(nc)/float(pc)
						pcu=str(float(pc)/float(pc+nc))
						ncu=str(float(nc)/float(pc+nc))
						dc=self.validate(q)
						str1=q
						if (dc==1) and (abs(pr1-nr1)<1) and (abs(pr2-nr2)<1):
							self.replaceAll("topic.dat",str1,pco,nco,pcu,ncu)
					else:
						pco=str(float(pc)/float(pc+nc))
						nco=str(float(nc)/float(pc+nc))
						pr1=float(pc)/float(nc)
						nr1=float(nc)/float(pc)
						pc=pc+1
						pr2=float(pc)/float(nc)
						nr2=float(nc)/float(pc)
						pcu=str(float(pc)/float(pc+nc))
						ncu=str(float(nc)/float(pc+nc))
						dc=self.validate(q)
						str1=q
						if (dc==1) and (abs(pr1-nr1)<1) and (abs(pr2-nr2)<1):
							self.replaceAll("topic.dat",str1,pco,nco,pcu,ncu)
				if (con==0):
					pco=str(float(pc)/float(pc+nc))
					nco=str(float(nc)/float(pc+nc))
					nc=nc+1
					pcu=str(float(pc)/float(pc+nc))
					ncu=str(float(nc)/float(pc+nc))
					dc=self.validate(q)
					str1=q
					if (dc==1) and (q[0]=="@"):
						self.replaceAll("user.dat",str1,pco,nco,pcu,ncu)
						#print(str1,pco,nco)
					elif (dc==1) and (q[0]=="#"):
						self.replaceAll("trend.dat",str1,pco,nco,pcu,ncu)
						#print(str1,pco,nco)
					elif (dc==1):
						self.replaceAll("train.dat",str1,pco,nco,pcu,ncu)
				else:
					pco=str(float(pc)/float(pc+nc))
					nco=str(float(nc)/float(pc+nc))
					pc=pc+1
					pcu=str(float(pc)/float(pc+nc))
					ncu=str(float(nc)/float(pc+nc))
					dc=self.validate(q)
					str1=q
					if (dc==1) and (q[0]=="@"):
						self.replaceAll("user.dat",str1,pco,nco,pcu,ncu)
						#print(str1,pco,nco)
					elif (dc==1) and (q[0]=="#"):
						self.replaceAll("trend.dat",str1,pco,nco,pcu,ncu)
						#print(str1,pco,nco)
					elif (dc==1):
						self.replaceAll("train.dat",str1,pco,nco,pcu,ncu)
	def replaceAll(self,file,str1,pco,nco,pcu,ncu):
		f = open(file,"r")
		lines = f.readlines()
		f.close()
		f = open(file,"w")
		for line in lines:
			if (str1==line[0:len(str1)]) and (pco==line[len(str1)+1:len(str1)+len(pco)+1]) and (nco==line[len(str1)+len(pco)+2:len(str1)+len(pco)+len(nco)+2]):
				continue
			f.write(line)
		f.write(str1)
		f.write(",")
		f.write(pcu)
		f.write(",")
		f.write(ncu)
		f.write("\n")
		f.close()
	def testtweet(self,dataset1,data8,data9,dataset3,threshold):
		outarr=[]
		for i in dataset3:
			#print(i)
			pc=0
			nc=0
			l=i[3].split()
			for j in l:
				f=len(j)
				c=0
				u=0
				for t in range(f):
					if ((ord(j[t])>64) and (ord(j[t])<91)) or ((ord(j[t])>96) and (ord(j[t])<124)) or (ord(j[t])==32):
						c=c+1
						u=u+1
				if (abs(f-c)<3) and (u>2):
					st=j.lower()
					if (st[0]=="@"):
						for wu in data8:
							if (wu[0]==st):
								pc=pc+0.25*wu[1]
								nc=nc+0.25*wu[2]
								#print("@",st,wu[1],wu[2])
								#print(pc1-nc1)
					elif (st[0]=="#"):
						for wt in data9:
							if (wt[0]==st):
								pc=pc+1.25*wt[1]
								nc=nc+1.25*wt[2]
								#print("#",st,wt[1],wt[2])
								#print(pc1-nc1)
					else:
						for w in dataset1:
							if (w[0]==st):
								pc=pc+w[1]
								nc=nc+w[2]
			if ((pc-nc)>0):
				outarr.append(1)
				if (abs(pc-nc)>threshold) and (i[1]==1):
					self.update(i,i[1])
			else:
				outarr.append(0)
				if (abs(pc-nc)>threshold) and (i[1]==0):
					self.update(i,i[1])
			#print(i)
			#print(pc,nc)
			#print("\n")
		return outarr
		#print(dataset1)
	def accur(self,outarr,dataset3):
		a=0
		tp=0.01
		tn=0.01
		fp=0.01
		fn=0.01
		f=len(outarr)
		#for i in range(f):
			#print(outarr[i],dataset3[i][1])
		for i in range(f):
			if (outarr[i]==dataset3[i][1]):
				if (outarr[i]==1) and (dataset3[i][1]==1):
					tp=tp+1
				elif (outarr[i]==0) and (dataset3[i][1]==0):
					tn=tn+1
				a=a+1
			else:
				if (outarr[i]==1) and (dataset3[i][1]==0):
					fp=fp+1
				elif (outarr[i]==0) and (dataset3[i][1]==1):
					fn=fn+1
		accuracy=float(a)/float(f)
		pospr=float(tp)/float(tp+fp)
		negpr=float(tn)/float(tn+fn)
		posre=float(tp)/float(tp+fn)
		negre=float(tn)/float(tn+fp)
		print("Positive Precision",pospr*100)
		print("Negitive Precision",negpr*100)
		print("Positive Recall",posre*100)
		print("Negitive Recall",negre*100)
		f_score=2*(pospr*posre)/(pospr+posre)
		print("F Score",f_score*100)
		return accuracy
	def inputtweet(self,dataset1,data8,data9,dataset4):
		outarr=[]
		for i in dataset4:
			pc=0
			nc=0
			l=i[2].split()
			for j in l:
				f=len(j)
				c=0
				u=0
				for t in range(f):
					if ((ord(j[t])>64) and (ord(j[t])<91)) or ((ord(j[t])>96) and (ord(j[t])<124)) or (ord(j[t])==32):
						c=c+1
						u=u+1
				if (abs(f-c)<3) and (u>2):
					st=j.lower()
					if (st[0]=="@"):
						for wu in data8:
							if (wu[0]==st):
								pc=pc+0.25*wu[1]
								nc=nc+0.25*wu[2]
					elif (st[0]=="#"):
						for wt in data9:
							if (wt[0]==st):
								pc=pc+1.25*wt[1]
								nc=nc+1.25*wt[2]
					else:
						for w in dataset1:
							if (w[0]==st):
								pc=pc+w[1]
								nc=nc+w[2]
			#print(pc,nc)
			if ((pc-nc)>0):
				outarr.append(1)
			else:
				outarr.append(0)
		return outarr

	
def main():
	start = timeit.default_timer()
	#print(start)
	df=pd.read_csv("sentiment.csv")
	data=df.values.tolist()
	shuffle(data)
	n=10
	p=tweets()
	testdata_fold = list()
	traindata_fold=list()
	fold_size = int(len(data) / n)
	#print(fold_size)
	data2 = list(data)
	fold = list()
	while len(fold) < fold_size:
		index = randrange(len(data2))
		fold.append(data2.pop(index))
	testdata_fold.append(fold)
	traindata_fold.append(data2)
	#print(len(fold))
	s=0
	thr=0.8
	#for i in range(n):
		#print(len(traindata_fold[i]),len(testdata_fold[i]))
	p.filter(traindata_fold[0])
	p.train()
	#p.words()
	df1=pd.read_csv("train.dat")
	data1=df1.values.tolist()
	df8=pd.read_csv("user.dat")
	data8=df8.values.tolist()
	df9=pd.read_csv("trend.dat")
	data9=df9.values.tolist()
	outarr=p.testtweet(data1,data8,data9,testdata_fold[0],thr)
	s=s+p.accur(outarr,testdata_fold[0])
	print("Accuracy : ",float(s)*100)
	stop = timeit.default_timer()
	#print(stop)
	print('Time: ', stop - start)
	d1=pd.read_csv("input.csv")
	dat1=d1.values.tolist()
	arr=p.inputtweet(data1,data8,data9,dat1)
	#for i in range(len(dat1)):
		#print(dat1[i][2],arr[i])

if __name__=="__main__":
	main()