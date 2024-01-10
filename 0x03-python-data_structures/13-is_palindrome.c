#include "lists.h"
#include <stddef.h> /* added this line */

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head; /* two pointers for finding the middle */
    listint_t *prev = NULL, *curr = NULL, *next = NULL; /* three pointers for reversing the second half */
    listint_t *first = *head, *second = NULL; /* two pointers for comparing the two halves */
    int result = 1; /* the return value */

    /* check if the list is empty or has one node */
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    /* find the middle of the list */
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    /* reverse the second half of the list */
    curr = slow;
    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    /* compare the first half and the second half of the list */
    second = prev;
    while (first != NULL && second != NULL)
    {
        if (first->n != second->n)
        {
            result = 0;
            break;
        }
        first = first->next;
        second = second->next;
    }

    /* restore the original list by reversing the second half again */
    curr = prev;
    prev = NULL;
    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    /* attach the second half back to the first half */
    first = *head;
    while (first->next != NULL)
        first = first->next;
    first->next = prev;

    /* return the result */
    return (result);
}

