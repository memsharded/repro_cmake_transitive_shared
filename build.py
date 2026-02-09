import subprocess, os


def run(cmd):
    subprocess.run(cmd, check=True, text=True, shell=True)


os.chdir("foobar")
run("cmake . -DCMAKE_BUILD_TYPE=Release")
run("cmake --build . --config Release")
run("cmake --install . --prefix=../myfoobar --config Release")


os.chdir("../consumer")
run("cmake . --graphviz=graph.dot -DCMAKE_BUILD_TYPE=Release "
    "-DCMAKE_PREFIX_PATH=../myfoobar -DCMAKE_VERBOSE_MAKEFILE=1")
run("cmake --build . --config Release")
