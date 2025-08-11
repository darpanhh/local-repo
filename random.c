#include <stdio.h>
#include <unistd.h>

void main() {
    int b[20], n, i, p, a, d;

    // Step 1: Read number of pages
    printf("\nProgram for paging");
    scanf("%d", &n);

    // Step 2: Read base address for each page
    printf("\nEnter the base address:");
    for(i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }

    // Step 3: Read logical address (displacement)
    printf("\nEnter the logical address:");
    scanf("%d", &d);

    // Step 4: Read the page number
    for(i = 0; i < n; i++) {
        scanf("%d", &p);

        if(i == p) {
            // Physical address calculation
            a = b[i] + d;
            printf("\n\tPageNo.\tBaseAdd.\tPhysicalAdd.\n\t%d\t%d\t%d", p, b[i], a);
            return; // Stop after finding the page
        }
    }

    // Step 5: If page number invalid
    printf("\nInvalid page");
}