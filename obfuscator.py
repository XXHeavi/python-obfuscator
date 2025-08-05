import base64
import random
from math import ceil
def ObfuscateCode(code):
  def randomStr(length):
    charset = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_"
    string = "_"
    for i in range(length):
      string+=charset[random.randint(1,len(charset)-1)]
    return string
  def functionify(code):
    func_codes = []
    func_names = []
    codeLen = len(code)
    chunkSize = ceil(codeLen/random.randint(5,25))
    template_func = "def func_name(): return output\n"
    for i in range(ceil(codeLen/chunkSize)):
      our_func = template_func
      our_func_name = randomStr(random.randint(10,20))
      codechunk = code[i*chunkSize:(i*chunkSize)+chunkSize]
      orded = [str(ord(a)) for a in codechunk]
      ret_code = "+".join(orded)+"+"
      our_func_code = f"\"{ret_code}\""
      our_func = our_func.replace("func_name",our_func_name)
      our_func = our_func.replace("output",our_func_code)
      func_codes.append(our_func)
      func_names.append(our_func_name)
    return func_codes, func_names
  def joinCode(func1):
    return "".join(func1)
  def forLoopThing(functNames):
    functNames2 = [a+"()" for a in functNames]
    realFunctNames = "+".join(functNames2)
    splitName1 = randomStr(15)
    splitName = f"{splitName1} = \"{realFunctNames}\".split(\"+\")\n"
    return splitName,splitName1
  finalCode = ""
  functCode, funcNames = functionify(code)
  finalCode += joinCode(functCode)
  compileSub = randomStr(15)
  execSub = randomStr(15)
  obfSub = randomStr(15)
  execNameSub = randomStr(15)
  splitSub = forLoopThing(funcNames)
  splitSubItr = randomStr(15)
  chrSub = randomStr(15)
  rebuildSub = randomStr(15)
  rebuildSub2 = randomStr(15)
  randoName = randomStr(20)
  intSub = randomStr(20)
  finalCode += f"{compileSub}=compile\n"
  finalCode += f"{execSub}=exec\n"
  finalCode += f"{obfSub}=\"<{randomStr(15)}>\"\n"
  finalCode += f"{execNameSub}=\"exec\"\n"
  finalCode += f"{rebuildSub}=\"\"\n"
  finalCode += f"{chrSub}=chr\n"
  finalCode += f"{intSub}=int\n"
  finalCode += f"{rebuildSub2}=\"\"\n"
  finalCode += splitSub[0]
  finalCode += f"""
for {splitSubItr} in {splitSub[1]}:
  {rebuildSub}+=globals()[{splitSubItr}[:-2]]()
  {rebuildSub2} = "".join([{chrSub}({intSub}({randoName})) for {randoName} in {rebuildSub}[:-1].split("+")])
{execSub}({compileSub}({rebuildSub2},{obfSub},{execNameSub}))
  """[1:]
  return finalCode