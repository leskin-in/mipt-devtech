#!/usr/bin/env python3

HEADER_TEMPLATE = """#ifndef GENERATE_H
#define GENERATE_H

/**
 * Generate some interesting number
 */
int generate_number();

int generate_number() {
    return 42;
}

#endif
"""


def generate():
    """
    Generate header file: index.h

    :return: String containing the whole header file
    """
    return HEADER_TEMPLATE


if __name__ == '__main__':
    f = open('C/index.h', 'w')
    f.write(generate())
    f.close()
