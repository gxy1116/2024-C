score=readmatrix('data3-3.xlsx','range','B2:I11');
[n,m]=size(score);
score2=zeros(n,m);
for j=1:m
    for i=1:n
        score2(i,j)=(score(i,j)-min(score(:,j)))/(max(score(:,j))-min(score(:,j)));
        if score2(i,j)==0
            score2(i,j)=0.0001;   % 求对数不能为0，故取个极小的数
        end
    end
end
p=score2./sum(score2);
e=-sum(p.*log(p))/log(n);       
g=1-e; 
w=g/sum(g) %计算权重
s=w*p'; %计算各个评价对象的综合评价值

[ss,rank]=sort(s,'descend') %对评价值从大到小排序；descend表示降序