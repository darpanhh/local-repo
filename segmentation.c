#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct Segment {
    char name[20];     // Segment name (Code, Data, Stack, etc.)
    int base;          // Starting address (simulated)
    int limit;         // Size of segment
    char *memory;      // Segment data
};


struct Segment createSegment(char name[], int base, int limit) {
    struct Segment seg;
    strcpy(seg.name, name);
    seg.base = base;
    seg.limit = limit;
    seg.memory = (char *)malloc(limit * sizeof(char));
    return seg;
}


void writeSegment(struct Segment *seg, char data[]) {
    if (strlen(data) > seg->limit) {
        printf("Error: Data exceeds segment limit for %s segment.\n", seg->name);
        return;
    }
    strcpy(seg->memory, data);
}


void readSegment(struct Segment seg) {
    printf("Segment: %s | Base: %d | Limit: %d | Data: %s\n",
           seg.name, seg.base, seg.limit, seg.memory);
}

int main() {
    
    struct Segment codeSeg = createSegment("Code", 1000, 50);
    struct Segment dataSeg = createSegment("Data", 2000, 100);
    struct Segment stackSeg = createSegment("Stack", 3000, 50);

  
    writeSegment(&codeSeg, "MOV A, B\nADD A, C\nHLT");
    writeSegment(&dataSeg, "x=10; y=20;");
    writeSegment(&stackSeg, "Function Calls & Local Vars");

    
    readSegment(codeSeg);
    readSegment(dataSeg);
    readSegment(stackSeg);

    
    free(codeSeg.memory);
    free(dataSeg.memory);
    free(stackSeg.memory);

    return 0;
}