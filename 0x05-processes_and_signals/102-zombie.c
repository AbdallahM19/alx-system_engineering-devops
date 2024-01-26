#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

/**
 * infinite_while - When your code is done
 *  creating the parent process and the zombies
 *  use the function bellow
 * Return: 0
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
 * main - Write a C program that creates 5 zombie processes
 * Return: 0
*/
int main(void)
{
	pid_t pid;
	int i = 1;

	while (i <= 5)
	{
		pid = fork();
		if (!pid)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
		i++;
	}
	infinite_while();
	return (0);
}
