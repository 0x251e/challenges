#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    printf("Welcome to MI6\n");
    if(argc != 3) {
        printf("Enter <agentname> <missionid>\n");
        exit(0);
    }
    if(strcmp(argv[1], "jamesbond") == 0) {
        if(strcmp(argv[2], "007") == 0) {
            printf("Congratulations agent, decode this: Q1RGe0wxYzNOczNfMl9oNGNLfQ==\n");
            exit(0);
        } else {
            printf("We know who you are, but what is your mission, %s?\n", argv[1]);
        }
    } else {
        printf("Sorry, your name is not found in the MI6 database, CIA perhaps.\n");
    }
    return 0;
}
