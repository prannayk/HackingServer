#include <stdio.h>
#include <string.h>

#define BUFSIZE 500

char out[2*BUFSIZE];

int main()
{
	char buf[BUFSIZE];

        gets(buf);
        int len = strlen(buf);
	
	FILE *f = fopen ("./random.txt", "w");
	fputs(buf, f);
	fclose(f);

        sprintf(out, "openssl dgst -sha256 random.txt");

        FILE *fp = popen(out, "r");
        if (fp == NULL) {
            printf("Error");
            return 1;
        }

        while (fgets(out, sizeof(out), fp) > 0)
            printf("%s", out);

        pclose(fp);

	return 0;
}
