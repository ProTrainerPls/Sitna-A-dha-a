import time
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

print("Halo Kerennn")
# ini adalah comment
a = 10 # ini adalah comment juga
"""ada apa denganku
dan kamu
dalam comment multiline"""
print(a)
for i in range(1, 1000):
    a = 10
    
print(time.time() - start_time, "detik")
# kita bisa mengcompile python ke
# yang namanya bytecode
# cara mengcompile, buka terminal dan tuliskan
# python -m py_compile Main.py
