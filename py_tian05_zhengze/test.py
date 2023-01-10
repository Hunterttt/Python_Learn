import re 
#pattern = re.compile(r'\d+') # 查找数字 

#result1 = re.findall('^-.{6}','-764.22,-648.20,-754.98,-838.93') 

#result1 = re.findall('^-[1-9]\d*\.\d*|-0\.\d*[1-9]\d*$','-764.22,-648.20,-754.98,-838.93') 

result1 = re.findall('^-[\d.]+[\d]','-764.22,-648.20,-754.98,-838.93') 

print(result1) 