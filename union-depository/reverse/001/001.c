#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  if(argc!=2) {
    printf("Enter flag: %s\n",argv[0]);
    exit(0);
  }
  if(strcmp(argv[1],"CTF{1nTR0_r3v_001}")==0) {
      printf("You string it didn't you");
      exit(0);
  }
  else {
    printf("Dude, string it");
    exit(0);
  }
}



