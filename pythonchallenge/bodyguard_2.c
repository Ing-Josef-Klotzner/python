#include <boost/regex.hpp>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <ctype.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>

enum {
        UP,
        LO
};

char getchars(int num, int fd, int ul, char ** save);

int main(void)
{
        int fd;
        int i;
        char c;                                  /* the interesting letters */
        char bsave[4], esave[4];                 /* begin, end */
        char * bsp = bsave, * esp = esave;       /* bsave, esave ptr */
        int found = 0;

        memset(&bsave, 0, sizeof(bsave));
        memset(&esave, 0, sizeof(esave));

        fd = open("bodyguard.txt", O_RDONLY);
        if (fd == -1) {
                fprintf(stderr, "Could not open file.\n");
                return 1;
        }

        for (i = 1; /* endless */; i++) {
                if ((getchars(1, fd, LO, NULL)) &&
                    (getchars(3, fd, UP, &bsp)) &&
                    (c = getchars(1, fd, LO, NULL)) &&
                    (getchars(3, fd, UP, &esp)) &&
                    (getchars(1, fd, LO, NULL))) {
                        /* Found a character */
                        fprintf(stderr, "%c", c);
                }
                /* Reset file position to the next place */
                lseek(fd, i, SEEK_SET);
        }

        /* Not reached */
        return 0;
}

/* Get "num" characters from file "fd" and see if they are of the case "ul"
 * (upper or lower). If they all are the correct case, save the letters into "save" 
 * and return the last letter found.
 * Otherwise return false.
 */
char getchars(int num, int fd, int ul, char ** save)
{
        int (* funcp)(int c);
        char * ptr;
        char buf[num + 1];
        int i = 0;

        memset(&buf, 0, sizeof(buf));

        switch (ul) {
                case UP:
                        funcp = isupper;
                        break;
                case LO:
                        funcp = islower;
                        break;
                default:
                        return 1;
                        break;
        }

        /* Get "num" letters from the file */
        errno = 0;
        if (read(fd, buf, num) <= 0) {
                if (errno)
                        perror("Couldn't read");
                else
                        fprintf(stderr, "\nEOF\n");
                close(fd);
                exit(1);
        }

        /* For every letter matching the case we wanted, increment i */
        for (ptr = buf; ptr <= &buf[num] && funcp((int) *ptr); ptr++)
                i++;

        /* If all letters were the correct case, copy these letters to save if
         * asked, and return the last letter we found; otherwise return false */
        if (i == num) {
                if (save)
                        strncpy(&(*save[0]), buf, 3);
                return *(ptr - 1);
        } else {
                return 0;
        }
}

