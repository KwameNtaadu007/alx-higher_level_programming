#include "lists.h"

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	dup = slow->next;
	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n != dup->n)
			return (0);

		temp = temp->next;
		dup = dup->next;
	}

	return (1);
}

