from math import ceil
import random
import base64
code1 = open("code.py").read()
code = str(base64.b64encode(code1.encode()))[2:-1]
print(code)
def randomID():
  chrset = "accordingtoallknownlawsofaviationthereisnowaythatabeeshouldbeabletofly"
  ix = "_"
  for i in range(random.randint(10,20)):
    ix+=chrset[random.randint(0,len(chrset)-1)]
  return ix



def ordStr(s):
  return [ord(c) for c in str(s)]
finalCode = "import base64, sys\nif sys.gettrace() != None:\n  exit()\n"
end = "\n"
trademark = " ".join([str(ord(c)) for c in "heavis super epic python obfuscator.discord:p16s"+randomID()])

execSub = randomID()
b64Sub = randomID()
returnSub = randomID()
orderedCode = ordStr(code)
strSub = randomID()
execFunc = randomID()
ItrName = randomID()
passSubs = [randomID() for i in range(1,100)]
chunkSize = ceil(len(code)/random.randint(10,20))
codeChunks = [[randomID()]]
finalCode += f"{randomID()} = \"{trademark};\"{end}"
finalCode += f"{execSub} = exec{end}"
finalCode += f"{b64Sub} = base64{end}"
finalCode += f"{strSub} = chr{end}"
rebuild=randomID()
rebuild2=randomID()
finalCode += f"{rebuild} = []{end}"
finalCode += f"{rebuild2} = ''{end}"
codeChunkItr = 0
itr2Name = randomID()
intSub = randomID()
finalCode += f"{intSub} = int{end}"

for passes in passSubs:
  finalCode += f"{passes} = lambda: exec('pass'){end}"
randomchunks =[f"""
def {randomID()}():
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
""",
              f"""
def {randomID()}():
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
              """,
              f"""
def {randomID()}():
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
              """,
              f"""
def {randomID()}():
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
              """,
              f"""
def {randomID()}():
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
                {random.choice(passSubs)}()
              """]
whichChunk = 0
for orChr in orderedCode:
  if codeChunkItr == chunkSize:
    codeChunkItr = 0
    whichChunk += 1
    codeChunks.append([randomID()])
    
  codeChunks[whichChunk].append(str(orChr))
  
  codeChunkItr+= 1

for chunk in codeChunks:
  if random.randint(1,5) == 2:
    finalCode += random.choice(randomchunks)+end
  finalCode += f"{chunk[0]} = \"{'+'.join(chunk[1:])}\"{end}"
  

finalCode += f"{execFunc} = {execSub}{end}"
finalCode += f"{ItrName}=["
for compiledChunk in codeChunks:
  finalCode+=f"{compiledChunk[0]},"
finalCode += f"]{end}for {itr2Name} in {ItrName}:{end}  {rebuild}.append({itr2Name}.split(\"+\")){end}for sxs in {rebuild}:{end}  for s in sxs:{end}    {rebuild2}+={strSub}({intSub}(s)){end}{execFunc}({b64Sub}.b64decode({rebuild2})){end}"
# {b64Sub}.b64decode({rebuild2})
base64.b64decode(code.encode())

print(finalCode)
with open("obfuscated.py","w") as f:
  f.write(finalCode)
