#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int i=0;
	int j=0;
	char* result;
	char* p;
	char* m;
	int a=0;
	int c=0;
	result=malloc(100000*sizeof(char));
	m=malloc(256*sizeof(char));
	FILE *fichier;
	fichier=fopen("view-source_www.pythonchallenge.com_pc_def_ocr.txt","r"); //enigme3.txt is the file containing the sequence of characters
	if (fichier != NULL)
	{
		p=result;
		while (!feof (fichier))
			fscanf(fichier,"%c",p++);
		fclose(fichier);
	}
	for (i=0;i<100000;i++)
	{
		a=0;
		for (j=0;j<256;j++)
		{
			if (result[i]!=m[j])
			{
				a++;
			}
			if (a==256)
			{
				m[c]=result[i];
				c++;
			}
		}
	}
	printf("%s",m);
	return 0;
}
