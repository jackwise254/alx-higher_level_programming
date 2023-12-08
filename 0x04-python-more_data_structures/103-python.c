#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyListObject *list;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = Py_SIZE(list);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        if (strcmp(Py_TYPE(PyList_GetItem(p, i))->tp_name, "bytes") == 0) {
            print_python_bytes(PyList_GetItem(p, i));
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *str;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    size = Py_SIZE(p);
    printf("  size: %ld\n", size);

    str = (unsigned char *)PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x ", str[i]);
    }
    printf("\n");
}`
