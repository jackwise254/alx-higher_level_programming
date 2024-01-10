#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - prints Python strings
 * @p: Python object
 */
void print_python_string(PyObject *p)
{
    PyUnicodeObject *unicode;
    PyASCIIObject *ascii;
    PyCompactUnicodeObject *compact;
    PyVarObject *varobj;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    unicode = (PyUnicodeObject *)p;
    varobj = (PyVarObject *)p;

    printf("  type: %s",
           (unicode->state.compact ? "compact " : (varobj->ob_size == 1 ? "single " : "interned ")));

    if (PyUnicode_ISASCII(unicode))
    {
        ascii = (PyASCIIObject *)p;
        printf("ascii\n");
        printf("  length: %lu\n", ascii->length);
        printf("  value: %s\n", ascii->wstr);
    }
    else
    {
        compact = (PyCompactUnicodeObject *)p;
        printf("compact unicode object\n");
        printf("  length: %lu\n", compact->length);
        printf("  value: %ls\n", compact->wstr);
    }
}

