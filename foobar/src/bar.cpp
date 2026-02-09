
#include "bar.h"
#include "foo.h"
int bar(int x, int y) {
    return foo(x, y) * 2;
}
