import glob
from random import randint
import shutil
import os

# print (glob.glob('TrainVal/*'))
apuleia=[]
aspidosperma=[]
astronium=[]
byrsonima=[]
calophyllum=[]
cecropia=[]
cedrelinga=[]
cochlospermum=[]
combretum=[]
copaifera=[]
for filename in glob.glob(os.path.join('TrainVal/*')):
	if (filename.find('Apuleia')!= -1):
		apuleia.append(filename)
	if (filename.find('Aspidosperma')!= -1):
		aspidosperma.append(filename)
	if (filename.find('Astronium')!= -1):
		astronium.append(filename)
	if (filename.find('Byrsonima')!= -1):
		byrsonima.append(filename)
	if (filename.find('Calophyllum')!= -1):
		calophyllum.append(filename)
	if (filename.find('Cecropia')!= -1):
		cecropia.append(filename)
	if (filename.find('Cedrelinga')!= -1):
		cedrelinga.append(filename)
	if (filename.find('Cochlospermum')!= -1):
		cochlospermum.append(filename)
	if (filename.find('Combretum')!= -1):
		combretum.append(filename)
	if (filename.find('Copaifera')!= -1):
		copaifera.append(filename)
# apuleia
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(apuleia[chosen]), 'test/'+apuleia[chosen][9:])
	apuleia.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(apuleia[index]), 'prac/'+apuleia[index][9:])
	index = index +1

count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(aspidosperma[chosen]), 'test/'+aspidosperma[chosen][9:])
	aspidosperma.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(aspidosperma[index]), 'prac/'+aspidosperma[index][9:])
	index = index +1

# Astronium
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(astronium[chosen]), 'test/'+astronium[chosen][9:])
	astronium.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(astronium[index]), 'prac/'+astronium[index][9:])
	index = index +1

# byrsonima
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(byrsonima[chosen]), 'test/'+byrsonima[chosen][9:])
	byrsonima.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(byrsonima[index]), 'prac/'+byrsonima[index][9:])
	index = index +1

# calophyllum
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(calophyllum[chosen]), 'test/'+calophyllum[chosen][9:])
	calophyllum.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(calophyllum[index]), 'prac/'+calophyllum[index][9:])
	index = index +1

# cecropia
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(cecropia[chosen]), 'test/'+cecropia[chosen][9:])
	cecropia.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(cecropia[index]), 'prac/'+cecropia[index][9:])
	index = index +1

# cedrelinga
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(cedrelinga[chosen]), 'test/'+cedrelinga[chosen][9:])
	cedrelinga.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(cedrelinga[index]), 'prac/'+cedrelinga[index][9:])
	index = index +1

# cochlospermum
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(cochlospermum[chosen]), 'test/'+cochlospermum[chosen][9:])
	cochlospermum.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(cochlospermum[index]), 'prac/'+cochlospermum[index][9:])
	index = index +1

# combretum
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(combretum[chosen]), 'test/'+combretum[chosen][9:])
	combretum.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(combretum[index]), 'prac/'+combretum[index][9:])
	index = index +1

# copaifera
count = 280
index = 0;
while (count>280*0.6):
	chosen = randint(0,count-1)
	shutil.copy(os.path.join(copaifera[chosen]), 'test/'+copaifera[chosen][9:])
	copaifera.pop(chosen)
	index = index +1
	count = count -1

index = 0
while (index<count):
	shutil.copy(os.path.join(copaifera[index]), 'prac/'+copaifera[index][9:])
	index = index +1
