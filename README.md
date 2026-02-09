# repro_cmake_transitive_shared


Reproduce with ``python build.py`` in Linux-gcc-ld


## Logs

-- The CXX compiler identification is GNU 11.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done (1.3s)
-- Generating done (0.2s)
-- Build files have been written to: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar
[ 25%] Building CXX object CMakeFiles/foo.dir/src/foo.cpp.o
[ 50%] Linking CXX shared library libfoo.so
[ 50%] Built target foo
[ 75%] Building CXX object CMakeFiles/bar.dir/src/bar.cpp.o
[100%] Linking CXX shared library libbar.so
[100%] Built target bar
-- Installing: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar/../myfoobar/lib/libfoo.so
-- Installing: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar/../myfoobar/include/foo.h
-- Installing: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar/../myfoobar/lib/libbar.so
-- Set non-toolchain portion of runtime path of "../myfoobar/lib/libbar.so" to ""
-- Installing: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar/../myfoobar/include/bar.h
-- Installing: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar/../myfoobar/foobar/cmake/foobarConfig.cmake
-- Installing: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/foobar/../myfoobar/foobar/cmake/foobarConfig-release.cmake
-- The CXX compiler identification is GNU 11.4.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done (1.4s)
-- Generating done (0.2s)
Generate graphviz: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/graph.dot
-- Build files have been written to: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer
Change Dir: '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'

Run Build Command(s): /snap/cmake/1515/bin/cmake -E env VERBOSE=1 /usr/bin/gmake -f Makefile
/snap/cmake/1515/bin/cmake -S/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer -B/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer --check-build-system CMakeFiles/Makefile.cmake 0
/snap/cmake/1515/bin/cmake -E cmake_progress_start /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/CMakeFiles /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer//CMakeFiles/progress.marks
/usr/bin/gmake  -f CMakeFiles/Makefile2 all
gmake[1]: Entering directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
/usr/bin/gmake  -f CMakeFiles/consumer.dir/build.make CMakeFiles/consumer.dir/depend
gmake[2]: Entering directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
cd /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer && /snap/cmake/1515/bin/cmake -E cmake_depends "Unix Makefiles" /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/CMakeFiles/consumer.dir/DependInfo.cmake "--color=" consumer
gmake[2]: Leaving directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
/usr/bin/gmake  -f CMakeFiles/consumer.dir/build.make CMakeFiles/consumer.dir/build
gmake[2]: Entering directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
[ 25%] Building CXX object CMakeFiles/consumer.dir/src/consumer.cpp.o
/usr/bin/c++ -Dconsumer_EXPORTS -I/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/include -isystem /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/myfoobar/include -O3 -DNDEBUG -fPIC -MD -MT CMakeFiles/consumer.dir/src/consumer.cpp.o -MF CMakeFiles/consumer.dir/src/consumer.cpp.o.d -o CMakeFiles/consumer.dir/src/consumer.cpp.o -c /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/src/consumer.cpp
[ 50%] Linking CXX shared library libconsumer.so
/snap/cmake/1515/bin/cmake -E cmake_link_script CMakeFiles/consumer.dir/link.txt --verbose=1
/usr/bin/c++ -fPIC -O3 -DNDEBUG -shared -Wl,-soname,libconsumer.so -o libconsumer.so CMakeFiles/consumer.dir/src/consumer.cpp.o  -Wl,-rpath,/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/myfoobar/lib: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/myfoobar/lib/libbar.so /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/myfoobar/lib/libfoo.so
gmake[2]: Leaving directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
[ 50%] Built target consumer
/usr/bin/gmake  -f CMakeFiles/my_app.dir/build.make CMakeFiles/my_app.dir/depend
gmake[2]: Entering directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
cd /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer && /snap/cmake/1515/bin/cmake -E cmake_depends "Unix Makefiles" /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/CMakeFiles/my_app.dir/DependInfo.cmake "--color=" my_app
gmake[2]: Leaving directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
/usr/bin/gmake  -f CMakeFiles/my_app.dir/build.make CMakeFiles/my_app.dir/build
gmake[2]: Entering directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
[ 75%] Building CXX object CMakeFiles/my_app.dir/src/my_app.cpp.o
/usr/bin/c++  -I/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/include -O3 -DNDEBUG -MD -MT CMakeFiles/my_app.dir/src/my_app.cpp.o -MF CMakeFiles/my_app.dir/src/my_app.cpp.o.d -o CMakeFiles/my_app.dir/src/my_app.cpp.o -c /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer/src/my_app.cpp
[100%] Linking CXX executable my_app
/snap/cmake/1515/bin/cmake -E cmake_link_script CMakeFiles/my_app.dir/link.txt --verbose=1
/usr/bin/c++ -O3 -DNDEBUG CMakeFiles/my_app.dir/src/my_app.cpp.o -o my_app  -Wl,-rpath,/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer libconsumer.so
/usr/bin/ld: warning: libfoo.so, needed by /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/myfoobar/lib/libbar.so, not found (try using -rpath or -rpath-link)
/usr/bin/ld: /mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/myfoobar/lib/libbar.so: undefined reference to `foo(int, int)'
collect2: error: ld returned 1 exit status
gmake[2]: *** [CMakeFiles/my_app.dir/build.make:104: my_app] Error 1
gmake[2]: Leaving directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
gmake[1]: *** [CMakeFiles/Makefile2:125: CMakeFiles/my_app.dir/all] Error 2
gmake[1]: Leaving directory '/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/consumer'
gmake: *** [Makefile:139: all] Error 2

Traceback (most recent call last):
  File "/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/build.py", line 17, in <module>
    run("cmake --build . --config Release")
  File "/mnt/c/Users/Myuser/conanws/repro_cmake_transitive_shared/build.py", line 5, in run
    subprocess.run(cmd, check=True, text=True, shell=True)
  File "/usr/lib/python3.10/subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command 'cmake --build . --config Release' returned non-zero exit status 2.
