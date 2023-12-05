#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        // Reverse the first half of the list
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the number of elements is odd, move to the next node
    if (fast != NULL)
        slow = slow->next;

    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
            return (0);

        prev = prev->next;
        slow = slow->next;
    }

    return (1);
}

