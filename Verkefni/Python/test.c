#include <stdio.h>

int main() {
    char str[] = "5\343\377\377\377\177";
    int value;

    int result = sscanf(str, "%d", &value);

    if (result == 1) {
        printf("Successfully parsed: %d\n", value);
    } else {
        printf("Parsing failed\n");
    }

    return 0;
}