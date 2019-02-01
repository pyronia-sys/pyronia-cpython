/** Defines the Python-specific Pyronia functionality: Callstack generator
 * and module isolation. This functionality is passed into libpyronia
 * as callback functions.
 *
 *@author: Marcela S. Melara
 */
#ifndef __PY_PYRONIA_H
#define __PY_PYRONIA_H

#include <linux/pyronia_mac.h>
#include <pyronia_lib.h>

#define LIB_POLICY "/home/pyronia/cpython/home.pyronia.cpython.pyronia_build.python-lib.prof"

#define PYR_LOGGING 0
#define pyrlog(format, ...) { \
    if (PYR_LOGGING) { \
      fprintf(stdout, "[pyronia] " format, ##__VA_ARGS__); \
      fflush(NULL);   \
    }\
  }

struct _ts;
typedef struct _ts PyThreadState; // forward declarations
PyThreadState *pyr_interp_tstate;
int is_class_constructor; // needed to support class constructors as sandbox functions

void acquire_gil(void);
void release_gil(void);

PyObject *_PyObject_GC_SecureMalloc(size_t);
PyVarObject *_PyObject_GC_NewSecureVar(PyTypeObject *, Py_ssize_t);
#define PyObject_GC_NewSecureVar(type, typeobj, n) \
                ( (type *) _PyObject_GC_NewSecureVar((typeobj), (n)) )
PyVarObject * _PyObject_GC_SecureResize(PyVarObject *, Py_ssize_t);
#define PyObject_GC_SecureResize(type, op, n) \
                ( (type *) _PyObject_GC_SecureResize((PyVarObject *)(op), (n)) )

void PyObject_GC_SecureDel(void *);

// these are wrappers around interp dom write access grant and revokes
// to enable toggling pyronia on and off (and so we don't need to import pyronia_lib.h directly anywhere but here)
#ifdef Py_PYRONIA
#define pyr_protected_mem_access_pre(op) do {		\
    if (op && pyr_is_isolated_data_obj((void *)op))	\
      pyr_grant_data_obj_write((void *)op);		\
    else						\
      pyr_grant_critical_state_write((void *)op);	\
  } while(0)
#else
#define pyr_protected_mem_access_pre(op) \
    do { } while(0)
#endif

#ifdef Py_PYRONIA
#define pyr_protected_mem_access_post(op) do {		\
    if (op && pyr_is_isolated_data_obj((void *)op))	\
      pyr_revoke_data_obj_write((void *)op);		\
    else						\
      pyr_revoke_critical_state_write((void *)op);	\
  } while(0)
#else
#define pyr_protected_mem_access_post(op) \
    do { } while(0)
#endif

#define Py_GetFullFuncName(func_fqn, mod, func)				\
  snprintf(func_fqn, strlen(func)+strlen(mod)+2, "%s.%s", mod, func)

pyr_cg_node_t *Py_Generate_Pyronia_Callstack(void);

// wrapper around pyr_data_obj_alloc for the current sandbox
void *Py_Pyronia_Sandbox_Malloc(size_t);

#endif /* __PY_PYRONIA_H */
