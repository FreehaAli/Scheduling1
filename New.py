p[10]={1,2,3,4,5,6,7,8,9,10}
btime = 0
min=int()
k=1
n=int()
i=int()
bt[10]
temp=int()
j=int()
ta=0
sum=0
at[10]
wt[10]
tt[10]
wavg=0
tavg=0
tsum=0
wsum=0

print("-----------SJF------------")

n = int(input('Enter the total no of processes: '))

for i in range(n):
    process_queue.append([])#append a list object to the list
    process_queue[i].append(input('Enter p_name in characters: '))
    process_queue[i].append(int(input('Enter p_arrival time in sec: ')))
    process_queue[i].append(int(input('Enter p_bust time in sec: ')))
    print ('')

print(" -------Shortest Job First Scheduling ( NP )-------\n")
print("\nEnter the No. of processes :")
n=input()
 
for i in range(n):
    print("\tEnter the burst time of %d process :",i+1)
    bt[i]=input()
    print("\tEnter the arrival time of %d process :",i+1)
    at[i]=input()

 

for i in range(n):
    for j in range(n):
        if at[i]<at[j]:
            temp=p[j]
            p[j]=p[i]
            p[i]=temp
            temp=at[j]
            at[j]=at[i]
            at[i]=temp
            temp=bt[j]
            bt[j]=bt[i]
            bt[i]=temp			
for j in range(n):
    btime=btime+bt[j]
    min=bt[k]
    for i in range(n):
		if btime>=at[i] and bt[i]<min:
			temp=p[k]
            p[k]=p[i]
            p[i]=temp
            temp=at[k]
            at[k]=at[i]
            at[i]=temp
            temp=bt[k]
            bt[k]=bt[i]
            bt[i]=temp
    k+=1
wt[0]=0
for i in range(n):
    sum=sum+bt[i-1]
    wt[i]=sum-at[i]
    wsum=wsum+wt[i]

wavg=(wsum/n)
for i in range(n):
    ta=ta+bt[i]
    tt[i]=ta-at[i]
    tsum=tsum+tt[i]

tavg=(tsum/n)
 
print("************************")
print("\n RESULT:-")
print("\nProcess\t Burst\t Arrival\t Waiting\t Turn-around" )
for i in range(n):
    print("\n p%d\t %d\t %d\t\t %d\t\t\t%d",p[i],bt[i],at[i],wt[i],tt[i])

print("\n\nAVERAGE WAITING TIME : %f",wavg)
print("\nAVERAGE TURN AROUND TIME : %f",tavg)
return 0

