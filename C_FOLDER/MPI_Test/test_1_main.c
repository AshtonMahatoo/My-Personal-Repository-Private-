#include <stdio.h>
#include "mpi.h"

int main(int argc, char** argv){

    MPI_Init(NULL, NULL);// This begins the MPI Call




    //This is to get the # of processes
    int size;
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    //This will get the rank of the process
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);

    //This will get the name of the processor
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    int name_len;
    MPI_Get_processor_name(processor_name, &name_len);

    //This will print message
    printf("This is from the Processor %s, rank%d out of %d processors\n", processor_name, rank, size);




    MPI_Finalize(); //This Ends the MPI Call
    
    /*
    *HOW YOU RUN THE MPI PROGRAM IN TERMINAL*

    mpicc mpi_hello_world.c -o hello-world  
    mpirun -np 5 ./hello-world
    */
    
}