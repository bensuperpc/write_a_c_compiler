import os
import shutil
import pathlib
import glob
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')


#https://gist.github.com/kirpit/1306188/ab800151c9128db3b763bb9f9ec19fda0df3a843

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

def copy_if(source, destination):
    if os.path.exists(source):
        shutil.copy2(source, destination)

#for file in glob.glob('**/*.c', recursive = True):
#    print(file)

#for file in glob.glob('**/invalid/*.c', recursive = True):
#    result_gcc = subprocess.call(['gcc', file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    result_clang = subprocess.call(['clang', file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #print(result_gcc)

    #pipe = subprocess.Popen(['gcc ' + file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    #res = pipe.communicate()
    #print("retcode =", pipe.returncode)
    #print("res =", res)
    #print("stderr =", res[1])

for file in glob.glob('tests/tests_nlsandler/**/invalid/*.c', recursive = True):
    build_gcc = subprocess.Popen(['gcc -pipe -o /tmp/out_gcc' + file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    build_clang = subprocess.Popen(['clang -pipe -o /tmp/out_clang ' + file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    print(file)
    if(build_gcc.returncode == build_clang.returncode):
        print('Build: OK')
    else:
        print('Build: FAIL')


for file in glob.glob('tests/tests_nlsandler/**/valid/*.c', recursive = True):
    build_gcc = subprocess.Popen(['gcc -pipe -o /tmp/out_gcc ' + file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    build_clang = subprocess.Popen(['clang -pipe -o /tmp/out_clang ' + file], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    print(file)
    if(build_gcc.returncode == build_clang.returncode):
        print('Build: OK')
    else:
        print('Build: FAIL')
    run_gcc = subprocess.Popen(['/tmp/out_gcc'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    run_clang = subprocess.Popen(['/tmp/out_clang'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    if(run_gcc.returncode == run_clang.returncode):
        print('Run:   OK')
    else:
        print('Run:   FAIL')