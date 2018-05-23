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

pyr_cg_node_t *Py_Generate_Pyronia_Callstack(void);

#endif /* __PY_PYRONIA_H */
