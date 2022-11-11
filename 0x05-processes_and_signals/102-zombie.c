#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - infinite loop
 * Return: 0 on success
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
/**
 * main - C program that creates 5 zombie processes.
 * Return: 0 on success
 */
int main(void)
{
	int a;
	pid_t zombie;

	for (a == 0; a < 5; a++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		printf("Zombie process created, PID: \n");
	}
	infinite_while();
	return (0);
}
