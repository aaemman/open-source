

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

// GLOBAL VARIABLES
int lineCounter = 0;
char* terms[] = {"for","while","if","int", "double", "float"};
int termCount[] = {0,0,0,0,0,0};
const int numTerms  = 6;
char* bracket [] = {"{", "}"};
int bracketCount = 0;
char line [100]; 

//FUNCTIONS

int termCounter( char* termSearch){

		if (strstr(line,termSearch) != NULL){
		return 1;
	
		} else{
			return 0;
	 	}
	}

int bracketCounter(void){

		if (strstr(line,bracket[0]) != NULL){
		return 1;
	
		}
		 if(strstr(line,bracket[1]) != NULL){
			return 0;
	 	}
		else{
		return 5;
	}
	}


void fileStream(char * inFile, char *outFile){
	

	
	FILE *out ;
	out = fopen("test1a.txt","w+");
	if (out == NULL){
		printf("ERROR: the out file, does not exist / you do not have permision to modify it\n");
		fclose(out);
	}

	FILE *in ;
	in = fopen("test11.txt","r");
	if (in == NULL){
		printf("ERROR: the in file, does not exist / you do not have permision to modify it\n");
		fopen("test11.txt","w+");
		fclose(in);
	}
	while (fgets(line, 100, in) != NULL){	
		fputs(line, out);
		lineCounter ++;
	

		for(int i =0 ; i < numTerms; i++){ 
			if (termCounter(terms[i]) != 0){
				termCount[i] ++;
			}

		
	}
	if (bracketCounter() == 1){
			bracketCount ++;
			}

	else if (bracketCounter()==0){
				bracketCount  --;
			}
	
			
		
	fprintf(out,"\n\nnumber of:");
	fprintf(out,"\nlines: %d",lineCounter);
	
	for(int i =0 ; i < numTerms; i++){ 
		fprintf(out,"\n %s: ",terms[i]); 
		fprintf(out,"%d",termCount[i]);
		}
	
	if (bracketCount != 0){
		fprintf(out, "\nERROR: there is an un-paired set of curly braces in the code provided. please fix this problem before continuing\n");
		fprintf(out,"%d",bracketCount);
	}
	
	fclose(out);
 	fclose(in);

	}
}
int main (int argc, char*argv[]){

	if (argc == 1) {
		printf("Usage: %s [-t]\n", argv[0]);
		exit(1);
       }

	 if (argc == 3){
		fileStream(argv[1], argv[2]);
		return 0;
	}



}


	
